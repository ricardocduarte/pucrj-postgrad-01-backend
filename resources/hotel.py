from flask_restful import reqparse, Resource
from models.hotel import HotelModel

#definindo as classes da api REST
class Hotels(Resource):
    def get(self):
        todos_hoteis = [hotel.json() for hotel in HotelModel.find_all()] #transformando a lista de hoteis no modelo json
        if todos_hoteis:
            return {'message': todos_hoteis}, 200 #retorna todos os hoteis cadastrados na base
        return {'message': 'hotel not found'}, 200
    
class NewHotel(Resource):
    def post(self):
        #tratando as propriedades do objeto recebido
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('name')
        argumentos.add_argument('stars')
        argumentos.add_argument('price')
        argumentos.add_argument('city')
        dados = argumentos.parse_args()
            
        #fazendo uma crítica básica para garantir o mínimo de integridade no banco
        if dados["name"] == None:
            return {'message': 'invalid value for name field'}, 400
            
        if dados["stars"] == None:
            return {'message': 'invalid value for stars field'}, 400
            
        if dados["price"] == None:
            return {'message': 'invalid value for stars field'}, 400
            
        if dados["city"] == None:
            return {'message': 'invalid value for city field'}, 400
            
        #para evitar duplicidade no banco
        busca_hotel = HotelModel.find_hotel_by_name(dados["name"])
        if busca_hotel:
            return {'message': 'hotel {} already exists' .format(dados["name"])}, 400 #retorna erro se estiver tentando cadastrar um nome de hotel que já existe na base

        hotel = HotelModel(None,**dados)
        hotel_criado = hotel.save_hotel()
        return {'message': hotel_criado.json()}, 201 #retorna o objeto hotel cadastrado
    
class Hotel(Resource):       
    
    def get(self,id):
        hotel =  HotelModel.find_hotel_by_id(id) 
        if hotel:
            return {'message': hotel.json()}, 200 #converte e retorna o objeto hotel com os dados 
            return {'message': 'hotel not found'}, 404

    def put(self,id):
        #pegando os agumentos do corpo da requisição
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('name')
        argumentos.add_argument('stars')
        argumentos.add_argument('price')
        argumentos.add_argument('city')
        dados = argumentos.parse_args()
                    
        hotel_encontrado = HotelModel.find_hotel_by_id(id)
        if hotel_encontrado:
            #convertendo no objeto Hotel                        
            hotel_encontrado.update_hotel(**dados)
            #atualizando no banco de dados
            hotel_atualizado = hotel_encontrado.save_hotel()
            return {'message': hotel_atualizado.json()}, 200 #retorna o objeto hotel atualizado
        return {'message': 'hotel not found'}, 404 #retorna o objeto hotel atualizado 

    def delete(self,id):
        hotel = HotelModel.find_hotel_by_id(id)
        if hotel:
            hotel.delete_hotel()
            return {'message' : 'deleted'}, 200
        return {'message' : 'hotel not found'}, 404
    

    
        