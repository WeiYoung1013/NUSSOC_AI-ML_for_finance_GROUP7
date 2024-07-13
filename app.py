from flask import Flask, request, session, g, make_response, jsonify
import config
from blueprints.homepage import hp
from blueprints.strategy import st
from blueprints.auth import auth
from extends import db, cache
from flask_migrate import Migrate
from models import UserModel


app = Flask(__name__)
app.secret_key = 'gaiucsahsaiuubviyh2'
app.config.from_object(config)
db.init_app(app)
migrate = Migrate(app, db)
# 配置缓存
cache.init_app(app, config={'CACHE_TYPE': 'simple'})  # 使用简单缓存


app.register_blueprint(hp)
app.register_blueprint(st)
app.register_blueprint(auth)

@app.before_request
def my_before_request():
    if 'user_name' in session:
        user_name = session['user_name']
        user = UserModel.query.get(user_name)
        setattr(g,"user",user)
    else:
        setattr(g,"user",None)
        
@app.context_processor
def my_context_processor():
    return {"user":g.user}

if __name__ == '__main__':
    app.run(debug=True)