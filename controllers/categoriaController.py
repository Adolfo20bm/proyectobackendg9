from flask_restful import Resource, request
from config import conexion
from models.categorias import CategoriaModel
from dtos.categoriaDto import CategoriaRequestDto

class CategoriasController(Resource):
    
    def get(self):
        
        categorias = conexion.session.query(CategoriaModel).all()

        serializador = CategoriaRequestDto(many=True)
    
        data = serializador.dump(categorias)
    
        return {
            'message': 'Los categorias son:',
            'content': data
        }
    
    def post(self):
        body = request.get_json()
        try:
    
            serializador = CategoriaRequestDto()
            dataSerializada =  serializador.load(body)
            print(dataSerializada)

            nuevoCategoria = CategoriaModel(**dataSerializada)

            conexion.session.add(nuevoCategoria)
            # guardar de manera permanente la informacion agregada al nuevo usuario
            conexion.session.commit()

            return {
                'message': 'Categoria creado exitosamente'
            }
        except Exception as error:
            print(error)
            return {
                'message': 'Error al crear categoria',
                'content': error.args
            }


class CategoriaController(Resource):
    def get(self, id):

        categoriaEncontrado = conexion.session.query(CategoriaModel).filter_by(id=id).first()

        serializador = CategoriaRequestDto()

        data = serializador.dump(categoriaEncontrado)

        return {
            'content': data
        }
    
    def put(self, id):
        try:
            categoriaEncontrado = conexion.session.query(CategoriaModel).filter_by(id=id).first()

            if categoriaEncontrado is None:
                raise Exception('Categoria no existe')
            
            body = request.get_json()
            serializador = CategoriaRequestDto()
            data = serializador.load(body)

            # aca sobreescribimos la informacion nueva del Categoria
            categoriaEncontrado.categoria = data.get('categoria')
            categoriaEncontrado.fecha = data.get('fecha')
            

            conexion.session.commit()

            return {
                'message':'Categoria actualizado exitosamente'
            }

        except Exception as error:
            return {
                'message': 'Error al actualizar el Categoria',
                'content': error.args
            }
    
    def delete(self, id):
        try:
            # Buscamos el usuario
            categoriaEncontrado = conexion.session.query(CategoriaModel).filter_by(id=id).first()
            # Si no hay el usuario emitimos un error
            if categoriaEncontrado is None:
                raise Exception('Usuario no existe')
            # asi eliminamos el usuario de la base de datos
            conexion.session.delete(categoriaEncontrado)
            # aqui confirmamos la eliminacion de manera permanente
            conexion.session.commit()
            return {
                'message': 'La Categoria se elimino exitosamente'
            }

        except Exception as error:
            return {
                'message': 'Error al eliminar La Categoria',
                'content': error.args
            }
