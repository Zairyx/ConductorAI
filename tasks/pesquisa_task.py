from crewai import Task
from agents.pesquisador import pesquisador

pesquisa_task = Task(
    description="Pesquisar tendências de marketing para o nicho informado",
    agent=pesquisador,
    expected_output="Relatório com insights estratégicos"
)

