import requests

REST_COUNTRIES_BASE = "https://restcountries.com/v3.1"

def get_country_by_code(code):
    """
    Retorna dicionário com informações do país (ou None se não encontrado).
    Usa endpoint /alpha/{code}
    """
    if not code:
        return None
    url = f"{REST_COUNTRIES_BASE}/alpha/{code}"
    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        data = resp.json()
        # data é lista com um objeto ou um objeto — garantir
        item = data[0] if isinstance(data, list) else data
        # extrair nome comum e outras info
        name = item.get('name', {}).get('common', '')
        capitals = item.get('capital', [])
        region = item.get('region', '')
        return {
            'name': name,
            'capital': capitals[0] if capitals else '',
            'region': region,
            'raw': item,
        }
    except requests.RequestException:
        return None
