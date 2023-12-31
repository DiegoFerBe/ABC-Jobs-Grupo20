from flask import Flask

#from app import create_app

#from .modelos import db, Cancion, Usuario, Album, Medio
#from .modelos import AlbumSchema, UsuarioSchema

# Flask-RESTful es una extensión de Flask que facilita la creación de APIs RESTful en Flask. 
# Proporciona una abstracción sobre las operaciones HTTP (GET, POST, PUT, DELETE, etc.) 
# y permite definir recursos y rutas de manera sencilla.
from flask_restful import Api
from flask_jwt_extended import JWTManager

from .vistas import ViewVoting, User


app = Flask('validador')


#app = create_app('default') 
app_context = app.app_context()
app_context.push()

# Registrar el manejador de excepciones
#app.errorhandler(Exception)(handle_exception)

#Comando para instalar los cors --> pip install flask.core
#cors = CORS(app)

api = Api(app)
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)

api.add_resource(User, '/user')
api.add_resource(ViewVoting, '/ver-resultados')



#Comando para la instalación de JWT, para generación de Tpkens --> pip install flask-jwt-extended


