#!/usr/bin/env python3
"""
Main CLI - CV Suite 2025
Interfaz de línea de comandos unificada para generación de CVs
Autor: Arturo Veras González
"""

import argparse
import sys
from pathlib import Path
from typing import List, Dict, Any, Optional

# Agregar path para imports
sys.path.append(str(Path(__file__).parent.parent))

from core.generator_base import GeneratorConfig, generator_registry
from core.color_system import ColorSystem
from generators.html_generator import HTMLGenerator
from generators.compact_generator import CompactGenerator
from generators.markdown_generator import MarkdownGenerator
from generators.latex_generator import LaTeXGenerator
from generators.reportlab_advanced_generator import AdvancedReportLabGenerator


class CVSuiteCLI:
    """Interfaz de línea de comandos unificada"""
    
    def __init__(self):
        self.color_system = ColorSystem()
        self._register_generators()
    
    def _register_generators(self):
        """Registra todos los generadores disponibles"""
        try:
            html_gen = HTMLGenerator()
            generator_registry.register(html_gen)
        except Exception as e:
            print(f"⚠️  HTML Generator no disponible: {e}")
        
        try:
            compact_gen = CompactGenerator()
            generator_registry.register(compact_gen)
        except Exception as e:
            print(f"⚠️  Compact Generator no disponible: {e}")
        
        try:
            md_gen = MarkdownGenerator()
            generator_registry.register(md_gen)
        except Exception as e:
            print(f"⚠️  Markdown Generator no disponible: {e}")
        
        try:
            latex_gen = LaTeXGenerator()
            generator_registry.register(latex_gen)
        except Exception as e:
            print(f"⚠️  LaTeX Generator no disponible: {e}")
        
        try:
            reportlab_gen = AdvancedReportLabGenerator()
            generator_registry.register(reportlab_gen)
        except Exception as e:
            print(f"⚠️  Advanced ReportLab Generator no disponible: {e}")
    
    def show_header(self):
        """Muestra el header del sistema"""
        print("=" * 60)
        print("🎯 CV SUITE 2025 - GENERADOR INTELIGENTE DE CVs")
        print("   Arturo Veras González - Sistema Unificado")
        print("=" * 60)
        print()
    
    def list_generators(self):
        """Lista todos los generadores disponibles"""
        print("📊 GENERADORES DISPONIBLES:")
        print()
        
        generators_info = [
            {
                'type': 'html',
                'name': 'HTML/CSS Moderno 2025',
                'description': 'CV ultra-moderno con control total del diseño',
                'pros': 'Diseño 2025, ATS optimizado, control completo',
                'cons': 'Requiere weasyprint para PDF',
                'emoji': '🎨',
                'recommended': True
            },
            {
                'type': 'compact',
                'name': 'PDF Compacto ReportLab',
                'description': 'CV optimizado para 1 página con ReportLab',
                'pros': 'Compacto, PDF nativo, sin dependencias web',
                'cons': 'Diseño menos flexible',
                'emoji': '📄',
                'recommended': True
            },
            {
                'type': 'markdown',
                'name': 'Markdown Simple',
                'description': 'CV rápido en Markdown → PDF',
                'pros': 'Velocidad, simplicidad, fácil edición',
                'cons': 'Diseño limitado',
                'emoji': '⚡',
                'recommended': False
            },
            {
                'type': 'latex',
                'name': 'LaTeX Profesional',
                'description': 'CV tradicional en LaTeX con personalización',
                'pros': 'Control tipográfico, profesional, ATS friendly',
                'cons': 'Requiere TeX Live instalado',
                'emoji': '📝',
                'recommended': True
            },
            {
                'type': 'reportlab_advanced',
                'name': 'ReportLab Avanzado',
                'description': 'PDF avanzado con diseño moderno 2025',
                'pros': 'Diseño moderno, control total, sin LaTeX',
                'cons': 'Requiere ReportLab instalado',
                'emoji': '🚀',
                'recommended': True
            }
        ]
        
        available_types = generator_registry.list_available_types()
        
        for i, gen_info in enumerate(generators_info, 1):
            available = gen_info['type'] in available_types
            status = "✅ DISPONIBLE" if available else "❌ NO DISPONIBLE"
            rec_badge = " 🌟 RECOMENDADO" if gen_info['recommended'] and available else ""
            
            print(f"{gen_info['emoji']} {i}. {gen_info['name']}{rec_badge}")
            print(f"   📊 Estado: {status}")
            print(f"   💡 Descripción: {gen_info['description']}")
            print(f"   ✅ Pros: {gen_info['pros']}")
            print(f"   ⚠️  Cons: {gen_info['cons']}")
            print()
    
    def check_dependencies(self):
        """Verifica dependencias de todos los generadores"""
        print("🔍 VERIFICANDO DEPENDENCIAS:")
        print()
        
        deps_status = generator_registry.validate_all_dependencies()
        
        for gen_type, status in deps_status.items():
            status_icon = "✅" if status else "❌"
            generator = generator_registry.get_generator(gen_type)
            
            print(f"{status_icon} {gen_type.upper()} Generator:")
            if generator:
                generator.validate_dependencies()
            print()
    
    def predict_colors(self, company: str, position: str):
        """Predice y muestra el esquema de colores"""
        print(f"🎨 PREDICCIÓN DE COLORES PARA {company.upper()}")
        print()
        
        scheme = self.color_system.get_colors_for_job(company, position)
        
        print(f"🏢 Empresa: {company}")
        print(f"💼 Posición: {position}")
        print(f"🎯 Categoría: {scheme.category.value.title()}")
        print(f"🎨 Color Principal: {scheme.primary}")
        print(f"🎨 Color Secundario: {scheme.secondary}")
        print(f"🎨 Color de Acento: {scheme.accent}")
        print()
        print(f"🧠 Justificación Psicológica:")
        print(f"   {scheme.psychology}")
        print()
    
    def generate_cv(self, generator_type: str, company: str, position: str, 
                   template: str = "modern", job_description: str = ""):
        """Genera CV con el generador especificado"""
        
        # Verificar que el generador existe
        generator = generator_registry.get_generator(generator_type)
        if not generator:
            print(f"❌ Error: Generador '{generator_type}' no disponible")
            print("💡 Usa 'cv-suite list' para ver generadores disponibles")
            return False
        
        # Crear configuración
        config = GeneratorConfig(
            company=company,
            position=position,
            job_description=job_description,
            template_name=template
        )
        
        # Mostrar predicción de colores
        self.predict_colors(company, position)
        
        # Generar CV
        output_path = generator.generate_cv(config)
        
        if output_path:
            print(f"🎉 ¡CV generado exitosamente!")
            print(f"   📁 Ubicación: {output_path}")
            return True
        else:
            print("❌ Error generando CV")
            return False
    
    def interactive_mode(self):
        """Modo interactivo para seleccionar opciones"""
        self.show_header()
        
        print("🎯 MODO INTERACTIVO")
        print("Responde las siguientes preguntas para generar tu CV personalizado:")
        print()
        
        # Empresa
        company = input("🏢 Nombre de la empresa objetivo: ").strip()
        if not company:
            print("❌ Error: Nombre de empresa requerido")
            return
        
        # Posición
        position = input("💼 Título de la posición: ").strip()
        if not position:
            print("❌ Error: Título de posición requerido")
            return
        
        # Mostrar predicción de colores
        print()
        self.predict_colors(company, position)
        
        # Seleccionar generador
        print("📊 Selecciona el tipo de CV:")
        available_types = generator_registry.list_available_types()
        
        if not available_types:
            print("❌ Error: No hay generadores disponibles")
            return
        
        for i, gen_type in enumerate(available_types, 1):
            print(f"   {i}. {gen_type.upper()}")
        
        try:
            choice = int(input("\nElige una opción (número): ").strip())
            if 1 <= choice <= len(available_types):
                selected_type = available_types[choice - 1]
            else:
                print("❌ Opción inválida")
                return
        except ValueError:
            print("❌ Por favor ingresa un número válido")
            return
        
        # Descripción del trabajo (opcional)
        print()
        job_desc = input("📝 Descripción del trabajo (opcional, Enter para omitir): ").strip()
        
        # Generar CV
        print()
        print("🚀 Generando CV...")
        print()
        
        success = self.generate_cv(selected_type, company, position, 
                                 job_description=job_desc)
        
        if success:
            print("\n💡 ¿Quieres generar otro formato?")
            another = input("Responde (s/n): ").strip().lower()
            if another in ['s', 'si', 'sí', 'y', 'yes']:
                remaining_types = [t for t in available_types if t != selected_type]
                if remaining_types:
                    print(f"\n📊 Generadores restantes:")
                    for i, gen_type in enumerate(remaining_types, 1):
                        print(f"   {i}. {gen_type.upper()}")
                    
                    try:
                        choice2 = int(input("\nElige una opción: ").strip())
                        if 1 <= choice2 <= len(remaining_types):
                            second_type = remaining_types[choice2 - 1]
                            print()
                            self.generate_cv(second_type, company, position, 
                                           job_description=job_desc)
                    except ValueError:
                        print("❌ Opción inválida")
    
    def batch_generate(self, companies_positions: List[tuple], generator_type: str):
        """Generación en lote para múltiples empresas/posiciones"""
        print(f"🔄 GENERACIÓN EN LOTE - {generator_type.upper()}")
        print(f"📊 {len(companies_positions)} CVs a generar")
        print()
        
        successful = 0
        failed = 0
        
        for i, (company, position) in enumerate(companies_positions, 1):
            print(f"[{i}/{len(companies_positions)}] {company} - {position}")
            
            success = self.generate_cv(generator_type, company, position)
            if success:
                successful += 1
            else:
                failed += 1
            
            print("-" * 40)
        
        print(f"\n📊 RESUMEN DE GENERACIÓN EN LOTE:")
        print(f"   ✅ Exitosos: {successful}")
        print(f"   ❌ Fallidos: {failed}")
        print(f"   📈 Tasa de éxito: {successful/(successful+failed)*100:.1f}%")


def create_parser() -> argparse.ArgumentParser:
    """Crea el parser de argumentos de línea de comandos"""
    parser = argparse.ArgumentParser(
        description="CV Suite 2025 - Sistema unificado de generación de CVs",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  cv-suite list                                    # Listar generadores
  cv-suite check                                   # Verificar dependencias
  cv-suite colors "Intel" "Embedded Engineer"     # Predecir colores
  cv-suite generate html "Google" "Software Engineer"
  cv-suite generate compact "Microsoft" "Program Manager"
  cv-suite interactive                             # Modo interactivo
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Comandos disponibles')
    
    # Comando list
    subparsers.add_parser('list', help='Lista generadores disponibles')
    
    # Comando check
    subparsers.add_parser('check', help='Verifica dependencias')
    
    # Comando colors
    colors_parser = subparsers.add_parser('colors', help='Predice esquema de colores')
    colors_parser.add_argument('company', help='Nombre de la empresa')
    colors_parser.add_argument('position', help='Título de la posición')
    
    # Comando generate
    gen_parser = subparsers.add_parser('generate', help='Genera CV')
    gen_parser.add_argument('type', choices=['html', 'compact', 'markdown', 'latex', 'reportlab_advanced'], 
                           help='Tipo de generador')
    gen_parser.add_argument('company', help='Nombre de la empresa')
    gen_parser.add_argument('position', help='Título de la posición')
    gen_parser.add_argument('--template', default='modern', 
                           help='Template a usar (default: modern)')
    gen_parser.add_argument('--job-description', default='',
                           help='Descripción del trabajo')
    
    # Comando interactive
    subparsers.add_parser('interactive', help='Modo interactivo')
    
    return parser


def main():
    """Función principal de la CLI"""
    parser = create_parser()
    args = parser.parse_args()
    
    cli = CVSuiteCLI()
    
    if not args.command:
        cli.show_header()
        parser.print_help()
        return
    
    if args.command == 'list':
        cli.show_header()
        cli.list_generators()
    
    elif args.command == 'check':
        cli.show_header()
        cli.check_dependencies()
    
    elif args.command == 'colors':
        cli.show_header()
        cli.predict_colors(args.company, args.position)
    
    elif args.command == 'generate':
        cli.show_header()
        cli.generate_cv(
            args.type, 
            args.company, 
            args.position,
            args.template,
            args.job_description
        )
    
    elif args.command == 'interactive':
        cli.interactive_mode()


if __name__ == "__main__":
    main()