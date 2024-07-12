import wtforms
from wtforms.validators import Length,EqualTo
from models import UserModel

class Registerform(wtforms.Form):
    user_name = wtforms.StringField(validators=[Length(min=4,max=20,message="用户名长度必须在4-20之间")])
    password = wtforms.StringField(validators=[Length(min=6,max=20,message="密码长度必须在6-20之间")])
    password_confirm = wtforms.StringField(validators=[Length(min=6,max=15,message="再次确认密码！")])
    password_confirm = wtforms.StringField(validators=[EqualTo("password",message="两次密码不一致！")])
    
    def validate_user_name(self,field):
        user_name = field.data
        user = UserModel.query.filter_by(user_name=user_name).first()
        if user:
            raise wtforms.ValidationError("用户名已存在！")
        
class Loginform(wtforms.Form):
    user_name = wtforms.StringField(validators=[Length(min=4,max=20,message="用户名长度必须在4-20之间")])
    password = wtforms.StringField(validators=[Length(min=6,max=20,message="密码长度必须在6-20之间")])
