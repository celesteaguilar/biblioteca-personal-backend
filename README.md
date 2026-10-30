# Biblioteca Personal - Backend (Django REST Framework)

Aplicación web Full-Stack desarrollada para la asignatura **Herramientas Avanzadas para el Desarrollo de Aplicaciones**.

## Repositorio relacionado

Este backend se conecta con el frontend desarrollado en React:
[biblioteca-personal-frontend](https://github.com/celesteaguilar/biblioteca-personal-frontend)

## Integrantes

* Marcela Saraí Ramírez Caceres (#0700424)
* María Celeste Hernández Aguilar (#0700923)

## Instalación y uso

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1      # en Linux/Mac: source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env             # y escribe tu propia SECRET_KEY dentro de .env
python manage.py migrate
python manage.py loaddata autores
python manage.py runserver
```

La API queda disponible en `http://127.0.0.1:8000/api/autores/`. El archivo `.env.example` lista las variables de entorno necesarias: `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS` y `CORS_ALLOWED_ORIGINS`.

## Sesión 2 - Estructura Inicial

* Inicialización del proyecto con Django y Django REST Framework.
* Configuración del directorio `config/` con settings, CORS (`django-cors-headers`) y variables de entorno (`.env`).
* Las apps de dominio `catalogo` y `lectura` se crearon en la Sesión 9 (ver más abajo).

## Flujo de Trabajo y Convenciones (Sesión 3)

### Ramas

* `main`: Rama principal y estable. Protegida contra pushes directos.
* `feature/<nombre>`: Ramas creadas para desarrollar nuevas características o mejoras.
* `fix/<nombre>`: Ramas para corrección de errores.

### Convención de Commits

* `feat:` para nuevas funcionalidades.
* `fix:` para corrección de errores.
* `docs:` para cambios o actualización en la documentación (`README.md`).

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

## Sesión 11 - API conectada al frontend

### Endpoints implementados (app `catalogo`)

| Método | URL | Descripción |
|---|---|---|
| GET | `/api/autores/` | Lista los autores |
| GET | `/api/autores/<id>/` | Muestra el detalle de un autor |

* Modelo `Autor` con los campos `nombre` y `pais` (se llama `pais` para coincidir con los datos que ya usaba el frontend en `mock.js`).
* `AutorSerializer` (`ModelSerializer`) y `AutorViewSet` (`ReadOnlyModelViewSet`), registrado con `DefaultRouter` y expuesto bajo `/api/`.
* El endpoint es de solo lectura en esta sesión: cualquier intento de crear, editar o borrar responde 405. El CRUD completo se implementará en la Sesión 13.
* El modelo `Autor` quedó registrado en el admin de Django.
* Datos de prueba en `catalogo/fixtures/autores.json`, que se cargan con `python manage.py loaddata autores`.

### CORS y variables de entorno

* `django-cors-headers` solo acepta los orígenes de `CORS_ALLOWED_ORIGINS` (por defecto `http://localhost:5173`, donde corre el frontend en desarrollo).
* `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS` y `CORS_ALLOWED_ORIGINS` se leen del archivo `.env`, que no se sube al repositorio. `.env.example` sirve de plantilla.