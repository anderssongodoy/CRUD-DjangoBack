# Usa una imagen base oficial de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de requisitos
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación
COPY . .

# Expone el puerto en el que la aplicación correrá
EXPOSE 8000

# Define el comando de entrada
CMD ["waitress-serve", "--port=8000", "crud_project.wsgi:application"]