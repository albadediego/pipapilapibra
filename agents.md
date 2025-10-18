# 🧠 Copilot Agent Context — Proyecto Pilengua

## 📘 Descripción general

Este proyecto es una aplicación Flask clásica (sin frontend JavaScript) que convierte texto en español al **lenguaje Pilengua** y viceversa.

La lógica lingüística ya está implementada en `app/logic/pi_language.py`, que contiene funciones como:

- `frase_a_pi(frase: str)` → convierte una frase al lenguaje pi.
- `pi_a_frase(frase: str)` → convierte una frase del lenguaje pi al español normal.

El frontend usa **plantillas HTML sencillas (Jinja2)** con formularios POST, procesados totalmente en el servidor.

---

## 🧩 Estructura esperada del proyecto

```
pilengua_app/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── logic/
│   │   ├── __init__.py
│   │   └── pi_language.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── css/
│           └── styles.css
│
├── tests/
│   └── test_pi_language.py
│
├── config.py
├── run.py
├── requirements.txt
├── README.md
└── agents.md
```

---

## 🎯 Objetivos del proyecto

1. Crear una aplicación Flask funcional con un solo endpoint (`/`) que:
   - Muestre un formulario con dos `<textarea>`: uno para introducir texto, otro para mostrar la conversión.
   - Ofrezca dos botones:
     - “Convertir a Pilengua” → llama a `frase_a_pi`.
     - “Convertir a Español” → llama a `pi_a_frase`.

2. Toda la lógica debe permanecer en **`pi_language.py`**, sin duplicación dentro de Flask.

3. No usar JavaScript; la interacción debe hacerse mediante formularios HTML (`method="POST"`).

4. Mantener código limpio, modular y con buenas prácticas de estilo PEP8.

---

## 🧩 Tareas sugeridas para Copilot

Cuando el desarrollador solicite ayuda, Copilot debe:

- **Generar o completar archivos** respetando esta estructura.
- **Explicar decisiones de diseño** en lenguaje claro y pedagógico.
- **Sugerir pruebas unitarias** en `tests/test_pi_language.py`.
- **No modificar** la lógica de `pi_language.py`, salvo para correcciones menores de compatibilidad o errores evidentes.
- **Mantener la separación de capas**:
  - Capa de presentación → Flask (`routes.py`, `templates/`).
  - Capa de negocio → `logic/pi_language.py`.

---

## 🧱 Tecnologías principales

- **Python 3.11+**
- **Flask** (para el servidor)
- **Jinja2** (para plantillas HTML)
- **Pytest** (para testing)
- **HTML5 / CSS3** (mínimos, sin JS)

---

## 🧑‍💻 Instrucciones para Copilot

1. **Contexto**: El usuario es un desarrollador junior con 11 semanas de experiencia.
2. **Estilo de enseñanza**: Explicar las sugerencias brevemente, con enfoque didáctico y profesional.
3. **Prioridades**:
   - Código simple, legible y modular.
   - Evitar complejidad innecesaria.
   - Mostrar ejemplos funcionales listos para ejecutar.
4. **No usar frameworks adicionales** (ni React, ni Bootstrap, ni JS).
5. **Mantener comentarios útiles** dentro del código para aprendizaje.

---

## ✅ Criterios de éxito

- El comando `flask run` ejecuta correctamente el servidor Flask.
- La interfaz HTML permite convertir texto en ambas direcciones.
- Los tests de `tests/test_pi_language.py` pasan sin errores.
- El proyecto es entendible y mantenible para un desarrollador junior.