# swarmcore.py - Multi-agent coordinator + Dreamweave memory + Matey companion
from rich.console import Console
from rich.panel import Panel
import time

console = Console()

# Import the other two repos
from dreamweave import Dreamweave
from matey import Matey

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
        self.memory = Dreamweave()      # ← Dreamweave memory
        self.matey = Matey()            # ← Matey companion
        self.history = []

    def run_task(self, user_task: str):
        # Store task in memory
        self.memory.add(f"New task: {user_task}")

        console.print(Panel.fit(f"[bold yellow]New Task:[/bold yellow] {user_task}", border_style="yellow"))

        results = []
        for agent in self.agents:
            result = agent.execute(user_task)
            results.append(result)
            self.history.append(result)

            # Store each result in Dreamweave
            self.memory.add(f"{agent.name} result: {result[:100]}")

            # Let Matey comment occasionally
            if agent.name == "Analyzer":
                console.print("[green]→ Passing insights to Summarizer...[/green]")
                self.matey.give_advice("Analyze this task")

        # Dream after every few tasks
        if len(self.history) % 3 == 0:
            self.memory.dream()

        console.print("\n[bold green]Swarm completed the task![/bold green]")
        for r in results:
            console.print(f"  • {r}")

        # Matey gives final feedback
        self.matey.give_advice("How did the swarm do?")

        return results


# Example usage
if __name__ == "__main__":
    swarm = SwarmCore()
    console.print("[bold magenta]🚀 SwarmCore Started — with Dreamweave + Matey[/bold magenta]\n")

    tasks = [
        "Explain why IBA is better than prompts for AI safety",
        "Design a governed local coding workflow using the leak insights"
    ]

    for task in tasks:
        swarm.run_task(task)
        console.print("\n" + "-"*70 + "\n")
