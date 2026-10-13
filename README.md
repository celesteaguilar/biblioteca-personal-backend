\# Biblioteca Personal - Backend (Django REST Framework)



Aplicación web Full-Stack desarrollada para la asignatura \*\*Herramientas Avanzadas para el Desarrollo de Aplicaciones\*\*.



\## Repositorio relacionado



Este backend se conecta con el frontend desarrollado en React:

\[biblioteca-personal-frontend](https://github.com/celesteaguilar/biblioteca-personal-frontend)



\## Integrantes



\* Marcela Saraí Ramírez Caceres (#0700424)

\* María Celeste Hernández Aguilar (#0700923)



\## Sesión 2 - Estructura Inicial



\* Inicialización del proyecto con Django y Django REST Framework.

\* Configuración del directorio `config/` con settings, CORS (`django-cors-headers`) y variables de entorno (`.env`).

\* Las apps de dominio `catalogo` y `lectura` se crearon en la Sesión 9 (ver más abajo).

\## Flujo de Trabajo y Convenciones (Sesión 3)


\### Ramas


\* `main`: Rama principal y estable. Protegida contra pushes directos.

\* `feature/<nombre>`: Ramas creadas para desarrollar nuevas características o mejoras.

\* `fix/<nombre>`: Ramas para corrección de errores.



\### Convención de Commits



\* `feat:` para nuevas funcionalidades.

\* `fix:` para corrección de errores.

\* `docs:` para cambios o actualización en la documentación (`README.md`).

## Sesión 9 - Modularización

### Apps de Django

El proyecto se organizó en dos apps separadas por dominio de negocio:

| App | Responsabilidad | Modelos previstos |
|---|---|---|
| `catalogo` | Información de los libros y sus autores | `Autor` y `Libro` (con `ForeignKey` a `Autor`) |
| `lectura` | Seguimiento personal de lectura: estado, calificación y notas | `Lectura` (con `ForeignKey` a `Libro` y campo `version` para el control de concurrencia) |

### Cambios realizados

* Se crearon las apps `catalogo` y `lectura` con `python manage.py startapp`.
* Ambas apps se registraron en `INSTALLED_APPS` de `config/settings.py`.
* Se mantuvo la configuración de CORS y de variables de entorno ya existente en el proyecto.
* Los modelos, serializers y endpoints se implementarán en las sesiones 11 y 13.

### Flujo de trabajo en esta sesión

* Se resolvió un conflicto de merge en los archivos del proyecto Django (`config/`, `requirements.txt` y `.gitignore`), conservando la configuración existente en `main` y agregando las dos apps.
* Pull Request revisado y aprobado por la otra integrante del equipo.
