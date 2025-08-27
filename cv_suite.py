#!/usr/bin/env python3
"""
🚀 CV Generator Suite - Alternativas modernas a LaTeX
Generador unificado con múltiples opciones de salida
"""

import argparse
import subprocess
import sys
from pathlib import Path

def main():
    print("🚀 CV GENERATOR SUITE - Alternativas Modernas a LaTeX")
    print("=" * 60)
    
    parser = argparse.ArgumentParser(
        description="Generador unificado de CVs con múltiples opciones",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
🎯 EJEMPLOS DE USO:

  Generar CV simple (Markdown → PDF):
    python3 cv_suite.py simple "Globant" "IoT Engineer"
  
  CV personalizado para oferta específica:
    python3 cv_suite.py simple "Globant" "IoT Engineer" --job-description "Descripción de la oferta"
  
  Generar CV moderno (HTML+CSS → PDF):
    python3 cv_suite.py modern "Google" "Software Engineer"
  
  Generar CV programático (Python → PDF):
    python3 cv_suite.py reportlab "Microsoft" "Technical Lead"
  
  Comparar todas las opciones:
    python3 cv_suite.py compare
  
  Instalar dependencias:
    python3 cv_suite.py install

📊 COMPARACIÓN RÁPIDA:

  simple    → 🟢 Más fácil, 5 minutos para aprender
  modern    → 🎨 Más bonito, control visual completo  
  reportlab → 🔧 Más potente, control programático total
  
💡 RECOMENDACIÓN: Empieza con 'simple', luego migra a 'modern'
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Comandos disponibles')
    
    # Comando simple
    simple_parser = subparsers.add_parser('simple', help='CV simple (Markdown → PDF)')
    simple_parser.add_argument('company', help='Empresa objetivo')
    simple_parser.add_argument('position', help='Posición objetivo')
    simple_parser.add_argument('--job-description', '-j', type=str, default="",
                              help='Descripción de la oferta para personalización específica')
    
    # Comando modern
    modern_parser = subparsers.add_parser('modern', help='CV moderno (HTML+CSS → PDF)')
    modern_parser.add_argument('company', help='Empresa objetivo')
    modern_parser.add_argument('position', help='Posición objetivo')
    
    # Comando reportlab
    reportlab_parser = subparsers.add_parser('reportlab', help='CV programático (Python → PDF)')
    reportlab_parser.add_argument('company', help='Empresa objetivo')
    reportlab_parser.add_argument('position', help='Posición objetivo')
    
    # Comando compare
    subparsers.add_parser('compare', help='Comparar LaTeX vs alternativas')
    
    # Comando install
    subparsers.add_parser('install', help='Instalar dependencias')
    
    # Comando help-extended
    subparsers.add_parser('help-extended', help='Ayuda detallada')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        show_quick_start()
        return
    
    script_dir = Path(__file__).parent
    
    try:
        if args.command == 'simple':
            print(f"🚀 Generando CV Simple para {args.company} - {args.position}")
            cmd = [
                sys.executable, 
                str(script_dir / "generate_cv_simple.py"),
                args.company, 
                args.position
            ]
            if hasattr(args, 'job_description') and args.job_description:
                cmd.extend(['--job-description', args.job_description])
            subprocess.run(cmd, check=True)
            
        elif args.command == 'modern':
            print(f"🚀 Generando CV Moderno para {args.company} - {args.position}")
            try:
                subprocess.run([
                    sys.executable, 
                    str(script_dir / "generate_cv_modern.py"),
                    args.company, 
                    args.position
                ], check=True)
            except subprocess.CalledProcessError:
                print("❌ Error: Dependencias faltantes")
                print("💡 Instala con: python3 cv_suite.py install")
                
        elif args.command == 'reportlab':
            print(f"🚀 Generando CV ReportLab para {args.company} - {args.position}")
            try:
                subprocess.run([
                    sys.executable, 
                    str(script_dir / "generate_cv_reportlab.py"),
                    args.company, 
                    args.position
                ], check=True)
            except subprocess.CalledProcessError:
                print("❌ Error: Dependencias faltantes")
                print("💡 Instala con: python3 cv_suite.py install")
                
        elif args.command == 'compare':
            subprocess.run([
                sys.executable, 
                str(script_dir / "compare_generators.py")
            ], check=True)
            
        elif args.command == 'install':
            subprocess.run([
                sys.executable, 
                str(script_dir / "install_modern_cv.py")
            ], check=True)
            
        elif args.command == 'help-extended':
            show_extended_help()
            
    except FileNotFoundError as e:
        print(f"❌ Error: Archivo no encontrado - {e}")
        print("💡 Asegúrate de estar en el directorio correcto")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error ejecutando comando: {e}")
    except KeyboardInterrupt:
        print("\n❌ Operación cancelada por el usuario")

def show_quick_start():
    print("\n🚀 INICIO RÁPIDO")
    print("=" * 30)
    print("1. 🧪 Prueba el generador simple:")
    print("   python3 cv_suite.py simple 'Globant' 'IoT Engineer'")
    print()
    print("2. 📊 Compara con tu método actual:")
    print("   python3 cv_suite.py compare")
    print()
    print("3. 🔧 Instala dependencias para más opciones:")
    print("   python3 cv_suite.py install")
    print()
    print("💡 El generador 'simple' funciona sin dependencias adicionales!")

def show_extended_help():
    print("📖 AYUDA EXTENDIDA - CV GENERATOR SUITE")
    print("=" * 50)
    
    print("\n🎯 FILOSOFÍA")
    print("LaTeX es poderoso pero COMPLEJO para CVs.")
    print("Estas alternativas ofrecen 90% del resultado con 10% del esfuerzo.")
    
    print("\n📋 OPCIONES DISPONIBLES")
    
    options = [
        {
            "name": "simple",
            "description": "Markdown → PDF",
            "complexity": "🟢 FÁCIL",
            "dependencies": "pandoc (opcional)",
            "learning": "5 minutos",
            "use_case": "CVs rápidos, contenido-first"
        },
        {
            "name": "modern", 
            "description": "HTML+CSS → PDF",
            "complexity": "🟡 MEDIO",
            "dependencies": "weasyprint, jinja2",
            "learning": "1-2 horas",
            "use_case": "CVs modernos, control visual"
        },
        {
            "name": "reportlab",
            "description": "Python → PDF",
            "complexity": "🟡 MEDIO",
            "dependencies": "reportlab",
            "learning": "2-4 horas", 
            "use_case": "Automatización avanzada"
        }
    ]
    
    for opt in options:
        print(f"\n🔧 {opt['name'].upper()}")
        print(f"   📝 Método: {opt['description']}")
        print(f"   🎚️  Complejidad: {opt['complexity']}")
        print(f"   📦 Dependencias: {opt['dependencies']}")
        print(f"   ⏱️  Aprendizaje: {opt['learning']}")
        print(f"   🎯 Ideal para: {opt['use_case']}")
    
    print("\n🆚 VS LATEX")
    comparison = [
        ("Configuración inicial", "❌ 30+ min", "🟢 2-5 min"),
        ("Sintaxis", "❌ Compleja", "🟢 Familiar"),
        ("Debugging", "❌ Difícil", "🟢 Fácil"),
        ("Tamaño instalación", "❌ 500MB+", "🟢 20-100MB"),
        ("Tiempo generación", "❌ 30-60s", "🟢 1-5s"),
        ("Personalización", "🟡 Potente", "🟢 Intuitiva")
    ]
    
    print(f"{'Aspecto':<20} {'LaTeX':<15} {'Moderno':<15}")
    print("-" * 50)
    for aspect, latex, modern in comparison:
        print(f"{aspect:<20} {latex:<15} {modern:<15}")
    
    print("\n🎯 FLUJO RECOMENDADO")
    steps = [
        "1. 🧪 Prueba 'simple' para familiarizarte",
        "2. 📊 Compara resultado con tu CV actual",
        "3. 🔧 Instala dependencias si estás satisfecho",
        "4. 🎨 Migra a 'modern' para mejor control visual",
        "5. 🚀 Usa 'reportlab' solo si necesitas lógica compleja"
    ]
    
    for step in steps:
        print(step)
    
    print("\n💡 TIPS PROFESIONALES")
    tips = [
        "✅ Actualiza anexos.md con tu información real",
        "✅ Cada método personaliza automáticamente por empresa",
        "✅ Todos optimizan keywords para sistemas ATS",
        "✅ Mantén LaTeX como backup hasta estar seguro",
        "✅ Los archivos generados son portables y editables"
    ]
    
    for tip in tips:
        print(tip)

if __name__ == "__main__":
    main()
