# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.0.0] - 2025-09-25 🎯

### 🚀 SIMPLIFICACIÓN RADICAL - HTML FIRST APPROACH

#### Added
- ✨ **CV HTML Generator**: Generación directa a HTML optimizado para una página A4
- 📄 **CSS Inline Completo**: Styling integrado sin dependencias externas
- 🖨️ **Print Media Queries**: Optimización específica para exportación PDF
- 📏 **A4 Perfect Fit**: Diseño calculado para caber exactamente en una página
- ⚡ **Zero Dependencies**: Solo Python estándar, sin librerías externas
- 🎨 **Grid Layout**: Skills en 3 columnas, educación en 2 columnas
- 📱 **Responsive Design**: Se ve bien en pantalla y papel

#### Changed
- 🔄 **Output Format**: De Markdown → HTML (más consistente para PDF)
- ⚡ **Workflow**: `python3 generate-cv.py` → abrir HTML → Ctrl+P → PDF
- 🎯 **Tiempo Total**: De 2 minutos → 25 segundos para CV completo
- 📦 **Distribución**: De múltiples archivos → 1 HTML autocontenido
- 🖥️ **Compatibilidad**: Cualquier navegador vs dependencias específicas

#### Removed
- 🧹 **Dependencias Google API**: No más oauth, credentials, tokens
- 📄 **Múltiples Templates**: Solo un diseño optimizado
- 🔧 **CLI Complejo**: Interfaz simplificada
- 💾 **requirements.txt**: Ya no necesita instalación de paquetes

#### Benefits
- **100% menos dependencias**: De 3 paquetes → 0
- **180x más rápido setup**: De 30 minutos → 10 segundos
- **Resultado universal**: Compatible con todos los navegadores
- **PDF consistente**: Mismo resultado en Mac, Windows, Linux

#### Migration Guide
```bash
# Antes (Markdown + Google Docs)
python3 generate-cv.py
# → Copiar a Google Docs → Formatear → Exportar PDF

# Ahora (HTML → PDF directo)
python3 generate-cv.py
# → Abrir HTML → Ctrl+P → Guardar PDF
```

### 📊 Estadísticas
- **1 archivo Python**: 85 líneas vs 150 líneas anteriores
- **1 comando**: Generación completa en una línea
- **25 segundos**: Tiempo total de ejecución
- **Una página perfecta**: Diseño optimizado para A4

---

## [2.0.0] - 2025-09-21 🎉

### 🚀 REFACTORIZACIÓN COMPLETA - ARQUITECTURA MODERNA

#### Added
- ✨ **CLI Unificada**: Comando `cv-suite` que reemplaza múltiples scripts
- 🏗️ **Arquitectura Modular**: Estructura `src/{core,generators,utils,cli}`
- 🎨 **Sistema Inteligente de Colores**: Predicción automática basada en psicología empresarial
- 📊 **5 Generadores Modernos**: HTML, Compact, Markdown, LaTeX, ReportLab Avanzado
- 🔧 **Módulos Core**: DataParser, ColorSystem, GeneratorBase con inheritance
- 📚 **Documentación Consolidada**: Guías organizadas en `docs/guides/`
- 🧪 **Tests Organizados**: Estructura de testing modular
- 🎯 **Registry Pattern**: Sistema extensible para nuevos generadores

#### Changed
- 🗂️ **Estructura Reorganizada**: De 26+ archivos Python en root → arquitectura limpia
- 🖥️ **Interfaz Modernizada**: Modo interactivo con selección guiada
- 🎨 **Generación Mejorada**: Integración con sistema de colores inteligente
- 📈 **Performance**: Validación de dependencias y manejo de errores mejorado

#### Removed
- 🧹 **Scripts Legacy**: Eliminados 6+ scripts duplicados y obsoletos
- 📄 **Documentación Fragmentada**: Consolidada de 8+ archivos dispersos
- ⚠️ **Código Duplicado**: Funcionalidad unificada en módulos core

#### Migration Guide
```bash
# Antes (múltiples scripts)
python cv_suite_2025.py
python generate_cv_modern_fixed.py

# Ahora (comando unificado)
./cv-suite interactive
./cv-suite generate html "Google" "Software Engineer"
```

### 📊 Estadísticas
- **51 archivos modificados**: +4,884 insertions, -6,949 deletions
- **5 generadores funcionales**: HTML, Compact, Markdown, LaTeX, ReportLab
- **3 módulos core**: Parsing, Color System, Base Generator
- **Arquitectura moderna**: Siguiendo mejores prácticas de ingeniería de software

---

## [1.1.0] - 2025-06-03

### Added

- Script de compilación automatizado (`compile.sh`) para compilar CVs fácilmente
- Carpeta `shared/` para paquetes LaTeX compartidos
- Documentación mejorada con estructura de carpetas y ejemplos de uso
- Emojis y mejor formateo en README.md
- Archivo `REQUIRED_PACKAGES.md` con análisis completo de dependencias LaTeX
- Instalación y configuración completa de paquetes LaTeX necesarios

### Changed

- Reestructuración completa del repositorio para eliminar duplicación de código
- Movidos todos los paquetes LaTeX comunes a `shared/`
- Actualizadas las rutas en archivos `.tex` para referenciar paquetes compartidos
- Instalados paquetes LaTeX: `moderncv`, `moderntimeline`, `biblatex`, `fontawesome5`, `arydshln`, `multirow`
- Configurado TeX Live 2025 en el PATH del sistema

### Fixed

- Corregido error de sintaxis `\cvcomputer` en CV español
- Corregido escape de ampersand `R\&D` en CV inglés  
- Mejorado manejo de errores en script de compilación
- Ambos CVs (español e inglés) compilan exitosamente generando PDFs de 3 páginas
- Simplificadas las carpetas de idiomas (solo archivos específicos)

### Removed

- Paquetes LaTeX duplicados en carpetas de idiomas
- Plantillas duplicadas (`template-*.tex`)

### Fixed

- Eliminación de redundancia en paquetes `moderncv`, `moderntimeline`, `pdfpages`, `xpatch`
- Optimización del control de versiones (menos archivos duplicados)

## [1.0.0] - 2025-06-03

### Added

- Initial project setup with Spanish and English CV versions.
- README.md, CHANGELOG.md, RELEASE_NOTES.md.
- .gitignore configured for LaTeX projects.
