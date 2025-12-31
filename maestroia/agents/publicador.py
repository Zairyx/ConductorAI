from langchain_openai import ChatOpenAI
from maestroia.config.settings import (
    OPENAI_API_KEY,
    DEFAULT_LLM_MODEL,
    DEFAULT_TEMPERATURE,
)
from maestroia.core.state import MaestroState

llm = ChatOpenAI(
    api_key=OPENAI_API_KEY,
    model=DEFAULT_LLM_MODEL,
    temperature=DEFAULT_TEMPERATURE,
)

def agente_publicador(state: MaestroState) -> MaestroState:
    """
    Agente responsável por publicar conteúdos em plataformas simuladas.
    """
    conteudos = state.get("conteudos", [])
    canais = state.get("canais", [])
    if not conteudos:
        return {"erros": ["Conteúdos não encontrados no estado."]}

    if not canais:
        return {"erros": ["Nenhum canal especificado para publicação."]}

    # Simulação de publicação por canal
    publicacoes = {}
    for canal in canais:
        canal_lower = canal.lower()
        if canal_lower in ["instagram", "facebook"]:
            # Simulação Meta (Instagram/Facebook)
            publicacoes[canal] = f"Publicado no {canal} com sucesso (simulado): {conteudos[0][:100]}..."
        elif canal_lower == "google ads":
            # Simulação Google Ads
            publicacoes[canal] = f"Campanha Google Ads criada com sucesso (simulado) para: {conteudos[0][:100]}..."
        elif canal_lower in ["twitter/x", "twitter"]:
            # Simulação Twitter/X API
            publicacoes[canal] = f"Post publicado no {canal} com sucesso (simulado): {conteudos[0][:100]}..."
        elif canal_lower == "linkedin":
            # Simulação LinkedIn API
            publicacoes[canal] = f"Post profissional publicado no {canal} com sucesso (simulado): {conteudos[0][:100]}..."
        elif canal_lower == "tiktok":
            # Simulação TikTok API
            publicacoes[canal] = f"Vídeo curto publicado no {canal} com sucesso (simulado): {conteudos[0][:100]}..."
        elif canal_lower == "youtube":
            # Simulação YouTube API
            publicacoes[canal] = f"Vídeo publicado no {canal} com sucesso (simulado): {conteudos[0][:100]}..."
        elif canal_lower == "pinterest":
            # Simulação Pinterest API
            publicacoes[canal] = f"Pin visual publicado no {canal} com sucesso (simulado): {conteudos[0][:100]}..."
        elif canal_lower == "snapchat":
            # Simulação Snapchat API
            publicacoes[canal] = f"Story/Snap publicado no {canal} com sucesso (simulado): {conteudos[0][:100]}..."
        else:
            publicacoes[canal] = f"Publicação em {canal} não suportada ainda."

    return {"publicacoes": publicacoes}
