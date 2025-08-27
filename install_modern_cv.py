#!/usr/bin/env python3
"""
Instalador de dependencias para generadores de CV modernos
"""

import subprocess
import sys
import os

def run_command(command, description):
    """Ejecuta un comando y maneja errores"""
    print(f"🔧 {description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} completado")
            return True
        else:
            print(f"❌ Error en {description}: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Error ejecutando {description}: {e}")
        return False

def install_python_packages():
    """Instala paquetes de Python necesarios"""
    packages = {
        "weasyprint": "Para conversión HTML → PDF (Opción 1)",
        "jinja2": "Para templates HTML (Opción 1)", 
        "reportlab": "Para generación PDF programática (Opción 2)",
        "markdown": "Para procesamiento Markdown (Opción 3)",
        "pyyaml": "Para configuración YAML"
    }
    
    print("📦 Instalando paquetes de Python...")
    print()
    
    success_count = 0
    for package, description in packages.items():
        print(f"🔧 Instalando {package} - {description}")
        if run_command(f"{sys.executable} -m pip install {package}", f"pip install {package}"):
            success_count += 1
        print()
    
    print(f"✅ {success_count}/{len(packages)} paquetes instalados correctamente")
    return success_count == len(packages)

def install_system_dependencies():
    """Instala dependencias del sistema"""
    print("🖥️  Verificando dependencias del sistema...")
    print()
    
    # Verificar pandoc
    try:
        result = subprocess.run(["pandoc", "--version"], capture_output=True)
        if result.returncode == 0:
            print("✅ Pandoc ya está instalado")
        else:
            raise FileNotFoundError
    except FileNotFoundError:
        print("⚠️  Pandoc no encontrado")
        if sys.platform == "darwin":  # macOS
            print("🔧 Instalando Pandoc con Homebrew...")
            if run_command("brew install pandoc", "Instalación de Pandoc"):
                print("✅ Pandoc instalado correctamente")
            else:
                print("❌ Error instalando Pandoc")
                print("💡 Instala manualmente: brew install pandoc")
        else:
            print("💡 Instala Pandoc manualmente desde: https://pandoc.org/installing.html")
    
    # Verificar LaTeX (opcional para pandoc PDF)
    try:
        result = subprocess.run(["xelatex", "--version"], capture_output=True)
        if result.returncode == 0:
            print("✅ XeLaTeX ya está instalado")
        else:
            raise FileNotFoundError
    except FileNotFoundError:
        print("⚠️  XeLaTeX no encontrado (opcional para mejor PDF)")
        if sys.platform == "darwin":  # macOS
            print("💡 Para mejor calidad PDF, instala: brew install --cask mactex")
        else:
            print("💡 Instala LaTeX para mejor calidad PDF")

def test_generators():
    """Prueba los generadores instalados"""
    print("🧪 Probando generadores...")
    print()
    
    # Test 1: HTML Generator
    try:
        import weasyprint
        import jinja2
        print("✅ Generador HTML+CSS funcional")
    except ImportError as e:
        print(f"❌ Generador HTML+CSS: {e}")
    
    # Test 2: ReportLab Generator
    try:
        import reportlab
        print("✅ Generador ReportLab funcional")
    except ImportError as e:
        print(f"❌ Generador ReportLab: {e}")
    
    # Test 3: Markdown Generator
    try:
        result = subprocess.run(["pandoc", "--version"], capture_output=True)
        if result.returncode == 0:
            print("✅ Generador Markdown funcional")
        else:
            print("❌ Generador Markdown: Pandoc no disponible")
    except FileNotFoundError:
        print("❌ Generador Markdown: Pandoc no encontrado")

def create_requirements_file():
    """Crea archivo requirements.txt"""
    requirements_content = """# Dependencias para generadores de CV modernos

# Opción 1: HTML+CSS → PDF (Recomendada)
weasyprint>=60.0
jinja2>=3.1.0

# Opción 2: Generación programática PDF
reportlab>=4.0.0

# Opción 3: Markdown → PDF (Más simple)
markdown>=3.5.0

# Utilidades
pyyaml>=6.0
pathlib2>=2.3.0 ; python_version < '3.4'

# Opcional: Para mejor manipulación de datos
pandas>=1.3.0
"""
    
    with open("requirements.txt", "w", encoding="utf-8") as f:
        f.write(requirements_content.strip())
    
    print("📝 Archivo requirements.txt creado")

def main():
    print("🚀 Instalador de Generadores de CV Modernos")
    print("=" * 50)
    print()
    
    print("Este script instalará las dependencias para 3 alternativas a LaTeX:")
    print("1. 🌐 HTML+CSS → PDF (weasyprint + jinja2)")
    print("2. 📊 Python directo → PDF (reportlab)")
    print("3. 📝 Markdown → PDF (pandoc)")
    print()
    
    response = input("¿Continuar con la instalación? (y/n): ")
    if response.lower() not in ['y', 'yes', 'sí', 'si']:
        print("❌ Instalación cancelada")
        return
    
    print()
    
    # Crear requirements.txt
    create_requirements_file()
    print()
    
    # Instalar paquetes Python
    python_success = install_python_packages()
    print()
    
    # Instalar dependencias del sistema
    install_system_dependencies()
    print()
    
    # Probar generadores
    test_generators()
    print()
    
    # Resumen final
    print("=" * 50)
    print("📋 RESUMEN DE INSTALACIÓN")
    print("=" * 50)
    
    if python_success:
        print("✅ Paquetes de Python instalados correctamente")
    else:
        print("⚠️  Algunos paquetes de Python fallaron")
    
    print()
    print("🎯 PRÓXIMOS PASOS:")
    print()
    print("1. 🌐 Prueba el generador HTML+CSS:")
    print("   python generate_cv_modern.py 'Globant' 'IoT Engineer'")
    print()
    print("2. 📊 Prueba el generador ReportLab:")
    print("   python generate_cv_reportlab.py 'Google' 'Software Engineer'")
    print()
    print("3. 📝 Prueba el generador Markdown:")
    print("   python generate_cv_simple.py 'Microsoft' 'Technical Lead'")
    print()
    print("💡 Ventajas de cada opción:")
    print("   HTML+CSS: Más flexible y moderno")
    print("   ReportLab: Control total programático")
    print("   Markdown: Simplicidad máxima")
    print()

if __name__ == "__main__":
    main()
