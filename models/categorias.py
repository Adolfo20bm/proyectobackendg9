from config import conexion
from sqlalchemy import Column, types
from datetime import datetime

class CategoriaModel(conexion.Model):
    __tablename__='categorias'

    id = Column(type_ = types.Integer, autoincrement=True, primary_key=True, nullable= False)
    categoria = Column(type_ = types.String(length=45), nullable=False)
    fecha = Column(type_=types.DateTime, name='fecha', default=datetime.now())
    