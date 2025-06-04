# Release Notes

## Version 1.1.0 - 2025-06-03

### 🎯 Major Optimization Release

Esta versión introduce mejoras significativas en la estructura del repositorio para eliminar duplicación de código y facilitar el mantenimiento.

#### 🚀 New Features

- **Script de Compilación Automatizado**: Nuevo script `compile.sh` que permite compilar fácilmente una o ambas versiones del CV
- **Estructura Optimizada**: Carpeta `shared/` centraliza todos los paquetes LaTeX comunes
- **Documentación Mejorada**: README completamente reescrito con ejemplos, emojis y mejor estructura

#### 🔧 Technical Improvements

- **Eliminación de Duplicación**: Movidos todos los paquetes LaTeX comunes (`moderncv`, `moderntimeline`, `pdfpages`, `xpatch`) a una carpeta compartida
- **Rutas Automáticas**: Los archivos `.tex` ahora referencian automáticamente los paquetes compartidos
- **Carpetas Simplificadas**: Las carpetas de idiomas ahora contienen solo archivos específicos del idioma
- **Control de Versiones Optimizado**: Reducción significativa de archivos duplicados en el historial de Git

#### 📈 Benefits

- **Mantenimiento Simplificado**: Actualizaciones de paquetes en un solo lugar
- **Menor Tamaño de Repositorio**: Eliminación de archivos duplicados
- **Compilación Más Rápida**: Script automatizado con mensajes de estado claros
- **Mejor Organización**: Estructura lógica y fácil de entender

#### 🛠️ Usage

```bash
# Compilar ambas versiones
./compile.sh

# Compilar solo español
./compile.sh esp

# Compilar solo inglés
./compile.sh eng
```

### Known Issues

- No known issues at this time.

---

## Version 1.0.0 - 2025-06-03

### New Features

- Initial release of the curriculum vitae repository.
- Contains CV versions in English and Spanish, presumably in LaTeX format and compiled PDFs.
- Basic project documentation: README, CHANGELOG, RELEASE_NOTES.
- `.gitignore` tailored for LaTeX development, allowing PDFs to be tracked.

### Improvements

- Clear project structure for managing different CV language versions.

### Known Issues

- No known issues at this time.
