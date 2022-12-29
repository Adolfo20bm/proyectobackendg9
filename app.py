from flask import Flask
from flask_migrate import Migrate
from os import environ
from dotenv import load_dotenv
from flask_restful import Api

from config import conexion
from models.categorias import CategoriaModel
from models.productos import ProductoModel
from controllers.categoriaController import CategoriasController, CategoriaController
from controllers.productoController import ProductosController, ProductoController

load_dotenv()
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URI')
app.config['SQLALCHEMY_ECHO'] = environ.get('MOSTRAR_SQL') 
conexion.init_app(app)
migrate = Migrate(app, conexion)

# Declarar todas las rutas que vamos a utilizar mediante los controladores
api.add_resource(CategoriasController, '/categorias')
api.add_resource(CategoriaController, '/categoria/<int:id>')
api.add_resource(ProductosController, '/productos')
api.add_resource(ProductoController, '/producto/<int:id>')
#api.add_resource(ProductoController, '/producto/<int:categoriaId>')

if __name__ == '__main__':
    app.run(debug=True)