# Practica1

## Como instalar y ejecutar:

1- Python manage.py makemigrations

2- Python manage.py migrate

3- Python manage.py runserver

## URLS

● http://127.0.0.1:8000/admin (Area de administración)

● http://127.0.0.1:8000 (Home)

## Deploy layers

● **Database layer:** PostgreSQL (Ahorro en costes de operaciones, gran capacidad de almacenamiento, buen sistema de seguridad mediante gestión de usuarios, grupos y contraseñas, estabilidad y confiabilidad) 

● **Cookie storage layer:** Redis, la principal ventaja es la velocidad, utiliza la RAM para almacenar y buscar datos

● **Aplication layer:** practica1

● **Server layer:** Apache Server con wsgi

● **Reverse proxy layer:** NGINX (Alto rendimiento, ligero)
