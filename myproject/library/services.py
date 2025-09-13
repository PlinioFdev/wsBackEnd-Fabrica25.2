import requests

def buscar_livro_por_isbn(isbn):
    url = f"https://openlibrary.org/isbn/{isbn}.json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return {
            "titulo": data.get("title", "Título não encontrado"),
            "numero_paginas": data.get("number_of_pages", "N/A"),
            "ano": data.get("publish_date", "N/A")
        }
    else:
        return {"erro": "Livro não encontrado na Open Library"}
