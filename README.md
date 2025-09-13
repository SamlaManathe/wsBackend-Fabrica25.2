# Workshop Back-End (Fábrica de Sofware, 2025.2)

## 🌏 Projeto Django: Estados e Turismo

Este projeto é uma aplicação Django que gerencia os Estados do Brasil, suas respectivas culturas e seus pontos turísticos. Além disso, consome a API do IBGE para listar os municípios de cada estado.

<img style="display: flex; align-items: center;" width="50%" height="25%" alt="Interface" src="https://github.com/user-attachments/assets/11fab228-5f26-47a9-9cb6-000ad65038b8" />

## ⚙️ Configuração

**Passo 1:** Criar o ambiente virtual
```bash
python -m venv venv
```
**Passo 2:** Ativar o ambiente virtual

Windows
```bash
.venv/Scripts/activate
```
Linux/Mac
```bash
souce venv/Scripts/activate
```
**Passo 3:** Instalar dependências
```bash
pip install -r requirements.txt
```
**Passo 4:** Criar as migrações
```bash
python manage.py makemigrations
```
**Passo 5:** Aplicar as migrações
```bash
python manage.py migrate
```
**Passo 6:** Carregar os dados iniciais (fixtures)
```bash
python manage.py loaddata estados.json
python manage.py loaddata pontos_turisticos.
```
**Passo 7:** Rodar o servidor
```bash
python manage.py runserver
```

## 📄 Requisitos

- Python 3.13.7
- Django 5.2.6
- Requests 2.32.5
- Venv (opcional)
<br><br>Requisitos adicionais conforme `requirements.txt`.

## 🔗 Endpoints (URLs)

- Listar —> http://127.0.0.1:8000/estados/<br>

- Adicionar —> http://127.0.0.1:8000/estados/novo/<br>

- Detalhar —> http://127.0.0.1:8000/estados/id/<br>

- Editar —> http://127.0.0.1:8000/estados/id/editar/<br>

- Deletar —> http://127.0.0.1:8000/estados/id/deletar/<br>
<br>Selecionar utilizando a `interface` ou o `id` correspondente.


## ℹ️ Informações

- Cada estado possui uma lista de cidades obtidas via API do IBGE.<br>

- Cada estado possui dois pontos turísticos cadastrados manualmente via `fixtures`.<br>

- As imagens e descrições dos estados podem ser alteradas no fixture `estados.json`.<br>

