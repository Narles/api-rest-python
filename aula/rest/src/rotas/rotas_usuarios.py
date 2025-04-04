from fastapi import APIRouter, Depends, status, HTTPException
import esquemas, repositorio
from banco_de_dados import obter_sessao
from configuracao import logger
from sqlalchemy.orm import Session

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

# Metodo POST
# ENDPOINT: http://localhost:8000/usuarios/
@router.post("/", response_model=esquemas.UsuarioResposta, status_code=status.HTTP_201_CREATED)
def criar_usuario(usuario:esquemas.UsuarioCriacao, db: Session = Depends(obter_sessao)):
    try:
        novo_usuario = repositorio.criar_usuario(db, usuario)
        logger.info(f"Usuário criado: {novo_usuario} - ID: {novo_usuario.id}")
        #return { "mensagem":"Usuário criado com sucesso.", "data": novo_usuario}
        return novo_usuario
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Erro: "+str(e))

# Metodo GET
# ENDPOINT: http://localhost:8000/usuarios/
@router.get("/")
def obter_usuarios(db: Session = Depends(obter_sessao)):
    try:
        usuarios = repositorio.obter_usuarios(db)
        logger.info(usuarios)
        return usuarios
        #return { "mensagem":"Usuário criado com sucesso.", "data": novo_usuario}
        #return esquemas.UsuarioResposta( id = usuarios.id, nome = usuarios.nome, email = usuarios.email   )
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Erro: "+str(e))
