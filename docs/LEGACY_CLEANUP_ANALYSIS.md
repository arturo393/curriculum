# Análisis de Scripts Legacy en Root

## 📊 Estado Actual

Los siguientes scripts Python permanecen en la raíz del repositorio:

### Scripts Legacy Identificados

| Archivo | Tipo | Estado | Equivalente Nuevo | Acción |
|---------|------|--------|-------------------|---------|
| `generate_cv.py` | Generador básico LaTeX | Legacy | `src/generators/latex_generator.py` | MIGRAR |
| `generate_cv_compact_2025.py` | PDF compacto ReportLab | Legacy | `src/generators/compact_generator.py` | ✅ MIGRADO |
| `generate_cv_modern_fixed.py` | HTML/CSS moderno | Legacy | `src/generators/html_generator.py` | ✅ MIGRADO |
| `generate_cv_reportlab_2025.py` | PDF ReportLab avanzado | Legacy | `src/generators/reportlab_generator.py` | MIGRAR |
| `generate_cv_simple.py` | Markdown simple | Legacy | `src/generators/markdown_generator.py` | ✅ MIGRADO |

### Análisis de Funcionalidades

#### ✅ YA MIGRADOS (Eliminar)
- `generate_cv_compact_2025.py` → Funcionalidad en `src/generators/compact_generator.py`
- `generate_cv_modern_fixed.py` → Funcionalidad en `src/generators/html_generator.py`  
- `generate_cv_simple.py` → Funcionalidad en `src/generators/markdown_generator.py`

#### 🔄 REQUIEREN MIGRACIÓN
- `generate_cv.py` → Contiene lógica LaTeX que falta en nueva arquitectura
- `generate_cv_reportlab_2025.py` → Variante avanzada de ReportLab con features únicas

## 🎯 Plan de Limpieza

### Fase 1: Eliminar Duplicados Migrados
```bash
# Scripts ya migrados a nueva arquitectura
git rm generate_cv_compact_2025.py     # → compact_generator.py
git rm generate_cv_modern_fixed.py     # → html_generator.py
git rm generate_cv_simple.py           # → markdown_generator.py
```

### Fase 2: Migrar Funcionalidad Faltante
```bash
# Scripts con funcionalidad única
generate_cv.py                  → src/generators/latex_generator.py
generate_cv_reportlab_2025.py   → src/generators/reportlab_generator.py (variant)
```

### Beneficios de la Limpieza

1. **Eliminación de Confusión**: Un solo punto de entrada (`cv-suite`)
2. **Mantenimiento Simplificado**: Una implementación por generador
3. **Arquitectura Consistente**: Todos heredan de `BaseGenerator`
4. **Testing Unificado**: Tests organizados en `tests/test_generators/`

## 🚀 Resultado Final

```
curriculum/
├── src/generators/
│   ├── html_generator.py       # HTML/CSS moderno
│   ├── compact_generator.py    # PDF compacto 
│   ├── markdown_generator.py   # Markdown simple
│   ├── latex_generator.py      # LaTeX tradicional (nuevo)
│   └── reportlab_generator.py  # ReportLab avanzado (nuevo)
├── cv-suite                    # CLI unificada
└── (root limpio)
```

## ⚠️ Consideraciones

- **Backup**: Scripts legacy se mantienen en git history
- **Funcionalidad**: Verificar que no se pierda lógica única
- **Tests**: Validar que nueva arquitectura cubra todos los casos
- **Documentación**: Actualizar guides con nuevos generadores