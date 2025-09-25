# 🚀 CV Simple HTML - Una Página Perfecta para PDF

> **Filosofía**: Un CV profesional en HTML, exportable a PDF en 2 minutos.

## ✨ ¿Por qué CV Simple HTML?

### El Problema
Los generadores de CV complejos tienen:
- ❌ **Múltiples formatos** confusos
- ❌ **Dependencias pesadas** (APIs, librerías)
- ❌ **Setup complicado** y configuraciones
- ❌ **Output inconsistente** entre plataformas

### La Solución Simple
CV Simple HTML ofrece:
- ✅ **Un solo formato**: HTML → PDF
- ✅ **Zero dependencias** (solo Python estándar)  
- ✅ **Una página perfecta** optimizada para A4
- ✅ **Resultado consistente** en todos los navegadores

## 🎯 Características

### 🔥 Output Profesional
- **A4 Optimizado**: Diseño que cabe perfectamente en una página
- **CSS Inline**: Fácil exportación sin dependencias externas
- **Print-Friendly**: Media queries específicas para PDF
- **Responsive**: Se ve bien en pantalla y papel

### ⚡ Workflow Ultra-Simple
1. **Ejecutar**: `python3 generate-cv.py` (10 segundos)
2. **Abrir HTML**: En cualquier navegador (5 segundos)
3. **Exportar PDF**: Ctrl+P → Guardar como PDF (10 segundos)
4. **Total**: **25 segundos** de CV profesional listo

### 🎨 Diseño Optimizado
- **Typography profesional**: Segoe UI, fuentes del sistema
- **Spacing perfecto**: Máximo contenido sin saturar
- **Grid layout**: Skills en 3 columnas, educación en 2
- **Color scheme**: Azul profesional con grises elegantes

## 🚀 Inicio Rápido

### Paso 1: Generar CV
```bash
python3 generate-cv.py
```

### Paso 2: Abrir HTML
```bash
# El archivo se genera en output/cv_arturo_veras_YYYYMMDD_HHMMSS.html
# Abrir con cualquier navegador
```

### Paso 3: Exportar PDF
1. **Ctrl+P** / **Cmd+P** (Imprimir)
2. **Destination**: Guardar como PDF
3. **Layout**: Retrato
4. **Margins**: Mínimos
5. **¡Listo!** CV profesional de una página

## 📁 Estructura

```
cv-simple/
├── 🚀 generate-cv.py           # Generador HTML único
├── 📊 cv-data.md               # Datos base (referencia)
├── 📄 output/                  # CVs HTML generados
├── 🔧 requirements.txt         # No dependencies!
└── 📖 README.md               # Esta guía
```

## 💡 Ejemplo de Output HTML

El generador crea un HTML como este:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <title>CV - Arturo Veras Olivos</title>
    <style>
        /* CSS optimizado para una página A4 */
        body { max-width: 794px; max-height: 1123px; }
        @media print { @page { size: A4; margin: 10mm; } }
    </style>
</head>
<body>
    <div class="header">
        <h1>Arturo Veras Olivos</h1>
        <div class="subtitle">Senior IoT Engineer & Embedded Systems Specialist</div>
    </div>
    <!-- Contenido optimizado en grid layout -->
</body>
</html>
```

**Resultado**: CV profesional que cabe perfectamente en una página A4.

## 📊 Comparación: Nuevo Enfoque

| Métrica | Sistema Anterior | CV Simple HTML | Mejora |
|---------|------------------|----------------|---------|
| **Dependencias** | 10+ paquetes | 0 (solo Python) | **100% menos** |
| **Output formats** | 5+ formatos | 1 óptimo (HTML→PDF) | **Foco claro** |
| **Setup time** | 30+ min | 10 segundos | **180x más rápido** |
| **File size** | Múltiples archivos | 1 HTML autocontenido | **Simple** |
| **Compatibilidad** | Depende de APIs | Cualquier navegador | **Universal** |

## ✅ Usar CV Simple Para:

- Generación rápida de CV profesional
- Export a PDF de alta calidad
- CV que cabe perfectamente en una página
- Workflow simple sin dependencias
- Resultado consistente multiplataforma

## ❌ No Usar Para:

- Múltiples páginas o formatos
- Personalización avanzada de diseño  
- Integración con sistemas complejos

## � Próximos Pasos

Si este enfoque HTML funciona bien, podemos:

1. **Perfeccionar el diseño** - Ajustar espacios y typography
2. **Agregar variantes** - Diferentes colores/estilos
3. **Optimizar PDF** - Print media queries más precisas
4. **Automatizar más** - Script para abrir y exportar automáticamente

---

**CV Simple HTML**: Una página perfecta, cero complicaciones. 🚀