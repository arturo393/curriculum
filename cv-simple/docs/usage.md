# 🚀 CV Simple - Guía de Uso

## ✨ Filosofía: Simplicidad > Complejidad

Este generador de CV sigue el principio de **máximo valor con mínima complejidad**:
- **Un script** vs 5 generadores complejos
- **150 líneas** vs 3000+ líneas de código  
- **3 dependencias** vs 10+ paquetes
- **1 workflow** vs múltiples formatos confusos

## 🎯 Objetivo

Generar **UN CV profesional excelente** optimizado para:
- ✅ **ATS (Applicant Tracking Systems)**
- ✅ **Reclutadores humanos**
- ✅ **Google Docs workflow familiar**
- ✅ **Exportación PDF de calidad**

## 🚀 Uso Rápido

### Paso 1: Generar CV Base
```bash
python generate-cv.py
```

### Paso 2: Seleccionar Perfil
- **IoT Engineer**: Para roles de sistemas embebidos e IoT
- **Firmware Developer**: Para desarrollo de firmware específico
- **Tech Lead**: Para liderazgo técnico y gestión
- **Product Engineer**: Para innovación y desarrollo de productos
- **Full-Stack IoT**: Para desarrollo completo hardware-software

### Paso 3: Workflow Google Docs
1. Copiar contenido Markdown generado
2. Pegar en Google Docs nuevo
3. Aplicar formato profesional (automático en v2.0)
4. Exportar como PDF

## 📁 Estructura de Archivos

```
cv-simple/
├── 📊 cv-data.md               # Datos base (editable)
├── 🚀 generate-cv.py           # Generador único
├── 📄 output/                  # CVs generados
│   └── cv_[rol]_[empresa]_[fecha].md
├── 📚 docs/                    
│   ├── usage.md               # Esta guía
│   └── setup-google-api.md    # Config Google API (v2.0)
└── 🔧 requirements.txt         # Dependencias mínimas
```

## 🎨 Personalización

### Modificar Datos Base
Editar `cv-data.md` con tus datos personales.

### Ajustar Templates
En `generate-cv.py`, personalizar métodos:
- `_get_professional_summary()`: Resumen por rol
- `_get_key_skills()`: Skills prioritarias  
- `_get_experience_section()`: Experiencia relevante

## 🆚 Comparación con Sistema Anterior

| Aspecto | Sistema Anterior | CV Simple |
|---------|------------------|-----------|
| **Archivos** | 20+ archivos Python | 1 archivo |
| **Líneas código** | 3000+ líneas | ~150 líneas |
| **Dependencias** | 10+ paquetes | 3 paquetes |
| **Setup time** | 30+ minutos | 2 minutos |
| **Mantenimiento** | Alto | Mínimo |
| **Usabilidad** | Técnica | Intuitiva |

## 🎯 Casos de Uso

### ✅ Perfecto Para:
- Generar CV para aplicaciones específicas
- Adaptación rápida a diferentes roles
- Workflow familiar (Google Docs)
- Mantenimiento simple de datos

### ❌ No Usar Para:
- Experimentación con múltiples formatos
- Showcase de habilidades de programación
- Sistemas complejos de templating

## 🔄 Roadmap Futuro

### v2.0 - Automatización Google Docs (Próximo)
- ✅ Crear documento automáticamente
- ✅ Aplicar formato profesional
- ✅ Exportar PDF sin intervención manual

### v3.0 - Optimizaciones (Futuro)
- Keywords automáticas por industria
- A/B testing de templates
- Métricas de efectividad

## 💡 Tips de Uso

### Para Máxima Efectividad:
1. **Personaliza cv-data.md** con tus datos reales
2. **Selecciona el rol correcto** según la aplicación
3. **Revisa el output** antes de enviar
4. **Usa Google Docs** para formato final
5. **Exporta PDF** con calidad alta

### Mejores Prácticas:
- Un CV por aplicación específica
- Keywords relevantes al rol objetivo
- Cuantifica logros cuando sea posible
- Mantén formato limpio y profesional

## 🆘 Solución de Problemas

### Error: Módulo no encontrado
```bash
pip install -r requirements.txt
```

### Output no se genera
- Verificar permisos de escritura en `output/`
- Comprobar que Python 3.7+ esté instalado

### Formato incorrecto en Google Docs
- Usar "Pegar sin formato" inicialmente
- Aplicar estilos después de pegar

## 📞 Soporte

Para problemas o mejoras:
1. Revisar esta documentación
2. Verificar ejemplos en `output/`
3. Consultar código fuente (solo 150 líneas!)

---

**Recuerda**: La simplicidad es una característica, no un defecto. Este generador hace exactamente lo que necesitas sin complicaciones innecesarias.