# 🚀 CV Arturo Veras - Generador Profesional 2026

Repositorio consolidado para la generación de CV profesional optimizado para **una página A4**.

## 🎯 Filosofía
Tras varias iteraciones (v1 LaTeX, v2 Modular), este repositorio ha sido simplificado radicalmente siguiendo la visión de **2026: Eficiencia + IA**. 

Utilizamos scripts de Python que generan un HTML autocontenido (con CSS inline) diseñado para ser impreso a PDF directamente desde el navegador, garantizando un diseño industrial perfecto y compatible con todos los sistemas.

---

## 🛠️ Cómo Generar tu CV

Sigue estos pasos para obtener tu CV en menos de 30 segundos:

### **1. Generar el archivo HTML**
Dependiendo del idioma que necesites:

```bash
# Para Español
python3 cv-simple/generate-cv.py

# Para Inglés (English)
python3 cv-simple/generate-cv-english.py
```

### **2. Guardar como PDF**
1. Ve a la carpeta `cv-simple/output/`.
2. Abre el archivo `.html` generado con tu navegador preferido (Chrome, Edge, Safari).
3. Presiona `Ctrl + P` (o `Cmd + P` en Mac).
4. Selecciona **"Guardar como PDF"**.
5. **Importante:** Asegúrate de que los márgenes estén configurados en "Mínimo" o "Ninguno" para un ajuste perfecto a una página.

---

## 🏢 Perfil Actual (Software Lead I+D)
Este generador está configurado con mi perfil actual como **Líder de Software I+D**, con un enfoque radical en:
- 🤖 **IA Agents & Workflows**: GitHub Copilot, Gemini.
- 🏗️ **Arquitectura Estratégica**: Diseño previo y planes de test robustos.
- 👥 **Liderazgo de Equipos**: Gestión y mentoría de equipos R&D.
- ⚡ **Experiencia Multistack**: Desde Firmware (STM32) hasta Full-Stack (Python, React).

---

## 📁 Estructura del Repositorio
- `cv-simple/`: Sistema principal de generación.
  - `generate-cv.py`: Script generador (Español).
  - `generate-cv-english.py`: Script generador (Inglés).
  - `output/`: Directorio donde se guardan los CVs generados.
- `CHANGELOG.md`: Historial de evoluciones del repositorio.

---
*"La tecnología debe simplificar, no complicar"* - Arturo Veras