# Plantilla de Proyecto

## Descripción

Se anexa una plantilla de proyecto para la materia TC2008B, esta permite tener la conexión más básica entre el cliente y servidor.

## Contenido
- Archivo tc2008B_server.py
- WebClient.cs

## Instrucciones
Descarga los archivos contenidos en esta carpeta, por un lado puedes ejecutar el servidor de python directamente ejecutando en terminal la línea.

```
python tc2008B_server 8585
```

El número de puerto es recibido por línea de comando como argumentos, puedes modificarlo si así lo deseas, pero toma en cuenta que **WebClient.cs** ya contiene configurado este puerto por default, si quieres modificarlo deberás modificarlo también.

Una vez que se ejecute el servidor crea un nuevo proyecto de Unity, crea un objeto vacío y ajusta tu proyecto para incorporar el Script de **WebClient.cs** como hemos visto en los laboratorios.

Con esta configuración deberás tener lo mínimo indispensable para la arquitectura cliente servidor de tu proyecto.

Si tienes dudas revisa con tus profesores.