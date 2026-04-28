from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import re
import time
import html

app = Flask(__name__)
CORS(app)

# ==================== EMOJIMAP COMPLETO ====================
EMOJI_MAP = {

    # 🌸 Nature & Plants
    'flower': '🌸', 'flowers': '🌸', 'flor': '🌸',
    'rose': '🌹', 'rosa': '🌹',
    'sunflower': '🌻', 'girassol': '🌻',
    'tulip': '🌷', 'tulips': '🌷',
    'tree': '🌳', 'árvore': '🌳',
    'plant': '🌱', 'planta': '🌱',
    'leaf': '🍃', 'folha': '🍃',
    'forest': '🌲', 'floresta': '🌲',
    'nature': '🌿', 'natureza': '🌿',

    # 🍎 Fruits
    'apple': '🍎', 'maçã': '🍎',
    'banana': '🍌',
    'orange': '🍊', 'laranja': '🍊',
    'grape': '🍇', 'uva': '🍇',
    'strawberry': '🍓', 'morango': '🍓',
    'pineapple': '🍍', 'abacaxi': '🍍',
    'watermelon': '🍉', 'melancia': '🍉',
    'mango': '🥭', 'kiwi': '🥝',
    'peach': '🍑', 'cherry': '🍒',

    # 🧠 Tech & AI
    'ai': '🧠', 'artificial intelligence': '🧠',
    'machine learning': '🤖',
    'robot': '🤖',
    'data': '📊', 'dados': '📊',
    'analytics': '📈',
    'algorithm': '🔢',
    'code': '💻', 'coding': '💻',
    'programming': '👨‍💻',
    'software': '📱',
    'computer': '💻',

    # 🌍 Science & Education
    'science': '🔬', 'ciência': '🔬',
    'biology': '🧬',
    'chemistry': '⚗️',
    'physics': '🧲',
    'math': '📐',
    'education': '📚', 'study': '📚',
    'book': '📖',

    # 🏥 Health
    'health': '🏥', 'saúde': '🏥',
    'doctor': '👨‍⚕️',
    'medicine': '💊',
    'fitness': '💪',
    'gym': '🏋️',

    # 💼 Business
    'business': '💼', 'negócio': '💼',
    'finance': '💰', 'finanças': '💰',
    'money': '💵',
    'startup': '🚀',
    'marketing': '📢',

    # 🎬 Media & Entertainment
    'movie': '🎬', 'film': '🎬',
    'music': '🎵',
    'song': '🎶',
    'game': '🎮',
    'video': '📹',

    # ⚽ Sports
    'sport': '⚽', 'sports': '⚽',
    'football': '⚽',
    'basketball': '🏀',
    'tennis': '🎾',
    'running': '🏃',

    # 🌎 Travel & Places
    'travel': '✈️', 'viagem': '✈️',
    'hotel': '🏨',
    'beach': '🏖️',
    'mountain': '⛰️',
    'city': '🏙️',

    # 🍔 Food
    'food': '🍔', 'comida': '🍔',
    'pizza': '🍕',
    'burger': '🍔',
    'coffee': '☕',
    'tea': '🍵',

    # 🐾 Animals
    'dog': '🐕', 'cachorro': '🐕',
    'cat': '🐈', 'gato': '🐈',
    'lion': '🦁',
    'bird': '🐦',
    'fish': '🐟',

    # 🌙 Space & Weather
    'sun': '☀️',
    'moon': '🌙',
    'star': '⭐',
    'snow': '❄️',
    'rain': '🌧️',
    'cloud': '☁️',
    'water': '💧',

    # ❤️ Abstract
    'love': '❤️',
    'energy': '⚡',
    'idea': '💡',
    'time': '⏳',
    'search': '🔍',  # ← vírgula corrigida aqui

    # 🏠 Home & Objects
    'home': '🏠', 'house': '🏠', 'casa': '🏠',
    'apartment': '🏢', 'building': '🏢',
    'room': '🚪', 'bedroom': '🛏️',
    'bed': '🛏️', 'kitchen': '🍳',
    'bathroom': '🚿', 'door': '🚪',
    'window': '🪟', 'chair': '🪑',
    'table': '🪑', 'lamp': '💡',
    'mirror': '🪞', 'key': '🔑',

    # 🎓 School & Classes
    'class': '🏫', 'classes': '🏫',
    'classroom': '🏫', 'school': '🏫',
    'college': '🎓', 'university': '🎓',
    'student': '🧑‍🎓', 'teacher': '🧑‍🏫',
    'lesson': '📘', 'course': '📚',
    'exam': '📝', 'test': '📝',
    'homework': '📄', 'notebook': '📓',
    'pencil': '✏️', 'pen': '🖊️',

    # 🧊 Materials
    'glass': '🥃', 'cup': '🥤',
    'bottle': '🍾', 'plastic': '♻️',
    'metal': '⚙️', 'wood': '🪵',
    'paper': '📄', 'stone': '🪨',
    'rock': '🪨', 'fire': '🔥',
    'ice': '🧊', 'sand': '🏜️',
    'clay': '🧱', 'brick': '🧱',

    # 👕 Clothing
    'clothes': '👕', 'clothing': '👕',
    'shirt': '👕', 'dress': '👗',
    'shoe': '👟', 'shoes': '👟',
    'hat': '🎩', 'bag': '👜',
    'watch': '⌚', 'glasses': '👓',

    # 🚗 Transport
    'car': '🚗', 'bus': '🚌',
    'train': '🚆', 'subway': '🚇',
    'bike': '🚲', 'bicycle': '🚲',
    'motorcycle': '🏍️', 'ship': '🚢',
    'boat': '⛵', 'rocket': '🚀',

    # 🧍 People & Society
    'person': '🧍', 'people': '👥',
    'family': '👨‍👩‍👧‍👦', 'child': '🧒',
    'baby': '👶', 'friend': '🤝',
    'community': '🌐', 'society': '🏛️',
    'culture': '🎭', 'language': '🗣️',
    'history': '🏺', 'law': '⚖️',

    # 🧩 Concepts
    'system': '🧩', 'process': '⚙️',
    'structure': '🏗️', 'design': '🎨',
    'network': '🌐', 'security': '🔐',
    'privacy': '🛡️', 'risk': '⚠️',
    'problem': '❓', 'solution': '✅',
    'research': '🔎', 'knowledge': '🧠',
}

def obter_emoji(tema):
    tema = tema.lower()
    palavras_ordenadas = sorted(EMOJI_MAP.keys(), key=len, reverse=True)

    for palavra in palavras_ordenadas:
        if palavra in tema:
            return EMOJI_MAP[palavra]

    return '🔍'


cache = {}

HEADERS = {
    "User-Agent": "AIResearcherPortfolio/1.0"
}

FALLBACK_TERMS = {
    "orange": "Orange (fruit)",
    "apple": "Apple",
    "mango": "Mango",
    "flower": "Flower",
    "flowers": "Flower",
    "tulip": "Tulip",
    "tulips": "Tulip",
    "snow": "Snow",
    "water": "Water",
    "rose": "Rose",
    "banana": "Banana",
    "grape": "Grape",
    "pineapple": "Pineapple",
    "strawberry": "Strawberry",
    "sunflower": "Sunflower",
    "tree": "Tree",
    "plant": "Plant",
    "computer": "Computer",
    "software": "Software",
    "artificial intelligence": "Artificial intelligence",
    "ai": "Artificial intelligence",
    "machine learning": "Machine learning",
    "data": "Data",
    "algorithm": "Algorithm"
}


def limpar_texto(texto):
    texto = html.unescape(texto or "")
    texto = re.sub(r'<.*?>', '', texto)
    texto = re.sub(r'\s+', ' ', texto)
    return texto.strip()


def normalizar(texto):
    texto = limpar_texto(texto).lower()
    texto = re.sub(r'[^a-z0-9\s]', '', texto)
    texto = re.sub(r'\s+', ' ', texto)
    return texto.strip()


def dividir_em_frases(texto):
    frases = re.split(r'(?<=[.!?])\s+', limpar_texto(texto))
    return [f.strip() for f in frases if len(f.strip()) > 35]


def buscar_artigo_por_titulo(titulo):
    url = "https://en.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "titles": titulo,
        "redirects": 1,
        "prop": "extracts|info|pageprops",
        "explaintext": 1,
        "exsentences": 14,
        "inprop": "url",
        "format": "json"
    }

    try:
        response = requests.get(url, params=params, headers=HEADERS, timeout=15)
        dados = response.json()
        pages = dados.get("query", {}).get("pages", {})

        for _, page in pages.items():
            if "missing" in page:
                return None

            if "pageprops" in page and "disambiguation" in page["pageprops"]:
                return None

            extract = limpar_texto(page.get("extract", ""))

            if not extract or len(extract) < 80:
                return None

            if "may refer to" in extract.lower():
                return None

            return {
                "titulo": limpar_texto(page.get("title", titulo)),
                "link": page.get("fullurl", ""),
                "descricao": extract
            }

    except Exception as e:
        print("ERRO ARTIGO:", e)

    return None


def buscar_candidatos(tema):
    url = "https://en.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "list": "search",
        "srsearch": tema,
        "srlimit": 15,
        "format": "json",
        "utf8": 1
    }

    lixo = [
        "album", "film", "song", "episode", "novel", "essay",
        "surname", "given name", "fictional", "character",
        "disambiguation", "may refer to"
    ]

    try:
        response = requests.get(url, params=params, headers=HEADERS, timeout=15)
        dados = response.json()
        candidatos = []

        for item in dados.get("query", {}).get("search", []):
            titulo = limpar_texto(item.get("title", ""))
            snippet = limpar_texto(item.get("snippet", ""))

            if not titulo or not snippet:
                continue

            texto = f"{titulo} {snippet}".lower()

            if any(l in texto for l in lixo):
                continue

            candidatos.append({
                "titulo": titulo,
                "snippet": snippet
            })

        return candidatos

    except Exception as e:
        print("ERRO CANDIDATOS:", e)
        return []


def escolher_melhor_candidato(tema, candidatos):
    termo = normalizar(tema)
    melhor = None
    melhor_score = -1

    for c in candidatos:
        titulo_norm = normalizar(c["titulo"])
        snippet_norm = normalizar(c["snippet"])
        texto = f"{titulo_norm} {snippet_norm}"

        score = 0

        if titulo_norm == termo:
            score += 100

        if titulo_norm.startswith(termo):
            score += 60

        if termo in titulo_norm:
            score += 40

        if termo in texto:
            score += 30

        if "(" not in c["titulo"]:
            score += 15

        if len(c["snippet"]) > 80:
            score += 5

        if score > melhor_score:
            melhor_score = score
            melhor = c

    return melhor


def construir_referencias(artigo):
    frases = dividir_em_frases(artigo["descricao"])

    titulos = [
        "Definition",
        "Main characteristics",
        "Context",
        "How it works",
        "Importance",
        "Applications"
    ]

    referencias = []

    for i, frase in enumerate(frases[:6]):
        referencias.append({
            "titulo": f"{artigo['titulo']} - {titulos[i]}",
            "link": artigo["link"],
            "descricao": frase
        })

    while len(referencias) < 4 and frases:
        idx = len(referencias)
        referencias.append({
            "titulo": f"{artigo['titulo']} - {titulos[idx]}",
            "link": artigo["link"],
            "descricao": frases[idx % len(frases)]
        })

    return referencias[:6]


def buscar_google(tema):
    termo_original = tema.strip()
    termo_normalizado = normalizar(termo_original)

    termo_preferido = FALLBACK_TERMS.get(termo_normalizado, termo_original)

    artigo = buscar_artigo_por_titulo(termo_preferido)

    if not artigo:
        candidatos = buscar_candidatos(termo_original)
        melhor = escolher_melhor_candidato(termo_original, candidatos)

        if melhor:
            artigo = buscar_artigo_por_titulo(melhor["titulo"])

    if not artigo:
        return construir_resultado_emergencial(termo_original)

    return construir_referencias(artigo)


def construir_resultado_emergencial(tema):
    link = "https://en.wikipedia.org/wiki/Main_Page"

    frases = [
        f"{tema.capitalize()} is a research topic that can be explored through its definition, main characteristics, uses, and broader context.",
        f"A reliable overview of {tema} should consider what it is, how it is commonly described, and why it matters in practical or educational settings.",
        f"The subject can be analyzed by comparing its structure, purpose, examples, and relationship with nearby concepts.",
        f"In an educational context, studying {tema} helps organize information, identify relevant patterns, and understand its importance.",
        f"A complete research summary should connect the definition of {tema} with its applications, limitations, and impact."
    ]

    titulos = [
        "Definition",
        "Main characteristics",
        "Context",
        "Importance",
        "Applications"
    ]

    return [
        {
            "titulo": f"{tema.capitalize()} - {titulos[i]}",
            "link": link,
            "descricao": frases[i]
        }
        for i in range(5)
    ]


def filtrar_resultados(resultados):
    lixo = [
        "album", "film", "song", "episode", "novel", "essay",
        "surname", "given name", "fictional", "character",
        "may refer to", "disambiguation"
    ]

    filtrados = []

    for r in resultados:
        titulo = limpar_texto(r.get("titulo", ""))
        descricao = limpar_texto(r.get("descricao", ""))
        link = r.get("link", "")

        texto = f"{titulo} {descricao}".lower()

        if not descricao or len(descricao) < 35:
            continue

        if any(l in texto for l in lixo):
            continue

        filtrados.append({
            "titulo": titulo,
            "link": link,
            "descricao": descricao
        })

    return filtrados


def gerar_resumo_educacional(tema, resultados):
    chave = tema.lower().strip()

    if chave in cache:
        return cache[chave]

    frases = []

    for r in resultados:
        desc = limpar_texto(r.get("descricao", ""))
        if desc and desc not in frases:
            frases.append(desc)

    if not frases:
        frases = [
            f"{tema.capitalize()} is a topic that can be studied through its definition, characteristics, context, and applications.",
            f"It is useful to analyze {tema} by identifying what it means, where it appears, and how it is commonly used.",
            f"A good educational summary should connect {tema} with examples, related concepts, and practical relevance.",
            f"This helps transform isolated information about {tema} into a clearer and more structured understanding.",
            f"In summary, researching {tema} supports broader knowledge and better interpretation of the subject."
        ]

    while len(frases) < 5:
        frases.append(frases[-1])

    resumo = "\n".join(frases[:5])
    cache[chave] = resumo

    return resumo


@app.route('/pesquisar', methods=['GET'])
def pesquisar():
    start_time = time.time()

    tema = request.args.get('tema', '').strip()

    if not tema:
        return jsonify({"erro": "Please enter a topic."})

    resultados = buscar_google(tema)
    filtrados = filtrar_resultados(resultados)

    if len(filtrados) < 4:
        filtrados = construir_resultado_emergencial(tema)

    resumo = gerar_resumo_educacional(tema, filtrados)

    duration = round(time.time() - start_time, 2)

    return jsonify({
        "tema": tema,
        "resultados": filtrados[:6],
        "resumo": resumo,
        "emoji": obter_emoji(tema),
        "execution_time": f"{duration}s",
        "engine": "Wikipedia Smart Research"
    })


if __name__ == '__main__':
    app.run(debug=True, port=5000)