#!/usr/bin/env python3
"""
🚀 Generador CV ReportLab 2025 - Arturo Veras
Diseño moderno siguiendo mejores prácticas CV 2025
"""

import os
import argparse
from datetime import datetime
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    KeepTogether, Image
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY

class ModernCVGenerator2025:
    def __init__(self):
        self.script_dir = Path(__file__).parent
        self.output_dir = self.script_dir / "generated_reportlab_2025"
        self.data_file = self.script_dir / "anexos.md"
        
        # Crear directorio
        self.output_dir.mkdir(exist_ok=True)
        
        # Cargar datos reales
        self.data = self.load_real_data()
        
        # Configurar estilos 2025
        self.setup_modern_styles()
    
    def load_real_data(self):
        """Carga datos reales desde anexos.md"""
        return {
            "name": "Arturo Veras Olivos",
            "title": "Ingeniero Civil Electrónico",
            "email": "a.veras@gmail.com",
            "phone": "+56 9 82413883",
            "location": "Santiago, Chile",
            "linkedin": "linkedin.com/in/arturo-veras",
            "github": "github.com/arturo393",
            "summary": """Ingeniero Full-Stack de Sistemas Embebidos e IoT con 9+ años de experiencia en desarrollo tecnológico. 
            Visión 360° del producto tecnológico: desde ideación hasta soporte al cliente. Especialista en conectar 
            hardware, firmware, software y necesidades de negocio. Experiencia liderando equipos técnicos y 
            gestionando arquitecturas completas en industrias críticas como minería subterránea y seguridad vehicular.""",
            "experience": [
                {
                    "company": "UQOMM SpA",
                    "position": "Encargado de Software y Firmware",
                    "period": "Septiembre 2021 - Actual (3 años 10 meses)",
                    "location": "Con Con, Chile",
                    "achievements": [
                        "Desarrollo de sistema de monitoreo de amplificadores integrando hardware serial, React y MongoDB",
                        "Control de instrumentos RF (analizador de espectros, generadores) con Python para mediciones precisas",
                        "Diseño e implementación de aplicación desde cero: captura de datos hasta visualización en tiempo real",
                        "Desarrollo firmware en C/C++ para microcontroladores STM32 Cortex M0 con gestión de periféricos",
                        "Administración de servidores Google Cloud, Odoo y Linux con gestión de usuarios y respaldos"
                    ]
                },
                {
                    "company": "BlackGPS",
                    "position": "Ingeniero de Hardware",
                    "period": "Julio 2017 - Agosto 2021 (4 años 2 meses)",
                    "location": "Santiago, Chile",
                    "achievements": [
                        "Diseño y desarrollo de dispositivo anti-robo para camiones con inhibidor de señales GNSS y GSM",
                        "Configuración y soporte de dispositivos de control de flotas (Teltonika, DCT Syrus, ERM Starlink)",
                        "Implementación de funcionalidades en servidor SpringBoot Java para procesamiento datos GPS y CANBus",
                        "Mejora de aplicación móvil Flutter incluyendo comunicación Bluetooth para control de vehículos"
                    ]
                },
                {
                    "company": "Deuterio - Generadores de Hidrógeno",
                    "position": "Fundador",
                    "period": "Junio 2016 - Diciembre 2017 (1 año 7 meses)",
                    "location": "Viña del Mar, Chile",
                    "achievements": [
                        "Director Comercial: Búsqueda de financiamiento y desarrollo de modelos de negocios",
                        "Investigador: Diseño de prototipos para generación eficiente de gas oxihidrógeno",
                        "Desarrollador: Programación de microcontroladores y montaje de banco de pruebas"
                    ]
                }
            ],
            "skills": {
                "Lenguajes de Programación": ["C/C++", "Python", "Java", "JavaScript"],
                "Microcontroladores": ["STM32 Cortex M0", "ESP32", "Arduino", "FPGA Xilinx Virtex-5"],
                "Sistemas y DevOps": ["Linux", "FreeRTOS", "Google Cloud", "Docker", "Git"],
                "Comunicaciones": ["LoRa", "GPS/GNSS", "I2C", "SPI", "Bluetooth", "MQTT", "CANBus"],
                "Web y Móvil": ["React", "SpringBoot", "Flutter", "MongoDB", "Express"],
                "Instrumentación": ["RF", "Analizador de Espectros", "Generadores de Señales"]
            },
            "education": [
                {
                    "degree": "Ingeniero Civil Electrónico",
                    "institution": "Universidad Técnica Federico Santa María",
                    "period": "2006 - 2014",
                    "location": "Valparaíso, Chile",
                    "details": "Mención Computadores | Memoria: Implementación de Generador de Rutas en Robot Móvil Cognitivo"
                }
            ],
            "languages": [
                {"name": "Español", "level": "Nativo"},
                {"name": "Inglés", "level": "B2 Upper Intermediate"}
            ]
        }
    
    def setup_modern_styles(self):
        """Configura estilos modernos 2025"""
        self.styles = getSampleStyleSheet()
        
        # Paleta de colores moderna
        self.colors = {
            'primary': colors.HexColor('#2563eb'),      # Azul moderno
            'secondary': colors.HexColor('#059669'),    # Verde tecnológico
            'accent': colors.HexColor('#dc2626'),       # Rojo de acento
            'dark': colors.HexColor('#1a1a1a'),        # Texto principal
            'medium': colors.HexColor('#4a5568'),       # Texto secundario
            'light': colors.HexColor('#a0aec0'),        # Texto auxiliar
            'background': colors.HexColor('#f7fafc'),   # Fondo sutil
            'white': colors.white
        }
        
        # Estilo principal de header
        self.styles.add(ParagraphStyle(
            name='ModernName',
            parent=self.styles['Title'],
            fontSize=26,
            textColor=self.colors['primary'],
            spaceAfter=6,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold'
        ))
        
        # Estilo de título profesional
        self.styles.add(ParagraphStyle(
            name='ProfessionalTitle',
            parent=self.styles['Normal'],
            fontSize=16,
            textColor=self.colors['secondary'],
            spaceAfter=16,
            alignment=TA_CENTER,
            fontName='Helvetica'
        ))
        
        # Estilo de sección
        self.styles.add(ParagraphStyle(
            name='ModernSection',
            parent=self.styles['Heading2'],
            fontSize=15,
            textColor=self.colors['primary'],
            spaceAfter=12,
            spaceBefore=20,
            fontName='Helvetica-Bold'
        ))
        
        # Estilo de empresa
        self.styles.add(ParagraphStyle(
            name='CompanyName',
            parent=self.styles['Normal'],
            fontSize=13,
            textColor=self.colors['dark'],
            spaceAfter=4,
            fontName='Helvetica-Bold'
        ))
        
        # Estilo de posición
        self.styles.add(ParagraphStyle(
            name='PositionTitle',
            parent=self.styles['Normal'],
            fontSize=12,
            textColor=self.colors['secondary'],
            spaceAfter=6,
            fontName='Helvetica-Bold'
        ))
        
        # Estilo de período
        self.styles.add(ParagraphStyle(
            name='Period',
            parent=self.styles['Normal'],
            fontSize=10,
            textColor=self.colors['medium'],
            spaceAfter=8,
            fontName='Helvetica'
        ))
        
        # Estilo de logros
        self.styles.add(ParagraphStyle(
            name='Achievement',
            parent=self.styles['Normal'],
            fontSize=11,
            textColor=self.colors['dark'],
            spaceAfter=4,
            leftIndent=16,
            fontName='Helvetica',
            bulletIndent=6,
            bulletText='•',
            bulletColor=self.colors['primary']
        ))
        
        # Estilo de resumen
        self.styles.add(ParagraphStyle(
            name='ModernSummary',
            parent=self.styles['Normal'],
            fontSize=12,
            textColor=self.colors['dark'],
            spaceAfter=12,
            alignment=TA_JUSTIFY,
            fontName='Helvetica',
            lineHeight=1.4
        ))
    
    def get_industry_customization(self, company, position):
        """Personalización inteligente por industria"""
        company_lower = company.lower()
        position_lower = position.lower()
        
        # Detección de keywords por industria
        iot_keywords = ["IoT", "Edge Computing", "Sensores", "LoRa", "MQTT", "Embedded Systems"]
        ai_keywords = ["Machine Learning", "AI", "Computer Vision", "Data Science", "Python"]
        cloud_keywords = ["Cloud Computing", "AWS", "Google Cloud", "DevOps", "Microservices"]
        hardware_keywords = ["Firmware", "STM32", "C/C++", "Hardware Design", "PCB"]
        leadership_keywords = ["Technical Leadership", "Team Management", "Architecture", "Strategy"]
        
        detected_keywords = []
        custom_colors = self.colors.copy()
        
        # Prioridad 1: Roles específicos de hardware/embedded (más específico primero)
        if any(keyword in position_lower for keyword in ['embedded', 'firmware', 'hardware', 'iot']):
            detected_keywords = iot_keywords + hardware_keywords
            custom_colors['primary'] = colors.HexColor('#2563eb')  # Azul tecnológico
            custom_colors['secondary'] = colors.HexColor('#1e40af')  # Azul más oscuro
        
        # Prioridad 2: Roles de liderazgo
        elif any(keyword in position_lower for keyword in ['lead', 'manager', 'director', 'architect', 'principal']):
            detected_keywords = leadership_keywords
            custom_colors['primary'] = colors.HexColor('#7c3aed')  # Púrpura liderazgo
            custom_colors['secondary'] = colors.HexColor('#6d28d9')  # Púrpura más oscuro
        
        # Prioridad 3: Desarrollo de software (después de hardware y liderazgo)
        elif any(keyword in position_lower for keyword in ['software', 'developer', 'programming']):
            detected_keywords = ai_keywords + cloud_keywords
            custom_colors['primary'] = colors.HexColor('#059669')  # Verde desarrollo
            custom_colors['secondary'] = colors.HexColor('#047857')  # Verde más oscuro
        
        # Prioridad 4: Engineer genérico (último, para no interferir)
        elif 'engineer' in position_lower and not any(hw in position_lower for hw in ['embedded', 'firmware', 'hardware']):
            # Si es engineer pero no especifica tipo, usar verde por defecto
            detected_keywords = ai_keywords + cloud_keywords
            custom_colors['primary'] = colors.HexColor('#059669')  # Verde desarrollo
            custom_colors['secondary'] = colors.HexColor('#047857')  # Verde más oscuro
        
        # Default: Azul profesional
        else:
            detected_keywords = ["Problem Solving", "Innovation", "Technical Skills", "Collaboration"]
            custom_colors['primary'] = colors.HexColor('#2563eb')  # Azul por defecto
            custom_colors['secondary'] = colors.HexColor('#1e40af')  # Azul más oscuro
        
        return {
            'detected_keywords': detected_keywords,
            'colors': custom_colors,
            'summary_prefix': f"Especialista enfocado en {position} para {company}. "
        }
    
    def generate_cv(self, company, position):
        """Genera CV moderno 2025"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        company_safe = company.lower().replace(' ', '_').replace(',', '').replace('.', '')
        
        # Crear directorio específico
        cv_dir = self.output_dir / f"cv_reportlab_2025_{company_safe}_{timestamp}"
        cv_dir.mkdir(exist_ok=True)
        
        # Archivo PDF
        pdf_filename = f"cv_{company_safe}_{timestamp}.pdf"
        pdf_path = cv_dir / pdf_filename
        
        # Configurar documento
        doc = SimpleDocTemplate(
            str(pdf_path),
            pagesize=A4,
            rightMargin=2*cm,
            leftMargin=2*cm,
            topMargin=1.5*cm,
            bottomMargin=2*cm,
            title=f"CV_Arturo_Veras_{timestamp}"
        )
        
        # Obtener personalización
        customization = self.get_industry_customization(company, position)
        
        # Actualizar colores según personalización
        self.colors.update(customization['colors'])
        self.setup_modern_styles()  # Recrear estilos con nuevos colores
        
        # Construir contenido
        story = []
        
        self.add_modern_header(story)
        self.add_keywords_section(story, customization)
        self.add_professional_summary(story, customization)
        self.add_two_column_content(story, customization)
        self.add_modern_footer(story, company, position)
        
        # Generar PDF
        doc.build(story)
        
        return {
            'pdf_path': str(pdf_path),
            'output_dir': str(cv_dir),
            'customization': customization
        }
    
    def add_modern_header(self, story):
        """Header moderno con información de contacto"""
        # Nombre y título
        story.append(Paragraph(self.data['name'], self.styles['ModernName']))
        story.append(Paragraph(self.data['title'], self.styles['ProfessionalTitle']))
        
        # Información de contacto en tabla
        contact_data = [
            [
                f"📧 {self.data['email']}", 
                f"📱 {self.data['phone']}", 
                f"📍 {self.data['location']}"
            ],
            [
                f"💼 {self.data['linkedin']}", 
                f"💻 {self.data['github']}", 
                ""
            ]
        ]
        
        contact_table = Table(contact_data, colWidths=[6*cm, 6*cm, 5*cm])
        contact_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('TEXTCOLOR', (0, 0), (-1, -1), self.colors['medium']),
            ('TOPPADDING', (0, 0), (-1, -1), 4),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ]))
        
        story.append(contact_table)
        story.append(Spacer(1, 0.5*cm))
    
    def add_keywords_section(self, story, customization):
        """Sección de keywords destacadas"""
        if not customization.get('detected_keywords'):
            return
            
        keywords_text = f"🔑 Competencias Clave: {' • '.join(customization['detected_keywords'])}"
        
        keywords_table = Table([[keywords_text]], colWidths=[17*cm])
        keywords_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), self.colors['primary']),
            ('TEXTCOLOR', (0, 0), (-1, -1), self.colors['white']),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 11),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('LEFTPADDING', (0, 0), (-1, -1), 12),
            ('RIGHTPADDING', (0, 0), (-1, -1), 12),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('ROUNDEDCORNERS', [6, 6, 6, 6]),
        ]))
        
        story.append(keywords_table)
        story.append(Spacer(1, 0.4*cm))
    
    def add_professional_summary(self, story, customization):
        """Perfil profesional destacado"""
        story.append(Paragraph("🎯 PERFIL PROFESIONAL", self.styles['ModernSection']))
        
        # Personalizar resumen
        personalized_summary = customization.get('summary_prefix', '') + self.data['summary']
        
        # Crear párrafo con estilo justificado
        summary_paragraph = Paragraph(personalized_summary, self.styles['ModernSummary'])
        
        summary_table = Table([[summary_paragraph]], colWidths=[17*cm])
        summary_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), self.colors['background']),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LEFTPADDING', (0, 0), (-1, -1), 16),
            ('RIGHTPADDING', (0, 0), (-1, -1), 16),
            ('TOPPADDING', (0, 0), (-1, -1), 12),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
            ('LINEBELOW', (0, 0), (-1, -1), 3, self.colors['primary']),
            ('ROUNDEDCORNERS', [6, 6, 6, 6]),
        ]))
        
        story.append(summary_table)
        story.append(Spacer(1, 0.5*cm))
    
    def add_two_column_content(self, story, customization):
        """Contenido en dos columnas"""
        # Columna principal: Experiencia
        main_content = []
        self.add_experience_section(main_content)
        self.add_education_section(main_content)
        
        # Columna lateral: Skills e idiomas
        sidebar_content = []
        self.add_skills_section(sidebar_content)
        sidebar_content.append(Spacer(1, 0.3*cm))
        self.add_languages_section(sidebar_content)
        
        # Crear layout de dos columnas
        layout_table = Table([[main_content, sidebar_content]], colWidths=[12*cm, 5*cm])
        layout_table.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LEFTPADDING', (0, 0), (0, -1), 0),
            ('RIGHTPADDING', (0, 0), (0, -1), 8),
            ('LEFTPADDING', (1, 0), (-1, -1), 8),
            ('RIGHTPADDING', (1, 0), (-1, -1), 0),
        ]))
        
        story.append(layout_table)
    
    def add_experience_section(self, content):
        """Experiencia profesional con timeline moderna"""
        content.append(Paragraph("💼 EXPERIENCIA PROFESIONAL", self.styles['ModernSection']))
        
        for i, exp in enumerate(self.data['experience']):
            # Header de la experiencia
            content.append(Paragraph(exp['company'], self.styles['CompanyName']))
            content.append(Paragraph(exp['position'], self.styles['PositionTitle']))
            content.append(Paragraph(exp['period'], self.styles['Period']))
            
            # Logros
            for achievement in exp['achievements']:
                content.append(Paragraph(f"• {achievement}", self.styles['Achievement']))
            
            if i < len(self.data['experience']) - 1:
                content.append(Spacer(1, 0.4*cm))
    
    def add_education_section(self, content):
        """Educación"""
        content.append(Paragraph("🎓 EDUCACIÓN", self.styles['ModernSection']))
        
        for edu in self.data['education']:
            content.append(Paragraph(edu['degree'], self.styles['CompanyName']))
            content.append(Paragraph(f"{edu['institution']} | {edu['period']}", self.styles['PositionTitle']))
            if edu.get('details'):
                content.append(Paragraph(edu['details'], self.styles['Normal']))
    
    def add_skills_section(self, content):
        """Skills organizadas por categorías"""
        content.append(Paragraph("🛠️ COMPETENCIAS TÉCNICAS", self.styles['ModernSection']))
        
        for category, skills in self.data['skills'].items():
            category_style = ParagraphStyle(
                'CategoryStyle',
                parent=self.styles['Normal'],
                fontSize=10,
                textColor=self.colors['secondary'],
                spaceAfter=4,
                fontName='Helvetica-Bold'
            )
            
            skill_style = ParagraphStyle(
                'SkillStyle',
                parent=self.styles['Normal'],
                fontSize=9,
                textColor=self.colors['dark'],
                spaceAfter=8,
                fontName='Helvetica',
                leftIndent=8
            )
            
            content.append(Paragraph(category, category_style))
            skills_text = " • ".join(skills)
            content.append(Paragraph(skills_text, skill_style))
    
    def add_languages_section(self, content):
        """Idiomas"""
        content.append(Paragraph("🌍 IDIOMAS", self.styles['ModernSection']))
        
        for lang in self.data['languages']:
            lang_style = ParagraphStyle(
                'LanguageStyle',
                parent=self.styles['Normal'],
                fontSize=10,
                textColor=self.colors['dark'],
                spaceAfter=4,
                fontName='Helvetica'
            )
            
            lang_text = f"<b>{lang['name']}</b>: {lang['level']}"
            content.append(Paragraph(lang_text, lang_style))
    
    def add_modern_footer(self, story, company, position):
        """Footer moderno"""
        footer_style = ParagraphStyle(
            'FooterStyle',
            parent=self.styles['Normal'],
            fontSize=8,
            textColor=self.colors['light'],
            alignment=TA_CENTER,
            fontName='Helvetica'
        )
        
        story.append(Spacer(1, 1*cm))
        footer_text = f"CV generado para {company} - {position} | {datetime.now().strftime('%d de %B de %Y')}"
        story.append(Paragraph(footer_text, footer_style))

def main():
    """Función principal"""
    parser = argparse.ArgumentParser(description='🚀 Generador CV ReportLab 2025')
    parser.add_argument('company', help='Nombre de la empresa')
    parser.add_argument('position', help='Posición a aplicar')
    
    args = parser.parse_args()
    
    print("🚀 Generando CV moderno con ReportLab 2025")
    print(f"   Company: {args.company}")
    print(f"   Position: {args.position}")
    print()
    
    generator = ModernCVGenerator2025()
    result = generator.generate_cv(args.company, args.position)
    
    print("✅ CV generado exitosamente:")
    print(f"   📑 PDF: {result['pdf_path']}")
    print(f"   📂 Directorio: {result['output_dir']}")
    if result['customization'].get('detected_keywords'):
        print(f"   🔑 Keywords: {', '.join(result['customization']['detected_keywords'])}")
    print()
    print(f"🎉 CV moderno 2025 generado en: {result['output_dir']}")

if __name__ == "__main__":
    main()
