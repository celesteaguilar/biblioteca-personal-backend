# biblioteca-personal-backend

Backend de la **Biblioteca Personal de Libros**, desarrollado con **Django REST Framework**.

Proyecto integrador de la asignatura *Herramientas Avanzadas para el Desarrollo de Aplicaciones* (102HAD1) — Ciclo II-2026, Universidad Técnica Latinoamericana.

## Repositorio relacionado

Este backend se conecta con el frontend desarrollado en React:
[biblioteca-personal-frontend](https://github.com/celesteaguilar/biblioteca-personal-frontend)

## Descripción

API REST que permitirá gestionar una colección personal de libros: registro de libros, autores, colecciones personalizadas y reseñas con calificación. El modelo de datos completo está detallado en la Definición Técnica del Proyecto entregada en la Evaluación 1.

## Tecnologías

* Python / Django
* Django REST Framework
* django-cors-headers
* SQLite (entorno de desarrollo)

## Estructura del proyecto (avance actual — Sesión 2)

```
biblioteca-personal-backend/
├── config/              # Configuración principal del proyecto Django
├── manage.py
├── requirements.txt
├── .env.example
└── .gitignore
```

> Las apps de dominio (`libros/`, `colecciones/`, `resenas/`) con sus modelos, migraciones y serializers se crearán en la Sesión 9 del cronograma ("Modularización frontend/back").

## Flujo de trabajo (Git)

Estrategia: **GitHub Flow**. La rama `main` está protegida y requiere Pull Request con al menos 1 aprobación antes de fusionar.

Convención de ramas:

* `feature/nombre-funcionalidad` — nuevas funcionalidades
* `fix/nombre-correccion` — correcciones de errores

Convención de commits:

* `feat:` nueva funcionalidad
* `fix:` corrección de errores
* `docs:` documentación
* `refactor:` cambios de estructura sin alterar funcionalidad
* `test:` pruebas

Todo cambio a `main` pasa por un Pull Request revisado por al menos un integrante distinto al autor.

## Instalación

*(Sección en construcción — se completará con instrucciones detalladas de instalación y uso conforme avance el desarrollo del proyecto.)*

## Integrantes

* Marcela Saraí Ramírez Caceres
* María Celeste Hernández Aguilar

## Historial de cambios de dominio

*(Si el dominio o el alcance del proyecto cambia durante el ciclo, se documentara aquí con fecha y razón.)*

