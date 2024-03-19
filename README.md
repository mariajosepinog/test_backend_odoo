# Prueba Backend ODOO

Este repositorio se utiliza para llevar a cabo la prueba técnica del proceso de selección para el puesto de Desarrollador Backend ODOO.

La prueba está desarrollada utilizando las siguientes tecnologías/frameworks:

- Odoo 16
- Postgres 15
- Docker

## Instalación

Para montar el proyecto en tu máquina local, sigue estos pasos:

1. Clona este repositorio en tu máquina local utilizando Git:

   ```bash
   git clone https://github.com/mariajosepinog/test_backend_odoo
   
2. Contruye la imagen de Docker:
   ```bash
   docker-compose up -d --build
3. Inicializa la base de datos de ser necesario, descomentando el la linea de estar comentada en docker-compose.yml
   ```bash
   command: sh -c "python3 -m debugpy --listen 0.0.0.0:8888 /usr/bin/odoo -i base"
4. Inicia sesion utilizando "admin" como usuario y password
5. Instala el addons test_contacts para poder obtener todos los addons que vas a necesitar.
6. Comencemos!
