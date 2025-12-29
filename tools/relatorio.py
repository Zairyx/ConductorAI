from crewai_tools import tool

@tool
def salvar_relatorio(texto: str, nome_arquivo: str = "relatorio.txt") -> str:
    """
    Salva um relatório em arquivo.
    """
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write(texto)
    return f"Relatório salvo com sucesso em {nome_arquivo}"
