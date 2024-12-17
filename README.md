# Proyecto Citybikes

## Descripción
Este proyecto contiene dos scripts en Python que interactúan con la API de Citybikes y una base de datos MongoDB. 

## Requisitos
- Python 3.x
- Docker 

## Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/citybikes-project.git
cd citybikes-project 

### 2. Instalar dependencias  
```bash
pip install -r requirements.txt

### 3. Ejecutar scripts
Antes que nada poner a funcionar nuestro docker con la base de datos:

docker run -d --name mongodb -p 27017:27017 mongo

Puedes ejecutar los scripts por linea de comandos, el primer script lo puedes ejecutar con Docker. Por línea de comandos sería:  
```bash
python script1.py
```bash
python script2.py

### 4. Ejecutar script 1 con Docker
Tienes que ejecutarlo a partir de la imagen subida en Docker Hub: citybikes-script1

despues de hacer docker ps y comprobar que funciona ejecutar el script con docker:

docker run -d --name citybikes-script1 --link mongodb:mongo noeliasd03/citybikes-script1
