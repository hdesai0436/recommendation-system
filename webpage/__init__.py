from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "helloworld"
    
    


    from .views import views
   
    app.register_blueprint(views,url_prefix='/')
   

    

    

    
    # @login_manager.user_loader
    # def load_user(id):
    #     return User.query.get(int(id))
    return app

# def create_database(app):
#     if not path.exists('webpage/' + DB_NAME):
#         db.create_all(app=app)
#         print('data createxd')
