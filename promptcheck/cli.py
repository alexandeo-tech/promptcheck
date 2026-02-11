import json
import os
from pathlib import Path
from typing import List

import typer
from dotenv import load_dotenv
from openai import OpenAI
from rich import print

PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env", override=True)

DEFAULT_MODEL = "gpt-4o-mini"
AI_MODEL = "gpt-4o-mini"

MODEL_PRICING = {
    "gpt-4o-mini": {
        "input_per_1k": 0.00015,
        "output_per_1k": 0.00060,
    }
}

AI_SYSTEM_PROMPT = """You are a prompt quality auditor.
Evaluate prompts conservatively and objectively.
Do not use marketing language.
Return structured JSON only.
"""

app = typer.Typer(help="Prompt Validator CLI")


def analyze_prompt(prompt: str):
    issues: List[str] = []
    suggestions: List[str] = []

    score = 10.0
    lower_prompt = prompt.lower()

    if "you are" not in lower_prompt:
        issues.append("No explicit role definition")
        suggestions.append("Define a clear role for the model.")
        score -= 1.5

    if "json" not in lower_prompt and "format" not in lower_prompt:
        issues.append("No output format specified")
        suggestions.append("Specify an explicit output format.")
        score -= 2.0

    if "if unsure" not in lower_prompt and "state uncertainty" not in lower_prompt:
        issues.append("No instruction to handle uncertainty")
        suggestions.append("Instruct the model to state uncertainty instead of guessing.")
        score -= 1.5

    vague_terms = ["explain", "describe", "tell me about"]
    if any(term in lower_prompt for term in vague_terms):
        issues.append("Task scope may be vague or open-ended")
        suggestions.append("Narrow the task scope with constraints.")
        score -= 1.0

    if "concise" not in lower_prompt and "brief" not in lower_prompt:
        issues.append("No verbosity guidance")
        suggestions.append("Add verbosity guidance.")
        score -= 1.0

    score = max(0.0, min(10.0, score))

    hallucination_risk = "High" if score < 5 else "Medium" if score < 7 else "Low"
    cost_risk = "High" if "explain" in lower_prompt and "concise" not in lower_prompt else "Low"

    return {
        "score": round(score, 1),
        "issues": issues,
        "suggestions": suggestions,
        "risk": {
            "hallucination": hallucination_risk,
            "cost": cost_risk,
        },
    }


def estimate_tokens_and_cost(prompt: str, model: str = DEFAULT_MODEL):
    input_tokens = max(1, len(prompt) // 4)
    estimated_output_tokens = 300

    pricing = MODEL_PRICING.get(model)
    if not pricing:
        return None

    input_cost = (input_tokens / 1000) * pricing["input_per_1k"]
    output_cost = (estimated_output_tokens / 1000) * pricing["output_per_1k"]
    total_cost = round(input_cost + output_cost, 6)

    return {
        "model": model,
        "input_tokens": input_tokens,
        "estimated_output_tokens": estimated_output_tokens,
        "estimated_cost_usd": total_cost,
    }


def ai_deep_analysis(prompt: str):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY is not set. Set it in .env or environment variables."
        )
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model=AI_MODEL,
        temperature=0.2,
        messages=[
            {"role": "system", "content": AI_SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"""
Analyze the following prompt and return JSON with:
- critique: short explanation of weaknesses
- improved_prompt: revised version fixing issues
- risk_notes: list of risks

Prompt:
\"\"\"
{prompt}
\"\"\"
""",
            },
        ],
        response_format={"type": "json_object"},
    )

    return response.choices[0].message.content


@app.command("validate")
def validate_command(
    file: str = typer.Argument(..., help="Path to prompt file"),
    json_output: bool = typer.Option(False, "--json", help="Output result as JSON"),
    ai_analysis: bool = typer.Option(False, "--ai", help="Enable AI-powered deep analysis"),
):
    """
    Validate a prompt file.
    """
    try:
        with open(file, "r", encoding="utf-8") as f:
            prompt = f.read()
    except FileNotFoundError:
        print(f"[red]File not found:[/red] {file}")
        raise typer.Exit(code=1)

    result = analyze_prompt(prompt)
    cost_estimate = estimate_tokens_and_cost(prompt)
    if cost_estimate:
        result["estimated_cost"] = cost_estimate

    if ai_analysis:
        try:
            ai_result = ai_deep_analysis(prompt)
            result["ai_analysis"] = json.loads(ai_result)
        except Exception as e:
            result["ai_analysis_error"] = str(e)

    if json_output:
        print(json.dumps(result, indent=2))
        return

    print("\n[bold cyan]Prompt Quality Report[/bold cyan]")
    print(f"[bold]Score:[/bold] {result['score']} / 10\n")

    if result["issues"]:
        print("[bold yellow]Issues detected:[/bold yellow]")
        for issue in result["issues"]:
            print(f" - {issue}")
    else:
        print("[bold green]No major issues detected.[/bold green]")

    print("\n[bold]Risk assessment:[/bold]")
    print(f" - Hallucination risk: {result['risk']['hallucination']}")
    print(f" - Cost inefficiency risk: {result['risk']['cost']}")
    if "ai_analysis" in result:
        print(f" - AI analysis: {result['ai_analysis']}")
    elif "ai_analysis_error" in result:
        print(f" - AI analysis error: {result['ai_analysis_error']}")

    if result["suggestions"]:
        print("\n[bold green]Suggested improvements:[/bold green]")
        for suggestion in result["suggestions"]:
            print(f" - {suggestion}")


def main():
    app()


if __name__ == "__main__":
    main()
