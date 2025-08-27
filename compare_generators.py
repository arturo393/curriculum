#!/usr/bin/env python3
"""
Comparador de Generadores de CV - LaTeX vs Alternativas Modernas
"""

import os
import subprocess
from pathlib import Path
from datetime import datetime

class CVGeneratorComparison:
    def __init__(self):
        self.script_dir = Path(__file__).parent
        
    def check_dependencies(self):
        """Verifica qué dependencias están instaladas"""
        print("🔍 VERIFICANDO DEPENDENCIAS")
        print("=" * 50)
        
        dependencies = {
            "LaTeX (actual)": {
                "commands": ["pdflatex", "--version"],
                "description": "Tu sistema actual LaTeX",
                "pros": ["Calidad profesional", "Control tipográfico"],
                "cons": ["Complejo", "Muchas dependencias", "Sintaxis difícil"]
            },
            "HTML+CSS (weasyprint)": {
                "commands": ["python", "-c", "import weasyprint; print('OK')"],
                "description": "Alternativa moderna recomendada",
                "pros": ["Fácil de entender", "Moderno", "Responsive", "Sin LaTeX"],
                "cons": ["Requiere Python packages"]
            },
            "ReportLab": {
                "commands": ["python", "-c", "import reportlab; print('OK')"],
                "description": "Generación programática directa",
                "pros": ["Control total", "Integración Python", "Sin templates"],
                "cons": ["Más código", "Menos flexible visualmente"]
            },
            "Markdown+Pandoc": {
                "commands": ["pandoc", "--version"],
                "description": "Opción más simple",
                "pros": ["Simplicidad máxima", "Focus en contenido", "Portable"],
                "cons": ["Menos control visual"]
            }
        }
        
        results = {}
        
        for name, config in dependencies.items():
            try:
                result = subprocess.run(
                    config["commands"], 
                    capture_output=True, 
                    text=True,
                    timeout=10
                )
                
                if result.returncode == 0:
                    print(f"✅ {name}: Disponible")
                    results[name] = True
                else:
                    print(f"❌ {name}: No disponible")
                    results[name] = False
                    
            except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
                print(f"❌ {name}: No disponible")
                results[name] = False
        
        print("\n📊 COMPARACIÓN DETALLADA")
        print("=" * 50)
        
        for name, config in dependencies.items():
            status = "✅ DISPONIBLE" if results[name] else "❌ NO DISPONIBLE"
            print(f"\n🔧 {name} - {status}")
            print(f"   📝 {config['description']}")
            print(f"   ✅ Pros: {', '.join(config['pros'])}")
            print(f"   ⚠️  Cons: {', '.join(config['cons'])}")
        
        return results
    
    def show_complexity_comparison(self):
        """Muestra comparación de complejidad"""
        print("\n🧩 COMPARACIÓN DE COMPLEJIDAD")
        print("=" * 50)
        
        comparisons = {
            "Configuración inicial": {
                "LaTeX": "❌ COMPLEJA - Instalar TeX Live (3GB+), múltiples paquetes",
                "HTML+CSS": "🟡 MEDIA - pip install weasyprint jinja2",
                "ReportLab": "🟡 MEDIA - pip install reportlab",
                "Markdown": "🟢 SIMPLE - brew install pandoc"
            },
            "Sintaxis para editar": {
                "LaTeX": "❌ DIFÍCIL - \\section{}, \\cventry{}, \\LaTeX{} sintaxis",
                "HTML+CSS": "🟢 FÁCIL - HTML familiar, CSS moderno",
                "ReportLab": "🟡 MEDIO - Python código",
                "Markdown": "🟢 SIMPLE - # Título, **negrita**, - lista"
            },
            "Debugging errores": {
                "LaTeX": "❌ PESADILLA - Errores crípticos, stack traces largos",
                "HTML+CSS": "🟢 FÁCIL - DevTools del navegador",
                "ReportLab": "🟡 MEDIO - Stack traces Python",
                "Markdown": "🟢 SIMPLE - Errores claros"
            },
            "Personalización": {
                "LaTeX": "🟡 COMPLEJA - Potente pero difícil",
                "HTML+CSS": "🟢 EXCELENTE - CSS moderno, flexbox, grid",
                "ReportLab": "🟡 PROGRAMÁTICA - Control total via código",
                "Markdown": "🟡 LIMITADA - Dependiente de pandoc templates"
            },
            "Tiempo de aprendizaje": {
                "LaTeX": "❌ SEMANAS - Sintaxis compleja",
                "HTML+CSS": "🟢 HORAS - Familiar para developers",
                "ReportLab": "🟡 DÍAS - API Python",
                "Markdown": "🟢 MINUTOS - Sintaxis natural"
            }
        }
        
        for category, options in comparisons.items():
            print(f"\n📋 {category}:")
            for method, rating in options.items():
                print(f"   {method}: {rating}")
    
    def show_examples(self):
        """Muestra ejemplos de código"""
        print("\n💻 EJEMPLOS DE CÓDIGO")
        print("=" * 50)
        
        print("\n🔧 LATEX (Tu método actual):")
        print("""```latex
\\section{Experience}
\\cventry{2021--Present}{IoT Engineer Sr.}{UQOMM}{Santiago}{}
{\\begin{itemize}
\\item Desarrollo de soluciones IoT para minería subterránea
\\item Implementación de sistemas tiempo real
\\end{itemize}}

% ¿Fácil de leer? ¿Fácil de editar?
```""")
        
        print("\n🌐 HTML+CSS (Alternativa recomendada):")
        print("""```html
<div class="experience">
    <h3>IoT Engineer Sr.</h3>
    <div class="company">UQOMM</div>
    <div class="period">2021 - Present</div>
    <ul>
        <li>Desarrollo de soluciones IoT para minería subterránea</li>
        <li>Implementación de sistemas tiempo real</li>
    </ul>
</div>

<!-- Mucho más legible y editable -->
```""")
        
        print("\n📝 MARKDOWN (Opción más simple):")
        print("""```markdown
## Experience

### UQOMM
**IoT Engineer Sr.** | *2021 - Present*

- Desarrollo de soluciones IoT para minería subterránea
- Implementación de sistemas tiempo real

# ¡Imposible de malinterpretar!
```""")
        
        print("\n🐍 PYTHON (Generación automática):")
        print("""```python
# Personalización automática por empresa
if company == "Globant":
    cv.add_experience(
        company="UQOMM",
        position="IoT Engineer Sr.", 
        highlights=["IoT Edge", "Digital Transformation"]
    )

# ¡Lógica programática!
```""")
    
    def show_file_sizes(self):
        """Muestra comparación de tamaños"""
        print("\n📁 COMPARACIÓN DE ARCHIVOS")
        print("=" * 50)
        
        file_info = {
            "LaTeX completo": {
                "size": "~500MB",
                "files": "TeX Live: 4000+ archivos",
                "description": "Instalación pesada"
            },
            "HTML+CSS": {
                "size": "~50MB", 
                "files": "weasyprint + jinja2",
                "description": "Instalación ligera"
            },
            "ReportLab": {
                "size": "~20MB",
                "files": "reportlab package",
                "description": "Muy ligero"
            },
            "Markdown": {
                "size": "~100MB",
                "files": "pandoc executable",
                "description": "Instalación media"
            }
        }
        
        for method, info in file_info.items():
            print(f"{method}:")
            print(f"   📦 Tamaño: {info['size']}")
            print(f"   📄 Archivos: {info['files']}")
            print(f"   📝 {info['description']}")
            print()
    
    def show_recommendations(self):
        """Muestra recomendaciones finales"""
        print("\n🎯 MIS RECOMENDACIONES")
        print("=" * 50)
        
        recommendations = [
            {
                "scenario": "🏆 PARA TI (Developer que quiere eficiencia)",
                "recommendation": "HTML+CSS con weasyprint",
                "reasons": [
                    "Familiar: Ya conoces HTML/CSS",
                    "Moderno: Flexbox, Grid, responsive design",
                    "Debuggeable: DevTools del navegador",
                    "Sin LaTeX: Elimina toda la complejidad",
                    "Automatable: Fácil integración con tu script Python"
                ]
            },
            {
                "scenario": "🚀 PARA MÁXIMA SIMPLICIDAD",
                "recommendation": "Markdown + Pandoc",
                "reasons": [
                    "Aprendizaje: 5 minutos",
                    "Edición: Cualquier editor de texto",
                    "Portabilidad: Funciona en cualquier sistema",
                    "Focus: Solo contenido, sin distracciones"
                ]
            },
            {
                "scenario": "🔧 PARA CONTROL TOTAL",
                "recommendation": "ReportLab Python",
                "reasons": [
                    "Programático: Lógica compleja en Python",
                    "Integración: Directo con tu base de datos",
                    "Performance: Genera PDFs muy rápido",
                    "Customización: Sin límites"
                ]
            }
        ]
        
        for rec in recommendations:
            print(f"\n{rec['scenario']}:")
            print(f"   🎯 Recomendación: {rec['recommendation']}")
            for reason in rec['reasons']:
                print(f"   ✅ {reason}")
    
    def show_migration_path(self):
        """Muestra cómo migrar desde LaTeX"""
        print("\n🔄 PLAN DE MIGRACIÓN DESDE LATEX")
        print("=" * 50)
        
        steps = [
            "1. 📦 Instalar dependencias:",
            "   pip install weasyprint jinja2  # Para HTML+CSS",
            "",
            "2. 🧪 Probar con un CV:",
            "   python generate_cv_modern.py 'Globant' 'IoT Engineer'",
            "",
            "3. 🎨 Personalizar template HTML:",
            "   Editar colores, fonts, layout en CSS",
            "",
            "4. 📊 Comparar resultados:",
            "   LaTeX PDF vs HTML+CSS PDF",
            "",
            "5. ✅ Migrar gradualmente:",
            "   Mantener LaTeX como backup inicial",
            "",
            "6. 🗑️ Limpiar LaTeX (opcional):",
            "   Desinstalar TeX Live cuando estés seguro"
        ]
        
        for step in steps:
            print(step)
        
        print(f"\n⏱️ Tiempo estimado de migración: 2-4 horas")
        print(f"💡 Beneficio: Ahorrarás horas en cada CV futuro")

def main():
    print("🆚 LATEX vs ALTERNATIVAS MODERNAS")
    print("=" * 50)
    
    comparator = CVGeneratorComparison()
    
    # Verificar dependencias
    results = comparator.check_dependencies()
    
    # Mostrar comparaciones
    comparator.show_complexity_comparison()
    comparator.show_examples()
    comparator.show_file_sizes()
    comparator.show_recommendations()
    comparator.show_migration_path()
    
    print("\n" + "=" * 50)
    print("🎉 CONCLUSIÓN")
    print("=" * 50)
    
    print("LaTeX es poderoso pero OVERKILL para CVs.")
    print("Las alternativas modernas son:")
    print("✅ Más fáciles de usar")
    print("✅ Más rápidas de configurar") 
    print("✅ Más fáciles de mantener")
    print("✅ Igual calidad de output")
    
    print(f"\n🚀 ¿Listo para probar las alternativas?")
    print(f"   python install_modern_cv.py")

if __name__ == "__main__":
    main()
