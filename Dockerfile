FROM python:3.8-slim
WORKDIR /app

# copiar documentos 
COPY requirements.txt requirements.txt
COPY script1.py script1.py

# instalar dependencias
RUN pip install -r requirements.txt

# ejecutar el script
CMD ["python", "script1.py"]
