from flask import Flask, render_template
from flask import request


import forms
app=Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/Alumnos",methods=['GET','POST'])
def alumnos():
    reg_alum=forms.UserForm(request.form)
    mat=''
    nom=''
    app=''
    apm=''
    correo=''
    if request.method == 'POST':
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
    app.run(debug=True,port=3000)