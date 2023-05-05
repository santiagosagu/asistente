añadir variables de entorno
C:\Users\USER\AppData\Local\Programs\Python\Python311
C:\Users\USER\AppData\Local\Programs\Python\Python311\Scripts

asegurarse de tener instalado Virtualenv
pip install virtualenv

virtualenv env

despues de tener python
source env/Scripts/activate # debe aparecerte en la consola entre parentesis env windows
source env/bin/activate # linux

instalar un lector de variables de entorno
pip install python-dotenv

crear un .env
y pegar ahi las key de las variables de entorno siguientes:

OPENIA=
OPEN_WEATHER_MAP=
WIT_API=

instalar paquetes
pip install -r requirements.txt

asegurarse que todos los paquetes esten instalos en el archivo asistente-three.py

correr el programa
python asistente-three.py

parar el entorno
deactivate
