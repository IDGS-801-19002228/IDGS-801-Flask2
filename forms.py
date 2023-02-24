from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField

from wtforms.fields import EmailField, TextAreaField, RadioField, PasswordField
from wtforms import validators

def mi_validacion(form,field):
    if len(field.data)==0:
        raise validators.ValidationError('El campo no tiene datos')

class UserForm(Form):
    matricula=StringField('Matricula',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=10,message='long de campo 4 min and 5 max')
    ])
    nombre=StringField('Nombre',[
        validators.DataRequired(message='El campo es requerido')
    ])
    apaterno=StringField('Apaterno')
    amaterno=StringField('Amaterno',[
        mi_validacion
    ])
    email=EmailField('Correo')
    
class LoginForm(Form):
    username=StringField('Usuario',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=10,message='long de campo 4 min and 5 max')
    ])
    password=StringField('Contraseña',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=10,message='long de campo 4 min and 5 max')
    ])
    
class TraductorForm(Form):
    esp=StringField('Español',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=10,message='long de campo 4 min and 5 max')
    ])
    eng=StringField('Ingles',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=10,message='long de campo 4 min and 5 max')
    ])
    radios = RadioField(choices=[('1', 'Español'), ('2', 'Ingles')],default='0')
    textoIngresado = StringField('Ingresa la palabra a buscar',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=10,message='long de campo 4 min and 5 max')
    ])