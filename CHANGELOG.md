# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
