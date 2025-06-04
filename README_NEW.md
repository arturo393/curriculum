# 🚀 Sistema de CVs Inteligente - Arturo Veras

Sistema avanzado de generación de CVs especializados con personalización automática por empresa y rol. Optimizado para el mercado laboral moderno con templates específicos y configuración inteligente.

## ✨ Características Principales

- **🎯 Templates Especializados**: 5 templates optimizados para diferentes roles
- **🤖 Personalización Automática**: Configuración inteligente por empresa
- **📊 Optimizado para ATS**: Formato compatible con sistemas de seguimiento
- **⚡ Generación Rápida**: Scripts automatizados para compilación
- **🌍 Multi-idioma**: Soporte para español e inglés
- **📈 Métricas Cuantificadas**: KPIs específicos por industria

## 🏗️ Arquitectura del Sistema

```text
curriculum/
├── templates/                       # Sistema de templates modular
│   ├── base/                       # Template base reutilizable
│   │   └── cv_base_template.tex    # Estructura base
│   ├── specialized/                # Templates especializados
│   │   ├── cv_software_developer.tex      # Desarrollador Software
│   │   ├── cv_firmware_developer.tex      # Desarrollador Firmware
│   │   ├── cv_iot_specialist.tex         # Especialista IoT
│   │   ├── cv_technical_lead.tex         # Technical Lead
│   │   └── cv_startup_entrepreneur.tex   # Startup/Entrepreneur
│   ├── variables/                  # Variables personalizables
│   │   └── cv_variables.tex        # Definiciones de variables
│   └── industry_config.py          # Configuración por industria
├── generated/                      # CVs generados automáticamente
├── Arturo_Veras_CV_ESP/           # CV original español
├── Arturo_Veras_CV_ENG/           # CV original inglés
├── generate_cv.py                 # Generador inteligente Python
├── generate_cv.sh                 # Generador bash (legacy)
├── MEJORAS_CV.md                  # Análisis y mejoras detalladas
└── compile.sh                     # Script de compilación
```

## 🚀 Uso Rápido

### Generación Automática (Recomendado)

```bash
# Desarrollador de Software para Google
python generate_cv.py software Google "Senior Software Engineer" --compile

# Firmware Developer para Tesla
python generate_cv.py firmware Tesla "Embedded Software Engineer" --compile

# IoT Specialist para Siemens
python generate_cv.py iot Siemens "IoT Solutions Architect" --compile

# Technical Lead para Microsoft
python generate_cv.py lead Microsoft "Engineering Manager" --compile

# Startup/Entrepreneur para Y Combinator
python generate_cv.py startup YCombinator "Technical Co-Founder" --compile
```

### Ver Templates Disponibles

```bash
python generate_cv.py --list
```

### Generación Manual (Legacy)

```bash
# Compilar CV original en español
./compile.sh esp

# Compilar CV original en inglés  
./compile.sh eng

# Compilar ambos
./compile.sh all
```

## 🎯 Templates Especializados

### 1. Software Developer (`software`)
- **Orientado a**: Empresas de tecnología, startups tech, desarrollo web/móvil
- **Enfoque**: Full-stack development, arquitecturas escalables, metodologías ágiles
- **Tecnologías destacadas**: Python, React, Node.js, MongoDB, AWS, microservicios
- **Métricas**: Usuarios activos, performance, uptime, code coverage

### 2. Firmware Developer (`firmware`)
- **Orientado a**: Empresas de hardware, IoT, sistemas embebidos, automotriz
- **Enfoque**: Sistemas embebidos, protocolos de comunicación, tiempo real
- **Tecnologías destacadas**: C/C++, STM32, LoRa, FreeRTOS, protocolos industriales
- **Métricas**: Uptime, consumo energético, throughput, reliability

### 3. IoT Specialist (`iot`)
- **Orientado a**: Industry 4.0, automatización industrial, smart manufacturing
- **Enfoque**: Ecosistemas IoT, edge computing, analytics en tiempo real
- **Tecnologías destacadas**: LoRaWAN, MQTT, AWS IoT, Grafana, edge computing
- **Métricas**: Dispositivos conectados, datos procesados, eficiencia operacional

### 4. Technical Lead (`lead`)
- **Orientado a**: Posiciones de liderazgo técnico, arquitectura, gestión de equipos
- **Enfoque**: Liderazgo técnico, arquitectura de sistemas, mentoring
- **Tecnologías destacadas**: Microservices, DevOps, cloud architecture
- **Métricas**: Team performance, delivery success, architectural decisions

### 5. Startup Entrepreneur (`startup`)
- **Orientado a**: Startups, founding engineer, CTO, technical co-founder
- **Enfoque**: Product development, MVP, growth hacking, fundraising
- **Tecnologías destacadas**: Full-stack, cloud native, emerging technologies
- **Métricas**: ARR, user growth, funding raised, product-market fit

## 🤖 Personalización Automática

El sistema personaliza automáticamente el CV según la empresa objetivo:

### Ejemplos de Personalización

**Google**: Enfoque en escalabilidad, machine learning, open source, data-driven
**Microsoft**: Azure, enterprise solutions, accessibility, growth mindset
**Tesla**: Real-time systems, safety-critical, automotive protocols, sustainability
**Startups**: MVP development, product-market fit, rapid iteration, resourcefulness

### Configuración por Industria

- **Tech Companies**: Keywords de escalabilidad, cloud, innovation
- **Hardware Companies**: Real-time, safety-critical, embedded systems
- **Mining Industry**: Industrial IoT, harsh environments, 24/7 operations
- **Startups**: Agility, growth hacking, technical leadership

## 📊 Análisis y Mejoras

El archivo [`MEJORAS_CV.md`](MEJORAS_CV.md) contiene:

- **Análisis detallado** del CV actual con problemas identificados
- **Propuestas específicas** de mejora con ejemplos
- **Estrategias por industria** para diferentes tipos de postulaciones
- **Métricas cuantificables** por sector
- **Keywords optimizados** para sistemas ATS

## 🔧 Instalación y Configuración

### Prerrequisitos

#### macOS
```bash
brew install --cask mactex
# O instalar BasicTeX para instalación mínima
brew install --cask basictex
```

#### Ubuntu/Debian
```bash
sudo apt-get install texlive-full
```

#### Windows
- Descargar e instalar [MiKTeX](https://miktex.org/) o [TeX Live](https://www.tug.org/texlive/)

### Dependencias LaTeX

```bash
# Actualizar distribución LaTeX
sudo tlmgr update --self

# Instalar paquetes necesarios
sudo tlmgr install moderncv moderntimeline pdfpages xpatch biblatex geometry tikz
```

### Configuración del Proyecto

```bash
# Clonar repositorio
git clone https://github.com/arturo-veras/curriculum.git
cd curriculum

# Hacer scripts ejecutables
chmod +x generate_cv.py generate_cv.sh compile.sh

# Verificar instalación
python generate_cv.py --list
```

## 📈 Workflow Recomendado

1. **Identificar el rol y empresa objetivo**
2. **Generar CV especializado**:
   ```bash
   python generate_cv.py [template] [company] [position] --compile
   ```
3. **Personalizar configuración** en `generated/*/job_config.tex`
4. **Revisar y ajustar** keywords específicos de la empresa
5. **Compilar y revisar** el PDF final
6. **Optimizar** según feedback o requisitos específicos

## 🎯 Estrategia de Aplicación

### Por Tipo de Empresa

- **FAANG/Big Tech**: Template `software` con énfasis en escalabilidad
- **Hardware/Automotive**: Template `firmware` con sistemas críticos
- **Consulting/Enterprise**: Template `iot` o `lead` según nivel
- **Startups**: Template `startup` con enfoque en growth y MVP

### Por Nivel de Experiencia

- **Senior Developer**: Templates `software`, `firmware`, `iot`
- **Tech Lead/Manager**: Template `lead`
- **Founding Engineer**: Template `startup`
- **Consultant**: Template según especialización técnica

## 📝 Contributing

Para contribuir al proyecto:

1. Fork del repositorio
2. Crear branch para nueva funcionalidad
3. Implementar mejoras o nuevos templates
4. Enviar Pull Request con descripción detallada

## 📞 Contacto

- **Email**: arturo.veras@example.com
- **LinkedIn**: [linkedin.com/in/arturo-veras](https://linkedin.com/in/arturo-veras)
- **GitHub**: [github.com/arturo-veras](https://github.com/arturo-veras)

## 📜 Licencia

Este proyecto está bajo la Licencia MIT. Ver `LICENSE` para más detalles.

---

⭐ **¿Te resulta útil este sistema?** ¡Dale una estrella al repositorio!
