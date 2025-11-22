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

SkillMatch es una aplicación pensada para quienes están en reconversión laboral y quieren entender qué tan cerca están de distintos roles del mercado tech.

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
Backend — Flask + SQLAlchemy + SQLite
Frontend — HTML + CSS + JS

Todo conectado con una API REST creada desde cero, pensada para ser simple, clara y extensible.

⸻

🎨 Tecnologías
Área            Stack
Backend         Python · Flask · SQLAlchemy · Flask-Migrate
Frontend        HTML5 · CSS3 · JavaScript Vanilla
Base de datos   SQLite
Otros           Fetch API · Entorno virtual con venv


⸻

🪄 Instalación

1. Clonar
git clone https://github.com/tu-usuario/skillmatch.git
cd skillmatch

2. Crear entorno
python3 -m venv .venv
source .venv/bin/activate

3. Instalar dependencias
pip install -r requirements.txt

4. Correr backend
flask --app app run

5. Abrir frontend
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
