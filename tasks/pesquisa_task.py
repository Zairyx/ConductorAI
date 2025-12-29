from crewai import Task
from agents.pesquisador import pesquisador

pesquisa_mercado = Task(
    description="Pesquisar tendências atuais de marketing digital no Brasil",
    expected_output="Um resumo com tendências, oportunidades e riscos",
    agent=pesquisador
)
