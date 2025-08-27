# 🚀 CV Generator Suite 2025

## Sistema Completo de Generación de CVs Modernos
**Arturo Veras González** - Ingeniero Civil Electrónico

### 🎯 Descripción
Sistema unificado para generar CVs profesionales usando múltiples tecnologías modernas. Diseñado siguiendo las **mejores prácticas de 2025** para optimización ATS, diseño visual y personalización automática.

---

## 🌟 Características Principales

### ✨ **Generadores Disponibles**

| Generador | Tecnología | Nivel | Recomendado 2025 | Descripción |
|-----------|------------|--------|------------------|-------------|
| 🎨 **HTML+CSS Moderno** | `weasyprint` + `jinja2` | ⭐⭐⭐ | ✅ **SÍ** | Control total del diseño, ATS optimizado |
| ⚡ **Markdown Simple** | `pandoc` | ⭐⭐ | ✅ **SÍ** | Velocidad y simplicidad |
| 📜 **LaTeX Clásico** | `pdflatex` | ⭐⭐⭐ | ❌ Complejo | Tipografía profesional tradicional |
| 🐍 **ReportLab** | `python` | ⭐⭐ | ❌ Técnico | Control programático total |

### 🚀 **Mejores Prácticas 2025 Implementadas**

#### **1. Diseño Visual Moderno**
- ✅ Paletas de colores específicas por industria
- ✅ Tipografía moderna (Inter, SF Pro Display)
- ✅ Gradientes sutiles y efectos visuales
- ✅ Layout CSS Grid responsivo
- ✅ Iconografía moderna con emojis

#### **2. Optimización ATS (Applicant Tracking Systems)**
- ✅ Estructura semántica HTML
- ✅ Keywords automáticas detectadas
- ✅ Texto legible para sistemas automáticos
- ✅ Jerarquía clara de información

#### **3. Personalización Inteligente**
- ✅ Detección automática de keywords de industria
- ✅ Colores específicos por tipo de trabajo
- ✅ Resumen personalizado por posición
- ✅ Skills destacadas automáticamente

#### **4. Tecnologías 2025**
- ✅ CSS Variables para theming dinámico
- ✅ Flexbox y CSS Grid para layouts
- ✅ Print CSS optimizado
- ✅ Animaciones sutiles para web

---

## 📦 Instalación

### **Requisitos del Sistema**
```bash
# macOS (recomendado)
brew install pandoc

# Python 3.8+
python3 --version
```

### **Dependencias Python**
```bash
# Instalar todas las dependencias
pip install weasyprint jinja2 reportlab matplotlib pandas

# O instalar por generador específico:
pip install weasyprint jinja2  # Para HTML+CSS Moderno
pip install reportlab           # Para ReportLab
# pandoc se instala con brew
```

### **Verificar Instalación**
```bash
# Clonar/descargar el proyecto
cd curriculum

# Verificar dependencias
python3 cv_suite_2025.py --recommendations
```

---

## 🎯 Uso

### **Modo Interactivo (Recomendado)**
```bash
python3 cv_suite_2025.py
```
- Guía paso a paso
- Verificación de dependencias
- Selección asistida de generador
- Personalización opcional

### **Modo Rápido**
```bash
# CV Moderno 2025 (RECOMENDADO)
python3 cv_suite_2025.py --type modern "Google" "Senior Software Engineer"

# CV Rápido Markdown
python3 cv_suite_2025.py --type markdown "Microsoft" "Technical Lead"

# CV LaTeX Tradicional
python3 cv_suite_2025.py --type latex "Universidad" "Investigador"

# CV Programático
python3 cv_suite_2025.py --type reportlab "Startup" "CTO"
```

### **Uso Directo de Generadores**
```bash
# HTML+CSS Moderno (Control Total)
python3 generate_cv_modern.py "Empresa" "Posición"

# Markdown Simple (Velocidad)
python3 generate_cv_simple.py "Empresa" "Posición"

# LaTeX Clásico (Elegancia)
python3 generate_cv.py "Empresa" "Posición"

# ReportLab (Programático)
python3 generate_cv_reportlab.py "Empresa" "Posición"
```

---

## 🎨 Personalización Avanzada

### **Colores por Industria (Automático)**
- 🔵 **IoT/Hardware**: Azul tecnológico + Verde IoT
- 🟣 **AI/ML**: Púrpura AI + Naranja innovación  
- 🔷 **Cloud/DevOps**: Azul cloud + Rojo infraestructura
- 🟪 **Startups**: Púrpura innovación + Verde crecimiento

### **Keywords Detectadas Automáticamente**
- **IoT**: sensors, embedded, arduino, mqtt, zigbee, edge computing
- **Cloud**: aws, azure, kubernetes, docker, microservices
- **AI/ML**: tensorflow, pytorch, machine learning, data science
- **Web**: react, node.js, javascript, apis, databases

### **Estructura del Template HTML+CSS 2025**
```css
:root {
  --primary-color: #2563eb;
  --secondary-color: #059669;
  --text-primary: #1a1a1a;
  /* Variables CSS modernas */
}

/* Grid Layout Moderno */
.main-grid {
  display: grid;
  grid-template-columns: 1fr 300px;
  gap: var(--spacing-xl);
}

/* Timeline de Experiencia */
.experience-item::before {
  /* Indicador visual de timeline */
}
```

---

## 📁 Estructura del Proyecto

```
curriculum/
├── 🎨 generate_cv_modern.py      # HTML+CSS Moderno 2025
├── ⚡ generate_cv_simple.py      # Markdown Rápido
├── 📜 generate_cv.py             # LaTeX Clásico
├── 🐍 generate_cv_reportlab.py   # ReportLab Programático
├── 🚀 cv_suite_2025.py          # Interfaz Unificada
├── 📊 anexos.md                 # Datos Personales
├── generated/                   # Output LaTeX
├── generated_markdown/          # Output Markdown
├── generated_modern/            # Output HTML+CSS
└── templates/                   # Templates base
```

---

## 🔄 Workflow Recomendado 2025

### **Para Aplicaciones Múltiples**
1. **Usar Markdown Simple** para velocidad
2. Generar CVs básicos para varias empresas
3. **Usar HTML+CSS Moderno** para finalistas
4. Personalizar colores y diseño específico

### **Para Posiciones Específicas**
1. **Copiar descripción del trabajo**
2. **Usar HTML+CSS Moderno** con personalización
3. Keywords detectadas automáticamente
4. Colores optimizados por industria

### **Para Roles Académicos/Investigación**
1. **Usar LaTeX Clásico** para elegancia
2. Tipografía profesional
3. Formato tradicional esperado

---

## 🎯 Ejemplos de Uso Real

### **Ejemplo 1: Ingeniero IoT**
```bash
python3 cv_suite_2025.py --type modern "AVOS Tech" "Ingeniero Especialista en Interfaces y Sensores IoT"
```
**Resultado:**
- ✅ Colores: Azul tecnológico + Verde IoT
- ✅ Keywords: IoT, sensors, embedded, arduino, mqtt
- ✅ Resumen personalizado para IoT
- ✅ Skills destacadas: Python, Arduino, MQTT

### **Ejemplo 2: Desarrollador Senior**
```bash
python3 cv_suite_2025.py --type modern "Google" "Senior Software Engineer"
```
**Resultado:**
- ✅ Colores: Azul profesional + Verde éxito
- ✅ Keywords: software, engineering, apis, cloud
- ✅ Resumen para liderazgo técnico
- ✅ Skills destacadas: Python, JavaScript, AWS

### **Ejemplo 3: Aplicación Rápida**
```bash
python3 cv_suite_2025.py --type markdown "Startup Tech" "Full Stack Developer"
```
**Resultado:**
- ✅ PDF generado en segundos
- ✅ Personalización automática
- ✅ Keywords detectadas
- ✅ Listo para enviar

---

## 📈 Rendimiento y Optimización

| Generador | Tiempo | Tamaño PDF | Personalización | ATS Score |
|-----------|---------|------------|-----------------|-----------|
| HTML+CSS | ~5s | ~200KB | ⭐⭐⭐ | ⭐⭐⭐ |
| Markdown | ~2s | ~150KB | ⭐⭐ | ⭐⭐ |
| LaTeX | ~10s | ~180KB | ⭐ | ⭐⭐⭐ |
| ReportLab | ~3s | ~120KB | ⭐⭐⭐ | ⭐⭐ |

---

## 🛠️ Troubleshooting

### **Error: weasyprint no encontrado**
```bash
pip install weasyprint
# En macOS: puede requerir brew install python-tk
```

### **Error: pandoc no encontrado**
```bash
brew install pandoc  # macOS
apt-get install pandoc  # Ubuntu
```

### **Error: LaTeX no encontrado**
```bash
brew install --cask mactex  # macOS
# O usar BasicTeX para instalación mínima
brew install --cask basictex
```

### **PDF no se abre automáticamente**
- Normal en sistemas no-macOS
- El archivo PDF se genera correctamente
- Abrir manualmente desde la ruta mostrada

---

## 🔮 Roadmap 2025

### **Q1 2025**
- [ ] Integración con APIs de ofertas de trabajo
- [ ] Templates por industria específica
- [ ] Generación batch para múltiples empresas

### **Q2 2025**
- [ ] AI para optimización automática de contenido
- [ ] Análisis de compatibilidad ATS
- [ ] Dashboard web para gestión

### **Q3 2025**
- [ ] Templates interactivos con JavaScript
- [ ] Exportación a múltiples formatos
- [ ] Integración con LinkedIn API

---

## 📄 Licencia

MIT License - Libre para uso personal y comercial

---

## 👨‍💻 Autor

**Arturo Veras González**
- 📧 Email: arturoveras93@gmail.com
- 💼 LinkedIn: [linkedin.com/in/arturo-veras](https://linkedin.com/in/arturo-veras)
- 📍 Santiago, Chile

---

## 🎉 ¿Por qué este proyecto?

Este sistema nació de la **frustración con LaTeX** para CVs. Aunque LaTeX es potente, es demasiado complejo para la mayoría de usuarios. 

**La solución 2025:**
- ✅ **HTML+CSS**: Control total + simplicidad
- ✅ **Markdown**: Velocidad + personalización
- ✅ **Unificado**: Una interfaz para todo
- ✅ **Moderno**: Siguiendo tendencias actuales

**Resultado:** CVs profesionales en minutos, no horas.

---

*"La tecnología debe simplificar, no complicar"* - Arturo Veras
