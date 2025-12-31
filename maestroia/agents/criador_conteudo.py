from langchain_openai import ChatOpenAI
from openai import OpenAI
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
client = OpenAI(api_key=OPENAI_API_KEY)

def agente_criador_conteudo(state: MaestroState) -> MaestroState:
    """
    Agente responsável por criar conteúdos de marketing
    com base na estratégia definida, otimizados por canal.
    """

    estrategia = state.get("estrategia")
    canais = state.get("canais", ["Instagram"])

    if not estrategia:
        return {
            "erros": ["Estratégia não encontrada no estado."]
        }

    conteudos = []

    # Templates por canal
    templates = {
        "instagram": """
        📸 **Post para Instagram:**
        - **Texto (até 2200 caracteres):** [Texto envolvente e visual]
        - **Hashtags:** #exemplo #conteudo
        - **Call to Action:** "Curtiu? Salve e compartilhe!"
        - **Imagem:** [Descrição detalhada para geração]
        """,
        "facebook": """
        📘 **Post para Facebook:**
        - **Texto (até 63206 caracteres):** [Texto informativo e conversacional]
        - **Hashtags:** #exemplo #conteudo
        - **Call to Action:** "Comente sua opinião!"
        - **Imagem:** [Descrição para geração]
        """,
        "twitter/x": """
        🐦 **Tweet para Twitter/X:**
        - **Texto (até 280 caracteres):** [Texto conciso e impactante]
        - **Hashtags:** #exemplo
        - **Mencionar:** @conta_relevante
        - **Imagem:** [Descrição opcional]
        """,
        "linkedin": """
        💼 **Post para LinkedIn:**
        - **Texto profissional:** [Conteúdo B2B, insights valiosos]
        - **Hashtags:** #business #marketing
        - **Call to Action:** "O que você acha? Compartilhe nos comentários!"
        - **Imagem:** [Gráfico ou infográfico profissional]
        """,
        "tiktok": """
        🎵 **Vídeo para TikTok:**
        - **Duração:** 15-60 segundos
        - **Roteiro:** [Passos do vídeo, fala, música]
        - **Hashtags:** #viral #conteudo
        - **Thumbnail:** [Descrição atraente]
        """,
        "youtube": """
        📺 **Vídeo para YouTube:**
        - **Título:** [Título otimizado para SEO]
        - **Descrição:** [Descrição com keywords, links]
        - **Thumbnail:** [Descrição chamativa]
        - **Tags:** palavra1, palavra2
        """,
        "pinterest": """
        📌 **Pin para Pinterest:**
        - **Título:** [Título descritivo]
        - **Descrição:** [Texto otimizado]
        - **Link:** [URL de destino]
        - **Imagem:** [Imagem vertical atraente]
        """,
        "snapchat": """
        👻 **Story para Snapchat:**
        - **Conteúdo:** [Texto curto, emoji, sticker]
        - **Duração:** 24 horas
        - **Filtro/Geofiltro:** [Sugestão]
        """,
        "google ads": """
        📢 **Anúncio para Google Ads:**
        - **Título:** [Título atraente, até 30 caracteres]
        - **Descrição:** [Descrição persuasiva, até 90 caracteres]
        - **URL:** [Página de destino]
        - **Keywords:** [Lista de palavras-chave]
        """
    }

    for canal in canais:
        canal_lower = canal.lower()
        template = templates.get(canal_lower, templates["instagram"])

        prompt = f"""
        Você é um especialista em criação de conteúdo para {canal}.

        Estratégia da campanha:
        {estrategia}

        Use este template para criar conteúdo otimizado:
        {template}

        Preencha o template com conteúdo relevante e persuasivo.
        """

        resposta = llm.invoke(prompt)
        conteudo = f"**{canal}:**\n{resposta.content.strip()}"
        conteudos.append(conteudo)

    # Gerar imagem com DALL-E baseada na sugestão do primeiro conteúdo

    # Gerar imagem com DALL-E baseada na sugestão
    image_prompt = "Uma imagem inspiradora para marketing digital sustentável"
    try:
        image_response = client.images.generate(
            model="dall-e-3",
            prompt=image_prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        image_url = image_response.data[0].url
    except Exception as e:
        image_url = f"Erro ao gerar imagem: {str(e)}"

    return {
        "conteudos": [resposta.content],
        "imagens": [image_url]
    }
