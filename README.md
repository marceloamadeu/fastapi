# FastAPI / uv / Data Science

<p align="center">
  <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI">
</p>

<p align="left">
<a href="https://pypi.org/project/fastapi" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058" alt="Supported Python versions">
</a>

</p>

---

## Creating a virtual environment

```bash
# uv supports creating virtual environments, e.g., to create a virtual environment at .venv:
$ uv venv
```

## Using a virtual environment

```bash
# When using the default virtual environment name, uv will automatically find and use the virtual environment during subsequent invocations.
$ uv venv

# Install a package in the new virtual environment
$ uv pip install ruff

# The virtual environment can be "activated" to make its packages available:

# Linux
$ source .venv/bin/activate

#windows
.venv\Scripts\activate

# Deactivating an environment
$ deactivate

```

## Creating a new project (Ex - project name: fastapi)

```bash
# You can create a new Python project using the uv init command:

$ uv init fastapi
$ cd fastapi

# Alternatively, you can initialize a project in the working directory:

$ mkdir fastapi
$ cd fastapi
$ uv init

# uv will create the following files:
.
├── .python-version
├── README.md
├── main.py
└── pyproject.toml

# The main.py file contains a simple "Hello world" program. Try it out with uv run:

$ uv run main.py
```

## pyproject.toml
```bash
The pyproject.toml contains metadata about your project:

pyproject.toml

[project]
name = "fastapi"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
dependencies = []
```

## For example, to use flask:
```bash
$ uv add flask
$ uv run -- flask run -p 3000
```

## Or, to run a script:
```python
# Require a project dependency
import flask

print("hello world")
```
```bash
$ uv run example.py
```
### Alternatively, you can use uv sync to manually update the environment then activate it before executing a command:

### Linux
```bash
$ uv sync
$ source .venv/bin/activate
$ flask run -p 3000
$ python example.py
```

### Windows
```bash
uv sync
source .venv\Scripts\activate
$ flask run -p 3000
$ python example.py
```

### Building distributions
uv build can be used to build source distributions and binary distributions (wheel) for your project.

By default, uv build will build the project in the current directory, and place the built artifacts in a dist/ subdirectory:

```bash
uv build
ls dist/
```
See the documentation on building projects for more details (https://docs.astral.sh/uv/concepts/projects/build/).


### Jinja2
```bash
$ uv pip install jinja2
```

## Example / Project Structure - FastAPI + Jinja2

### 📁 Estrutura do Projeto

```bash
fastapi/
│
├── main.py                  # Arquivo principal da app FastAPI
│
├── templates/               # Pasta com os templates HTML
│   ├── base.html            # Layout principal (herdado)
│   ├── home.html            # Página inicial
│   └── about.html           # Página "Sobre"
│
└── static/                  # Arquivos estáticos (CSS, JS, imagens)
    └── style.css            # Estilo global
```

### 1. Install the dependencies If you haven't already installed them, run the following in the terminal:
```bash
pip install fastapi jinja2 uvicorn
```

### 2. main.py – Arquivo principal do FastAPI
```python
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Configuração dos templates
templates = Jinja2Templates(directory="templates")

# Servir arquivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Rota principal - renderiza home.html
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    usuario = {
        "nome": "Lucas",
        "idade": 25,
        "hobbies": ["ler", "jogar", "viajar"]
    }
    return templates.TemplateResponse("home.html", {"request": request, "usuario": usuario})

# Rota sobre - renderiza about.html
@app.get("/sobre", response_class=HTMLResponse)
async def sobre(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})
```

### 3. templates/base.html – Template base (main layout )
```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Página Inicial{% endblock %}</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>

<header>
    <h1>Meu Site com FastAPI + Jinja2</h1>
    <nav>
        <a href="/">Home</a> |
        <a href="/sobre">Sobre</a>
    </nav>
</header>

<main>
    {% block content %}
    <p>Conteúdo padrão (será substituído pelas páginas filhas).</p>
    {% endblock %}
</main>

<footer>
    <p>&copy; 2025 - Todos os direitos reservados.</p>
</footer>

</body>
</html>
```

### 4. templates/home.html – Página inicial
### Herda de base.html e preenche o bloco content.
```html
{% extends "base.html" %}

{% block title %}
Perfil de {{ usuario.nome }}
{% endblock %}

{% block content %}
<h2>Bem-vindo(a), {{ usuario.nome }}!</h2>
<p>Você tem <strong>{{ usuario.idade }}</strong> anos.</p>

<h3>Hobbies:</h3>
<ul>
    {% for hobby in usuario.hobbies %}
        <li>{{ hobby }}</li>
    {% endfor %}
</ul>
{% endblock %}
```

### 5. templates/about.html – Página Sobre
### Outra página que herda de base.html.
```html
{% extends "base.html" %}

{% block title %}
Sobre Nós
{% endblock %}

{% block content %}
<h2>Sobre o site</h2>
<p>Este é um exemplo simples de como usar FastAPI com Jinja2 para criar páginas HTML dinâmicas.</p>
<p>O projeto foi feito para fins educacionais e demonstra a integração entre as tecnologias.</p>
{% endblock %}
```

### 6. static/style.css
```css
body {
    font-family: Arial, sans-serif;
    background-color: #f9f9f9;
    color: #333;
    margin: 0;
    padding: 0;
}
header {
    background-color: #0078d4;
    color: white;
    padding: 20px;
    text-align: center;
}
nav a {
    color: white;
    margin: 0 10px;
    text-decoration: none;
}
main {
    padding: 20px;
}
footer {
    background-color: #eee;
    text-align: center;
    padding: 10px;
    font-size: 0.9em;
}
```
### Rodando a Aplicação
### No terminal, dentro da pasta do projeto:
```bash
$ uvicorn main:app --reload
```
### Acesse:
```bash
http://127.0.0.1:8000 → Home
http://127.0.0.1:8000/sobre → Sobre
```
#### ✅ Benefícios dessa abordagem
- Você pode ter uma API REST completa com documentação automática (Swagger / Redoc).
- Além disso, consegue servir páginas HTML dinâmicas com Jinja2 , se precisar.
- Tudo isso com alta performance , graças ao FastAPI.

#### 🚀 Próximos passos sugeridos
Se quiser continuar evoluindo nesse projeto, posso te ajudar com:

- Login de usuário com sessões (usando request.session)
- Formulários POST com validação
- Banco de dados (SQLite, PostgreSQL, SQLAlchemy)
- Templates reutilizáveis com {% include %} e {% macro %}
- Componentes reativos com HTMX ou JavaScript