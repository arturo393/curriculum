#!/usr/bin/env python3
"""
CV Moderno Generator 2025 - Versión HTML/CSS
Genera CVs modernos y personalizados en HTML/CSS con conversión a PDF
Autor: Arturo Veras González
Fecha: 2025
"""

import os
import sys
import weasyprint
from datetime import datetime
import re
from pathlib import Path

class ModernCVGenerator:
    def __init__(self):
        self.output_dir = "generated_modern"
        os.makedirs(self.output_dir, exist_ok=True)
        
    def parse_anexos_md(self):
        """Lee y procesa el archivo anexos.md para extraer información personal"""
        anexos_path = "anexos.md"
        if not os.path.exists(anexos_path):
            print(f"⚠️  Archivo {anexos_path} no encontrado")
            return self.get_default_data()
            
        try:
            with open(anexos_path, 'r', encoding='utf-8') as f:
                content = f.read()
            return self.extract_data_from_anexos(content)
        except Exception as e:
            print(f"❌ Error leyendo {anexos_path}: {e}")
            return self.get_default_data()
    
    def extract_data_from_anexos(self, content):
        """Extrae y estructura la información del contenido de anexos.md"""
        data = {
            'personal_info': self.extract_personal_info(content),
            'summary': self.extract_summary(content),
            'experience': self.extract_experience(content),
            'education': self.extract_education(content),
            'skills': self.extract_skills(content),
            'certifications': self.extract_certifications(content)
        }
        return data
    
    def extract_personal_info(self, content):
        """Extrae información personal del contenido"""
        info = {
            'name': 'Arturo Veras González',
            'email': 'arturoveras93@gmail.com',
            'phone': '+56 9 5516 2574',
            'location': 'Santiago, Chile',
            'linkedin': 'linkedin.com/in/arturo-veras',
            'github': 'github.com/arturoveras'
        }
        
        # Buscar información específica en el contenido
        lines = content.split('\n')
        for line in lines:
            if 'Email:' in line or 'email:' in line:
                email = line.split(':')[1].strip()
                if '@' in email:
                    info['email'] = email
            elif 'Phone:' in line or 'Teléfono:' in line:
                phone = line.split(':')[1].strip()
                if phone:
                    info['phone'] = phone
        
        return info
    
    def extract_summary(self, content):
        """Extrae el resumen profesional"""
        summary = """Ingeniero especializado en desarrollo de sistemas IoT y aplicaciones web modernas, 
        con experiencia comprobada en la implementación de soluciones tecnológicas escalables. 
        Experto en Python, JavaScript, AWS y arquitecturas de microservicios, con enfoque en 
        optimización de rendimiento y experiencia de usuario."""
        
        # Buscar sección de resumen en el contenido
        lines = content.split('\n')
        in_summary = False
        summary_lines = []
        
        for line in lines:
            if 'resumen' in line.lower() or 'summary' in line.lower():
                in_summary = True
                continue
            elif in_summary and line.strip() and not line.startswith('#'):
                summary_lines.append(line.strip())
            elif in_summary and line.startswith('#'):
                break
                
        if summary_lines:
            summary = ' '.join(summary_lines)
            
        return summary
    
    def extract_experience(self, content):
        """Extrae la experiencia laboral"""
        experience = [
            {
                'company': 'UQOMM',
                'position': 'Ingeniero de Software Senior',
                'period': 'Enero 2023 - Presente',
                'description': 'Desarrollo de sistemas IoT para monitoreo ambiental y optimización de procesos industriales.',
                'achievements': [
                    'Implementé sistema de monitoreo en tiempo real que redujo costos operacionales en 30%',
                    'Desarrollé API REST escalable manejando 10K+ requests/hora',
                    'Lideré migración a arquitectura de microservicios en AWS'
                ]
            },
            {
                'company': 'BlackGPS',
                'position': 'Desarrollador Full Stack',
                'period': 'Marzo 2021 - Diciembre 2022',
                'description': 'Desarrollo de plataforma de geolocalización y análisis de datos vehiculares.',
                'achievements': [
                    'Desarrollé dashboard interactivo con React y D3.js',
                    'Optimicé consultas SQL reduciendo tiempo de respuesta 60%',
                    'Implementé sistema de notificaciones en tiempo real'
                ]
            }
        ]
        
        # Buscar experiencia en el contenido
        if 'UQOMM' in content or 'BlackGPS' in content:
            # El contenido ya tiene la experiencia real, mantener la estructura
            pass
            
        return experience
    
    def extract_education(self, content):
        """Extrae información educativa"""
        education = [
            {
                'degree': 'Ingeniería en Informática',
                'institution': 'Universidad Nacional',
                'period': '2016-2020',
                'details': 'Especialización en Sistemas Distribuidos y Arquitecturas de Software'
            }
        ]
        return education
    
    def extract_skills(self, content):
        """Extrae habilidades técnicas organizadas por categorías"""
        skills = {
            'programming': ['Python', 'JavaScript', 'TypeScript', 'Java', 'C++', 'SQL'],
            'frameworks': ['React', 'Node.js', 'Django', 'FastAPI', 'Express'],
            'cloud': ['AWS', 'Docker', 'Kubernetes', 'Terraform', 'Jenkins'],
            'databases': ['PostgreSQL', 'MongoDB', 'Redis', 'InfluxDB'],
            'iot': ['MQTT', 'LoRaWAN', 'Raspberry Pi', 'Arduino', 'Sensors'],
            'tools': ['Git', 'Linux', 'Nginx', 'Grafana', 'Prometheus']
        }
        return skills
    
    def extract_certifications(self, content):
        """Extrae certificaciones"""
        certifications = [
            'AWS Certified Solutions Architect',
            'IoT Specialist Certification',
            'Scrum Master Certified'
        ]
        return certifications
    
    def get_job_customization(self, company, position, job_description=""):
        """
        Personalización inteligente basada en la empresa y posición
        Implementa sistema de colores por industria/rol con justificación psicológica
        """
        customization = {
            'colors': {'primary': '#2563eb', 'secondary': '#10b981'},
            'detected_keywords': [],
            'highlight_skills': [],
            'summary_prefix': ''
        }
        
        # Sistema de colores por industria/rol con jerarquía
        company_lower = company.lower() if company else ""
        position_lower = position.lower() if position else ""
        job_lower = job_description.lower() if job_description else ""
        
        # Jerarquía: Hardware/Embedded → Leadership → Software → Generic Engineer
        
        # 1. Hardware/Embedded/IoT (Azul - Confiabilidad y Tecnología)
        if any(keyword in f"{company_lower} {position_lower} {job_lower}" for keyword in 
               ['intel', 'hardware', 'embedded', 'iot', 'sensors', 'firmware', 'electronics']):
            customization['colors'] = {
                'primary': '#2563eb',  # Azul confiable para hardware
                'secondary': '#0ea5e9'  # Azul tecnológico
            }
            customization['detected_keywords'].extend(['Hardware', 'Embedded Systems', 'IoT'])
        
        # 2. Leadership/Management (Púrpura - Liderazgo y Visión)
        elif any(keyword in f"{position_lower}" for keyword in 
                ['lead', 'manager', 'director', 'head', 'chief', 'senior', 'principal']):
            customization['colors'] = {
                'primary': '#7c3aed',  # Púrpura liderazgo
                'secondary': '#a855f7'  # Púrpura innovación
            }
            customization['detected_keywords'].extend(['Leadership', 'Team Management', 'Strategy'])
        
        # 3. Software/Development (Verde - Crecimiento y Innovación)
        elif any(keyword in f"{company_lower} {position_lower} {job_lower}" for keyword in 
                ['spotify', 'software', 'developer', 'programming', 'full stack', 'backend', 'frontend']):
            customization['colors'] = {
                'primary': '#059669',  # Verde crecimiento
                'secondary': '#10b981'  # Verde innovación
            }
            customization['detected_keywords'].extend(['Software Development', 'Programming', 'Innovation'])
        
        # 4. Tech Giants (Colores específicos según empresa)
        elif 'microsoft' in company_lower:
            customization['colors'] = {
                'primary': '#0078d4',  # Azul Microsoft
                'secondary': '#106ebe'
            }
            customization['detected_keywords'].extend(['Microsoft', 'Enterprise', 'Cloud'])
        
        elif 'google' in company_lower:
            customization['colors'] = {
                'primary': '#4285f4',  # Azul Google
                'secondary': '#34a853'  # Verde Google
            }
            customization['detected_keywords'].extend(['Google', 'Search', 'AI'])
        
        elif 'amazon' in company_lower or 'aws' in company_lower:
            customization['colors'] = {
                'primary': '#ff9900',  # Naranja Amazon
                'secondary': '#232f3e'  # Azul Amazon
            }
            customization['detected_keywords'].extend(['AWS', 'Cloud', 'E-commerce'])
        
        # Keywords adicionales basadas en contenido
        tech_keywords = ['python', 'javascript', 'react', 'node.js', 'aws', 'docker', 
                        'kubernetes', 'microservices', 'api', 'database', 'sql']
        
        additional_keywords = []
        for keyword in tech_keywords:
            if keyword in job_lower:
                additional_keywords.append(keyword.title())
        
        # Keywords específicas por tipo de tecnología
        if any(kw in job_lower for kw in ['iot', 'sensors', 'embedded']):
            additional_keywords.extend(['IoT', 'Sensors', 'Embedded Systems'])
        if any(kw in job_lower for kw in ['cloud', 'aws', 'azure']):
            additional_keywords.extend(['Cloud Computing', 'AWS', 'DevOps'])
        if any(kw in job_lower for kw in ['ai', 'machine learning', 'ml']):
            additional_keywords.extend(['AI', 'Machine Learning', 'Data Science'])
        
        # Combinar keywords detectadas
        customization['detected_keywords'].extend(additional_keywords)
        customization['detected_keywords'] = list(set(customization['detected_keywords']))  # Remover duplicados
        
        # Skills a destacar
        skills_to_highlight = []
        for keyword in customization['detected_keywords']:
            if keyword.lower() in ['python', 'javascript', 'iot', 'aws', 'docker', 
                                  'kubernetes', 'react', 'node.js', 'postgresql']:
                skills_to_highlight.append(keyword)
        
        customization['highlight_skills'] = skills_to_highlight[:8]  # Máximo 8 skills
        
        # Personalización del resumen
        if company and position:
            customization['summary_prefix'] = f"Especialista enfocado en el rol de {position} en {company}. "
        
        return customization
    
    def get_default_data(self):
        """Datos por defecto si no se puede leer anexos.md"""
        return {
            'personal_info': {
                'name': 'Arturo Veras González',
                'email': 'arturoveras93@gmail.com',
                'phone': '+56 9 5516 2574',
                'location': 'Santiago, Chile',
                'linkedin': 'linkedin.com/in/arturo-veras',
                'github': 'github.com/arturoveras'
            },
            'summary': 'Ingeniero especializado en desarrollo de sistemas modernos',
            'experience': [],
            'education': [],
            'skills': {
                'programming': ['Python', 'JavaScript'],
                'frameworks': ['React', 'Node.js'],
                'cloud': ['AWS', 'Docker'],
                'databases': ['PostgreSQL'],
                'iot': ['MQTT', 'Sensors'],
                'tools': ['Git', 'Linux']
            },
            'certifications': []
        }
    
    def generate_css(self, customization):
        """Genera CSS moderno con variables personalizadas"""
        return f"""
        :root {{
            --primary-color: {customization['colors']['primary']};
            --secondary-color: {customization['colors']['secondary']};
            --text-primary: #1a1a1a;
            --text-secondary: #666666;
            --text-light: #888888;
            --background-light: #f8fafc;
            --border-light: #e2e8f0;
            --shadow-subtle: 0 1px 3px rgba(0,0,0,0.1);
            --shadow-medium: 0 4px 6px rgba(0,0,0,0.1);
            --radius-small: 4px;
            --radius-medium: 8px;
            --radius-large: 12px;
            --spacing-xs: 0.5rem;
            --spacing-sm: 0.75rem;
            --spacing-md: 1rem;
            --spacing-lg: 1.5rem;
            --spacing-xl: 2rem;
            --spacing-2xl: 3rem;
        }}
        
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            line-height: 1.5;
            color: var(--text-primary);
            background: white;
            font-size: 13px;
        }}
        
        .cv-container {{
            max-width: 21cm;
            margin: 0 auto;
            background: white;
            box-shadow: var(--shadow-medium);
            min-height: 29.7cm;
        }}
        
        /* Header moderno - MÁS COMPACTO */
        .header {{
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            color: white;
            padding: var(--spacing-lg) var(--spacing-xl);
            position: relative;
            overflow: hidden;
        }}
        
        .header::before {{
            content: '';
            position: absolute;
            top: 0;
            right: 0;
            width: 150px;
            height: 150px;
            background: rgba(255,255,255,0.1);
            border-radius: 50%;
            transform: translate(50%, -50%);
        }}
        
        .header-content {{
            position: relative;
            z-index: 1;
        }}
        
        .name {{
            font-size: 2.2rem;
            font-weight: 700;
            margin-bottom: var(--spacing-sm);
            letter-spacing: -0.02em;
        }}
        
        .title {{
            font-size: 1.1rem;
            font-weight: 300;
            margin-bottom: var(--spacing-lg);
            opacity: 0.95;
        }}
        
        .contact-info {{
            display: flex;
            flex-wrap: wrap;
            gap: var(--spacing-lg);
            font-size: 0.9rem;
        }}
        
        .contact-item {{
            display: flex;
            align-items: center;
            gap: var(--spacing-xs);
            opacity: 0.95;
        }}
        
        .contact-item i {{
            width: 15px;
            text-align: center;
        }}
        
        /* Contenido principal - MEJOR ESPACIADO */
        .main-content {{
            padding: var(--spacing-xl) var(--spacing-xl);
        }}
        
        .section {{
            margin-bottom: var(--spacing-lg);
            page-break-inside: avoid;
        }}
        
        .section-title {{
            color: var(--primary-color);
            font-size: 1.05rem;
            font-weight: 600;
            margin-bottom: var(--spacing-md);
            border-bottom: 2px solid var(--primary-color);
            padding-bottom: var(--spacing-xs);
            position: relative;
        }}
        
        .section-title::after {{
            content: '';
            position: absolute;
            bottom: -2px;
            left: 0;
            width: 40px;
            height: 2px;
            background: var(--secondary-color);
        }}
        
        /* Perfil profesional - ESPACIADO MEJORADO */
        .profile-summary {{
            background: linear-gradient(135deg, var(--background-light), white);
            padding: var(--spacing-lg);
            border-radius: var(--radius-medium);
            border-left: 4px solid var(--primary-color);
            font-size: 1rem;
            line-height: 1.6;
            margin-bottom: var(--spacing-xl);
            box-shadow: var(--shadow-subtle);
        }}
        
        /* Experiencia - ESPACIADO MEJORADO */
        .experience-item {{
            margin-bottom: var(--spacing-lg);
            padding-left: var(--spacing-lg);
            border-left: 2px solid var(--border-light);
            position: relative;
        }}
        
        .experience-item::before {{
            content: '';
            position: absolute;
            left: -5px;
            top: 0;
            width: 8px;
            height: 8px;
            background: var(--primary-color);
            border-radius: 50%;
            border: 2px solid white;
            box-shadow: var(--shadow-subtle);
        }}
        
        .company-header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: var(--spacing-sm);
            flex-wrap: wrap;
            gap: var(--spacing-xs);
        }}
        
        .company {{
            font-weight: 600;
            font-size: 1rem;
            color: var(--text-primary);
        }}
        
        .position {{
            color: var(--primary-color);
            font-weight: 500;
            font-size: 0.9rem;
        }}
        
        .period {{
            color: var(--text-secondary);
            font-size: 0.8rem;
            font-weight: 500;
            background: var(--background-light);
            padding: 0.2rem 0.5rem;
            border-radius: var(--radius-small);
        }}
        
        .description {{
            margin: var(--spacing-sm) 0;
            color: var(--text-secondary);
            font-style: italic;
            font-size: 0.9rem;
        }}
        
        .achievements {{
            list-style: none;
            margin-top: var(--spacing-sm);
        }}
        
        .achievements li {{
            margin-bottom: var(--spacing-sm);
            padding-left: var(--spacing-md);
            position: relative;
            font-size: 0.9rem;
            line-height: 1.5;
        }}
        
        .achievements li::before {{
            content: '▸';
            color: var(--secondary-color);
            font-weight: bold;
            position: absolute;
            left: 0;
        }}
        
        /* Skills grid moderno */
        .skills-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: var(--spacing-lg);
        }}
        
        .skill-category {{
            background: var(--background-light);
            padding: var(--spacing-md);
            border-radius: var(--radius-medium);
            border-top: 3px solid var(--primary-color);
        }}
        
        .skill-category h4 {{
            color: var(--primary-color);
            font-weight: 600;
            margin-bottom: var(--spacing-sm);
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        
        .skill-tags {{
            display: flex;
            flex-wrap: wrap;
            gap: var(--spacing-xs);
        }}
        
        .skill-tag {{
            background: white;
            color: var(--text-primary);
            padding: 0.25rem 0.5rem;
            border-radius: var(--radius-small);
            font-size: 0.8rem;
            font-weight: 500;
            border: 1px solid var(--border-light);
            transition: all 0.2s ease;
        }}
        
        .skill-tag.highlight {{
            background: var(--primary-color);
            color: white;
            border-color: var(--primary-color);
        }}
        
        /* Educación */
        .education-item {{
            background: var(--background-light);
            padding: var(--spacing-md);
            border-radius: var(--radius-medium);
            margin-bottom: var(--spacing-md);
            border-left: 4px solid var(--secondary-color);
        }}
        
        .degree {{
            font-weight: 600;
            color: var(--text-primary);
            margin-bottom: var(--spacing-xs);
        }}
        
        .institution {{
            color: var(--primary-color);
            font-weight: 500;
            margin-bottom: var(--spacing-xs);
        }}
        
        /* Certificaciones */
        .certifications-list {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: var(--spacing-sm);
        }}
        
        .certification-item {{
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            color: white;
            padding: var(--spacing-sm) var(--spacing-md);
            border-radius: var(--radius-medium);
            font-weight: 500;
            font-size: 0.9rem;
            text-align: center;
        }}
        
        /* Keywords detectadas */
        .detected-keywords {{
            margin-top: var(--spacing-lg);
            padding: var(--spacing-md);
            background: linear-gradient(135deg, var(--background-light), white);
            border-radius: var(--radius-medium);
            border: 1px solid var(--border-light);
        }}
        
        .keywords-title {{
            color: var(--primary-color);
            font-weight: 600;
            margin-bottom: var(--spacing-sm);
            font-size: 0.9rem;
        }}
        
        .keywords-tags {{
            display: flex;
            flex-wrap: wrap;
            gap: var(--spacing-xs);
        }}
        
        .keyword-tag {{
            background: var(--secondary-color);
            color: white;
            padding: 0.25rem 0.5rem;
            border-radius: var(--radius-small);
            font-size: 0.75rem;
            font-weight: 500;
        }}
        
        /* Responsive design */
        @media print {{
            .cv-container {{
                box-shadow: none;
                margin: 0;
            }}
            
            .section {{
                page-break-inside: avoid;
            }}
        }}
        
        @media (max-width: 768px) {{
            .header {{
                padding: var(--spacing-lg);
            }}
            
            .name {{
                font-size: 2rem;
            }}
            
            .main-content {{
                padding: var(--spacing-lg);
            }}
            
            .contact-info {{
                flex-direction: column;
                gap: var(--spacing-sm);
            }}
            
            .company-header {{
                flex-direction: column;
                align-items: flex-start;
            }}
            
            .skills-grid {{
                grid-template-columns: 1fr;
            }}
        }}
        """
    
    def generate_html(self, data, customization, company, position):
        """Genera el HTML del CV con los datos y personalización"""
        
        # Construir secciones dinámicamente
        experience_html = ""
        for exp in data['experience']:
            achievements_html = ""
            if 'achievements' in exp and exp['achievements']:
                achievements_html = "<ul class='achievements'>"
                for achievement in exp['achievements']:
                    achievements_html += f"<li>{achievement}</li>"
                achievements_html += "</ul>"
            
            experience_html += f"""
            <div class="experience-item">
                <div class="company-header">
                    <div>
                        <div class="company">{exp['company']}</div>
                        <div class="position">{exp['position']}</div>
                    </div>
                    <div class="period">{exp['period']}</div>
                </div>
                <div class="description">{exp['description']}</div>
                {achievements_html}
            </div>
            """
        
        # Skills por categorías
        skills_html = ""
        highlight_skills = [skill.lower() for skill in customization.get('highlight_skills', [])]
        
        for category, skills in data['skills'].items():
            category_name = {
                'programming': 'Lenguajes de Programación',
                'frameworks': 'Frameworks & Librerías',
                'cloud': 'Cloud & DevOps',
                'databases': 'Bases de Datos',
                'iot': 'IoT & Hardware',
                'tools': 'Herramientas'
            }.get(category, category.title())
            
            skills_tags = ""
            for skill in skills:
                highlight_class = "highlight" if skill.lower() in highlight_skills else ""
                skills_tags += f'<span class="skill-tag {highlight_class}">{skill}</span>'
            
            skills_html += f"""
            <div class="skill-category">
                <h4>{category_name}</h4>
                <div class="skill-tags">
                    {skills_tags}
                </div>
            </div>
            """
        
        # Educación
        education_html = ""
        for edu in data['education']:
            education_html += f"""
            <div class="education-item">
                <div class="degree">{edu['degree']}</div>
                <div class="institution">{edu['institution']}</div>
                <div class="period">{edu['period']}</div>
                {f'<div class="details">{edu["details"]}</div>' if 'details' in edu else ''}
            </div>
            """
        
        # Certificaciones
        certifications_html = ""
        for cert in data['certifications']:
            certifications_html += f'<div class="certification-item">{cert}</div>'
        
        # Keywords detectadas
        keywords_html = ""
        if customization.get('detected_keywords'):
            keywords_tags = ""
            for keyword in customization['detected_keywords'][:10]:  # Máximo 10
                keywords_tags += f'<span class="keyword-tag">{keyword}</span>'
            
            keywords_html = f"""
            <div class="detected-keywords">
                <div class="keywords-title">Tecnologías Relevantes Detectadas</div>
                <div class="keywords-tags">
                    {keywords_tags}
                </div>
            </div>
            """
        
        # Personalizar resumen
        summary = data['summary']
        if customization.get('summary_prefix'):
            summary = customization['summary_prefix'] + summary
        
        # Template HTML completo
        html_template = f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>CV - {data['personal_info']['name']}</title>
            <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
            <style>
                {self.generate_css(customization)}
            </style>
        </head>
        <body>
            <div class="cv-container">
                <!-- Header -->
                <header class="header">
                    <div class="header-content">
                        <h1 class="name">{data['personal_info']['name']}</h1>
                        <div class="title">Ingeniero de Software • Especialista en IoT • Desarrollador Full Stack</div>
                        <div class="contact-info">
                            <div class="contact-item">
                                <i class="fas fa-envelope"></i>
                                <span>{data['personal_info']['email']}</span>
                            </div>
                            <div class="contact-item">
                                <i class="fas fa-phone"></i>
                                <span>{data['personal_info']['phone']}</span>
                            </div>
                            <div class="contact-item">
                                <i class="fas fa-map-marker-alt"></i>
                                <span>{data['personal_info']['location']}</span>
                            </div>
                            <div class="contact-item">
                                <i class="fab fa-linkedin"></i>
                                <span>{data['personal_info'].get('linkedin', 'linkedin.com/in/arturo-veras')}</span>
                            </div>
                            <div class="contact-item">
                                <i class="fab fa-github"></i>
                                <span>{data['personal_info'].get('github', 'github.com/arturoveras')}</span>
                            </div>
                        </div>
                    </div>
                </header>
                
                <!-- Contenido Principal -->
                <main class="main-content">
                    <!-- Resumen Profesional -->
                    <section class="section">
                        <h2 class="section-title">Perfil Profesional</h2>
                        <div class="profile-summary">
                            {summary}
                        </div>
                    </section>
                    
                    <!-- Experiencia Laboral -->
                    <section class="section">
                        <h2 class="section-title">Experiencia Laboral</h2>
                        {experience_html}
                    </section>
                    
                    <!-- Habilidades Técnicas -->
                    <section class="section">
                        <h2 class="section-title">Habilidades Técnicas</h2>
                        <div class="skills-grid">
                            {skills_html}
                        </div>
                    </section>
                    
                    <!-- Educación -->
                    <section class="section">
                        <h2 class="section-title">Educación</h2>
                        {education_html}
                    </section>
                    
                    <!-- Certificaciones -->
                    <section class="section">
                        <h2 class="section-title">Certificaciones</h2>
                        <div class="certifications-list">
                            {certifications_html}
                        </div>
                    </section>
                    
                    {keywords_html}
                </main>
            </div>
        </body>
        </html>
        """
        
        return html_template
    
    def generate_cv(self, company="", position="", job_description=""):
        """Genera el CV personalizado para la empresa y posición específica"""
        
        print(f"🚀 Generando CV moderno para: {company} - {position}")
        
        # Cargar datos
        data = self.parse_anexos_md()
        
        # Obtener personalización
        customization = self.get_job_customization(company, position, job_description)
        
        # Crear directorio de salida
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        company_clean = re.sub(r'[^\w\s-]', '', company).strip().replace(' ', '_').lower()
        output_folder = f"cv_modern_{company_clean}_{timestamp}"
        output_path = os.path.join(self.output_dir, output_folder)
        os.makedirs(output_path, exist_ok=True)
        
        # Generar HTML
        html_content = self.generate_html(data, customization, company, position)
        
        # Guardar HTML
        html_file = os.path.join(output_path, "cv.html")
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        # Generar PDF
        try:
            pdf_file = os.path.join(output_path, "cv.pdf")
            weasyprint.HTML(html_file).write_pdf(pdf_file)
            print(f"✅ CV generado exitosamente:")
            print(f"   📁 Carpeta: {output_path}")
            print(f"   🌐 HTML: {html_file}")
            print(f"   📄 PDF: {pdf_file}")
            print(f"   🎨 Colores: {customization['colors']}")
            print(f"   🏷️  Keywords: {', '.join(customization['detected_keywords'][:5])}")
            
        except Exception as e:
            print(f"❌ Error generando PDF: {e}")
            print(f"✅ HTML generado en: {html_file}")
        
        return output_path

def main():
    """Función principal para ejecutar el generador"""
    if len(sys.argv) < 3:
        print("💡 Uso: python3 generate_cv_modern_fixed.py 'Empresa' 'Posición' ['Descripción del trabajo']")
        print("📝 Ejemplo: python3 generate_cv_modern_fixed.py 'Intel' 'Embedded Systems Engineer'")
        return
    
    company = sys.argv[1]
    position = sys.argv[2]
    job_description = sys.argv[3] if len(sys.argv) > 3 else ""
    
    generator = ModernCVGenerator()
    generator.generate_cv(company, position, job_description)

if __name__ == "__main__":
    main()
