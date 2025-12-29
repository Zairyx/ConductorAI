from crewai_tools import tool

@tool
def ler_arquivo(caminho: str) -> str:
    """
    Lê o conteúdo de um arquivo de texto.
    """
    with open(caminho, "r", encoding="utf-8") as f:
        return f.read()
