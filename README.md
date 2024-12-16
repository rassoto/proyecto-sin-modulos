# ProyectoTallerAutomotriz
Es una aplicacion web creada con django y nodejs para implementar un sistema de gestion automotriz


# ProyectoTallerAutomotriz
Es una aplicacion web creada con django y nodejs para implementar un sistema de gestion automotriz


para hacer funcionar el programa se debe instalar varias cosas en cada carpeta

en la carpeta node debes instalar 
npm install nodejs
npm install express firebase-admin
npm install punycode



y en la carpeta django instalar un entorno virtual
si aun no tienes la virtualizacion pon esto

pip install virtualenv

si ya lo tenias no es necesario instalarlo y prosigue con esto 

Python -m venv entorno    entorno es como yo la llame puedes ponerle el nombre que quieras

luego ingresamos al entorno creado 
cd entorno 
cd scripts
.\Activate.ps1

y al estar dentro del entorno instalamos django

 pip install django

 luego fuera del entorno creamos el proyecto
 pip install requests

 django-admin startproject MiProyectoDjango .

miproyectodjango lo puedes cambiar por el nobre que desees 

luego se crea la app 
python manage.py startapp nombre_app
 
 y estariamos listos para usarlo