from sqlalchemy.orm import Session
from . import models, schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_clave_cifrada(clave):
    return pwd_context.hash(clave)

def crear_usuario(db: Session, usuario: schemas.CrearUsuario):
    clave_cifrada = get_clave_cifrada(usuario.clave)
    usuario_db = models.Usuario(nombre_usuario = usuario.nombre_usuario, 
    clave_cifrada = clave_cifrada, privilegio = usuario.privilegio)
    db.add(usuario_db)
    db.commit()
    db.refresh(usuario_db)
    return usuario_db
    #Hola esto es un comentario
