from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.productos import ProductoModel

class ProductoRequestDto(SQLAlchemyAutoSchema):
    class Meta:
        model = ProductoModel
        # cuando nosotros creamos un DTO este solamente servira para las columnas de ese modelo PERO sin ninguna llave foranea
        # si queremos utilizar tambien las llaves foraneas:
        include_fk = True