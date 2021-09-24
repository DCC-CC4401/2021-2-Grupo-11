# Comandos para instalar django

    python -m venv env
    env\Scripts\activate
    cd project1
    python -m pip install --upgrade pip
    pip install -r requirements.txt

# Comandos para usar env

    env\Scripts\activate
    cd project1

# Para crear un superusuario

    python manage.py createsuperuser

# Para importar las bases de datos
# Antes es necesario borrar el archivo db.sqlite3 y las carpetas migrations
# Esto se hace solo la primera vez que se corre el server

    python manage.py makemigrations Componentes Web
    python manage.py migrate
    python manage.py loaddata componentes/json/computer_cases.json
    python manage.py loaddata componentes/json/cpu_coolers.json
    python manage.py loaddata componentes/json/motherboards.json
    python manage.py loaddata componentes/json/power_supplies.json
    python manage.py loaddata componentes/json/processors.json
    python manage.py loaddata componentes/json/rams.json
    python manage.py loaddata componentes/json/solid_state_drives.json
    python manage.py loaddata componentes/json/storage_drives.json
    python manage.py loaddata componentes/json/video_cards.json

# Comandos para correr django

    python manage.py makemigrations Componentes Web
    python manage.py migrate
    python manage.py runserver