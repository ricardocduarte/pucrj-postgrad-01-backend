import os
from flask import Flask
from sql_alchemy import banco
from pathlib import Path
from flask_restful import Api
from resources.hotel import Hotels, Hotel, NewHotel


app = Flask (__name__)
api = Api(app)

#definindo a localização do banco de dados
db_path = os.path.join(Path(__file__).parent.resolve(),'database', 'hotel.sqlite3')
db_uri = 'sqlite:///{}'.format(db_path)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
#desabilitando os warnings do framework
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#api = Api(app, title='API Sprint 01 - Controle de Hotéis', version='1.0', description='MVP - Pós Gradução Engenharia de softwares',prefix='/')
banco.init_app(app)

#vinculando as rotas de publicação
#initialize_routes(api)

#definindo que o banco de dados será criado de forma automática
with app.app_context():
    banco.create_all()

api.add_resource(Hotels, '/hotels')
api.add_resource(Hotel, '/hotel/<int:id>')
api.add_resource(NewHotel, '/hotel')

if __name__  == '__main__':
    app.run(debug=True)
    

    