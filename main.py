from dotenv import load_dotenv
load_dotenv()

from crewai import Crew
from agents.pesquisador import pesquisador
from tasks.pesquisa_task import pesquisa_mercado

crew = Crew(
    agents=[pesquisador],
    tasks=[pesquisa_mercado],
    verbose=True
)

resultado = crew.kickoff()

print("\nRESULTADO FINAL:\n")
print(resultado)
