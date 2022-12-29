from config import conexion
from sqlalchemy import Column, types
from datetime import datetime
from sqlalchemy.sql.schema import ForeignKey

class ProductoModel(conexion.Model):
    __tablename__ = 'productos'

    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
    descripcion = Column(type_ = types.String(length=45), nullable=False)
    unidad = Column(type_ = types.Integer, nullable=False)
    imagen = Column(type_=types.String(45))
    stock = Column(type_ = types.Integer, nullable=False)
    entregas = Column(type_ = types.Integer, nullable=False)
    fecha = Column(type_=types.DateTime, name='fecha', default=datetime.now())
    descripcion = Column(type_ = types.String(length=12), nullable=False)
      
    # La clase ForeignKey va en los argumentos adicionales (*args)
    categoriaId = Column(ForeignKey(column='categorias.id'), type_=types.Integer, nullable=False, name='categorias_id')