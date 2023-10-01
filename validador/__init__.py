from flask import Flask

def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tutorial_canciones.db'
    #  flag para las modificaciones en desarrollo
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  

    # Configuracion JWT
    app.config['JWT_SECRET_KEY']= 'frase-secreta'
    app.config['PROPAGATE_EXCEPTIONS'] = True
    return app