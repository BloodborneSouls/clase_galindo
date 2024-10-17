from sqlalchemy import Boolean, Column, Integer, String, Text
from .database import Base

class Usuario(Base):
    __tablename__ = "usuarios_2"

    id = Column(Integer, primary_key=True, index=True)
    nombre_usuario = Column(String(30), unique=True, index=True)
    clave_cifrada = Column(Text)
    activo = Column(Boolean, default=True)
    #Cree este campo para verificar la existencia de un administrador XD
    privilegio = Column(Boolean, default=False)