#!/usr/bin/env python3
"""
CV Suite 2025 - Interfaz Unificada para Generación de CVs
Arturo Veras González
Sistema completo con mejores prácticas 2025
"""

import os
import sys
import argparse
from pathlib import Path

def show_header():
    """Muestra header del sistema"""
    print("=" * 70)
    print("🚀 CV SUITE 2025 - SISTEMA COMPLETO DE GENERACIÓN DE CVs")
    print("   👨‍💻 Arturo Veras González")
    print("   🎨 Tecnologías: LaTeX, Markdown, HTML+CSS, ReportLab")
    print("   ⭐ Año: 2025 - Mejores prácticas actuales")
    print("=" * 70)
    print()

def show_generators():
    """Muestra generadores disponibles"""
    generators = [
        {
            'name': 'LaTeX Clásico',
            'script': 'generate_cv.py',
            'description': 'CV tradicional LaTeX (complejo pero elegante)',
            'pros': 'Tipografía profesional, control total',
            'cons': 'Requiere LaTeX, curva de aprendizaje alta',
            'emoji': '📜',
            'recommended': False
        },
        {
            'name': 'Markdown Simple',
            'script': 'generate_cv_simple.py',
            'description': 'CV rápido en Markdown → PDF',
            'pros': 'Velocidad, simplicidad, personalización automática',
            'cons': 'Diseño limitado',
            'emoji': '⚡',
            'recommended': True
        },
        {
            'name': 'HTML+CSS Moderno 2025',
            'script': 'generate_cv_modern.py',
            'description': 'CV ultra-moderno con control total del diseño',
            'pros': 'Diseño 2025, ATS optimizado, control completo',
            'cons': 'Requiere weasyprint',
            'emoji': '🎨',
            'recommended': True
        },
        {
            'name': 'ReportLab Programático',
            'script': 'generate_cv_reportlab.py',
            'description': 'CV generado programáticamente con Python',
            'pros': 'Control programático total, gráficos avanzados',
            'cons': 'Más código, curva de aprendizaje',
            'emoji': '🐍',
            'recommended': False
        }
    ]
    
    print("📊 GENERADORES DISPONIBLES:")
    print()
    
    for i, gen in enumerate(generators, 1):
        rec_badge = " 🌟 RECOMENDADO" if gen['recommended'] else ""
        print(f"{gen['emoji']} {i}. {gen['name']}{rec_badge}")
        print(f"   📄 Script: {gen['script']}")
        print(f"   💡 Descripción: {gen['description']}")
        print(f"   ✅ Pros: {gen['pros']}")
        print(f"   ⚠️  Cons: {gen['cons']}")
        print()
    
    return generators

def check_dependencies():
    """Verifica dependencias de cada generador"""
    print("🔍 VERIFICANDO DEPENDENCIAS:")
    print()
    
    # LaTeX
    latex_ok = os.system("which pdflatex > /dev/null 2>&1") == 0
    status = "✅" if latex_ok else "❌"
    print(f"{status} LaTeX (pdflatex): {'Disponible' if latex_ok else 'No instalado'}")
    
    # Pandoc
    pandoc_ok = os.system("which pandoc > /dev/null 2>&1") == 0
    status = "✅" if pandoc_ok else "❌"
    print(f"{status} Pandoc: {'Disponible' if pandoc_ok else 'No instalado'}")
    
    # Python packages
    packages = ['weasyprint', 'jinja2', 'reportlab', 'matplotlib']
    for package in packages:
        try:
            __import__(package)
            print(f"✅ Python {package}: Disponible")
        except ImportError:
            print(f"❌ Python {package}: No instalado")
    
    print()
    
    # Recomendaciones
    print("💡 RECOMENDACIONES:")
    if not pandoc_ok:
        print("   📦 Instalar Pandoc: brew install pandoc")
    
    missing_packages = []
    for package in packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"   🐍 Instalar Python packages: pip install {' '.join(missing_packages)}")
    
    print()

def run_generator(script_name, company, position, job_description=""):
    """Ejecuta un generador específico"""
    script_path = Path(__file__).parent / script_name
    
    if not script_path.exists():
        print(f"❌ Error: {script_name} no encontrado")
        return False
    
    # Comandos específicos por generador
    if script_name == "generate_cv_simple.py":
        cmd = f'python3 "{script_path}" "{company}" "{position}"'
        if job_description:
            # Para Markdown, podemos pasar la descripción como argumento adicional
            import tempfile
            with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
                f.write(job_description)
                temp_file = f.name
            cmd += f' --job-description "{temp_file}"'
    
    elif script_name == "generate_cv_modern.py":
        cmd = f'python3 "{script_path}" "{company}" "{position}"'
    
    elif script_name == "generate_cv_reportlab.py":
        cmd = f'python3 "{script_path}" "{company}" "{position}"'
    
    elif script_name == "generate_cv.py":
        cmd = f'python3 "{script_path}" "{company}" "{position}"'
    
    else:
        cmd = f'python3 "{script_path}" "{company}" "{position}"'
    
    print(f"🚀 Ejecutando: {cmd}")
    print()
    
    result = os.system(cmd)
    return result == 0

def interactive_mode():
    """Modo interactivo para seleccionar opciones"""
    show_header()
    generators = show_generators()
    check_dependencies()
    
    # Selección de generador
    while True:
        try:
            choice = input(f"🎯 Selecciona un generador (1-{len(generators)}) o 'q' para salir: ").strip()
            
            if choice.lower() == 'q':
                print("👋 ¡Hasta luego!")
                return
            
            choice_num = int(choice)
            if 1 <= choice_num <= len(generators):
                selected_gen = generators[choice_num - 1]
                break
            else:
                print(f"❌ Selección inválida. Usa 1-{len(generators)}")
        except ValueError:
            print("❌ Por favor ingresa un número válido")
    
    print(f"\n🎨 Generador seleccionado: {selected_gen['name']}")
    if selected_gen['recommended']:
        print("🌟 ¡Excelente elección! Este es uno de nuestros generadores recomendados para 2025.")
    print()
    
    # Obtener información del trabajo
    company = input("🏢 Nombre de la empresa: ").strip()
    position = input("💼 Posición/Cargo: ").strip()
    
    job_description = ""
    if input("\n📝 ¿Tienes descripción del trabajo para personalizar? (y/n): ").strip().lower() == 'y':
        print("📄 Pega la descripción del trabajo (presiona Enter dos veces para terminar):")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        job_description = "\n".join(lines)
    
    print(f"\n🚀 Generando CV con {selected_gen['name']}...")
    print(f"   🏢 Empresa: {company}")
    print(f"   💼 Posición: {position}")
    if job_description:
        print(f"   📝 Personalización: Activada ({len(job_description)} caracteres)")
    print()
    
    # Ejecutar generador
    success = run_generator(selected_gen['script'], company, position, job_description)
    
    if success:
        print("🎉 ¡CV generado exitosamente!")
        print("💡 Tip: Revisa el archivo PDF generado y personaliza según necesites.")
    else:
        print("❌ Error generando CV")
        print("💡 Tip: Verifica que todas las dependencias estén instaladas.")

def quick_mode(generator_type, company, position, job_description=""):
    """Modo rápido con parámetros de línea de comandos"""
    generator_map = {
        'latex': 'generate_cv.py',
        'markdown': 'generate_cv_simple.py', 
        'modern': 'generate_cv_modern.py',
        'reportlab': 'generate_cv_reportlab.py'
    }
    
    if generator_type not in generator_map:
        print(f"❌ Tipo de generador inválido: {generator_type}")
        print(f"   Tipos disponibles: {', '.join(generator_map.keys())}")
        return False
    
    script_name = generator_map[generator_type]
    
    show_header()
    print(f"🎨 Generador: {generator_type.title()}")
    print(f"🏢 Empresa: {company}")
    print(f"💼 Posición: {position}")
    if generator_type in ['markdown', 'modern']:
        print("🌟 ¡Excelente elección para 2025!")
    print()
    
    return run_generator(script_name, company, position, job_description)

def show_recommendations():
    """Muestra recomendaciones específicas para 2025"""
    print("🎯 RECOMENDACIONES CV 2025:")
    print()
    print("1. 🎨 Para máximo control visual: HTML+CSS Moderno")
    print("   - Diseño 2025 actualizado")
    print("   - ATS-friendly")
    print("   - Personalización automática por industria")
    print()
    print("2. ⚡ Para velocidad y simplicidad: Markdown Simple")
    print("   - Generación rápida")
    print("   - Personalización automática")
    print("   - Ideal para aplicaciones múltiples")
    print()
    print("3. 📜 Para roles académicos/formales: LaTeX Clásico")
    print("   - Tipografía profesional")
    print("   - Ideal para investigación/academia")
    print("   - Requiere configuración técnica")
    print()

def main():
    parser = argparse.ArgumentParser(
        description="CV Suite 2025 - Sistema completo de generación de CVs",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
🎯 EJEMPLOS DE USO:

Modo interactivo (recomendado para nuevos usuarios):
  python cv_suite_2025.py

Modo rápido:
  python cv_suite_2025.py --type modern "AVOS Tech" "Ingeniero IoT"
  python cv_suite_2025.py --type markdown "Google" "Software Engineer"
  python cv_suite_2025.py --type latex "Microsoft" "Technical Lead"
  python cv_suite_2025.py --type reportlab "Startup" "CTO"

Ver recomendaciones:
  python cv_suite_2025.py --recommendations

Tipos disponibles: latex, markdown, modern, reportlab

🚀 RECOMENDACIÓN 2025: 
   - Para máximo control: 'modern' 
   - Para velocidad: 'markdown'
        """
    )
    
    parser.add_argument("company", nargs="?", help="Nombre de la empresa")
    parser.add_argument("position", nargs="?", help="Posición/cargo")
    parser.add_argument("--type", "-t", choices=['latex', 'markdown', 'modern', 'reportlab'],
                       help="Tipo de generador")
    parser.add_argument("--job-description", "-j", 
                       help="Archivo con descripción del trabajo para personalización")
    parser.add_argument("--recommendations", action="store_true",
                       help="Mostrar recomendaciones para 2025")
    
    args = parser.parse_args()
    
    # Mostrar recomendaciones
    if args.recommendations:
        show_header()
        show_recommendations()
        return
    
    # Modo interactivo si no se proporcionan argumentos
    if not args.company or not args.position or not args.type:
        interactive_mode()
        return
    
    # Cargar descripción del trabajo si se proporciona
    job_description = ""
    if args.job_description and os.path.exists(args.job_description):
        with open(args.job_description, 'r', encoding='utf-8') as f:
            job_description = f.read()
    
    # Modo rápido
    success = quick_mode(args.type, args.company, args.position, job_description)
    
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()
