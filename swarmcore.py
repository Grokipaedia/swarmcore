# swarmcore.py - Lightweight multi-agent coordinator
from rich.console import Console
from rich.panel import Panel
import time

console = Console()

class Agent:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

    def execute(self, task: str):
        console.print(f"[cyan]{self.name} ({self.role}):[/cyan] Working on: {task[:80]}...")
        time.sleep(0.8)
        return f"{self.name} completed: {task[:60]}..."

class SwarmCore:
    def __init__(self):
        self.agents = [
            Agent("Researcher", "gathers information"),
            Agent("Analyzer", "processes and understands"),
            Agent("Summarizer", "creates clear output"),
            Agent("Executor", "takes final action")
        ]
        self.history = []

    def run_task(self, user_task: str):
        console.print(Panel.fit(f"[bold yellow]New Task:[/bold yellow] {user_task}", border_style="yellow"))

        results = []
        for agent in self.agents:
            result = agent.execute(user_task)
            results.append(result)
            self.history.append(result)

            # Simple hand-off simulation
            if agent.name == "Analyzer":
                console.print("[green]→ Passing insights to Summarizer...[/green]")

        console.print("\n[bold green]Swarm completed the task![/bold green]")
        for r in results:
            console.print(f"  • {r}")

        return results

# Example usage
if __name__ == "__main__":
    swarm = SwarmCore()
    console.print("[bold magenta]🚀 SwarmCore Started — Multi-Agent Coordinator[/bold magenta]\n")

    tasks = [
        "Explain Intent-Bound Authorization and why it's better than prompts",
        "Analyze the Anthropic Claude Code leak and suggest safe improvements",
        "Design a governed AI coding workflow using IBA + Dreamweave + Matey"
    ]

    for task in tasks:
        swarm.run_task(task)
        console.print("\n" + "-"*60 + "\n")

    console.print("[bold]SwarmCore is ready for extension with IBA, Dreamweave, and Matey.[/bold]")
