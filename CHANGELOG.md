# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2025-06-03

### Added

- Script de compilación automatizado (`compile.sh`) para compilar CVs fácilmente
- Carpeta `shared/` para paquetes LaTeX compartidos
- Documentación mejorada con estructura de carpetas y ejemplos de uso
- Emojis y mejor formateo en README.md

### Changed

- Reestructuración completa del repositorio para eliminar duplicación de código
- Movidos todos los paquetes LaTeX comunes a `shared/`
- Actualizadas las rutas en archivos `.tex` para referenciar paquetes compartidos
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
