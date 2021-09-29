<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/DCC-CC4401/2021-2-Grupo-11">
    <img src="project1/Web/static/web/img/favicon.ico" alt="Logo" width="80" height="80">
  </a>
  <h1 align="center">2021-2-Grupo-11</h1>

  <p align="center">
    Proyecto para Ingeniería de Software
    <br />
    <a href="#"><strong>Explora la documentación »</strong></a>
    <br />
    <br />
  </p>
</p>


<!-- ABOUT THE PROJECT -->
## About The Project

Lorem ipsum dolor sit amet


### Built With

Lorem ipsum dolor sit amet

* [Django](https://www.djangoproject.com/)


<!-- GETTING STARTED -->
## Getting Started

Lorem ipsum dolor sit amet


### Prerequisites

* Ambiente virtual python
    ```sh
    python -m venv env
    env\Scripts\activate
    cd project1
    ```

* Instalar las librerias
    ```sh
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```


### Installation

1. Clonar el repositorio
   ```sh
   git clone https://github.com/DCC-CC4401/2021-2-Grupo-11.git
   ```
2. Activar ambiente virtual
    ```sh
    env\Scripts\activate
    cd project1
    ```
3. Borrar el archivo db.sqlite3 y las carpetas migrations

4. Migrar la base de datos
    ```sh
    python manage.py makemigrations Componentes Web
    python manage.py migrate
    python manage.py loaddata componentes/json/computer_cases.json
    python manage.py loaddata componentes/json/cpu_coolers.json
    python manage.py loaddata componentes/json/gaming_chairs.json
    python manage.py loaddata componentes/json/headphones.json
    python manage.py loaddata componentes/json/keyboards.json
    python manage.py loaddata componentes/json/monitors.json
    python manage.py loaddata componentes/json/motherboards.json
    python manage.py loaddata componentes/json/mouse.json
    python manage.py loaddata componentes/json/power_supplies.json
    python manage.py loaddata componentes/json/processors.json
    python manage.py loaddata componentes/json/rams.json
    python manage.py loaddata componentes/json/solid_state_drives.json
    python manage.py loaddata componentes/json/storage_drives.json
    python manage.py loaddata componentes/json/video_cards.json
    ```
5. Crear el superusuario
    ```sh
    python manage.py createsuperuser
    ```
6. Iniciar el servidor
    ```sh
    python manage.py makemigrations Componentes Web
    python manage.py migrate
    python manage.py runserver
    ```


<!-- USAGE EXAMPLES -->
## Usage

Lorem ipsum dolor sit amet


<!-- LICENSE -->
## License

Lorem ipsum dolor sit amet
