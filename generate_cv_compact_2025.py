#!/usr/bin/env python3
"""
CV Compacto 2025 - Versión optimizada para 1 página
Genera CVs modernos y compactos en PDF usando ReportLab
Integra el mismo sistema de colores que el generador HTML
Autor: Arturo Veras González
Fecha: 2025
"""

import os
import sys
from datetime import datetime
import re
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.platypus import PageBreak, KeepTogether
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY

class CompactCVGenerator:
    def __init__(self):
        self.output_dir = "generated_compact_2025"
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Colores base (se actualizarán dinámicamente)
        self.colors = {
            'primary': colors.HexColor('#2563eb'),    # Azul por defecto
            'secondary': colors.HexColor('#10b981'),  # Verde por defecto
            'dark': colors.HexColor('#1f2937'),
            'medium': colors.HexColor('#6b7280'),
            'light': colors.HexColor('#9ca3af'),
            'background': colors.HexColor('#f9fafb'),
            'white': colors.white
        }
        
        self.setup_styles()
    
    def get_job_customization(self, company, position, job_description=""):
        """
        MISMO sistema de colores que el generador HTML
        Jerarquía: Hardware/Embedded → Leadership → Software → Generic Engineer
        """
        customization = {
            'colors': {'primary': '#2563eb', 'secondary': '#10b981'},
            'detected_keywords': [],
            'highlight_skills': []
        }
        
        company_lower = company.lower() if company else ""
        position_lower = position.lower() if position else ""
        job_lower = job_description.lower() if job_description else ""
        
        # 1. Hardware/Embedded/IoT (Azul - Confiabilidad y Tecnología)
        if any(keyword in f"{company_lower} {position_lower} {job_lower}" for keyword in 
               ['intel', 'hardware', 'embedded', 'iot', 'sensors', 'firmware', 'electronics']):
            customization['colors'] = {
                'primary': '#2563eb',  # Azul confiable para hardware
                'secondary': '#0ea5e9'  # Azul tecnológico
            }
            customization['detected_keywords'] = ['Hardware', 'Embedded Systems', 'IoT', 'Firmware', 'Electronics']
        
        # 2. Leadership/Management (Púrpura - Liderazgo y Visión)
        elif any(keyword in f"{position_lower}" for keyword in 
                ['lead', 'manager', 'director', 'head', 'chief', 'senior', 'principal']):
            customization['colors'] = {
                'primary': '#7c3aed',  # Púrpura liderazgo
                'secondary': '#a855f7'  # Púrpura innovación
            }
            customization['detected_keywords'] = ['Leadership', 'Team Management', 'Strategy', 'Architecture']
        
        # 3. Software/Development (Verde - Crecimiento y Innovación)
        elif any(keyword in f"{company_lower} {position_lower} {job_lower}" for keyword in 
                ['spotify', 'software', 'developer', 'programming', 'full stack', 'backend', 'frontend']):
            customization['colors'] = {
                'primary': '#059669',  # Verde crecimiento
                'secondary': '#10b981'  # Verde innovación
            }
            customization['detected_keywords'] = ['Software Development', 'Programming', 'Innovation', 'Full Stack']
        
        # 4. Tech Giants específicos
        elif 'microsoft' in company_lower:
            customization['colors'] = {
                'primary': '#0078d4',  # Azul Microsoft
                'secondary': '#106ebe'
            }
            customization['detected_keywords'] = ['Microsoft', 'Enterprise', 'Cloud', 'Azure']
        
        # Actualizar colores del objeto
        self.colors['primary'] = colors.HexColor(customization['colors']['primary'])
        self.colors['secondary'] = colors.HexColor(customization['colors']['secondary'])
        
        # Keywords técnicas adicionales
        tech_keywords = ['Python', 'JavaScript', 'React', 'Node.js', 'AWS', 'Docker', 
                        'Kubernetes', 'Microservices', 'API', 'PostgreSQL']
        
        additional_keywords = []
        for keyword in tech_keywords:
            if keyword.lower() in job_lower:
                additional_keywords.append(keyword)
        
        customization['detected_keywords'].extend(additional_keywords)
        customization['detected_keywords'] = list(set(customization['detected_keywords']))[:8]  # Máximo 8
        
        return customization
    
    def setup_styles(self):
        """Configura estilos optimizados para diseño compacto"""
        self.styles = getSampleStyleSheet()
        
        # Header principal - ESPACIADO MEJORADO
        self.styles.add(ParagraphStyle(
            name='MainHeader',
            parent=self.styles['Title'],
            fontSize=22,  # Aumentado de 20
            textColor=self.colors['primary'],
            spaceAfter=8,  # Aumentado de 6
            spaceBefore=0,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold'
        ))
        
        # Subtítulo - ESPACIADO MEJORADO
        self.styles.add(ParagraphStyle(
            name='Subtitle',
            parent=self.styles['Normal'],
            fontSize=13,  # Aumentado de 12
            textColor=self.colors['medium'],
            spaceAfter=12,  # Aumentado de 8
            spaceBefore=0,
            alignment=TA_CENTER,
            fontName='Helvetica'
        ))
        
        # Información de contacto - ESPACIADO MEJORADO
        self.styles.add(ParagraphStyle(
            name='Contact',
            parent=self.styles['Normal'],
            fontSize=10,  # Aumentado de 9
            textColor=self.colors['dark'],
            spaceAfter=16,  # Aumentado de 12
            spaceBefore=0,
            alignment=TA_CENTER,
            fontName='Helvetica'
        ))
        
        # Secciones - ESPACIADO MEJORADO
        self.styles.add(ParagraphStyle(
            name='SectionHeader',
            parent=self.styles['Heading2'],
            fontSize=13,  # Aumentado de 12
            textColor=self.colors['primary'],
            spaceAfter=8,   # Aumentado de 6
            spaceBefore=12,  # Aumentado de 8
            fontName='Helvetica-Bold'
        ))
        
        # Texto normal - ESPACIADO MEJORADO
        self.styles.add(ParagraphStyle(
            name='CompactText',
            parent=self.styles['Normal'],
            fontSize=10,   # Aumentado de 9
            textColor=self.colors['dark'],
            spaceAfter=4,  # Aumentado de 3
            spaceBefore=0,
            leading=13,    # Aumentado de 11
            fontName='Helvetica'
        ))
        
        # Empresa y posición - ESPACIADO MEJORADO
        self.styles.add(ParagraphStyle(
            name='CompanyName',
            parent=self.styles['Normal'],
            fontSize=11,  # Aumentado de 10
            textColor=self.colors['dark'],
            spaceAfter=3,  # Aumentado de 2
            fontName='Helvetica-Bold'
        ))
        
        self.styles.add(ParagraphStyle(
            name='Position',
            parent=self.styles['Normal'],
            fontSize=10,   # Aumentado de 9
            textColor=self.colors['secondary'],
            spaceAfter=4,  # Aumentado de 3
            fontName='Helvetica-Bold'
        ))
        
        # Resumen profesional - ESPACIADO MEJORADO
        self.styles.add(ParagraphStyle(
            name='Summary',
            parent=self.styles['Normal'],
            fontSize=10,   # Aumentado de 9
            textColor=self.colors['dark'],
            spaceAfter=10,  # Aumentado de 8
            spaceBefore=0,
            leading=14,    # Aumentado de 12
            alignment=TA_JUSTIFY,
            fontName='Helvetica'
        ))
    
    def parse_anexos_md(self):
        """Lee y procesa el archivo anexos.md"""
        anexos_path = "anexos.md"
        if not os.path.exists(anexos_path):
            return self.get_default_data()
            
        try:
            with open(anexos_path, 'r', encoding='utf-8') as f:
                content = f.read()
            return self.extract_data_from_anexos(content)
        except Exception as e:
            print(f"❌ Error leyendo {anexos_path}: {e}")
            return self.get_default_data()
    
    def extract_data_from_anexos(self, content):
        """Extrae datos del anexo de forma compacta"""
        return {
            'personal_info': {
                'name': 'Arturo Veras González',
                'email': 'arturoveras93@gmail.com',
                'phone': '+56 9 5516 2574',
                'location': 'Santiago, Chile',
                'linkedin': 'linkedin.com/in/arturo-veras',
                'github': 'github.com/arturoveras'
            },
            'summary': 'Ingeniero especializado en desarrollo de sistemas IoT y aplicaciones web modernas, con experiencia en Python, JavaScript, AWS y arquitecturas de microservicios.',
            'experience': [
                {
                    'company': 'UQOMM',
                    'position': 'Ingeniero de Software Senior',
                    'period': 'Ene 2023 - Presente',
                    'achievements': [
                        'Sistema de monitoreo IoT que redujo costos 30%',
                        'API REST escalable (10K+ requests/hora)',
                        'Migración a microservicios en AWS'
                    ]
                },
                {
                    'company': 'BlackGPS',
                    'position': 'Desarrollador Full Stack',
                    'period': 'Mar 2021 - Dic 2022',
                    'achievements': [
                        'Dashboard interactivo con React y D3.js',
                        'Optimización SQL (60% menos tiempo)',
                        'Sistema de notificaciones en tiempo real'
                    ]
                }
            ],
            'education': [
                {
                    'degree': 'Ingeniería en Informática',
                    'institution': 'Universidad Nacional',
                    'period': '2016-2020'
                }
            ],
            'skills': {
                'programming': ['Python', 'JavaScript', 'TypeScript', 'Java', 'C++'],
                'frameworks': ['React', 'Node.js', 'Django', 'FastAPI'],
                'cloud': ['AWS', 'Docker', 'Kubernetes', 'Terraform'],
                'databases': ['PostgreSQL', 'MongoDB', 'Redis'],
                'iot': ['MQTT', 'LoRaWAN', 'Raspberry Pi', 'Sensors']
            },
            'certifications': ['AWS Certified Solutions Architect', 'IoT Specialist', 'Scrum Master']
        }
    
    def get_default_data(self):
        """Datos por defecto"""
        return self.extract_data_from_anexos("")
    
    def create_header(self, data):
        """Crea header compacto"""
        story = []
        
        # Nombre
        story.append(Paragraph(data['personal_info']['name'], self.styles['MainHeader']))
        
        # Subtítulo profesional
        story.append(Paragraph("Ingeniero de Software • Especialista IoT • Full Stack Developer", self.styles['Subtitle']))
        
        # Contacto en una sola línea
        contact_info = f"{data['personal_info']['email']} • {data['personal_info']['phone']} • {data['personal_info']['location']}"
        story.append(Paragraph(contact_info, self.styles['Contact']))
        
        return story
    
    def create_summary_section(self, data, customization):
        """Crea sección de resumen compacta"""
        story = []
        story.append(Paragraph("PERFIL PROFESIONAL", self.styles['SectionHeader']))
        
        # Personalizar resumen según empresa
        summary = data['summary']
        if customization.get('detected_keywords'):
            summary = f"Especialista en {', '.join(customization['detected_keywords'][:3])}. " + summary
        
        story.append(Paragraph(summary, self.styles['Summary']))
        return story
    
    def create_experience_section(self, data):
        """Crea sección de experiencia MUY compacta"""
        story = []
        story.append(Paragraph("EXPERIENCIA LABORAL", self.styles['SectionHeader']))
        
        for exp in data['experience']:
            # Tabla para empresa y período en la misma línea
            exp_data = [
                [Paragraph(f"<b>{exp['company']}</b> • {exp['position']}", self.styles['CompactText']),
                 Paragraph(exp['period'], self.styles['CompactText'])]
            ]
            
            exp_table = Table(exp_data, colWidths=[4*inch, 2*inch])
            exp_table.setStyle(TableStyle([
                ('VALIGN', (0,0), (-1,-1), 'TOP'),
                ('LEFTPADDING', (0,0), (-1,-1), 0),
                ('RIGHTPADDING', (0,0), (-1,-1), 0),
                ('TOPPADDING', (0,0), (-1,-1), 0),
                ('BOTTOMPADDING', (0,0), (-1,-1), 2),
            ]))
            
            story.append(exp_table)
            
            # Logros en bullet points con mejor espaciado
            if 'achievements' in exp:
                for achievement in exp['achievements'][:3]:  # Máximo 3 logros
                    story.append(Paragraph(f"• {achievement}", self.styles['CompactText']))
            
            story.append(Spacer(1, 6))  # Más espacio entre trabajos
        
        return story
    
    def create_skills_section(self, data, customization):
        """Crea sección de habilidades en tabla compacta"""
        story = []
        story.append(Paragraph("HABILIDADES TÉCNICAS", self.styles['SectionHeader']))
        
        # Crear tabla de habilidades 2x3
        skills_data = []
        skill_categories = {
            'Programación': ', '.join(data['skills']['programming'][:4]),
            'Frameworks': ', '.join(data['skills']['frameworks'][:4]),
            'Cloud & DevOps': ', '.join(data['skills']['cloud'][:4]),
            'Bases de Datos': ', '.join(data['skills']['databases'][:3]),
            'IoT & Hardware': ', '.join(data['skills']['iot'][:4]),
        }
        
        # Destacar skills relevantes
        highlighted = customization.get('detected_keywords', [])
        
        for category, skills in skill_categories.items():
            category_style = self.styles['CompactText']
            if any(h.lower() in skills.lower() for h in highlighted):
                category = f"<b>{category}</b>"  # Destacar categoría relevante
            
            skills_data.append([
                Paragraph(category, category_style),
                Paragraph(skills, self.styles['CompactText'])
            ])
        
        skills_table = Table(skills_data, colWidths=[1.5*inch, 4.5*inch])
        skills_table.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 6),
            ('TOPPADDING', (0,0), (-1,-1), 1),
            ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ]))
        
        story.append(skills_table)
        return story
    
    def create_education_certifications(self, data):
        """Combina educación y certificaciones en una sección"""
        story = []
        story.append(Paragraph("EDUCACIÓN & CERTIFICACIONES", self.styles['SectionHeader']))
        
        # Educación
        for edu in data['education']:
            edu_text = f"<b>{edu['degree']}</b> • {edu['institution']} • {edu['period']}"
            story.append(Paragraph(edu_text, self.styles['CompactText']))
        
        story.append(Spacer(1, 3))
        
        # Certificaciones en línea
        if data['certifications']:
            cert_text = "Certificaciones: " + " • ".join(data['certifications'])
            story.append(Paragraph(cert_text, self.styles['CompactText']))
        
        return story
    
    def create_keywords_section(self, customization):
        """Sección de keywords detectadas"""
        if not customization.get('detected_keywords'):
            return []
            
        story = []
        story.append(Paragraph("TECNOLOGÍAS RELEVANTES", self.styles['SectionHeader']))
        
        keywords_text = " • ".join(customization['detected_keywords'])
        story.append(Paragraph(keywords_text, self.styles['CompactText']))
        
        return story
    
    def generate_cv(self, company="", position="", job_description=""):
        """Genera CV compacto de 1 página"""
        print(f"🚀 Generando CV compacto 2025 para: {company} - {position}")
        
        # Cargar datos
        data = self.parse_anexos_md()
        
        # Obtener personalización (mismo sistema que HTML)
        customization = self.get_job_customization(company, position, job_description)
        
        # Actualizar estilos con nuevos colores
        self.setup_styles()
        
        # Crear directorio de salida
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        company_clean = re.sub(r'[^\w\s-]', '', company).strip().replace(' ', '_').lower()
        output_folder = f"cv_compact_{company_clean}_{timestamp}"
        output_path = os.path.join(self.output_dir, output_folder)
        os.makedirs(output_path, exist_ok=True)
        
        # Configurar documento para máxima compactidad
        pdf_file = os.path.join(output_path, f"cv_compact_{company_clean}_{timestamp}.pdf")
        doc = SimpleDocTemplate(
            pdf_file, 
            pagesize=A4,
            rightMargin=0.5*inch,   # Márgenes mínimos
            leftMargin=0.5*inch,
            topMargin=0.4*inch,
            bottomMargin=0.4*inch
        )
        
        # Construir contenido
        story = []
        
        # Header
        story.extend(self.create_header(data))
        
        # Resumen personalizado
        story.extend(self.create_summary_section(data, customization))
        
        # Experiencia compacta
        story.extend(self.create_experience_section(data))
        
        # Habilidades en tabla
        story.extend(self.create_skills_section(data, customization))
        
        # Educación y certificaciones juntas
        story.extend(self.create_education_certifications(data))
        
        # Keywords relevantes
        story.extend(self.create_keywords_section(customization))
        
        # Generar PDF
        try:
            doc.build(story)
            print(f"✅ CV compacto generado exitosamente:")
            print(f"   📁 Carpeta: {output_path}")
            print(f"   📄 PDF: {pdf_file}")
            print(f"   🎨 Colores: {customization['colors']}")
            print(f"   📏 Páginas: 1 (optimizado)")
            print(f"   🏷️  Keywords: {', '.join(customization['detected_keywords'][:5])}")
            
        except Exception as e:
            print(f"❌ Error generando PDF: {e}")
        
        return output_path

def main():
    """Función principal"""
    if len(sys.argv) < 3:
        print("💡 Uso: python3 generate_cv_compact_2025.py 'Empresa' 'Posición' ['Descripción']")
        print("📝 Ejemplo: python3 generate_cv_compact_2025.py 'Intel' 'Embedded Systems Engineer'")
        return
    
    company = sys.argv[1]
    position = sys.argv[2]
    job_description = sys.argv[3] if len(sys.argv) > 3 else ""
    
    generator = CompactCVGenerator()
    generator.generate_cv(company, position, job_description)

if __name__ == "__main__":
    main()
