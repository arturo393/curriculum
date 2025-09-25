#!/usr/bin/env python3
"""
HTML Generator - CV Suite 2025
Generador moderno de CVs en HTML/CSS con conversión a PDF
Autor: Arturo Veras González
"""

import os
import sys
from pathlib import Path
from typing import List, Optional, Dict, Any
from jinja2 import Environment, FileSystemLoader, Template
from datetime import datetime

# Imports desde core
sys.path.append(str(Path(__file__).parent.parent))
from core.generator_base import BaseGenerator, GeneratorConfig
from core.data_parser import PersonalData


class HTMLGenerator(BaseGenerator):
    """Generador de CVs en HTML/CSS con conversión a PDF"""
    
    def __init__(self):
        super().__init__("html")
        self._setup_jinja()
    
    def _setup_jinja(self):
        """Configura el entorno Jinja2"""
        template_dir = self.templates_dir / "html"
        template_dir.mkdir(exist_ok=True)
        
        self.jinja_env = Environment(
            loader=FileSystemLoader(str(template_dir)),
            trim_blocks=True,
            lstrip_blocks=True
        )
    
    def generate_cv(self, config: GeneratorConfig) -> Optional[Path]:
        """
        Genera CV en HTML/CSS y opcionalmente convierte a PDF
        
        Args:
            config: Configuración del generador
            
        Returns:
            Path: Directorio con archivos generados
        """
        if not self.validate_config(config):
            return None
        
        try:
            self.log_generation_start(config)
            
            # Crear directorio de salida
            output_dir = self.create_output_directory(config)
            
            # Obtener contexto de personalización
            context = self.get_customization_context(config)
            
            # Generar HTML
            html_file = self._generate_html(context, output_dir, config.template_name)
            
            # Generar CSS
            css_file = self._generate_css(context, output_dir)
            
            # Intentar generar PDF si weasyprint está disponible
            pdf_file = self._generate_pdf(html_file, output_dir)
            
            self.log_generation_success(output_dir)
            return output_dir
            
        except Exception as e:
            self.log_generation_error(e)
            return None
    
    def _generate_html(self, context: Dict[str, Any], output_dir: Path, template_name: str) -> Path:
        """Genera el archivo HTML"""
        template_file = f"{template_name}.html"
        
        try:
            template = self.jinja_env.get_template(template_file)
        except:
            # Usar template por defecto si no existe el solicitado
            template = self._get_default_template()
        
        html_content = template.render(**context)
        
        html_file = output_dir / "cv.html"
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return html_file
    
    def _generate_css(self, context: Dict[str, Any], output_dir: Path) -> Path:
        """Genera el archivo CSS con variables de color"""
        css_content = self._get_modern_css(context['colors'])
        
        css_file = output_dir / "style.css"
        with open(css_file, 'w', encoding='utf-8') as f:
            f.write(css_content)
        
        return css_file
    
    def _generate_pdf(self, html_file: Path, output_dir: Path) -> Optional[Path]:
        """Genera PDF desde HTML usando weasyprint"""
        try:
            import weasyprint
            
            pdf_file = output_dir / "cv.pdf"
            
            # Configurar weasyprint
            css_file = output_dir / "style.css"
            css = weasyprint.CSS(str(css_file))
            
            html_doc = weasyprint.HTML(filename=str(html_file))
            html_doc.write_pdf(str(pdf_file), stylesheets=[css])
            
            print(f"   📄 PDF: {pdf_file.name}")
            return pdf_file
            
        except ImportError:
            print("   ⚠️  weasyprint no disponible - solo HTML generado")
            return None
        except Exception as e:
            print(f"   ⚠️  Error generando PDF: {e}")
            return None
    
    def _get_default_template(self) -> Template:
        """Retorna template HTML por defecto"""
        template_content = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ personal.name }} - {{ position }}</title>
    <link rel="stylesheet" href="style.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
</head>
<body>
    <div class="container">
        <!-- Header -->
        <header class="header">
            <div class="header-content">
                <div class="personal-info">
                    <h1 class="name">{{ personal.name }}</h1>
                    <h2 class="title">{{ position }}</h2>
                    <p class="company-target">{{ company }}</p>
                </div>
                <div class="contact-info">
                    <div class="contact-item">
                        <i class="fas fa-envelope"></i>
                        <span>{{ personal.email }}</span>
                    </div>
                    <div class="contact-item">
                        <i class="fas fa-phone"></i>
                        <span>{{ personal.phone }}</span>
                    </div>
                    <div class="contact-item">
                        <i class="fas fa-map-marker-alt"></i>
                        <span>{{ personal.location }}</span>
                    </div>
                    <div class="contact-item">
                        <i class="fab fa-linkedin"></i>
                        <a href="{{ personal.linkedin }}">LinkedIn</a>
                    </div>
                    <div class="contact-item">
                        <i class="fab fa-github"></i>
                        <a href="{{ personal.github }}">GitHub</a>
                    </div>
                </div>
            </div>
        </header>

        <!-- Main Content -->
        <main class="main-content">
            <!-- Summary -->
            <section class="section">
                <h3 class="section-title">
                    <i class="fas fa-user"></i>
                    Perfil Profesional
                </h3>
                <p class="summary">{{ personal.summary }}</p>
            </section>

            <!-- Experience -->
            <section class="section">
                <h3 class="section-title">
                    <i class="fas fa-briefcase"></i>
                    Experiencia Laboral
                </h3>
                <div class="experience-list">
                    {% for exp in personal.experience %}
                    <div class="experience-item">
                        <div class="experience-header">
                            <h4 class="position">{{ exp.position }}</h4>
                            <span class="company">{{ exp.company }}</span>
                            <span class="period">{{ exp.period }}</span>
                        </div>
                        <ul class="responsibilities">
                            {% for resp in exp.responsibilities %}
                            <li>{{ resp }}</li>
                            {% endfor %}
                        </ul>
                    </div>
                    {% endfor %}
                </div>
            </section>

            <!-- Skills -->
            <section class="section">
                <h3 class="section-title">
                    <i class="fas fa-code"></i>
                    Competencias Técnicas
                </h3>
                <div class="skills-grid">
                    {% for skill in personal.technical_skills %}
                    <span class="skill-tag">{{ skill }}</span>
                    {% endfor %}
                </div>
            </section>

            <!-- Education -->
            <section class="section">
                <h3 class="section-title">
                    <i class="fas fa-graduation-cap"></i>
                    Educación
                </h3>
                <div class="education-list">
                    {% for edu in personal.education %}
                    <div class="education-item">
                        <h4 class="degree">{{ edu.degree }}</h4>
                        <span class="institution">{{ edu.institution }}</span>
                        <span class="year">{{ edu.year }}</span>
                    </div>
                    {% endfor %}
                </div>
            </section>

            <!-- Certifications -->
            {% if personal.certifications %}
            <section class="section">
                <h3 class="section-title">
                    <i class="fas fa-certificate"></i>
                    Certificaciones
                </h3>
                <div class="certifications-list">
                    {% for cert in personal.certifications %}
                    <div class="certification-item">
                        <span class="cert-name">{{ cert.name }}</span>
                        {% if cert.issuer %}
                        <span class="cert-issuer">{{ cert.issuer }}</span>
                        {% endif %}
                    </div>
                    {% endfor %}
                </div>
            </section>
            {% endif %}
        </main>

        <!-- Footer -->
        <footer class="footer">
            <div class="footer-content">
                <p class="generation-info">
                    <i class="fas fa-palette"></i>
                    {{ meta.color_explanation }}
                </p>
                <p class="timestamp">
                    Generado el {{ meta.generated_at[:10] }} para {{ company }}
                </p>
            </div>
        </footer>
    </div>
</body>
</html>
        """
        return Template(template_content)
    
    def _get_modern_css(self, colors: Dict[str, str]) -> str:
        """Genera CSS moderno con variables de color"""
        return f"""
/* CV Suite 2025 - Modern CSS */
:root {{
    /* Colors */
    --primary-color: {colors['primary']};
    --secondary-color: {colors['secondary']};
    --accent-color: {colors['accent']};
    --text-color: {colors['text']};
    --background-color: {colors['background']};
    
    /* Typography */
    --font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    --font-size-base: 11pt;
    --font-size-small: 10pt;
    --line-height: 1.4;
    
    /* Spacing */
    --spacing-xs: 0.25rem;
    --spacing-sm: 0.5rem;
    --spacing-md: 1rem;
    --spacing-lg: 1.5rem;
    --spacing-xl: 2rem;
    
    /* Layout */
    --container-max-width: 210mm;
    --section-gap: 1.2rem;
}}

/* Reset and Base Styles */
* {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}}

body {{
    font-family: var(--font-family);
    font-size: var(--font-size-base);
    line-height: var(--line-height);
    color: var(--text-color);
    background-color: var(--background-color);
}}

/* Container */
.container {{
    max-width: var(--container-max-width);
    margin: 0 auto;
    background: white;
    box-shadow: 0 0 20px rgba(0,0,0,0.1);
    min-height: 100vh;
}}

/* Header */
.header {{
    background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
    color: white;
    padding: var(--spacing-lg);
}}

.header-content {{
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: var(--spacing-lg);
}}

.personal-info {{
    flex: 1;
}}

.name {{
    font-size: 1.8rem;
    font-weight: 700;
    margin-bottom: var(--spacing-xs);
}}

.title {{
    font-size: 1.2rem;
    font-weight: 500;
    margin-bottom: var(--spacing-xs);
    opacity: 0.95;
}}

.company-target {{
    font-size: var(--font-size-small);
    opacity: 0.9;
    font-weight: 300;
}}

.contact-info {{
    display: flex;
    flex-direction: column;
    gap: var(--spacing-xs);
    font-size: var(--font-size-small);
}}

.contact-item {{
    display: flex;
    align-items: center;
    gap: var(--spacing-sm);
}}

.contact-item i {{
    width: 16px;
    text-align: center;
    opacity: 0.9;
}}

.contact-item a {{
    color: white;
    text-decoration: none;
}}

.contact-item a:hover {{
    text-decoration: underline;
}}

/* Main Content */
.main-content {{
    padding: var(--spacing-lg);
}}

.section {{
    margin-bottom: var(--section-gap);
}}

.section-title {{
    display: flex;
    align-items: center;
    gap: var(--spacing-sm);
    font-size: 1.1rem;
    font-weight: 600;
    color: var(--primary-color);
    margin-bottom: var(--spacing-md);
    padding-bottom: var(--spacing-xs);
    border-bottom: 2px solid var(--accent-color);
}}

.section-title i {{
    font-size: 1rem;
}}

/* Summary */
.summary {{
    text-align: justify;
    font-size: var(--font-size-base);
    line-height: 1.5;
}}

/* Experience */
.experience-item {{
    margin-bottom: var(--spacing-md);
}}

.experience-header {{
    display: grid;
    grid-template-columns: 1fr auto;
    gap: var(--spacing-sm);
    margin-bottom: var(--spacing-sm);
}}

.position {{
    font-size: 1rem;
    font-weight: 600;
    color: var(--primary-color);
}}

.company {{
    font-weight: 500;
    color: var(--secondary-color);
}}

.period {{
    font-size: var(--font-size-small);
    color: #666;
    font-weight: 400;
    grid-column: 2;
    grid-row: 1 / 3;
    text-align: right;
}}

.responsibilities {{
    list-style: none;
    padding-left: var(--spacing-md);
}}

.responsibilities li {{
    position: relative;
    margin-bottom: var(--spacing-xs);
    font-size: var(--font-size-small);
    line-height: 1.4;
}}

.responsibilities li::before {{
    content: '▸';
    position: absolute;
    left: -var(--spacing-md);
    color: var(--accent-color);
    font-weight: bold;
}}

/* Skills */
.skills-grid {{
    display: flex;
    flex-wrap: wrap;
    gap: var(--spacing-sm);
}}

.skill-tag {{
    background: linear-gradient(45deg, var(--primary-color), var(--accent-color));
    color: white;
    padding: var(--spacing-xs) var(--spacing-sm);
    border-radius: 12px;
    font-size: var(--font-size-small);
    font-weight: 500;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}}

/* Education */
.education-item {{
    display: grid;
    grid-template-columns: 1fr auto;
    gap: var(--spacing-sm);
    margin-bottom: var(--spacing-sm);
}}

.degree {{
    font-size: 1rem;
    font-weight: 600;
    color: var(--primary-color);
}}

.institution {{
    font-size: var(--font-size-small);
    color: var(--secondary-color);
}}

.year {{
    font-size: var(--font-size-small);
    color: #666;
    grid-column: 2;
    grid-row: 1 / 3;
    text-align: right;
}}

/* Certifications */
.certifications-list {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: var(--spacing-sm);
}}

.certification-item {{
    background: var(--background-color);
    padding: var(--spacing-sm);
    border-radius: 8px;
    border-left: 3px solid var(--accent-color);
}}

.cert-name {{
    font-weight: 500;
    display: block;
    margin-bottom: var(--spacing-xs);
}}

.cert-issuer {{
    font-size: var(--font-size-small);
    color: #666;
}}

/* Footer */
.footer {{
    background: var(--background-color);
    padding: var(--spacing-md) var(--spacing-lg);
    border-top: 1px solid #e5e7eb;
    margin-top: auto;
}}

.footer-content {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: var(--font-size-small);
    color: #666;
}}

.generation-info {{
    display: flex;
    align-items: center;
    gap: var(--spacing-xs);
}}

.generation-info i {{
    color: var(--accent-color);
}}

/* Responsive */
@media (max-width: 768px) {{
    .header-content {{
        flex-direction: column;
        text-align: center;
    }}
    
    .contact-info {{
        align-items: center;
    }}
    
    .experience-header {{
        grid-template-columns: 1fr;
    }}
    
    .period {{
        grid-column: 1;
        grid-row: auto;
        text-align: left;
    }}
    
    .footer-content {{
        flex-direction: column;
        gap: var(--spacing-sm);
        text-align: center;
    }}
}}

/* Print Styles */
@media print {{
    body {{
        font-size: 10pt;
    }}
    
    .container {{
        box-shadow: none;
        max-width: none;
    }}
    
    .header {{
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
    }}
    
    .skill-tag {{
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
    }}
    
    .section {{
        break-inside: avoid;
    }}
    
    .experience-item {{
        break-inside: avoid;
    }}
}}

/* Single Page Optimization */
@page {{
    margin: 0.5in;
    size: A4;
}}

@media print {{
    .main-content {{
        padding: var(--spacing-md);
    }}
    
    .section {{
        margin-bottom: 1rem;
    }}
    
    .section-title {{
        margin-bottom: 0.7rem;
    }}
    
    .experience-item {{
        margin-bottom: 0.8rem;
    }}
    
    .responsibilities li {{
        margin-bottom: 0.2rem;
    }}
}}
        """
    
    def get_supported_templates(self) -> List[str]:
        """Retorna templates soportados"""
        templates = ["modern", "professional", "creative", "minimal"]
        
        # Buscar templates reales en directorio
        template_dir = self.templates_dir / "html"
        if template_dir.exists():
            real_templates = [
                f.stem for f in template_dir.glob("*.html")
                if not f.name.startswith('_')
            ]
            templates.extend(real_templates)
        
        return list(set(templates))
    
    def validate_dependencies(self) -> bool:
        """Valida dependencias del generador HTML"""
        try:
            import jinja2
            print("   ✅ jinja2: OK")
            
            try:
                import weasyprint
                print("   ✅ weasyprint: OK (PDF generation available)")
                return True
            except ImportError:
                print("   ⚠️  weasyprint: Missing (HTML only)")
                return True  # HTML funciona sin weasyprint
                
        except ImportError as e:
            print(f"   ❌ Missing dependency: {e}")
            return False
    
    def _get_template_extension(self) -> str:
        """Extensión de templates HTML"""
        return "html"


def main():
    """Función principal para uso directo del generador"""
    if len(sys.argv) < 3:
        print("💡 Uso: python html_generator.py 'Empresa' 'Posición' ['Template']")
        print("📝 Ejemplo: python html_generator.py 'Intel' 'Embedded Engineer' 'modern'")
        return
    
    company = sys.argv[1]
    position = sys.argv[2]
    template = sys.argv[3] if len(sys.argv) > 3 else "modern"
    
    # Crear configuración
    config = GeneratorConfig(
        company=company,
        position=position,
        template_name=template
    )
    
    # Generar CV
    generator = HTMLGenerator()
    output_path = generator.generate_cv(config)
    
    if output_path:
        print(f"🎉 CV HTML generado exitosamente en: {output_path}")
        
        # Abrir en navegador si está disponible
        import webbrowser
        html_file = output_path / "cv.html"
        if html_file.exists():
            webbrowser.open(str(html_file))
    else:
        print("❌ Error generando CV HTML")


if __name__ == "__main__":
    main()