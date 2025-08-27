#!/usr/bin/env python3
"""
Generador de CV Moderno - Arturo Veras
Alternativa moderna a LaTeX usando HTML+CSS → PDF
"""

import os
import json
import argparse
from datetime import datetime
from pathlib import Path
import weasyprint
from jinja2 import Template
import yaml

class ModernCVGenerator:
    def __init__(self):
        self.script_dir = Path(__file__).parent
        self.templates_dir = self.script_dir / "templates_modern"
        self.output_dir = self.script_dir / "generated_modern"
        self.data_file = self.script_dir / "anexos.md"
        
        # Crear directorios
        self.templates_dir.mkdir(exist_ok=True)
        self.output_dir.mkdir(exist_ok=True)
        
        # Cargar datos personales
        self.personal_data = self.load_personal_data()
        
    def load_personal_data(self):
        """Carga datos personales desde anexos.md"""
        if not self.data_file.exists():
            return self.get_default_data()
            
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                content = f.read()
                return self.parse_anexos_md(content)
        except Exception as e:
            print(f"⚠️  Error cargando datos: {e}")
            return self.get_default_data()
    
    def parse_anexos_md(self, content):
        """Parsea anexos.md y extrae información estructurada"""
        data = {
            "name": "Arturo Veras González",
            "title": "Ingeniero Civil Electrónico",
            "email": "arturoveras93@gmail.com",
            "phone": "+56 9 5516 2574",
            "location": "Santiago, Chile",
            "linkedin": "linkedin.com/in/arturo-veras",
            "github": "github.com/arturo393",
            "experience": [],
            "education": [],
            "skills": {},
            "languages": [],
            "summary": ""
        }
        
        # Extraer experiencia
        if "## 💼 EXPERIENCIA PROFESIONAL" in content:
            exp_section = content.split("## 💼 EXPERIENCIA PROFESIONAL")[1]
            if "##" in exp_section:
                exp_section = exp_section.split("##")[0]
            
            # Parsear cada experiencia
            experiences = []
            for line in exp_section.split('\n'):
                if line.strip().startswith('###'):
                    company = line.replace('###', '').strip()
                    experiences.append({"company": company, "positions": []})
                elif line.strip().startswith('**') and 'Cargo:' in line:
                    if experiences:
                        position = line.split('**Cargo:**')[1].strip()
                        experiences[-1]["positions"].append({"title": position})
            
            data["experience"] = experiences
        
        # Extraer habilidades técnicas
        if "## 🛠️ COMPETENCIAS TÉCNICAS" in content:
            skills_section = content.split("## 🛠️ COMPETENCIAS TÉCNICAS")[1]
            if "##" in skills_section:
                skills_section = skills_section.split("##")[0]
            
            current_category = ""
            for line in skills_section.split('\n'):
                if line.strip().startswith('###'):
                    current_category = line.replace('###', '').strip()
                    data["skills"][current_category] = []
                elif line.strip().startswith('-') and current_category:
                    skill = line.replace('-', '').strip()
                    if skill:
                        data["skills"][current_category].append(skill)
        
        return data
    
    def get_default_data(self):
        """Datos por defecto en caso de error"""
        return {
            "name": "Arturo Veras González",
            "title": "Ingeniero Civil Electrónico",
            "email": "arturoveras93@gmail.com",
            "phone": "+56 9 5516 2574",
            "location": "Santiago, Chile",
            "linkedin": "linkedin.com/in/arturo-veras",
            "github": "github.com/arturo393",
            "experience": [
                {
                    "company": "UQOMM",
                    "positions": [{"title": "Ingeniero de Software IoT Sr."}]
                }
            ],
            "education": [
                {
                    "degree": "Ingeniería Civil Electrónica",
                    "institution": "Universidad Técnica Federico Santa María",
                    "year": "2017"
                }
            ],
            "skills": {
                "Embedded Systems": ["STM32", "ARM Cortex", "FreeRTOS"],
                "Programming": ["C/C++", "Python", "JavaScript"],
                "IoT": ["MQTT", "LoRa", "Edge Computing"]
            },
            "languages": [
                {"name": "Español", "level": "Nativo"},
                {"name": "Inglés", "level": "Avanzado"}
            ],
            "summary": "Ingeniero Civil Electrónico con 9+ años desarrollando soluciones IoT innovadoras."
        }
    
    def get_job_customization(self, company, position):
        """Personalización específica por empresa/rol"""
        company_lower = company.lower()
        position_lower = position.lower()
        
        customizations = {
            "globant": {
                "colors": {"primary": "#00D4AA", "secondary": "#1F2937"},
                "keywords": ["digital transformation", "iot edge", "embedded systems", "agile"],
                "summary_suffix": " Especializado en transformación digital empresarial con tecnologías IoT Edge.",
                "highlight_skills": ["STM32", "FreeRTOS", "C++", "Python", "Agile", "Linux"]
            },
            "google": {
                "colors": {"primary": "#4285F4", "secondary": "#34A853"},
                "keywords": ["scalability", "distributed systems", "cloud", "innovation"],
                "summary_suffix": " Enfocado en sistemas escalables y tecnologías cloud-native.",
                "highlight_skills": ["Python", "Distributed Systems", "Cloud", "Machine Learning"]
            },
            "microsoft": {
                "colors": {"primary": "#0078D4", "secondary": "#107C10"},
                "keywords": ["azure", "enterprise", "productivity", "ai"],
                "summary_suffix": " Especializado en soluciones enterprise y plataformas Azure.",
                "highlight_skills": ["Azure", "C#", "Enterprise", "AI"]
            }
        }
        
        # Personalización por tipo de rol
        role_customizations = {
            "iot": {
                "highlight_skills": ["IoT", "Edge Computing", "MQTT", "LoRa", "Embedded Systems"],
                "summary_prefix": "Especialista IoT con "
            },
            "firmware": {
                "highlight_skills": ["C/C++", "STM32", "FreeRTOS", "Embedded Systems", "Hardware"],
                "summary_prefix": "Desarrollador Firmware con "
            },
            "software": {
                "highlight_skills": ["Python", "JavaScript", "React", "MongoDB", "APIs"],
                "summary_prefix": "Desarrollador Software con "
            }
        }
        
        # Combinar personalizaciones
        customization = customizations.get(company_lower, {
            "colors": {"primary": "#2563EB", "secondary": "#1F2937"},
            "keywords": ["technology", "innovation"],
            "summary_suffix": "",
            "highlight_skills": []
        })
        
        # Agregar personalización por rol
        for role_key, role_config in role_customizations.items():
            if role_key in position_lower:
                customization.update(role_config)
                break
        
        return customization
    
    def create_html_template(self):
        """Crea template HTML moderno siguiendo mejores prácticas 2025"""
        html_template = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ data.name }} - CV</title>
    <style>
        /* Mejores prácticas CV 2025 */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        @page {
            size: A4;
            margin: 1.5cm;
        }
        
        :root {
            /* Variables CSS modernas */
            --primary-color: {{ customization.colors.primary }};
            --secondary-color: {{ customization.colors.secondary }};
            --text-primary: #1a1a1a;
            --text-secondary: #666;
            --text-light: #888;
            --background-light: #f8f9fa;
            --border-light: #e1e5e9;
            --shadow-subtle: 0 2px 4px rgba(0,0,0,0.08);
            --shadow-medium: 0 4px 12px rgba(0,0,0,0.12);
            --radius-small: 6px;
            --radius-medium: 8px;
            --spacing-xs: 0.5rem;
            --spacing-sm: 0.75rem;
            --spacing-md: 1rem;
            --spacing-lg: 1.5rem;
            --spacing-xl: 2rem;
        }
        
        body {
            font-family: 'Inter', 'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.5;
            color: var(--text-primary);
            font-size: 10.5pt;
            background: white;
        }
        
        .container {
            max-width: 21cm;
            margin: 0 auto;
            background: white;
        }
        
        /* Header moderno con gradiente sutil */
        .header {
            background: linear-gradient(135deg, var(--primary-color), {{ customization.colors.secondary }});
            color: white;
            padding: var(--spacing-xl);
            position: relative;
            overflow: hidden;
        }
        
        .header::before {
            content: '';
            position: absolute;
            top: 0;
            right: 0;
            width: 200px;
            height: 200px;
            background: rgba(255,255,255,0.1);
            border-radius: 50%;
            transform: translate(50px, -100px);
        }
        
        .header-content {
            position: relative;
            z-index: 2;
        }
        
        .header h1 {
            font-size: 2.2rem;
            font-weight: 600;
            margin-bottom: var(--spacing-xs);
            letter-spacing: -0.02em;
        }
        
        .header h2 {
            font-size: 1.2rem;
            opacity: 0.95;
            font-weight: 400;
            margin-bottom: var(--spacing-lg);
            letter-spacing: 0.01em;
        }
        
        .contact-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: var(--spacing-sm);
            font-size: 0.9rem;
        }
        
        .contact-item {
            display: flex;
            align-items: center;
            gap: var(--spacing-xs);
            opacity: 0.95;
        }
        
        .contact-icon {
            width: 16px;
            height: 16px;
            opacity: 0.8;
        }
        
        /* Layout moderno con CSS Grid */
        .main-grid {
            display: grid;
            grid-template-columns: 1fr 300px;
            gap: var(--spacing-xl);
            padding: var(--spacing-xl);
        }
        
        .main-content {
            min-width: 0; /* Previene overflow */
        }
        
        .sidebar {
            background: var(--background-light);
            padding: var(--spacing-lg);
            border-radius: var(--radius-medium);
            height: fit-content;
            position: sticky;
            top: var(--spacing-lg);
        }
        
        /* Secciones optimizadas */
        .section {
            margin-bottom: var(--spacing-xl);
            page-break-inside: avoid;
        }
        
        .section-title {
            color: var(--primary-color);
            font-size: 1.1rem;
            font-weight: 600;
            margin-bottom: var(--spacing-md);
            border-bottom: 2px solid var(--primary-color);
            padding-bottom: var(--spacing-xs);
            position: relative;
        }
        
        .section-title::after {
            content: '';
            position: absolute;
            bottom: -2px;
            left: 0;
            width: 40px;
            height: 2px;
            background: var(--secondary-color);
        }
        
        /* Perfil profesional destacado */
        .profile-summary {
            background: linear-gradient(135deg, var(--background-light), white);
            padding: var(--spacing-lg);
            border-radius: var(--radius-medium);
            border-left: 4px solid var(--primary-color);
            font-size: 1.05rem;
            line-height: 1.6;
            margin-bottom: var(--spacing-xl);
            box-shadow: var(--shadow-subtle);
        }
        
        /* Experiencia con timeline moderna */
        .experience-item {
            margin-bottom: var(--spacing-lg);
            padding-left: var(--spacing-lg);
            border-left: 2px solid var(--border-light);
            position: relative;
        }
        
        .experience-item::before {
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
        }
        
        .company-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: var(--spacing-xs);
            flex-wrap: wrap;
            gap: var(--spacing-xs);
        }
        
        .company {
            font-weight: 600;
            font-size: 1.05rem;
            color: var(--text-primary);
        }
        
        .period {
            color: var(--text-secondary);
            font-size: 0.85rem;
            font-weight: 500;
            background: var(--background-light);
            padding: 0.2rem 0.5rem;
            border-radius: var(--radius-small);
        }
        
        .position {
            font-weight: 500;
            color: var(--primary-color);
            margin-bottom: var(--spacing-xs);
        }
        
        .achievements {
            list-style: none;
            margin-left: 0;
        }
        
        .achievements li {
            margin-bottom: var(--spacing-xs);
            padding-left: var(--spacing-md);
            position: relative;
            line-height: 1.5;
        }
        
        .achievements li::before {
            content: '▸';
            position: absolute;
            left: 0;
            color: var(--primary-color);
            font-weight: bold;
        }
        
        /* Skills modernas con categorías visuales */
        .skills-grid {
            display: grid;
            gap: var(--spacing-md);
        }
        
        .skill-category {
            background: white;
            border: 1px solid var(--border-light);
            border-radius: var(--radius-medium);
            padding: var(--spacing-md);
            transition: all 0.2s ease;
        }
        
        .skill-category:hover {
            box-shadow: var(--shadow-medium);
            transform: translateY(-1px);
        }
        
        .skill-category h4 {
            color: var(--secondary-color);
            margin-bottom: var(--spacing-sm);
            font-size: 0.9rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }
        
        .skills-list {
            display: flex;
            flex-wrap: wrap;
            gap: var(--spacing-xs);
        }
        
        .skill-tag {
            background: var(--primary-color);
            color: white;
            padding: 0.25rem 0.6rem;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 500;
            transition: all 0.2s ease;
        }
        
        .skill-tag.highlight {
            background: var(--secondary-color);
            font-weight: 600;
            box-shadow: var(--shadow-subtle);
        }
        
        .skill-tag:hover {
            transform: scale(1.05);
        }
        
        /* Educación elegante */
        .education-item {
            background: white;
            border: 1px solid var(--border-light);
            border-radius: var(--radius-medium);
            padding: var(--spacing-md);
            margin-bottom: var(--spacing-sm);
        }
        
        .degree {
            font-weight: 600;
            color: var(--text-primary);
            margin-bottom: 0.2rem;
        }
        
        .institution {
            color: var(--primary-color);
            font-weight: 500;
            margin-bottom: 0.2rem;
        }
        
        .edu-details {
            color: var(--text-secondary);
            font-size: 0.85rem;
        }
        
        /* Idiomas con niveles visuales */
        .languages-grid {
            display: grid;
            gap: var(--spacing-sm);
        }
        
        .language-item {
            background: white;
            border: 1px solid var(--border-light);
            border-radius: var(--radius-medium);
            padding: var(--spacing-sm);
            text-align: center;
        }
        
        .language-name {
            font-weight: 600;
            color: var(--text-primary);
            margin-bottom: 0.2rem;
        }
        
        .language-level {
            font-size: 0.8rem;
            color: var(--text-secondary);
            background: var(--background-light);
            padding: 0.2rem 0.5rem;
            border-radius: var(--radius-small);
        }
        
        /* Keywords destacadas - tendencia 2025 */
        .keywords-section {
            background: linear-gradient(45deg, var(--primary-color), var(--secondary-color));
            color: white;
            padding: var(--spacing-md);
            border-radius: var(--radius-medium);
            margin-bottom: var(--spacing-lg);
            text-align: center;
        }
        
        .keywords-title {
            font-size: 0.8rem;
            opacity: 0.9;
            margin-bottom: var(--spacing-xs);
            text-transform: uppercase;
            letter-spacing: 0.1em;
        }
        
        .keywords-list {
            font-weight: 600;
            font-size: 0.9rem;
            letter-spacing: 0.05em;
        }
        
        /* Footer moderno */
        .footer {
            text-align: center;
            margin-top: var(--spacing-xl);
            padding-top: var(--spacing-md);
            border-top: 1px solid var(--border-light);
            color: var(--text-light);
            font-size: 0.75rem;
        }
        
        /* Responsive para impresión */
        @media print {
            .container { 
                max-width: none; 
                box-shadow: none;
            }
            
            .main-grid {
                grid-template-columns: 1fr 280px;
                gap: var(--spacing-md);
                padding: var(--spacing-md);
            }
            
            .section { 
                page-break-inside: avoid; 
            }
            
            .experience-item {
                page-break-inside: avoid;
            }
            
            .skill-category:hover,
            .skill-tag:hover {
                transform: none;
                box-shadow: none;
            }
        }
        
        /* Animaciones sutiles para web */
        @media screen {
            .section {
                animation: fadeInUp 0.6s ease-out;
            }
            
            @keyframes fadeInUp {
                from {
                    opacity: 0;
                    transform: translateY(20px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Header -->
        <div class="header">
            <div class="header-content">
                <h1>{{ data.name }}</h1>
                <h2>{{ data.title }}</h2>
                <div class="contact-grid">
                    <div class="contact-item">
                        <span class="contact-icon">📧</span>
                        {{ data.email }}
                    </div>
                    <div class="contact-item">
                        <span class="contact-icon">📱</span>
                        {{ data.phone }}
                    </div>
                    <div class="contact-item">
                        <span class="contact-icon">📍</span>
                        {{ data.location }}
                    </div>
                    {% if data.linkedin %}
                    <div class="contact-item">
                        <span class="contact-icon">💼</span>
                        {{ data.linkedin }}
                    </div>
                    {% endif %}
                    {% if data.github %}
                    <div class="contact-item">
                        <span class="contact-icon">💻</span>
                        {{ data.github }}
                    </div>
                    {% endif %}
                </div>
            </div>
        </div>
        
        <!-- Keywords Section - Tendencia 2025 -->
        {% if customization.get('detected_keywords') %}
        <div class="keywords-section">
            <div class="keywords-title">Competencias Clave Detectadas</div>
            <div class="keywords-list">{{ customization.detected_keywords | join(' • ') }}</div>
        </div>
        {% endif %}
        
        <!-- Perfil Profesional -->
        {% if data.summary %}
        <div class="profile-summary">
            {{ customization.get('summary_prefix', '') }}{{ data.summary }}{{ customization.get('summary_suffix', '') }}
        </div>
        {% endif %}
        
        <div class="main-grid">
            <div class="main-content">
                <!-- Experiencia -->
                {% if data.experience %}
                <div class="section">
                    <h3 class="section-title">Experiencia Profesional</h3>
                    {% for exp in data.experience %}
                    <div class="experience-item">
                        <div class="company-header">
                            <div class="company">{{ exp.company }}</div>
                            <div class="period">{{ exp.period }}</div>
                        </div>
                        <div class="position">{{ exp.position }}</div>
                        {% if exp.achievements %}
                        <ul class="achievements">
                            {% for achievement in exp.achievements %}
                            <li>{{ achievement }}</li>
                            {% endfor %}
                        </ul>
                        {% endif %}
                    </div>
                    {% endfor %}
                </div>
                {% endif %}
                
                <!-- Educación -->
                {% if data.education %}
                <div class="section">
                    <h3 class="section-title">Educación</h3>
                    {% for edu in data.education %}
                    <div class="education-item">
                        <div class="degree">{{ edu.degree }}</div>
                        <div class="institution">{{ edu.institution }}</div>
                        <div class="edu-details">{{ edu.year }} | {{ edu.location }}</div>
                    </div>
                    {% endfor %}
                </div>
                {% endif %}
            </div>
            
            <div class="sidebar">
                <!-- Skills -->
                {% if data.skills %}
                <div class="section">
                    <h3 class="section-title">Competencias</h3>
                    <div class="skills-grid">
                        {% for category, skills in data.skills.items() %}
                        <div class="skill-category">
                            <h4>{{ category }}</h4>
                            <div class="skills-list">
                                {% for skill in skills %}
                                <span class="skill-tag {% if skill in customization.get('highlight_skills', []) %}highlight{% endif %}">
                                    {{ skill }}
                                </span>
                                {% endfor %}
                            </div>
                        </div>
                        {% endfor %}
                    </div>
                </div>
                {% endif %}
                
                <!-- Idiomas -->
                {% if data.languages %}
                <div class="section">
                    <h3 class="section-title">Idiomas</h3>
                    <div class="languages-grid">
                        {% for lang in data.languages %}
                        <div class="language-item">
                            <div class="language-name">{{ lang.name }}</div>
                            <div class="language-level">{{ lang.level }}</div>
                        </div>
                        {% endfor %}
                    </div>
                </div>
                {% endif %}
            </div>
        </div>
        
        <!-- Footer -->
        <div class="footer">
            Generado automáticamente el {{ generation_date }} | Personalizado para {{ company }} - {{ position }}
        </div>
    </div>
</body>
</html>
        """
        
        template_file = self.templates_dir / "cv_modern_2025.html"
        with open(template_file, 'w', encoding='utf-8') as f:
            f.write(html_template.strip())
        
        return template_file
    
    def customize_for_job_offer(self, job_description, position="", company=""):
        """Personaliza el CV según oferta de trabajo - Mejores prácticas 2025"""
        customization = {
            'colors': {
                'primary': '#2563eb',    # Azul profesional
                'secondary': '#059669'   # Verde éxito
            },
            'highlight_skills': [],
            'summary_prefix': '',
            'summary_suffix': '',
            'detected_keywords': [],
            'company': company,
            'position': position,
            'generation_date': datetime.now().strftime("%d/%m/%Y")
        }
        
        if not job_description:
            return customization
            
        # Palabras clave IoT y tecnológicas modernas 2025
        iot_keywords = [
            'iot', 'internet of things', 'sensors', 'sensores', 'edge computing',
            'embedded systems', 'sistemas embebidos', 'microcontroladores',
            'arduino', 'raspberry pi', 'esp32', 'mqtt', 'zigbee', 'bluetooth',
            'wifi', 'lora', 'lorawan', 'nb-iot', '5g', 'edge ai', 'tinyml',
            'industrial iot', 'iiot', 'smart city', 'smart agriculture',
            'monitoring', 'monitoreo', 'data collection', 'telemetry',
            'remote sensing', 'predictive maintenance', 'digital twin',
            'time series', 'real-time', 'cloud connectivity', 'aws iot',
            'azure iot', 'google cloud iot', 'firmware', 'rtos',
            'micropython', 'c++', 'python', 'javascript', 'node.js',
            'interfaces', 'api', 'protocols', 'protocolos', 'modbus',
            'can bus', 'spi', 'i2c', 'uart', 'tcp/ip', 'http', 'https',
            'restful', 'websockets', 'machine learning', 'ai', 'analytics',
            'dashboard', 'visualization', 'grafana', 'influxdb', 'elasticsearch',
            'kubernetes', 'docker', 'devops', 'ci/cd', 'agile', 'scrum',
            'security', 'cybersecurity', 'encryption', 'certificates',
            'digital transformation', 'industry 4.0', 'smart manufacturing'
        ]
        
        tech_keywords = [
            'python', 'javascript', 'typescript', 'react', 'node.js', 'express',
            'django', 'flask', 'fastapi', 'postgresql', 'mongodb', 'mysql',
            'redis', 'elasticsearch', 'docker', 'kubernetes', 'aws', 'azure',
            'gcp', 'terraform', 'ansible', 'jenkins', 'gitlab ci', 'github actions',
            'microservices', 'apis', 'graphql', 'grpc', 'machine learning',
            'tensorflow', 'pytorch', 'scikit-learn', 'pandas', 'numpy',
            'data science', 'analytics', 'big data', 'spark', 'kafka',
            'linux', 'bash', 'git', 'agile', 'scrum', 'devops', 'sre',
            'monitoring', 'prometheus', 'grafana', 'elk stack', 'observability'
        ]
        
        # Combinar todas las keywords
        all_keywords = iot_keywords + tech_keywords
        
        # Detectar keywords en la descripción del trabajo
        job_lower = job_description.lower()
        detected = []
        
        for keyword in all_keywords:
            if keyword in job_lower:
                detected.append(keyword.title())
                
        # Personalización basada en palabras clave detectadas
        customization['detected_keywords'] = list(set(detected))[:15]  # Máximo 15 keywords
        
        # Colores específicos por industria/tecnología
        if any(word in job_lower for word in ['iot', 'sensors', 'embedded', 'hardware']):
            customization['colors'] = {
                'primary': '#0ea5e9',    # Azul tecnológico
                'secondary': '#10b981'   # Verde IoT
            }
        elif any(word in job_lower for word in ['ai', 'machine learning', 'data science']):
            customization['colors'] = {
                'primary': '#8b5cf6',    # Púrpura AI
                'secondary': '#f59e0b'   # Naranja innovación
            }
        elif any(word in job_lower for word in ['cloud', 'aws', 'azure', 'devops']):
            customization['colors'] = {
                'primary': '#1e40af',    # Azul cloud
                'secondary': '#dc2626'   # Rojo infraestructura
            }
        elif any(word in job_lower for word in ['startup', 'innovation', 'digital transformation']):
            customization['colors'] = {
                'primary': '#7c3aed',    # Púrpura innovación
                'secondary': '#059669'   # Verde crecimiento
            }
        
        # Skills a destacar basadas en la oferta
        skills_to_highlight = []
        for keyword in detected:
            if keyword.lower() in ['python', 'javascript', 'iot', 'aws', 'docker', 
                                  'kubernetes', 'react', 'node.js', 'postgresql', 
                                  'machine learning', 'tensorflow', 'apis', 'microservices']:
                skills_to_highlight.append(keyword)
                
        customization['highlight_skills'] = skills_to_highlight
        
        # Personalización del resumen profesional
        if company and position:
            if 'iot' in job_lower or 'sensores' in job_lower:
                customization['summary_prefix'] = f"Especialista en IoT y sistemas embebidos con experiencia específica para el rol de {position} en {company}. "
            elif 'lead' in position.lower() or 'senior' in position.lower():
                customization['summary_prefix'] = f"Ingeniero Senior especializado en liderazgo técnico, ideal para el puesto de {position} en {company}. "
            elif 'data' in job_lower or 'analytics' in job_lower:
                customization['summary_prefix'] = f"Especialista en ciencia de datos y análisis, perfectamente alineado con el rol de {position} en {company}. "
            else:
                customization['summary_prefix'] = f"Profesional versátil en tecnología con enfoque específico para {position} en {company}. "
                
        return customization
    
    def generate_cv(self, company, position, template_type="professional"):
        """Genera CV moderno en HTML y PDF"""
        
        print(f"🚀 Generando CV Moderno")
        print(f"   Company: {company}")
        print(f"   Position: {position}")
        print(f"   Template: {template_type}")
        print()
        
        # Crear directorio de salida
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_company = "".join(c if c.isalnum() else "_" for c in company.lower())
        output_name = f"cv_modern_{safe_company}_{timestamp}"
        output_path = self.output_dir / output_name
        output_path.mkdir(exist_ok=True)
        
        try:
            # Crear template HTML
            template_file = self.create_html_template()
            
            # Cargar template
            with open(template_file, 'r', encoding='utf-8') as f:
                template_content = f.read()
            
            template = Template(template_content)
            
            # Obtener personalización avanzada 2025
            customization = self.customize_for_job_offer("", position, company)
            
            # Renderizar HTML
            html_content = template.render(
                data=self.personal_data,
                customization=customization,
                company=company,
                position=position,
                generation_date=datetime.now().strftime("%d de %B de %Y")
            )
            
            # Guardar HTML
            html_file = output_path / "cv.html"
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            # Generar PDF
            pdf_file = output_path / "cv.pdf"
            weasyprint.HTML(filename=str(html_file)).write_pdf(str(pdf_file))
            
            print(f"✅ CV generado exitosamente:")
            print(f"   📄 HTML: {html_file}")
            print(f"   📑 PDF: {pdf_file}")
            
            # Abrir PDF en macOS
            if os.path.exists(pdf_file):
                import subprocess
                subprocess.run(["open", str(pdf_file)])
            
            return output_path
            
        except Exception as e:
            print(f"❌ Error generando CV: {e}")
            import traceback
            traceback.print_exc()
            return None

def main():
    parser = argparse.ArgumentParser(
        description="Generador de CV Moderno (HTML+CSS → PDF)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  python generate_cv_modern.py "Globant" "IoT Edge Engineer"
  python generate_cv_modern.py "Google" "Senior Software Engineer"
  python generate_cv_modern.py "Microsoft" "Technical Lead"
        """
    )
    
    parser.add_argument("company", help="Nombre de la empresa objetivo")
    parser.add_argument("position", help="Nombre de la posición")
    parser.add_argument("--template", "-t", default="professional", 
                       help="Tipo de template (professional, creative, minimal)")
    
    args = parser.parse_args()
    
    # Verificar dependencias
    try:
        import weasyprint
        import jinja2
    except ImportError as e:
        print("❌ Dependencias faltantes. Instala con:")
        print("   pip install weasyprint jinja2")
        return
    
    generator = ModernCVGenerator()
    
    output_path = generator.generate_cv(args.company, args.position, args.template)
    
    if output_path:
        print(f"🎉 CV moderno generado en: {output_path}")
    else:
        print("❌ Error generando CV")

if __name__ == "__main__":
    main()
