from flask import Flask, render_template
from flask import request
from flask import make_response
from flask import flash
from flask_wtf import CSRFProtect
from io import open

import forms
app=Flask(__name__)
app.config['SECRET_KEY']= 'my_secret_key'
csrf=CSRFProtect()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cookie",methods=['GET','POST'])
def cookie():
    reg_user=forms.LoginForm(request.form)
    
    if request.method == 'POST' and reg_user.validate():
        user=reg_user.username.data
        pasw=reg_user.password.data
        datos=user+"@"+pasw
        response.set_cookie('datos_user',datos)
        success_message='Bienvenido {}'.format(user)
        flash(success_message)
    response=make_response(render_template('cookie.html',form=reg_user))
        #print(user+'\n'+pasw)
    #response.set_cookie('nombre_cookie','Fernando')    
    return response

@app.route("/traductor",methods=['GET','POST'])
def traductor():
    reg_traductor = forms.TraductorForm(request.form)
    reg_buscar = forms.BuscarForm(request.form)
    btn1 = request.form.get("Guardar")
    btn2 = request.form.get("Buscar")
    if request.method=="POST" and 'Guardar' in request.form:
        if reg_traductor.validate():
            if btn1=='Guardar':
                español=request.form['esp']
                ingles=request.form['eng']
                g=open('diccionario.txt','a')
                g.write('Espanol: ' + español.lower() + '\n' + 'Ingles: ' + ingles.lower() + '\n')
                
                return render_template("traductor.html",form=reg_traductor,form2=reg_buscar)
    if request.method=="POST" and 'Buscar' in request.form:
        if reg_buscar.validate():
            ingles=None
            español=None
            if btn2=='Buscar':
                idioma=reg_buscar.radios.data
                lenguaje=reg_buscar.textoIngresado.data.lower()
                file=open('diccionario.txt','r')
                lineas=file.readlines()
                mensaje=''
                for linea in lineas:
                    ingles, español = linea.strip().lower().split(' ')
                    
                    if idioma=='español':
                        if lenguaje==ingles:
                            mensaje = f'La traduccion de "{ingles.upper()}" es "{español.upper()}".'
                            break
                    elif idioma=='ingles':
                        if lenguaje==español:
                            mensaje = f'La traduccion de "{español.upper}" es "{ingles.upper}".'
                            break
                if not mensaje:
                    mensaje="La palabra ingresada no existe"
                    file.close()
                return render_template("traductor.html",form=reg_traductor,form2=reg_buscar,mensaje=mensaje)
    return render_template('traductor.html',form=reg_traductor,form2=reg_buscar)

@app.route("/Alumnos",methods=['GET','POST'])
def alumnos():
    reg_alum=forms.UserForm(request.form)
    mat=''
    nom=''
    app=''
    apm=''
    correo=''
    if request.method == 'POST' and reg_alum.validate():
        mat=reg_alum.matricula.data
        nom=reg_alum.nombre.data
        app=reg_alum.apaterno.data
        apm=reg_alum.amaterno.data
        correo=reg_alum.email.data
    return render_template("Alumnos.html",form=reg_alum,mat=mat,nom=nom,app=app,apm=apm,correo=correo)

@app.route("/cajasDinamicas", methods=['GET','POST'])
def cajas():    
    if request.method=="POST":
        n1=request.form.get('txtNum1')
        
        return render_template("cajasDinamicas.html",n1=int(n1))    
    else:
        n1=0
        return render_template("cajasDinamicas.html",n1=n1)

   
@app.route("/promedioCajas",methods=['GET','POST'])
def promedioCajas():
    
    s=request.form.get('val')
    
    
    suma=0
    promedio=0
    #mayor=max(repetido)
    #menor=min(repetido)
    
    mayor=0
    menor=0
    
    #a=[]
    repetido=request.form.get('txtNum1')
    #repetido=request.form.get(list(map(float,'txtNum1')))
    
    result = {} # Meter contador 0
    for dato in repetido:
        if dato == repetido:  
            result[dato]=0 
            result[dato] += 1   # Incrementar el contador de ese dato'''
    #print(result)
    
    for i in range(int(s)):
        suma+=int(request.form.get('txtNum'+str(i+1)))
        promedio+=int(request.form.get('txtNum'+str(i+1)))/int(s)
    
    
    #s2=int(request.form.get('txtNum'+str(numero+1)))
    for numero in range(int(s)):
        if menor==0 and mayor==0:
            menor==numero
            mayor==numero
        else:
            if numero<menor:
                menor=numero
            if numero>mayor:
                mayor=numero
    #result=result,
    #print(mayor,menor)
    return render_template("Pcajas.html",suma=suma,promedio=promedio,result=result,mayor=mayor,menor=menor)


if __name__=="__main__":
    #csrf.init_app(app)
    app.run(debug=True,port=3000)
