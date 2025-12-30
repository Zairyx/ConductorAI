from crewai import Agent

pesquisador = Agent(
    role="Pesquisador de Marketing",
    goal="Analisar mercado, concorrentes e tendências",
    backstory="Especialista em marketing digital e dados",
    verbose=True
)
