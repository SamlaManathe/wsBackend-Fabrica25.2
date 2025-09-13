## Workshop Back-End (Fábrica de Sofware, 2025.2)

### 🌏 Projeto Django: Estados e Turismo

Este projeto é uma aplicação Django que gerencia os Estados do Brasil, suas respectivas culturas e seus pontos turísticos. Além disso, consome a API do IBGE para listar os municípios de cada estado.

### ⚙️ Configuração

```bash
python -m venv venv
.venv/Scripts/activate ou souce venv/Scripts/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata estados.json
python manage.py loaddata pontos_turisticos.
python manage.py runserver
```

### 📄 Requisitos

- Python 3.13.7
- Django 5.2.6
- Requests 2.32.5
- Venv (opcional)
<br><br>Requisitos adicionais conforme `requirements.txt`.

### 🔗 Endpoints (URLs)

- Listar —> http://127.0.0.1:8000/estados/<br>

- Adicionar —> http://127.0.0.1:8000/estados/novo/<br>

- Detalhar —> http://127.0.0.1:8000/estados/id/<br>

- Editar —> http://127.0.0.1:8000/estados/id/editar/<br>

- Deletar —> http://127.0.0.1:8000/estados/id/deletar/<br>
<br>Selecionar utilizando a `interface` ou o `id` correspondente.


### ℹ️ Informações

- Cada estado possui uma lista de cidades obtidas via API do IBGE.<br>

- Cada estado possui dois pontos turísticos cadastrados manualmente via `fixtures`.<br>

- As imagens e descrições dos estados podem ser alteradas no fixture `estados.json`.<br>
