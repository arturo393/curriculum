#!/usr/bin/env python3
"""
LaTeX Generator
Generador de CVs en LaTeX con personalización por empresa
Migrado desde generate_cv.py a nueva arquitectura
"""

import os
import sys
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional
import shutil

# Agregar path para imports
sys.path.append(str(Path(__file__).parent.parent))

from core.generator_base import BaseGenerator, GeneratorConfig
from core.data_parser import DataParser


class LaTeXGenerator(BaseGenerator):
    """Generador de CVs en LaTeX con personalización inteligente"""
    
    def __init__(self):
        super().__init__()
        self.generator_type = "latex"
        self.templates_dir = self.base_path / "templates"
        
        # Configuraciones por empresa/industria
        self.company_configs = {
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
            "consultancy_companies": {
                "globant": {
                    "keywords": ["digital transformation", "iot edge", "embedded systems", "microcontrollers", "rtos"],
                    "emphasis": ["c++", "python", "embedded systems", "linux", "cross-compilation", "agile"],
                    "culture": ["innovation", "collaboration", "client success", "technical excellence"],
                    "specific_tech": ["STM32", "ARM", "FreeRTOS", "I2C", "SPI", "PWM", "DMA", "cmake", "git"]
                }
            }
        }
    
    def get_dependencies(self) -> list:
        """Dependencias requeridas para LaTeX"""
        return ['pdflatex', 'texlive']
    
    def validate_dependencies(self) -> bool:
        """Valida que LaTeX esté instalado"""
        try:
            result = subprocess.run(['pdflatex', '--version'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                print(f"✅ pdflatex disponible")
                return True
            else:
                print(f"❌ pdflatex no encontrado")
                print(f"💡 Instala TeX Live: brew install --cask mactex")
                return False
        except FileNotFoundError:
            print(f"❌ pdflatex no instalado")
            print(f"💡 Instala TeX Live: brew install --cask mactex")
            return False
    
    def get_company_config(self, company_name: str) -> Dict[str, Any]:
        """Obtiene configuración específica para una empresa"""
        company_lower = company_name.lower()
        
        for industry, companies in self.company_configs.items():
            if company_lower in companies:
                return companies[company_lower]
        
        # Configuración por defecto
        return {
            "keywords": ["technology", "innovation", "excellence"],
            "emphasis": ["technical skills", "problem solving", "teamwork"],
            "culture": ["innovation", "collaboration", "excellence"]
        }
    
    def generate_personalized_profile(self, template_type: str, company: str, position: str) -> str:
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
            return f"{base_profile}, especializado en ecosistema Microsoft y Azure. Experto en soluciones enterprise con integración cloud nativa, accessibility y productividad. Experiencia en desarrollo inclusivo y metodologías growth mindset."
        
        elif "tesla" in company.lower():
            return f"{base_profile}, especializado en sistemas de tiempo real y safety-critical. Experto en automotive protocols, sistemas autónomos y desarrollo rápido de productos. Experiencia en innovación sostenible y iteración continua."
        
        elif "globant" in company.lower():
            return f"{base_profile}, especializado en IoT edge y sistemas embebidos. Experto en microcontroladores, RTOS y arquitecturas distribuidas. Experiencia en transformación digital y desarrollo ágil para clientes globales."
        
        else:
            return f"{base_profile}, con enfoque en {position.lower()} y tecnologías innovadoras. Experto en desarrollo de soluciones robustas y escalables con metodologías ágiles."
    
    def create_config_file(self, output_path: Path, config: GeneratorConfig) -> None:
        """Crea archivo de configuración específico de LaTeX"""
        company_config = self.get_company_config(config.company)
        keywords = ", ".join(company_config["keywords"][:5])  # Primeras 5 keywords
        
        config_content = f"""% Configuración específica para {config.company}
% Posición: {config.position}
% Template: {config.template_name}
% Generado: {datetime.now().strftime('%d de %B de %Y')}

% Variables de personalización
\\newcommand{{\\JOBCOMPANY}}{{{config.company}}}
\\newcommand{{\\JOBPOSITION}}{{{config.position}}}
\\newcommand{{\\JOBTEMPLATE}}{{{config.template_name}}}

% Configuración de compilación
\\newcommand{{\\SHOWPERSONALIZATION}}{{true}}  % Mostrar info de personalización
\\newcommand{{\\COLORSCHEME}}{{professional}}  % professional/modern/creative
\\newcommand{{\\FONTSIZE}}{{11pt}}             % 10pt/11pt/12pt
\\newcommand{{\\PAGELAYOUT}}{{compact}}        % compact/spacious

% Keywords para ATS (personalizar según empresa)
\\newcommand{{\\JOBKEYWORDS}}{{{keywords}}}

% Perfil personalizado
\\newcommand{{\\PERSONALIZEDPROFILE}}{{{self.generate_personalized_profile(config.template_name, config.company, config.position)}}}
"""
        
        config_file = output_path / "job_config.tex"
        with open(config_file, 'w', encoding='utf-8') as f:
            f.write(config_content)
    
    def copy_base_files(self, output_path: Path) -> None:
        """Copia archivos base necesarios"""
        # Copiar template base
        base_dir = self.templates_dir / "base"
        if base_dir.exists():
            shutil.copytree(base_dir, output_path / "base", dirs_exist_ok=True)
        
        # Copiar variables
        variables_dir = self.templates_dir / "variables"
        if variables_dir.exists():
            shutil.copytree(variables_dir, output_path / "variables", dirs_exist_ok=True)
        
        # Copiar archivos comunes
        common_dir = self.base_path / "common"
        if common_dir.exists():
            for file in common_dir.glob("*.tex"):
                shutil.copy2(file, output_path)
    
    def compile_pdf(self, cv_path: Path) -> bool:
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
    
    def create_main_tex(self, output_path: Path, data: Dict[str, Any], config: GeneratorConfig) -> None:
        """Crea el archivo main.tex principal"""
        main_content = f"""\\documentclass[11pt,a4paper,sans]{{moderncv}}

% Configuración específica del trabajo
\\input{{job_config}}

% Paquetes y configuración base
\\input{{common/packages}}
\\input{{personal_info}}

% Tema y colores
\\moderncvstyle{{classic}}
\\moderncvcolor{{blue}}

% Información personal
\\name{{{data['personal_info']['name']}}}{{{data['personal_info'].get('lastname', '')}}}
\\title{{{config.position}}}
\\address{{{data['personal_info'].get('address', '')}}}
\\phone[mobile]{{{data['personal_info'].get('phone', '')}}}
\\email{{{data['personal_info'].get('email', '')}}}
\\social[linkedin]{{{data['personal_info'].get('linkedin', '')}}}
\\social[github]{{{data['personal_info'].get('github', '')}}}

\\begin{{document}}

\\makecvtitle

% Perfil personalizado
\\section{{Perfil Profesional}}
\\cvitem{{}}{{\\PERSONALIZEDPROFILE}}

% Experiencia
\\section{{Experiencia Profesional}}
"""
        
        # Agregar experiencia
        for exp in data.get('experience', []):
            main_content += f"""
\\cventry{{{exp.get('period', '')}}}{{{exp.get('position', '')}}}{{{exp.get('company', '')}}}{{}}{{}}{{{exp.get('description', '')}}}
"""
        
        # Agregar educación
        main_content += f"""
\\section{{Educación}}
"""
        for edu in data.get('education', []):
            main_content += f"""
\\cventry{{{edu.get('period', '')}}}{{{edu.get('degree', '')}}}{{{edu.get('institution', '')}}}{{}}{{}}{{{edu.get('details', '')}}}
"""
        
        # Agregar habilidades
        main_content += f"""
\\section{{Habilidades Técnicas}}
"""
        for skill_cat in data.get('skills', []):
            skills_text = ", ".join(skill_cat.get('skills', []))
            main_content += f"""
\\cvitem{{{skill_cat.get('category', '')}}}{{{skills_text}}}
"""
        
        # Cerrar documento
        main_content += f"""
\\section{{Keywords para ATS}}
\\cvitem{{Tecnologías}}{{\\JOBKEYWORDS}}

\\end{{document}}
"""
        
        main_file = output_path / "main.tex"
        with open(main_file, 'w', encoding='utf-8') as f:
            f.write(main_content)
    
    def generate_cv(self, config: GeneratorConfig) -> Optional[Path]:
        """Genera CV en LaTeX"""
        try:
            # Validar dependencias
            if not self.validate_dependencies():
                return None
            
            # Crear directorio de salida
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            output_dir_name = f"cv_latex_{config.company.lower().replace(' ', '_')}_{timestamp}"
            output_path = self.output_dir / output_dir_name
            output_path.mkdir(parents=True, exist_ok=True)
            
            print(f"📁 Generando en: {output_path}")
            
            # Obtener datos
            data_parser = DataParser()
            data = data_parser.parse_anexos_md()
            
            # Copiar archivos base
            self.copy_base_files(output_path)
            
            # Crear configuración específica
            self.create_config_file(output_path, config)
            
            # Crear archivo principal
            self.create_main_tex(output_path, data, config)
            
            # Compilar PDF
            if self.compile_pdf(output_path):
                print(f"✅ CV LaTeX generado exitosamente en: {output_path}")
                return output_path / "main.pdf"
            else:
                print(f"⚠️  CV LaTeX creado (sin compilar) en: {output_path}")
                return output_path / "main.tex"
                
        except Exception as e:
            print(f"❌ Error generando CV LaTeX: {e}")
            return None
    
    def show_instructions(self, output_path: Path) -> None:
        """Muestra instrucciones para el usuario"""
        print()
        print("📋 Próximos pasos:")
        print(f"   1. Revisar personalización: {output_path}/job_config.tex")
        print(f"   2. Compilar PDF: cd {output_path} && pdflatex main.tex")
        print()
        print("💡 Tips:")
        print("   - Edita job_config.tex para personalización adicional")
        print("   - Revisa keywords para optimización ATS")
        print("   - Usa moderncv themes: classic, casual, oldstyle, banking")


# Registro del generador
if __name__ == "__main__":
    from core.generator_base import generator_registry
    
    generator = LaTeXGenerator()
    generator_registry.register(generator)
    
    # Test básico
    config = GeneratorConfig(
        company="Google",
        position="Software Engineer",
        template_name="software"
    )
    
    result = generator.generate_cv(config)
    if result:
        print(f"✅ Test exitoso: {result}")
    else:
        print("❌ Test fallido")