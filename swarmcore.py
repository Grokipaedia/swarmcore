# swarmcore.py - Simple standalone multi-agent coordinator
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

            if agent.name == "Analyzer":
                console.print("[green]→ Passing insights to Summarizer...[/green]")

        console.print("\n[bold green]Swarm completed the task![/bold green]")
        for r in results:
            console.print(f"  • {r}")

        return results


# Example usage
if __name__ == "__main__":
    swarm = SwarmCore()
    console.print("[bold magenta]🚀 SwarmCore Started — Standalone Multi-Agent Coordinator[/bold magenta]\n")

    tasks = [
        "Explain why IBA is better than prompts for AI safety",
        "Design a governed local coding workflow using the Anthropic leak insights",
        "Create a simple plan to combine governance, memory, and personality in agents"
    ]

    for task in tasks:
        swarm.run_task(task)
        console.print("\n" + "-"*70 + "\n")

    console.print("[bold]SwarmCore is ready. You can later connect it with Dreamweave and Matey if desired.[/bold]")
