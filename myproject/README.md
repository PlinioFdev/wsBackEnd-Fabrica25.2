# Django Library Project (Exemplo para desafio)

Projeto demo com CRUD de duas entidades relacionadas (Author, Book)
e consumo de API externa (REST Countries).

## Requisitos
- Python 3.10+
- pip

## Instalação
1. Criar virtualenv:
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows

2. Instalar dependências:
   pip install -r requirements.txt

3. Rodar migrações:
   python manage.py migrate

4. Criar superuser (opcional):
   python manage.py createsuperuser

5. Rodar servidor:
   python manage.py runserver

## Uso
- Acesse: http://127.0.0.1:8000/authors/  (lista de autores)
- Ao adicionar/editar autor, você pode informar `country_code` (ex: BR) para que o sistema busque dados do país via REST Countries.

## Observações
- Não foi usada a API BuscaCep conforme restrição.
- Troque o serviço em `library/services.py` caso precise usar outra API da lista do instrutor.
