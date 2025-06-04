#!/usr/bin/env python3
"""
CV Generator Avanzado - Arturo Veras
Generador inteligente de CVs con personalización automática por empresa y rol
"""

import os
import sys
import json
import argparse
import configparser
from datetime import datetime
from pathlib import Path
import subprocess

class CVGenerator:
    def __init__(self):
        self.script_dir = Path(__file__).parent
        self.templates_dir = self.script_dir / "templates"
        self.output_dir = self.script_dir / "generated"
        self.config_file = self.templates_dir / "industry_config.py"
        
        # Crear directorio de salida
        self.output_dir.mkdir(exist_ok=True)
        
        # Cargar configuraciones
        self.load_configurations()
    
    def load_configurations(self):
        """Carga las configuraciones de industrias y empresas"""
        # Por simplicidad, usamos configuraciones hardcoded
        # En una implementación más avanzada, se cargarían desde archivo
        self.configs = {
            "tech_companies": {
                "google": {
                    "keywords": ["scalability", "distributed systems", "machine learning", "cloud native"],
                    "emphasis": ["python", "kubernetes", "big data", "open source"],
                    "culture": ["innovation", "collaboration", "data-driven", "user-focused"]
                },
                "microsoft": {
                    "keywords": ["azure", "enterprise", "cloud", "ai", "productivity"],
                    "emphasis": ["c#", "azure", "enterprise integration", "accessibility"],
                    "culture": ["inclusive", "growth mindset", "customer obsession"]
                }
            },
            "hardware_companies": {
                "tesla": {
                    "keywords": ["autonomous driving", "real-time systems", "safety critical"],
                    "emphasis": ["c++", "real-time", "automotive protocols", "safety standards"],
                    "culture": ["innovation", "sustainability", "rapid iteration"]
                }
            },
            "mining_industry": {
                "codelco": {
                    "keywords": ["mining operations", "industrial iot", "predictive maintenance"],
                    "emphasis": ["industrial protocols", "harsh environments", "24/7 operations"],
                    "culture": ["safety first", "operational excellence", "sustainability"]
                }
            }
        }
    
    def get_company_config(self, company_name):
        """Obtiene configuración específica para una empresa"""
        company_lower = company_name.lower()
        
        for industry, companies in self.configs.items():
            if company_lower in companies:
                return companies[company_lower]
        
        # Configuración por defecto si no se encuentra la empresa
        return {
            "keywords": ["technology", "innovation", "excellence"],
            "emphasis": ["technical skills", "problem solving", "teamwork"],
            "culture": ["innovation", "collaboration", "excellence"]
        }
    
    def generate_personalized_profile(self, template_type, company, position):
        """Genera perfil personalizado según empresa y posición"""
        config = self.get_company_config(company)
        
        base_profiles = {
            "software": "Ingeniero Civil Electrónico con 9+ años desarrollando soluciones end-to-end",
            "firmware": "Ingeniero Electrónico especializado en sistemas embebidos con 9+ años",
            "iot": "Ingeniero Electrónico especializado en IoT e Industria 4.0 con 9+ años",
            "lead": "Ingeniero Electrónico con 9+ años de experiencia técnica y 4+ años liderando equipos",
            "startup": "Ingeniero Electrónico emprendedor con 9+ años construyendo productos tecnológicos"
        }
        
        base_profile = base_profiles.get(template_type, base_profiles["software"])
        
        # Personalizar según empresa
        if "google" in company.lower():
            return f"{base_profile}, especializado en sistemas escalables y tecnologías cloud-native. Experto en arquitecturas distribuidas que procesan millones de transacciones, con experiencia en machine learning aplicado y contribuciones open source. Enfocado en soluciones data-driven que mejoran la experiencia del usuario."
        
        elif "microsoft" in company.lower():
            return f"{base_profile}, especializado en soluciones enterprise y cloud con Azure. Experto en integración de sistemas empresariales y desarrollo de aplicaciones productivas accesibles. Experiencia liderando transformación digital con enfoque en inclusividad y growth mindset."
        
        elif "tesla" in company.lower():
            return f"{base_profile}, especializado en sistemas críticos de tiempo real para aplicaciones automotrices. Experto en sistemas embebidos safety-critical, protocolos automotrices y desarrollo de firmware para vehículos autónomos. Enfocado en innovación sostenible y iteración rápida."
        
        else:
            return f"{base_profile}, con track record desarrollando soluciones innovadoras para {company}. Especializado en tecnologías de vanguardia con enfoque en excelencia técnica y resultados medibles."
    
    def create_customized_template(self, template_type, company, position, output_path):
        """Crea template personalizado con configuración específica"""
        
        # Leer template base
        template_file = self.templates_dir / "specialized" / f"cv_{template_type}.tex"
        
        if not template_file.exists():
            raise FileNotFoundError(f"Template no encontrado: {template_file}")
        
        with open(template_file, 'r', encoding='utf-8') as f:
            template_content = f.read()
        
        # Generar perfil personalizado
        custom_profile = self.generate_personalized_profile(template_type, company, position)
        
        # Reemplazar perfil en el template
        template_content = template_content.replace(
            r"\newcommand{\CVPROFILE}{%",
            f"\\newcommand{{\\CVPROFILE}}{{%\n{custom_profile}\n}}\n\n% Original profile:\n% \\newcommand{{\\CVPROFILEORIGINAL}}{{%"
        )
        
        # Agregar información de personalización
        customization_header = f"""% =============================================================================
% CV Personalizado para {company} - {position}
% Generado automáticamente el {datetime.now().strftime('%d de %B de %Y')}
% Template base: {template_type}
% =============================================================================

% Configuración de personalización
\\newcommand{{\\TARGETCOMPANY}}{{{company}}}
\\newcommand{{\\TARGETPOSITION}}{{{position}}}
\\newcommand{{\\CUSTOMIZATIONDATE}}{{{datetime.now().strftime('%d/%m/%Y')}}}

"""
        
        # Agregar header al contenido
        template_content = customization_header + template_content
        
        # Escribir template personalizado
        output_file = output_path / "main.tex"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(template_content)
        
        return output_file
    
    def generate_cv(self, template_type, company, position, compile=False):
        """Genera CV personalizado"""
        
        print(f"🚀 Generando CV personalizado")
        print(f"   Template: {template_type}")
        print(f"   Company: {company}")
        print(f"   Position: {position}")
        print()
        
        # Crear directorio de salida único
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_company = "".join(c if c.isalnum() else "_" for c in company.lower())
        output_name = f"cv_{template_type}_{safe_company}_{timestamp}"
        output_path = self.output_dir / output_name
        output_path.mkdir(exist_ok=True)
        
        try:
            # Crear template personalizado
            template_file = self.create_customized_template(template_type, company, position, output_path)
            
            # Copiar archivos base necesarios
            self.copy_base_files(output_path)
            
            # Crear archivo de configuración
            self.create_config_file(output_path, company, position, template_type)
            
            print(f"✅ CV generado en: {output_path}")
            
            # Compilar si se solicita
            if compile:
                self.compile_pdf(output_path)
            
            # Mostrar instrucciones
            self.show_instructions(output_path)
            
            return output_path
            
        except Exception as e:
            print(f"❌ Error generando CV: {e}")
            return None
    
    def copy_base_files(self, output_path):
        """Copia archivos base necesarios"""
        import shutil
        
        # Copiar template base
        base_dir = self.templates_dir / "base"
        if base_dir.exists():
            shutil.copytree(base_dir, output_path / "base", dirs_exist_ok=True)
        
        # Copiar variables
        variables_dir = self.templates_dir / "variables"
        if variables_dir.exists():
            shutil.copytree(variables_dir, output_path / "variables", dirs_exist_ok=True)
    
    def create_config_file(self, output_path, company, position, template_type):
        """Crea archivo de configuración específico"""
        config_content = f"""% Configuración específica para {company}
% Posición: {position}
% Template: {template_type}
% Generado: {datetime.now().strftime('%d de %B de %Y')}

% Variables de personalización
\\newcommand{{\\JOBCOMPANY}}{{{company}}}
\\newcommand{{\\JOBPOSITION}}{{{position}}}
\\newcommand{{\\JOBTEMPLATE}}{{{template_type}}}

% Configuración de compilación
\\newcommand{{\\SHOWPERSONALIZATION}}{{true}}  % Mostrar info de personalización
\\newcommand{{\\COLORSCHEME}}{{professional}}  % professional/modern/creative
\\newcommand{{\\FONTSIZE}}{{11pt}}             % 10pt/11pt/12pt
\\newcommand{{\\PAGELAYOUT}}{{compact}}        % compact/spacious

% Keywords para ATS (personalizar según empresa)
\\newcommand{{\\JOBKEYWORDS}}{{{company.lower()}, {position.lower()}, technology, engineering}}
"""
        
        config_file = output_path / "job_config.tex"
        with open(config_file, 'w', encoding='utf-8') as f:
            f.write(config_content)
    
    def compile_pdf(self, cv_path):
        """Compila el CV a PDF"""
        print("📄 Compilando PDF...")
        
        original_dir = os.getcwd()
        try:
            os.chdir(cv_path)
            
            # Ejecutar pdflatex dos veces para referencias
            for i in range(2):
                result = subprocess.run(
                    ["pdflatex", "-interaction=nonstopmode", "main.tex"],
                    capture_output=True,
                    text=True
                )
                
                if result.returncode != 0:
                    print(f"❌ Error en compilación {i+1}/2:")
                    print(result.stderr)
                    return False
            
            if (cv_path / "main.pdf").exists():
                print("✅ PDF generado exitosamente")
                
                # Abrir PDF en macOS
                if sys.platform == "darwin":
                    subprocess.run(["open", "main.pdf"])
                
                return True
            else:
                print("❌ No se pudo generar el PDF")
                return False
                
        finally:
            os.chdir(original_dir)
    
    def show_instructions(self, output_path):
        """Muestra instrucciones para el usuario"""
        print()
        print("📋 Próximos pasos:")
        print(f"   1. Revisar personalización: {output_path}/job_config.tex")
        print(f"   2. Compilar PDF: cd {output_path} && pdflatex main.tex")
        print(f"   3. O usar: python {__file__} --compile-path {output_path}")
        print()
        print("💡 Tips:")
        print("   - Edita job_config.tex para personalización adicional")
        print("   - Revisa keywords para optimización ATS")
        print("   - Ajusta colorscheme y layout según preferencias")
        print()
    
    def list_templates(self):
        """Lista templates disponibles"""
        print("📋 Templates disponibles:")
        print()
        
        specialized_dir = self.templates_dir / "specialized"
        if specialized_dir.exists():
            for template_file in specialized_dir.glob("cv_*.tex"):
                template_name = template_file.stem.replace("cv_", "")
                
                # Leer descripción del template
                try:
                    with open(template_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                        # Buscar línea de descripción
                        for line in content.split('\n'):
                            if "% Orientado a" in line:
                                description = line.replace("% Orientado a ", "").strip()
                                break
                        else:
                            description = "Template especializado"
                    
                    print(f"  🎯 {template_name}")
                    print(f"     {description}")
                    print()
                except:
                    print(f"  🎯 {template_name}")
                    print(f"     Template disponible")
                    print()

def main():
    parser = argparse.ArgumentParser(
        description="Generador inteligente de CVs personalizados",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  python generate_cv.py software Google "Senior Software Engineer"  
  python generate_cv.py firmware Tesla "Embedded Software Engineer" --compile
  python generate_cv.py iot Siemens "IoT Solutions Architect"
  python generate_cv.py lead Microsoft "Engineering Manager" --compile
  python generate_cv.py startup YCombinator "Technical Co-Founder"
        """
    )
    
    parser.add_argument("template", nargs="?", help="Tipo de template (software, firmware, iot, lead, startup)")
    parser.add_argument("company", nargs="?", help="Nombre de la empresa objetivo")
    parser.add_argument("position", nargs="?", help="Nombre de la posición")
    parser.add_argument("--compile", "-c", action="store_true", help="Compilar automáticamente a PDF")
    parser.add_argument("--list", "-l", action="store_true", help="Listar templates disponibles")
    parser.add_argument("--compile-path", help="Compilar CV en directorio específico")
    
    args = parser.parse_args()
    
    generator = CVGenerator()
    
    if args.list:
        generator.list_templates()
        return
    
    if args.compile_path:
        generator.compile_pdf(Path(args.compile_path))
        return
    
    if not all([args.template, args.company, args.position]):
        parser.print_help()
        return
    
    # Generar CV
    output_path = generator.generate_cv(
        args.template, 
        args.company, 
        args.position, 
        compile=args.compile
    )
    
    if output_path:
        print(f"🎉 CV generado exitosamente en: {output_path}")
    else:
        print("❌ Error generando CV")
        sys.exit(1)

if __name__ == "__main__":
    main()
