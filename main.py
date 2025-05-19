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
        "nome": "Clovis",
        "idade": 2,
        "hobbies": ["dormir", "comer", "arranhar"]
    }
    return templates.TemplateResponse("home.html", {"request": request, "usuario": usuario})

# Rota sobre - renderiza about.html
@app.get("/sobre", response_class=HTMLResponse)
async def sobre(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})