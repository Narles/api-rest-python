from fastapi import FastAPI
from banco_de_dados import motor, Base
from configuracao import logger
from rotas import rotas_usuarios

app = FastAPI(
    title="API teste",
    version='1.0',
    description="Apenas testando...",
    openapi_url="/api/v1/openapi.json"
)

# Endpoint /test - GET
@app.get('/test')
def testa_status():
    return {"mensagem": "aplicação ok" }

@app.on_event("startup")
async def startup():
    Base.metadata.create_all(bind=motor)
    logger.info("Tabelas do banco foram criadas com suecesso!")

app.include_router(rotas_usuarios.router)