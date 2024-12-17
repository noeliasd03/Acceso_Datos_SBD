# Proyecto Citybikes

## Descripción
Este proyecto contiene dos scripts en Python que interactúan con la API de Citybikes y una base de datos MongoDB. 

## Requisitos
- Python 3.x
- Docker 

## Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/noeliasd03/Acceso_Datos_SBD.git
cd Acceso_Datos_SBD
```
### 2. Instalar dependencias  
```bash
pip install -r requirements.txt
```
### 3. Ejecutar scripts
Antes de ejecutar los scripts, asegúrate de que MongoDB esté funcionando: 
```bash
docker run -d --name mongodb -p 27017:27017 mongo
```
Puedes ejecutar los scripts por linea de comandos. El primer script también se puede ejecutar con Docker. Por línea de comandos sería:  
```bash
python script1.py
```
```bash
python script2.py
```
### 4. Ejecutar script 1 con Docker
Para ejecutar el script 1 usando Docker, utiliza la imagen subida en Docker Hub:
Asegúrate de que el contenedor de MongoBD esté funcionando antes de ejecutarlo.
```bash
docker run -d --name citybikes-script1 --link mongodb:mongo noeliasd03/citybikes-script1
```
