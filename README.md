
django-admin startproject TiendaOnline

En cada projecto se puede crear 1 o varias aplicaciones. Estas aplicaciones son reutilizables en otros proyectos.
Una vez creado el projecto TiendaOnline creamos la primera aplicacion que se llamará gestionPedidos
Vamos a la carpeta del proyecto TiendaOnline y en consola:

python manage.py startapp gestionPedidos

BBDD con SQLLITE3

Se registra en el proyecto en settings.py -> INSTALLET_APPS la aplicacion gestionPedidos

Para empezar crearemos Models. Una clase por cada tabla que necesites en la BBDD
Clases : Tabla Clientes, Tabla Pedidos y Tabla Artículos

Una vez creados los modelos vamos a la consola:
python manage.py makemigrations
python manage.py sqlmigrate gestionPedidos(nombre aplicacion) 0001(num migracion)
python manage.py migrate


CON SQLLITE3

INSERTAR, ACTUALIZAR Y BORRAR REGISTROS: desde la consola de momento:
python manage.py shell
from gestionPedidos.models import Articulos

CREATE
art = Articulos(nombre='mesa', seccion='decoracion', precio=90)
art.save()

ó

art3 = Articulos.objects.create(nombre='taladros', seccion='ferreteria', precio=65)


UPDATE
art.seccion='decoración'
art.save()

DELETE
art5 = Articulo.objects.get(id=1)
art5.delete()






CON POSTGRESQL

Vamos a pgAdmin, password: 5732

Y creamos las bases de datos, vamos a la BBDD de postgres boton derecho y query tool, para crearla por codigo sql:

create database gestion_pedidos

Conectamos el proyecto django con esta bbdd
Instalamos la libreria para conectar: carpeta de proyecto:
pip install psycopg2



VAMOS A settings.py -> DATABASES

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gestion_pedidos',
        'USER': 'postgres',
        'PASSWORD': '5732',
        'HOST': '127.0.0.1',
        'DATABASE_PORT': '5432',
    }


Y CREAMOS REGISTROS DE LA MISMA FORMA QUE CON SQLLITE3 POR CONSOLA, MAS A DELANTE LOS CREAMOS CON FORMULARIOS

CONSULTAS CON WHERE EN CONSOLA:

Articulos.objects.filter(seccion='deporte')    #filter() lo de dentro de los parantesis es el where de siempre

Devuelve dos objetos porque hay 2 rows de deportes
<QuerySet [<Articulos: Articulos object (5)>, <Articulos: Articulos object (6)>]>

Para conseguir la info de los objetos:

Vamos a la clase y añadimos la funcion:

def __str__(self):
        return 'El nombre es %s, la sección es %s con precio %s' %(self.nombre, self.seccion, self.precio)

Hacemos la migraciones otra vez desde la raiz del proyecto

Volvemos al python manage.py shell

Articulos.objects.filter(seccion='deporte')

<QuerySet [<Articulos: El nombre es balón, la sección es deporte con precio 30>,
 <Articulos: El nombre es raqueta, la sección es deporte con precio 45>]>

Mas de un criterio, se pueden agregar varios criterios de busqueda, es decir, id o nombre o id y seccion

Articulos.objects.filter(nombre='raqueta', seccion='deporte')
<QuerySet [<Articulos: El nombre es raqueta, la sección es deporte con precio 45>]>

Articulos.objects.filter(seccion='deporte', precio__gte=40) #mayor que
Articulos.objects.filter(seccion='deporte', precio__lte=40) #menor que
Articulos.objects.filter(seccion='deporte', precio__range(40, 50)) #entre dos valores
Articulos.objects.filter(precio__gte=50).order_by('precio') #ordena
Articulos.objects.filter(precio__gte=50).order_by('-precio') #ordena desc











