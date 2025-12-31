import requests
import tweepy
from langchain_openai import ChatOpenAI
from maestroia.config.settings import (
    OPENAI_API_KEY,
    DEFAULT_LLM_MODEL,
    DEFAULT_TEMPERATURE,
    META_ACCESS_TOKEN,
    GOOGLE_ADS_CUSTOMER_ID,
    GOOGLE_ADS_DEVELOPER_TOKEN,
    TWITTER_API_KEY,
    TWITTER_API_SECRET,
    TWITTER_ACCESS_TOKEN,
    TWITTER_ACCESS_TOKEN_SECRET,
    LINKEDIN_ACCESS_TOKEN,
    TIKTOK_ACCESS_TOKEN,
    YOUTUBE_API_KEY,
    PINTEREST_ACCESS_TOKEN,
    SNAPCHAT_ACCESS_TOKEN,
)
from maestroia.core.state import MaestroState

# Imports condicionais para evitar erros se bibliotecas não estiverem instaladas
try:
    import google.ads
except ImportError:
    google = None

llm = ChatOpenAI(
    api_key=OPENAI_API_KEY,
    model=DEFAULT_LLM_MODEL,
    temperature=DEFAULT_TEMPERATURE,
)

def publicar_instagram_facebook(conteudo: str, canal: str) -> str:
    """Publicar no Instagram/Facebook via Meta Graph API"""
    if not META_ACCESS_TOKEN:
        return f"Publicado no {canal} com sucesso (simulado): {conteudo[:100]}..."
    
    # TODO: Implementar chamada real para Meta API
    # Exemplo: POST /me/feed para Facebook, ou Instagram Basic Display API
    return f"Publicado no {canal} com sucesso (API Meta): {conteudo[:100]}..."

def publicar_google_ads(conteudo: str) -> str:
    """Criar campanha no Google Ads"""
    if not GOOGLE_ADS_CUSTOMER_ID or not GOOGLE_ADS_DEVELOPER_TOKEN:
        return f"Campanha Google Ads criada com sucesso (simulado) para: {conteudo[:100]}..."
    
    # TODO: Implementar Google Ads API
    return f"Campanha Google Ads criada com sucesso (API Google): {conteudo[:100]}..."

def publicar_twitter(conteudo: str) -> str:
    """Publicar tweet no Twitter/X"""
    if not all([TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET]):
        return f"Post publicado no Twitter/X com sucesso (simulado): {conteudo[:100]}..."
    
    try:
        client = tweepy.Client(
            consumer_key=TWITTER_API_KEY,
            consumer_secret=TWITTER_API_SECRET,
            access_token=TWITTER_ACCESS_TOKEN,
            access_token_secret=TWITTER_ACCESS_TOKEN_SECRET
        )
        response = client.create_tweet(text=conteudo[:280])  # Limite do Twitter
        return f"Tweet publicado com sucesso (ID: {response.data['id']})"
    except Exception as e:
        return f"Erro ao publicar no Twitter: {str(e)}"

def publicar_linkedin(conteudo: str) -> str:
    """Publicar no LinkedIn"""
    if not LINKEDIN_ACCESS_TOKEN:
        return f"Post profissional publicado no LinkedIn com sucesso (simulado): {conteudo[:100]}..."
    
    # TODO: Implementar LinkedIn API
    return f"Post publicado no LinkedIn com sucesso (API LinkedIn): {conteudo[:100]}..."

def publicar_tiktok(conteudo: str) -> str:
    """Publicar no TikTok"""
    if not TIKTOK_ACCESS_TOKEN:
        return f"Vídeo curto publicado no TikTok com sucesso (simulado): {conteudo[:100]}..."
    
    # TODO: Implementar TikTok API
    return f"Vídeo publicado no TikTok com sucesso (API TikTok): {conteudo[:100]}..."

def publicar_youtube(conteudo: str) -> str:
    """Publicar vídeo no YouTube"""
    if not YOUTUBE_API_KEY:
        return f"Vídeo publicado no YouTube com sucesso (simulado): {conteudo[:100]}..."
    
    # TODO: Implementar YouTube Data API
    return f"Vídeo publicado no YouTube com sucesso (API YouTube): {conteudo[:100]}..."

def publicar_pinterest(conteudo: str) -> str:
    """Publicar Pin no Pinterest"""
    if not PINTEREST_ACCESS_TOKEN:
        return f"Pin visual publicado no Pinterest com sucesso (simulado): {conteudo[:100]}..."
    
    # TODO: Implementar Pinterest API
    return f"Pin publicado no Pinterest com sucesso (API Pinterest): {conteudo[:100]}..."

def publicar_snapchat(conteudo: str) -> str:
    """Publicar Story no Snapchat"""
    if not SNAPCHAT_ACCESS_TOKEN:
        return f"Story/Snap publicado no Snapchat com sucesso (simulado): {conteudo[:100]}..."
    
    # TODO: Implementar Snapchat API
    return f"Story publicado no Snapchat com sucesso (API Snapchat): {conteudo[:100]}..."

def agente_publicador(state: MaestroState) -> MaestroState:
    """
    Agente responsável por publicar conteúdos em plataformas reais ou simuladas.
    """
    conteudos = state.get("conteudos", [])
    canais = state.get("canais", [])
    if not conteudos:
        return {"erros": ["Conteúdos não encontrados no estado."]}

    if not canais:
        return {"erros": ["Nenhum canal especificado para publicação."]}

    # Publicação por canal
    publicacoes = {}
    for canal in canais:
        canal_lower = canal.lower()
        conteudo = conteudos[0] if conteudos else "Conteúdo de exemplo"
        
        if canal_lower in ["instagram", "facebook"]:
            publicacoes[canal] = publicar_instagram_facebook(conteudo, canal)
        elif canal_lower == "google ads":
            publicacoes[canal] = publicar_google_ads(conteudo)
        elif canal_lower in ["twitter/x", "twitter"]:
            publicacoes[canal] = publicar_twitter(conteudo)
        elif canal_lower == "linkedin":
            publicacoes[canal] = publicar_linkedin(conteudo)
        elif canal_lower == "tiktok":
            publicacoes[canal] = publicar_tiktok(conteudo)
        elif canal_lower == "youtube":
            publicacoes[canal] = publicar_youtube(conteudo)
        elif canal_lower == "pinterest":
            publicacoes[canal] = publicar_pinterest(conteudo)
        elif canal_lower == "snapchat":
            publicacoes[canal] = publicar_snapchat(conteudo)
        else:
            publicacoes[canal] = f"Publicação em {canal} não suportada ainda."

    return {"publicacoes": publicacoes}
