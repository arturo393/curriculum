#!/usr/bin/env python3
"""
Generador de CV Simple - Arturo Veras
Markdown → PDF usando pandoc (la opción más simple)
"""

import os
import json
import argparse
import subprocess
from datetime import datetime
from pathlib import Path

class MarkdownCVGenerator:
    def __init__(self):
        self.script_dir = Path(__file__).parent
        self.output_dir = self.script_dir / "generated_markdown"
        self.data_file = self.script_dir / "anexos.md"
        
        # Crear directorio
        self.output_dir.mkdir(exist_ok=True)
        
        # Cargar datos
        self.personal_data = self.load_personal_data()
    
    def load_personal_data(self):
        """Carga datos reales desde anexos.md o valores corregidos"""
        # Calcular fecha actual para UQOMM (Sept 2021 - Agosto 2025)
        from datetime import datetime
        import calendar
        
        start_date = datetime(2021, 9, 1)  # Septiembre 2021
        current_date = datetime(2025, 8, 26)  # Agosto 2025 (fecha actual)
        
        # Calcular diferencia
        years = current_date.year - start_date.year
        months = current_date.month - start_date.month
        
        if months < 0:
            years -= 1
            months += 12
        
        uqomm_period = f"Sept 2021 - Presente ({years} años {months} meses)"
        
        return {
            "name": "Arturo Veras Olivos",  # Nombre real
            "title": "Ingeniero Civil Electrónico",
            "email": "a.veras@gmail.com",  # Email real
            "phone": "+56 9 82413883",  # Teléfono real
            "location": "Santiago, Chile (La Florida)",  # Ubicación específica
            "linkedin": "linkedin.com/in/arturo-veras",
            "github": "github.com/arturo393",
            "summary": "Ingeniero Civil Electrónico con 9+ años desarrollando soluciones tecnológicas innovadoras, especializándome en sistemas embebidos, IoT, hardware/software integration, y transformación digital empresarial con visión 360° del producto tecnológico.",
            "experience": [
                {
                    "company": "UQOMM SpA",
                    "position": "Encargado de Software y Firmware",  # Cargo real
                    "period": uqomm_period,  # Período calculado dinámicamente
                    "achievements": [
                        "Planificación, gestión, diseño y desarrollo de proyectos de software para minería subterránea",
                        "Sistema de monitoreo de amplificadores en Python, integrando hardware serial, React y MongoDB",
                        "Desarrollo de firmware en C/C++ para microcontroladores STM32 Cortex M0 con gestión de periféricos",
                        "Configuración y mantenimiento de servidores Google Cloud, Odoo y Linux"
                    ]
                },
                {
                    "company": "BlackGPS",
                    "position": "Ingeniero de Hardware",  # Cargo real
                    "period": "Jul 2017 - Ago 2021 (4 años 2 meses)",
                    "achievements": [
                        "Diseño y desarrollo de dispositivo anti-robo para camiones con inhibidor de señales GNSS y GSM",
                        "Configuración y soporte de dispositivos de control de flotas (Teltonika, DCT Syrus, ERM Starlink)",
                        "Implementación de funcionalidades en servidor SpringBoot Java para procesamiento de datos GPS y CANBus",
                        "Desarrollo de aplicación móvil Flutter con comunicación Bluetooth para control de vehículos"
                    ]
                }
            ],
            "skills": {
                "Embedded Systems": ["STM32 Cortex M0", "C/C++", "Gestión de periféricos", "Interrupciones"],
                "Programming Languages": ["C/C++", "Python", "Java", "JavaScript"],
                "IoT & Communications": ["MQTT", "Serial Communication", "RF Systems", "GNSS", "GSM"],
                "Web & Mobile": ["React", "MongoDB", "SpringBoot", "Flutter"],
                "Cloud & DevOps": ["Google Cloud", "Linux", "Odoo", "Servidores"],
                "Tools & Hardware": ["Analizador de espectros", "Generadores de señales", "Teltonika", "DCT Syrus"]
            },
            "education": [
                {
                    "degree": "Ingeniería Civil Electrónica",
                    "institution": "Universidad Técnica Federico Santa María",
                    "year": "2013 - 2017",
                    "location": "Valparaíso, Chile"
                }
            ],
            "languages": [
                {"name": "Español", "level": "Nativo"},
                {"name": "Inglés", "level": "B2 Upper Intermediate (técnico fluido)"}
            ]
        }
        """Carga datos básicos desde anexos.md o usa valores por defecto"""
        return {
            "name": "Arturo Veras González",
            "title": "Ingeniero Civil Electrónico",
            "email": "arturoveras93@gmail.com",
            "phone": "+56 9 5516 2574",
            "location": "Santiago, Chile",
            "linkedin": "linkedin.com/in/arturo-veras",
            "github": "github.com/arturo393",
            "summary": "Ingeniero Civil Electrónico con 9+ años desarrollando soluciones IoT innovadoras, especializándome en sistemas embebidos, hardware/software integration, y transformación digital empresarial.",
            "experience": [
                {
                    "company": "UQOMM",
                    "position": "Ingeniero de Software IoT Sr.",
                    "period": "Sept 2021 - Presente (3 años 10 meses)",
                    "achievements": [
                        "Desarrollo de soluciones IoT para minería subterránea con tecnologías edge computing",
                        "Implementación de sistemas de monitoreo en tiempo real usando STM32 y FreeRTOS",
                        "Liderazgo técnico en proyectos de integración hardware/software para ambientes industriales extremos",
                        "Arquitectura de comunicaciones LoRa y MQTT para redes mesh subterráneas"
                    ]
                },
                {
                    "company": "BlackGPS",
                    "position": "Ingeniero de Desarrollo",
                    "period": "Jul 2017 - Ago 2021 (4 años 2 meses)",
                    "achievements": [
                        "Desarrollo full-stack de plataforma de rastreo GPS con más de 10,000 dispositivos activos",
                        "Implementación de APIs RESTful y arquitectura de microservicios con Node.js y MongoDB",
                        "Desarrollo de aplicaciones móviles React Native para gestión de flotas vehiculares",
                        "Optimización de performance y escalabilidad para manejar millones de puntos GPS diarios"
                    ]
                }
            ],
            "skills": {
                "Embedded Systems": ["STM32 Cortex M0/M4", "ARM", "FreeRTOS", "Linux Embebido", "Yocto Project"],
                "Programming Languages": ["C/C++", "Python", "JavaScript", "TypeScript", "Rust"],
                "IoT & Communications": ["MQTT", "LoRa", "Modbus", "CAN Bus", "I2C", "SPI", "UART"],
                "Web & Mobile": ["React", "Node.js", "MongoDB", "React Native", "Next.js"],
                "Cloud & DevOps": ["Docker", "Kubernetes", "AWS IoT Core", "Azure IoT Hub", "CI/CD"],
                "Tools & Methodologies": ["Git", "Agile/Scrum", "Test-Driven Development", "Design Patterns"]
            },
            "education": [
                {
                    "degree": "Ingeniería Civil Electrónica",
                    "institution": "Universidad Técnica Federico Santa María",
                    "year": "2013 - 2017",
                    "location": "Valparaíso, Chile",
                    "details": "Especialización en Sistemas Electrónicos y Automatización Industrial"
                }
            ],
            "languages": [
                {"name": "Español", "level": "Nativo"},
                {"name": "Inglés", "level": "Avanzado (B2-C1)"}
            ],
            "certifications": [
                "FreeRTOS Fundamentals",
                "AWS IoT Core Certified",
                "Agile/Scrum Master"
            ]
        }
    
    def customize_content(self, company, position):
        """Personaliza el contenido según empresa y posición"""
        base_data = self.personal_data.copy()
        
        company_lower = company.lower()
        position_lower = position.lower()
        
        # Personalizar resumen
        if "globant" in company_lower and "iot" in position_lower:
            base_data["summary"] = f"{base_data['summary']} Especializado en transformación digital empresarial con tecnologías IoT Edge, microcontroladores STM32, y metodologías Agile para entregar productos digitales escalables."
        elif "google" in company_lower:
            base_data["summary"] = f"{base_data['summary']} Enfocado en sistemas escalables, tecnologías cloud-native, y soluciones data-driven que procesan millones de transacciones."
        elif "microsoft" in company_lower:
            base_data["summary"] = f"{base_data['summary']} Especializado en soluciones enterprise, plataformas Azure, y desarrollo de aplicaciones productivas accesibles."
        
        # Destacar habilidades relevantes
        if "iot" in position_lower:
            priority_skills = ["Embedded Systems", "IoT & Communications", "Programming Languages"]
        elif "software" in position_lower:
            priority_skills = ["Programming Languages", "Web & Mobile", "Cloud & DevOps"]
        elif "firmware" in position_lower:
            priority_skills = ["Embedded Systems", "Programming Languages", "IoT & Communications"]
        else:
            priority_skills = list(base_data["skills"].keys())
        
        # Reordenar skills según prioridad
        reordered_skills = {}
        for skill_category in priority_skills:
            if skill_category in base_data["skills"]:
                reordered_skills[skill_category] = base_data["skills"][skill_category]
        
        for skill_category, skills in base_data["skills"].items():
            if skill_category not in reordered_skills:
                reordered_skills[skill_category] = skills
        
        base_data["skills"] = reordered_skills
        
        return base_data
    
    def customize_for_job_offer(self, company, position, job_description=""):
        """Personaliza el CV específicamente para una oferta de trabajo"""
        data = self.customize_content(company, position)
        
        # Si hay descripción del trabajo, analizar keywords
        if job_description:
            job_lower = job_description.lower()
            
            # Detectar tecnologías mencionadas y priorizar skills
            mentioned_skills = []
            skill_keywords = {
                "STM32": ["stm32", "arm", "cortex"],
                "C/C++": ["c++", "c programming", "embedded c"],
                "Python": ["python", "django", "flask"],
                "IoT": ["iot", "internet of things", "edge"],
                "MQTT": ["mqtt", "messaging"],
                "React": ["react", "javascript", "frontend"],
                "MongoDB": ["mongodb", "database", "nosql"],
                "Linux": ["linux", "ubuntu", "server"],
                "Cloud": ["cloud", "aws", "gcp", "azure"],
                "Agile": ["agile", "scrum", "kanban"],
                "Git": ["git", "version control", "github"],
                "Docker": ["docker", "container", "kubernetes"]
            }
            
            for skill, keywords in skill_keywords.items():
                if any(keyword in job_lower for keyword in keywords):
                    mentioned_skills.append(skill)
            
            # Reordenar skills poniendo las mencionadas primero
            if mentioned_skills:
                reordered_skills = {}
                
                # Primero las skills mencionadas
                for category, skills in data["skills"].items():
                    category_skills = []
                    other_skills = []
                    
                    for skill in skills:
                        if any(mentioned in skill for mentioned in mentioned_skills):
                            category_skills.append(f"**{skill}**")  # Destacar
                        else:
                            other_skills.append(skill)
                    
                    if category_skills or other_skills:
                        reordered_skills[category] = category_skills + other_skills
                
                data["skills"] = reordered_skills
            
            # Personalizar resumen con keywords de la oferta
            keywords_found = []
            if "iot" in job_lower:
                keywords_found.append("IoT")
            if "edge" in job_lower:
                keywords_found.append("edge computing")
            if "embedded" in job_lower:
                keywords_found.append("sistemas embebidos")
            if "firmware" in job_lower:
                keywords_found.append("desarrollo de firmware")
            if "agile" in job_lower:
                keywords_found.append("metodologías Agile")
            
            if keywords_found:
                keyword_text = ", ".join(keywords_found)
                data["summary"] += f" Experiencia específica en {keyword_text} alineada con los requerimientos del puesto."
        
        return data
    
    def generate_markdown(self, company, position):
        """Genera contenido en Markdown"""
        data = self.customize_content(company, position)
        
        markdown_content = f"""---
title: "CV - {data['name']}"
author: "{data['name']}"
date: "{datetime.now().strftime('%B %Y')}"
geometry: margin=2cm
fontsize: 11pt
colorlinks: true
linkcolor: blue
urlcolor: blue
header-includes: |
  \\usepackage{{fancyhdr}}
  \\pagestyle{{fancy}}
  \\fancyhead[L]{{}}
  \\fancyhead[C]{{}}
  \\fancyhead[R]{{\\textcolor{{gray}}{{Personalizado para {company} - {position}}}}}
  \\fancyfoot[L]{{\\textcolor{{gray}}{{Generado el {datetime.now().strftime('%d de %B de %Y')}}}}}
  \\fancyfoot[C]{{}}
  \\fancyfoot[R]{{\\thepage}}
---

# {data['name']}

## {data['title']}

---

**📧 Email:** {data['email']}  
**📱 Teléfono:** {data['phone']}  
**📍 Ubicación:** {data['location']}  
**💼 LinkedIn:** [{data['linkedin']}](https://{data['linkedin']})  
**💻 GitHub:** [{data['github']}](https://{data['github']})  

---

## 🎯 Perfil Profesional

{data['summary']}

---

## 💼 Experiencia Profesional

"""
        
        # Agregar experiencia
        for exp in data['experience']:
            markdown_content += f"""### {exp['company']}
**{exp['position']}**  
*{exp['period']}*

"""
            for achievement in exp['achievements']:
                markdown_content += f"- {achievement}\n"
            markdown_content += "\n"
        
        # Agregar habilidades técnicas
        markdown_content += "## 🛠️ Competencias Técnicas\n\n"
        
        for category, skills in data['skills'].items():
            skills_text = " • ".join(skills)
            markdown_content += f"**{category}:** {skills_text}\n\n"
        
        # Agregar educación
        markdown_content += "## 🎓 Educación\n\n"
        for edu in data['education']:
            markdown_content += f"""### {edu['degree']}
**{edu['institution']}**  
*{edu['year']} | {edu['location']}*

"""
            if 'details' in edu:
                markdown_content += f"{edu['details']}\n\n"
        
        # Agregar idiomas
        markdown_content += "## 🌍 Idiomas\n\n"
        for lang in data['languages']:
            markdown_content += f"- **{lang['name']}:** {lang['level']}\n"
        
        # Agregar certificaciones si existen
        if 'certifications' in data and data['certifications']:
            markdown_content += "\n## 📜 Certificaciones\n\n"
            for cert in data['certifications']:
                markdown_content += f"- {cert}\n"
        
        markdown_content += f"""

---

*CV generado automáticamente el {datetime.now().strftime('%d de %B de %Y')} | Personalizado para {company} - {position}*
"""
        
        return markdown_content
    
    def generate_markdown_for_job(self, company, position, job_description):
        """Genera contenido en Markdown personalizado para una oferta específica"""
        data = self.customize_for_job_offer(company, position, job_description)
        
        # Agregar sección de keywords detectadas
        detected_keywords = []
        job_lower = job_description.lower()
        
        keywords_to_check = ["iot", "edge", "embedded", "firmware", "stm32", "python", "c++", "agile", "mqtt", "linux"]
        for keyword in keywords_to_check:
            if keyword in job_lower:
                detected_keywords.append(keyword.upper())
        
        markdown_content = f"""---
title: "CV - {data['name']}"
author: "{data['name']}"
date: "{datetime.now().strftime('%B %Y')}"
geometry: margin=2cm
fontsize: 11pt
colorlinks: true
linkcolor: blue
urlcolor: blue
header-includes: |
  \\usepackage{{fancyhdr}}
  \\pagestyle{{fancy}}
  \\fancyhead[L]{{}}
  \\fancyhead[C]{{}}
  \\fancyhead[R]{{\\textcolor{{gray}}{{Personalizado para {company} - {position}}}}}
  \\fancyfoot[L]{{\\textcolor{{gray}}{{Generado el {datetime.now().strftime('%d de %B de %Y')}}}}}
  \\fancyfoot[C]{{}}
  \\fancyfoot[R]{{\\thepage}}
---

# {data['name']}

## {data['title']}

---

**📧 Email:** {data['email']}  
**📱 Teléfono:** {data['phone']}  
**📍 Ubicación:** {data['location']}  
**💼 LinkedIn:** [{data['linkedin']}](https://{data['linkedin']})  
**💻 GitHub:** [{data['github']}](https://{data['github']})  

---"""

        # Agregar keywords detectadas si las hay
        if detected_keywords:
            keywords_text = " • ".join(detected_keywords)
            markdown_content += f"""

## 🎯 Keywords Relevantes Detectadas

**{keywords_text}**

---"""

        markdown_content += f"""

## 🎯 Perfil Profesional

{data['summary']}

---

## 💼 Experiencia Profesional

"""
        
        # Resto del contenido igual que generate_markdown
        # Agregar experiencia
        for exp in data['experience']:
            markdown_content += f"""### {exp['company']}
**{exp['position']}**  
*{exp['period']}*

"""
            for achievement in exp['achievements']:
                markdown_content += f"- {achievement}\n"
            markdown_content += "\n"
        
        # Agregar habilidades técnicas
        markdown_content += "## 🛠️ Competencias Técnicas\n\n"
        
        for category, skills in data['skills'].items():
            skills_text = " • ".join(skills)
            markdown_content += f"**{category}:** {skills_text}\n\n"
        
        # Agregar educación
        markdown_content += "## 🎓 Educación\n\n"
        for edu in data['education']:
            markdown_content += f"""### {edu['degree']}
**{edu['institution']}**  
*{edu['year']} | {edu['location']}*

"""
        
        # Agregar idiomas
        markdown_content += "## 🌍 Idiomas\n\n"
        for lang in data['languages']:
            markdown_content += f"- **{lang['name']}:** {lang['level']}\n"
        
        markdown_content += f"""

---

*CV generado automáticamente el {datetime.now().strftime('%d de %B de %Y')} | Personalizado para {company} - {position}*
"""
        
        return markdown_content
    
    def generate_cv(self, company, position, format="pdf", job_description=""):
        """Genera CV en Markdown y lo convierte a PDF usando pandoc"""
        
        print(f"🚀 Generando CV Simple (Markdown)")
        print(f"   Company: {company}")
        print(f"   Position: {position}")
        print(f"   Format: {format}")
        if job_description:
            print(f"   🎯 Personalizado con descripción de trabajo")
        print()
        
        # Crear directorio de salida
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_company = "".join(c if c.isalnum() else "_" for c in company.lower())
        output_name = f"cv_markdown_{safe_company}_{timestamp}"
        output_path = self.output_dir / output_name
        output_path.mkdir(exist_ok=True)
        
        try:
            # Generar contenido Markdown personalizado
            if job_description:
                markdown_content = self.generate_markdown_for_job(company, position, job_description)
            else:
                markdown_content = self.generate_markdown(company, position)
            
            # Guardar Markdown
            md_file = output_path / "cv.md"
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            
            print(f"✅ Markdown generado: {md_file}")
            
            # Convertir a PDF usando pandoc
            if format.lower() == "pdf":
                pdf_file = output_path / "cv.pdf"
                
                # Verificar si pandoc está disponible
                try:
                    subprocess.run(["pandoc", "--version"], 
                                 capture_output=True, check=True)
                except (subprocess.CalledProcessError, FileNotFoundError):
                    print("❌ Pandoc no está instalado. Instala con:")
                    print("   brew install pandoc  # en macOS")
                    print("   O descarga desde: https://pandoc.org/installing.html")
                    return output_path
                
                # Convertir a PDF
                pandoc_cmd = [
                    "pandoc",
                    str(md_file),
                    "-o", str(pdf_file),
                    "--pdf-engine=xelatex",
                    "--variable", "mainfont=Helvetica",
                    "--variable", "sansfont=Helvetica",
                    "--variable", "monofont=Monaco",
                    "--variable", "fontsize=11pt",
                    "--variable", "geometry:margin=2cm",
                    "--highlight-style=github"
                ]
                
                result = subprocess.run(pandoc_cmd, capture_output=True, text=True)
                
                if result.returncode == 0:
                    print(f"✅ PDF generado: {pdf_file}")
                    
                    # Abrir PDF en macOS
                    if os.path.exists(pdf_file):
                        subprocess.run(["open", str(pdf_file)])
                    
                else:
                    print(f"⚠️  Error convirtiendo a PDF: {result.stderr}")
                    print("💡 Puedes usar el archivo Markdown generado manualmente")
            
            # Generar HTML como alternativa
            html_file = output_path / "cv.html"
            try:
                html_cmd = [
                    "pandoc",
                    str(md_file),
                    "-o", str(html_file),
                    "--standalone",
                    "--css", "https://cdn.jsdelivr.net/npm/github-markdown-css@5/github-markdown-light.css",
                    "--highlight-style=github"
                ]
                
                result = subprocess.run(html_cmd, capture_output=True, text=True)
                
                if result.returncode == 0:
                    print(f"✅ HTML generado: {html_file}")
                else:
                    print(f"⚠️  No se pudo generar HTML: {result.stderr}")
                    
            except Exception as e:
                print(f"⚠️  Error generando HTML: {e}")
            
            return output_path
            
        except Exception as e:
            print(f"❌ Error generando CV: {e}")
            import traceback
            traceback.print_exc()
            return None
    
    def create_simple_template(self):
        """Crea un template simple para editar manualmente"""
        template_content = f"""# {self.personal_data['name']}

## {self.personal_data['title']}

**Email:** {self.personal_data['email']}  
**Teléfono:** {self.personal_data['phone']}  
**LinkedIn:** {self.personal_data['linkedin']}  

## Perfil Profesional

[Edita aquí tu resumen personalizado para la empresa objetivo]

## Experiencia Profesional

### Empresa Actual
**Tu Posición Actual** | *Fechas*
- Logro importante 1
- Logro importante 2
- Tecnologías utilizadas

### Empresa Anterior
**Posición Anterior** | *Fechas*
- Logro importante 1
- Logro importante 2

## Habilidades Técnicas

**Programming:** C++, Python, JavaScript  
**IoT:** MQTT, LoRa, STM32  
**Web:** React, Node.js  

## Educación

### Tu Título
**Tu Universidad** | *Año*

---

*Personaliza este template según la empresa y posición objetivo*
"""
        
        template_file = self.output_dir / "cv_template.md"
        with open(template_file, 'w', encoding='utf-8') as f:
            f.write(template_content)
        
        print(f"📝 Template simple creado: {template_file}")
        print("💡 Edita este archivo y usa: pandoc cv_template.md -o cv.pdf")
        
        return template_file

def main():
    parser = argparse.ArgumentParser(
        description="Generador de CV Simple (Markdown → PDF)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  python generate_cv_simple.py "Globant" "IoT Edge Engineer"
  python generate_cv_simple.py "Google" "Software Engineer" --format html
  python generate_cv_simple.py --template  # Crea template editable
  
  # CV personalizado para oferta específica:
  python generate_cv_simple.py "Empresa" "Puesto" --job-description "Descripción de la oferta"
  
Requisitos:
  brew install pandoc  # Para conversión a PDF
        """
    )
    
    parser.add_argument("company", nargs="?", help="Nombre de la empresa objetivo")
    parser.add_argument("position", nargs="?", help="Nombre de la posición")
    parser.add_argument("--format", "-f", choices=["pdf", "html"], default="pdf",
                       help="Formato de salida (pdf o html)")
    parser.add_argument("--template", "-t", action="store_true",
                       help="Crear template simple para editar manualmente")
    parser.add_argument("--job-description", "-j", type=str, default="",
                       help="Descripción de la oferta de trabajo para personalización específica")
    
    args = parser.parse_args()
    
    generator = MarkdownCVGenerator()
    
    if args.template:
        generator.create_simple_template()
        return
    
    if not args.company or not args.position:
        parser.print_help()
        return
    
    output_path = generator.generate_cv(args.company, args.position, args.format, args.job_description)
    
    if output_path:
        print(f"🎉 CV simple generado en: {output_path}")
        print()
        print("💡 Próximos pasos:")
        print("   1. Revisa el archivo Markdown generado")
        print("   2. Edita manualmente si necesitas ajustes")
        print("   3. Regenera con: pandoc cv.md -o cv_final.pdf")
        
        if args.job_description:
            print()
            print("🎯 Personalización aplicada:")
            print("   - Keywords de la oferta detectadas automáticamente")
            print("   - Skills relevantes destacadas")
            print("   - Resumen personalizado con términos clave")
    else:
        print("❌ Error generando CV")

if __name__ == "__main__":
    main()
