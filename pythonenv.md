# Comandos para instalar django

    python -m venv env
    env\Scripts\activate
    python -m pip install --upgrade pip
    pip install -r requirements.txt

# Comandos para usar env

    env\Scripts\activate
    cd project1

# Para crear un superusuario

    python manage.py createsuperuser

# Para importar las bases de datos
# Antes es necesario borrar db.sqlite3 y migrations
# Esto se hace solo la primera vez que se corre el server

    python manage.py makemigrations Componentes Web
    python manage.py migrate
    python manage.py loaddata componentes/json/almacenamientos.json
    python manage.py loaddata componentes/json/coolers.json
    python manage.py loaddata componentes/json/fuentespoder.json
    python manage.py loaddata componentes/json/gabinetes.json
    python manage.py loaddata componentes/json/memorias.json
    python manage.py loaddata componentes/json/placasmadre.json
    python manage.py loaddata componentes/json/procesadores.json
    python manage.py loaddata componentes/json/tarjetasvideo.json

# Comandos para correr django

    python manage.py makemigrations Componentes Web
    python manage.py migrate
    python manage.py runserver