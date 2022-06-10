# habi-test-api-rest

api desarrollada en servidor con virtual environtment .venv con python 3.8.9

Se crea una estructura 

Para utilizar el API se deben seguir los siguientes pasos despues del checkout.

En linea de comandos ubicarse dentro de la carpeta descargada:

habi-test-api-rest %

para ejecutar el API se debe crear un virtual environtment posicionado en la carpeta descargada:

Descarga de virtual Env (en caso de no tenerlo instalado):

Unix/macOS
python3 -m pip install --user virtualenv

Windows
py -m pip install --user virtualenv


Creación de Virtual Env:

Unix/macOS
python3 -m venv .venv

Windows
py -m venv .venv


una vez creado se utiliza el siguiente comando para activar el entorno virtual:

source .venv/bin/activate

Se actualiza pip:

Unix/macOS
python3 -m install --upgrade pip

Windows
py -m install --upgrade pip

Posteriormente se realiza la instalación de las dependencias con el siguiente comando

pip install -r requeriments.txt


Se debe modificar el password en el archivo conf.ini Linea (20) y cambiar XXXXXX por el password real de la DB

para iniciar la aplicación se ejecuta el siguiente comando:

python app.py

1. Servicio de consulta

endpoint:

GET

Option 1:
http://127.0.0.1:5000/property?state=pre_venta

Option 2:
http://127.0.0.1:5000/property?state=pre_venta&year=2000

Option 3:
http://127.0.0.1:5000/property?state=pre_venta&year=2000&city=bogota

para el endpoint es obligatoria la variable state, las demas no son obligatorias y solo se tendra en cuenta si estan correctamente escritas

state(string)
year(integer)
city(string)

El modelo entidad relación se encuentra en el repositorio, archivo llamado:
ER_Optimized.png
https://github.com/tomdeveloper1991/habi-test-api-rest/blob/ec5fac036cf60763c6536186aa1b4022ffab1dfc/ER_Optimized.png

Codigo para extender el modelo de base de datos para el modulo de like:

CREATE TABLE like_history (
    id int NOT NULL,
    property_id int NOT NULL,
    user_id int NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (property_id) REFERENCES property(id),
    FOREIGN KEY (user_id) REFERENCES auth_user(id)
);