from crewai import Crew
from tasks.pesquisa_task import pesquisa_task
from core.database import create_tables

def run_maestro():
    create_tables()

    crew = Crew(
        agents=[pesquisa_task.agent],
        tasks=[pesquisa_task],
        verbose=True
    )

    return crew.kickoff()

if __name__ == "__main__":
    print(run_maestro())
