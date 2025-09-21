# CLI Unificada - CV Suite 2025

## 🚀 Uso de la Nueva CLI

La nueva CLI unificada reemplaza a `cv_suite_2025.py` con una interfaz moderna y modular.

### Comandos Principales

```bash
# Listar generadores disponibles
./cv-suite list

# Verificar dependencias
./cv-suite check

# Predecir esquema de colores
./cv-suite colors "Intel" "Embedded Engineer"

# Generar CV específico
./cv-suite generate html "Google" "Software Engineer"
./cv-suite generate compact "Microsoft" "Program Manager"

# Modo interactivo (recomendado)
./cv-suite interactive
```

### Modo Interactivo

El modo interactivo guía paso a paso:

```bash
./cv-suite interactive
```

1. 🏢 Solicita nombre de empresa
2. 💼 Solicita título de posición  
3. 🎨 Muestra predicción de colores
4. 📊 Lista generadores disponibles
5. 🚀 Genera CV personalizado
6. 💡 Opción de generar formatos adicionales

### Generadores Disponibles

| Tipo | Descripción | Recomendado |
|------|-------------|-------------|
| **html** | CV ultra-moderno HTML/CSS 2025 | ✅ |
| **compact** | PDF compacto con ReportLab | ✅ |
| **markdown** | Markdown simple y rápido | - |

### Migración desde cv_suite_2025.py

**Antes:**
```bash
python cv_suite_2025.py
```

**Ahora:**
```bash
./cv-suite interactive
```

### Estructura del CLI

```
src/cli/
├── main_cli.py         # CLI principal unificada
└── __init__.py         # Módulo CLI

cv-suite                # Script ejecutable wrapper
```

### Características

- ✅ **Interfaz Unificada**: Un solo comando para todos los generadores
- ✅ **Modo Interactivo**: Guía paso a paso amigable
- ✅ **Predicción de Colores**: Integración con sistema de colores inteligente
- ✅ **Validación de Dependencias**: Verificación automática
- ✅ **Generación en Lote**: Soporte para múltiples CVs
- ✅ **Retrocompatibilidad**: Mantiene funcionalidad de cv_suite_2025.py