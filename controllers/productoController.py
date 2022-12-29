from flask_restful import Resource, request
from config import conexion
from models.productos import ProductoModel
from models.categorias import CategoriaModel
from dtos.productoDto import ProductoRequestDto

class ProductosController(Resource):
    def get(self):
        
        productos = conexion.session.query(ProductoModel).all()

        serializador = ProductoRequestDto(many=True)
    
        data = serializador.dump(productos)
    
        return {
            'message': 'Los productos son:',
            'content': data
        }

    def post(self):
        body = request.get_json()
        try:
            serializador = ProductoRequestDto()
            dataSerializada = serializador.load(body)
            # buscar si existe el categoria con ese id, si no existe emitir un error indicando que el categoria no existe
            # dataSerializada.get('categoriaId') > esta el categoria
            categoriaEncontrado = conexion.session.query(CategoriaModel).filter_by(id= dataSerializada.get('categoriaId')).first()
            # if categorriaEncontrado is None:
            if not categoriaEncontrado:
                raise Exception('categoria no existe')

            nuevoProducto = ProductoModel(**dataSerializada)
            conexion.session.add(nuevoProducto)
            conexion.session.commit()

            return {
                'message': 'Producto agregada exitosamente'
            }

        except Exception as error:
            return {
                'message': 'Error al crear Producto',
                'content': error.args
            }

class ProductoController(Resource):
    def get(self, categoriaId):
        # Buscar todas las tareas utilizando el categoriaId y luego serializarlas y devoverlas
        productosEncontrados = conexion.session.query(ProductoModel).filter_by(categoriaId= categoriaId).all()
        serializador = ProductoRequestDto(many=True)
        
        data = serializador.dump(productosEncontrados)
        return {
            'message': 'Los productos son',
            'content': data
        }
    
    def put(self, id):
        try:
            productoEncontrado = conexion.session.query(ProductoModel).filter_by(id=id).first()

            if productoEncontrado is None:
                raise Exception('Producto no existe')
            
            body = request.get_json()
            serializador = ProductoRequestDto()
            data = serializador.load(body)

            # aca sobreescribimos la informacion nueva del Categoria
            productoEncontrado.descripcion = data.get('descripcion')
            productoEncontrado.unidad = data.get('unidad')
            productoEncontrado.imagen = data.get('imagen')
            productoEncontrado.stock = data.get('stock')
            productoEncontrado.entregas = data.get('entregas')
            productoEncontrado.fecha = data.get('fecha')
            productoEncontrado.cod_patrimonial = data.get('cod_patrimonial')
            productoEncontrado.categoriaId = data.get('categoriaId')
            
            conexion.session.commit()

            return {
                'message':'Producto actualizado exitosamente'

            }

        except Exception as error:
            return {
                'message': 'Error al actualizar el Producto',
                'content': error.args
            }
