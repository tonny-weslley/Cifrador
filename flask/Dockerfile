# Use the official Python 3.10 image as a base
FROM python:3.10-alpine

WORKDIR /code

# Instale as dependências do aplicativo
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código do aplicativo
COPY . /code/

# Exponha a porta que o Flask irá escutar
EXPOSE 5000

# Comando para iniciar o aplicativo Flask
CMD ["python3", "main.py"]