🌸 SkillMatch

Encuentra el rol que busca tus skills.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-ffd7e7?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Flask-Backend-f3c7ff?logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/JavaScript-Frontend-e1f5ff?logo=javascript&logoColor=white" />
  <img src="https://img.shields.io/badge/HTML-CSS-minimal-ffe9d6" />
</p>


⸻

🌿 ¿Qué es SkillMatch?

SkillMatch es una aplicación pensada para quienes están en reconversión laboral y quieren entender qué tan cerca están de distintos roles.

Ayuda a:
	•	visualizar tus skills actuales
	•	compararlas con el perfil ideal de cada oferta
	•	descubrir tu porcentaje de compatibilidad
	•	ver qué habilidades necesitas fortalecer

Todo en una interfaz sencilla, suave y sin distracciones ✨

⸻

🧁 Características principales

👤 Perfil
	•	Nombre, email e ID
	•	Lista editable de skills + nivel
	•	Chips minimalistas para visualizar habilidades

🎯 Match con ofertas
	•	Cálculo automático del porcentaje
	•	Vista de qué skills cumples y cuáles faltan
	•	Barras de colores según nivel de compatibilidad

🔎 Exploración de ofertas
	•	Buscador instantáneo
	•	Vista limpia y estructurada de cada trabajo
	•	Modalidades, seniority y empresa

💜 Top Matches
	•	Ranking de tus 3 mejores oportunidades
	•	Barra visual estética (verde/amarillo/gris)
	•	Diseño súper minimalista

⸻

🧩 Arquitectura
Backend — Flask (Python) + SQLAlchemy + PostgreSQL
Frontend — HTML + CSS + JavaScript

Todo conectado con una API REST creada desde cero, pensada para ser simple, clara y extensible.

⸻

🎨 Tecnologías
Área            Stack
Backend         Python · Flask · SQLAlchemy · Flask-Migrate
Frontend        HTML5 · CSS3 · JavaScript Vanilla
Base de datos   PostgreSQL
Otros           Fetch API · Entorno virtual con venv


⸻

🪄 Instalación

1. Clonar el repositorio
git clone https://github.com/tu-usuario/skillmatch.git
cd skillmatch

2. Crear y activar entorno virtual
python3 -m venv .venv
source .venv/bin/activate

3. Instalar dependencias
pip install -r requirements.txt

4. Configurar variables de entorno
Para ejecutar el proyecto necesitas un archivo .env con tus credenciales locales.
Este repositorio incluye un archivo .env.example con un ejemplo listo para copiar.

# 1. Copiar archivo de ejemplo

cp .env.example .env

# 2. Editar .env con tus credenciales

# Reemplaza TU_PASSWORD por la contraseña real de tu usuario Postgres

DATABASE_URL=postgresql+psycopg2://postgres:TU_PASSWORD@localhost:5432/skillmatch

# Ambiente y clave secreta

FLASK_ENV=development
FLASK_APP=app:create_app
SECRET_KEY=dev-secret

5. Crear base de datos en PostgreSQL

En psql o pgAdmin:
CREATE DATABASE skillmatch;

Luego aplicar migraciones:
flask db upgrade

6. Correr backend
flask --app app run

7. Abrir frontend
Solo abre este archivo en tu navegador:
frontend/index.html


⸻

📊 ¿Cómo se calcula el match?

El backend compara:
✔️ Skills requeridas por la oferta
✔️ Skills del usuario
✔️ Niveles mínimos
✔️ Skills faltantes

Devuelve un JSON con:
{
  "compatibility": 82,
  "matched_skills": [...],
  "missing_skills": [...]
}

Minimal, claro y útil ✨

⸻

🌱 Roadmap futuro
	•	Login real
	•	Base de datos remota
	•	Dashboard para empresas
	•	Recomendación de cursos según brechas
	•	IA para sugerir roles alternativos

(Visión delulu, pero hermosa 💫)

⸻

🫶 Autora

Constanza Vallejos
Product Manager · Scrum Product Owner certificada
Bootcamp Latinas in Cloud de Python · Cohorte 2025

⸻

🍃 Licencia

MIT — úsalo, modifícalo, inspírate.
