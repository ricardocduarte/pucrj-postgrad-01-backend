from sql_alchemy import banco

class HotelModel(banco.Model):
    #nome físico da tabela
    __tablename__ = 'hotels'
    
    #mapeando os objetos de banco dados
    id = banco.Column(banco.Integer, primary_key =True)
    name = banco.Column(banco.String(50), unique=True, index=True)
    stars = banco.Column(banco.Float(precision=1))
    price = banco.Column(banco.Float(precision=2))
    city = banco.Column(banco.String(50))
      
    
    def __init__(self,id, name, stars, price, city):
        self.id = id
        self.name = name
        self.stars = stars
        self.price = price
        self.city = city
    
    #usado para padronizar o retorno das rotas da api
    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'stars': self.stars,
            'price': self.price,
            'city': self.city
        }
    
    #selecionando o hotel pelo id informado
    @classmethod
    def find_hotel_by_id(cls, id):
        hotel = cls.query.filter_by(id=id).first() 
        #sql que será gerado:
        #select * from hoteis WHERE id = id
        if hotel: 
            return hotel
        return None
    
    #obter todos os hoteis cadastrados
    @classmethod
    def find_all(cls):
        hotel = cls.query.all() 
        #sql que será gerado:
        #select * from hoteis
        if hotel: 
            return hotel
        return None

    #seleciona o hotel pelo nome informado
    @classmethod
    def find_hotel_by_name(cls, hotel_name):
        hotel = cls.query.filter_by(name=hotel_name).first() 
        #sql que será gerado:
        #select * from hoteis WHERE nome = nome_hotel
        if hotel: 
            return hotel
        return None
    
    #cria ou atualiza um hotel, pegando o objeto já convertido
    def save_hotel(self):
        banco.session.add(self)
        banco.session.commit()
        return self
    
    #atualizando o objeto 
    def update_hotel(self, name, stars, price, city):
        self.name = name
        self.stars = stars
        self.price = price
        self.city = city
            
    #remove um hotel, pegando o objeto já convertido
    def delete_hotel(self):
        banco.session.delete(self)
        banco.session.commit()
