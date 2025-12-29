from crewai import Agent

pesquisador = Agent(
    role="Pesquisador de Mercado",
    goal="Pesquisar tendências, público-alvo e concorrentes",
    backstory="Especialista em análise de mercado e comportamento do consumidor",
    verbose=True
)
