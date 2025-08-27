#!/usr/bin/env python3
"""
Generador de CV con ReportLab - Arturo Veras
Generación programática de PDFs sin dependencias LaTeX
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
    PageBreak, Frame, PageTemplate, BaseDocTemplate
)
from reportlab.platypus.flowables import HRFlowable
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY

class ReportLabCVGenerator:
    def __init__(self):
        self.script_dir = Path(__file__).parent
        self.output_dir = self.script_dir / "generated_reportlab"
        self.data_file = self.script_dir / "anexos.md"
        
        # Crear directorio
        self.output_dir.mkdir(exist_ok=True)
        
        # Cargar datos
        self.personal_data = self.load_personal_data()
        
        # Configurar estilos
        self.setup_styles()
    
    def load_personal_data(self):
        """Carga datos básicos (simplificado para el ejemplo)"""
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
                        "Desarrollo de soluciones IoT para minería subterránea",
                        "Implementación de sistemas de monitoreo en tiempo real",
                        "Liderazgo técnico en proyectos de hardware/software"
                    ]
                },
                {
                    "company": "BlackGPS",
                    "position": "Ingeniero de Desarrollo",
                    "period": "Jul 2017 - Ago 2021 (4 años 2 meses)",
                    "achievements": [
                        "Desarrollo de sistemas de rastreo GPS",
                        "Implementación de APIs y sistemas backend",
                        "Desarrollo de aplicaciones móviles y web"
                    ]
                }
            ],
            "skills": {
                "Embedded Systems": ["STM32 Cortex M0/M4", "ARM", "FreeRTOS", "Linux Embebido"],
                "Programming": ["C/C++", "Python", "JavaScript", "TypeScript"],
                "IoT & Communications": ["MQTT", "LoRa", "Modbus", "I2C", "SPI", "UART"],
                "Web & Mobile": ["React", "Node.js", "MongoDB", "React Native"],
                "Tools & Methodologies": ["Git", "Docker", "Agile/Scrum", "CI/CD"]
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
                {"name": "Inglés", "level": "Avanzado (B2-C1)"}
            ]
        }
    
    def setup_styles(self):
        """Configura estilos para el documento"""
        self.styles = getSampleStyleSheet()
        
        # Estilo para el nombre
        self.styles.add(ParagraphStyle(
            name='Name',
            parent=self.styles['Heading1'],
            fontSize=24,
            textColor=colors.HexColor('#2563EB'),
            spaceAfter=6,
            alignment=TA_CENTER
        ))
        
        # Estilo para el título profesional
        self.styles.add(ParagraphStyle(
            name='JobTitle',
            parent=self.styles['Heading2'],
            fontSize=16,
            textColor=colors.HexColor('#4B5563'),
            spaceAfter=12,
            alignment=TA_CENTER
        ))
        
        # Estilo para secciones
        self.styles.add(ParagraphStyle(
            name='SectionHeader',
            parent=self.styles['Heading2'],
            fontSize=14,
            textColor=colors.HexColor('#2563EB'),
            spaceAfter=8,
            spaceBefore=16,
            borderWidth=0,
            borderColor=colors.HexColor('#2563EB'),
            leftIndent=0
        ))
        
        # Estilo para texto de contacto
        self.styles.add(ParagraphStyle(
            name='Contact',
            parent=self.styles['Normal'],
            fontSize=10,
            textColor=colors.HexColor('#6B7280'),
            alignment=TA_CENTER,
            spaceAfter=16
        ))
        
        # Estilo para resumen
        self.styles.add(ParagraphStyle(
            name='Summary',
            parent=self.styles['Normal'],
            fontSize=11,
            textColor=colors.HexColor('#374151'),
            alignment=TA_JUSTIFY,
            spaceAfter=12,
            leftIndent=12,
            rightIndent=12,
            borderWidth=1,
            borderColor=colors.HexColor('#E5E7EB'),
            borderPadding=8
        ))
        
        # Estilo para nombres de empresa
        self.styles.add(ParagraphStyle(
            name='Company',
            parent=self.styles['Normal'],
            fontSize=12,
            textColor=colors.HexColor('#1F2937'),
            fontName='Helvetica-Bold',
            spaceAfter=4
        ))
        
        # Estilo para posiciones
        self.styles.add(ParagraphStyle(
            name='Position',
            parent=self.styles['Normal'],
            fontSize=11,
            textColor=colors.HexColor('#2563EB'),
            fontName='Helvetica-Bold',
            spaceAfter=2
        ))
        
        # Estilo para períodos
        self.styles.add(ParagraphStyle(
            name='Period',
            parent=self.styles['Normal'],
            fontSize=10,
            textColor=colors.HexColor('#6B7280'),
            fontName='Helvetica-Oblique',
            spaceAfter=6
        ))
        
        # Estilo para logros
        self.styles.add(ParagraphStyle(
            name='Achievement',
            parent=self.styles['Normal'],
            fontSize=10,
            textColor=colors.HexColor('#374151'),
            leftIndent=20,
            spaceAfter=3,
            bulletIndent=10
        ))
    
    def get_company_colors(self, company):
        """Obtiene colores personalizados por empresa"""
        company_lower = company.lower()
        
        color_schemes = {
            "globant": {
                "primary": colors.HexColor('#00D4AA'),
                "secondary": colors.HexColor('#1F2937')
            },
            "google": {
                "primary": colors.HexColor('#4285F4'),
                "secondary": colors.HexColor('#34A853')
            },
            "microsoft": {
                "primary": colors.HexColor('#0078D4'),
                "secondary": colors.HexColor('#107C10')
            }
        }
        
        return color_schemes.get(company_lower, {
            "primary": colors.HexColor('#2563EB'),
            "secondary": colors.HexColor('#1F2937')
        })
    
    def customize_summary(self, company, position):
        """Personaliza el resumen según empresa/posición"""
        base_summary = self.personal_data["summary"]
        
        company_lower = company.lower()
        position_lower = position.lower()
        
        if "globant" in company_lower and "iot" in position_lower:
            return f"{base_summary} Especializado en transformación digital empresarial con tecnologías IoT Edge y metodologías Agile."
        elif "google" in company_lower:
            return f"{base_summary} Enfocado en sistemas escalables, tecnologías cloud-native y soluciones data-driven."
        elif "microsoft" in company_lower:
            return f"{base_summary} Especializado en soluciones enterprise, plataformas Azure y desarrollo productivo accesible."
        else:
            return f"{base_summary} Especializado en {position.lower()} para {company}."
    
    def build_header(self, story, company, position):
        """Construye el header del CV"""
        # Nombre
        story.append(Paragraph(self.personal_data["name"], self.styles['Name']))
        
        # Título profesional
        story.append(Paragraph(self.personal_data["title"], self.styles['JobTitle']))
        
        # Información de contacto
        contact_info = [
            f"📧 {self.personal_data['email']}",
            f"📱 {self.personal_data['phone']}",
            f"📍 {self.personal_data['location']}"
        ]
        
        if self.personal_data.get('linkedin'):
            contact_info.append(f"💼 {self.personal_data['linkedin']}")
        
        if self.personal_data.get('github'):
            contact_info.append(f"💻 {self.personal_data['github']}")
        
        contact_text = " | ".join(contact_info)
        story.append(Paragraph(contact_text, self.styles['Contact']))
        
        # Línea separadora
        story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#E5E7EB')))
        story.append(Spacer(1, 8))
    
    def build_summary(self, story, company, position):
        """Construye la sección de resumen"""
        story.append(Paragraph("PERFIL PROFESIONAL", self.styles['SectionHeader']))
        
        # Línea bajo el título
        story.append(HRFlowable(width="30%", thickness=2, color=colors.HexColor('#2563EB')))
        story.append(Spacer(1, 6))
        
        # Resumen personalizado
        custom_summary = self.customize_summary(company, position)
        story.append(Paragraph(custom_summary, self.styles['Summary']))
        story.append(Spacer(1, 12))
    
    def build_experience(self, story):
        """Construye la sección de experiencia"""
        story.append(Paragraph("EXPERIENCIA PROFESIONAL", self.styles['SectionHeader']))
        story.append(HRFlowable(width="30%", thickness=2, color=colors.HexColor('#2563EB')))
        story.append(Spacer(1, 6))
        
        for exp in self.personal_data["experience"]:
            # Empresa
            story.append(Paragraph(exp["company"], self.styles['Company']))
            
            # Posición
            story.append(Paragraph(exp["position"], self.styles['Position']))
            
            # Período
            story.append(Paragraph(exp["period"], self.styles['Period']))
            
            # Logros
            for achievement in exp["achievements"]:
                story.append(Paragraph(f"• {achievement}", self.styles['Achievement']))
            
            story.append(Spacer(1, 12))
    
    def build_skills(self, story, company, position):
        """Construye la sección de habilidades"""
        story.append(Paragraph("COMPETENCIAS TÉCNICAS", self.styles['SectionHeader']))
        story.append(HRFlowable(width="30%", thickness=2, color=colors.HexColor('#2563EB')))
        story.append(Spacer(1, 6))
        
        # Crear tabla de habilidades
        skills_data = []
        
        for category, skills in self.personal_data["skills"].items():
            skills_text = " • ".join(skills)
            skills_data.append([category, skills_text])
        
        # Crear tabla
        skills_table = Table(skills_data, colWidths=[4*cm, 12*cm])
        skills_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#2563EB')),
            ('TEXTCOLOR', (1, 0), (1, -1), colors.HexColor('#374151')),
            ('ROWBACKGROUNDS', (0, 0), (-1, -1), [colors.white, colors.HexColor('#F9FAFB')]),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#E5E7EB')),
            ('LEFTPADDING', (0, 0), (-1, -1), 8),
            ('RIGHTPADDING', (0, 0), (-1, -1), 8),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ]))
        
        story.append(skills_table)
        story.append(Spacer(1, 12))
    
    def build_education(self, story):
        """Construye la sección de educación"""
        story.append(Paragraph("EDUCACIÓN", self.styles['SectionHeader']))
        story.append(HRFlowable(width="30%", thickness=2, color=colors.HexColor('#2563EB')))
        story.append(Spacer(1, 6))
        
        for edu in self.personal_data["education"]:
            story.append(Paragraph(edu["degree"], self.styles['Company']))
            story.append(Paragraph(edu["institution"], self.styles['Position']))
            story.append(Paragraph(f"{edu['year']} | {edu['location']}", self.styles['Period']))
            story.append(Spacer(1, 8))
    
    def build_languages(self, story):
        """Construye la sección de idiomas"""
        story.append(Paragraph("IDIOMAS", self.styles['SectionHeader']))
        story.append(HRFlowable(width="30%", thickness=2, color=colors.HexColor('#2563EB')))
        story.append(Spacer(1, 6))
        
        for lang in self.personal_data["languages"]:
            story.append(Paragraph(f"<b>{lang['name']}</b>: {lang['level']}", self.styles['Achievement']))
        
        story.append(Spacer(1, 12))
    
    def generate_cv(self, company, position, output_filename=None):
        """Genera el CV en PDF"""
        
        print(f"🚀 Generando CV con ReportLab")
        print(f"   Company: {company}")
        print(f"   Position: {position}")
        print()
        
        # Crear directorio de salida
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_company = "".join(c if c.isalnum() else "_" for c in company.lower())
        output_name = f"cv_reportlab_{safe_company}_{timestamp}"
        output_path = self.output_dir / output_name
        output_path.mkdir(exist_ok=True)
        
        # Nombre del archivo
        if not output_filename:
            output_filename = f"cv_{safe_company}_{timestamp}.pdf"
        
        pdf_file = output_path / output_filename
        
        try:
            # Crear documento
            doc = SimpleDocTemplate(
                str(pdf_file),
                pagesize=A4,
                rightMargin=2*cm,
                leftMargin=2*cm,
                topMargin=2*cm,
                bottomMargin=2*cm
            )
            
            # Story (contenido del documento)
            story = []
            
            # Construir secciones
            self.build_header(story, company, position)
            self.build_summary(story, company, position)
            self.build_experience(story)
            self.build_skills(story, company, position)
            self.build_education(story)
            self.build_languages(story)
            
            # Información de generación
            story.append(Spacer(1, 20))
            story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#E5E7EB')))
            story.append(Spacer(1, 6))
            
            generation_info = f"Generado automáticamente el {datetime.now().strftime('%d de %B de %Y')} | Personalizado para {company} - {position}"
            story.append(Paragraph(generation_info, self.styles['Contact']))
            
            # Construir PDF
            doc.build(story)
            
            print(f"✅ CV generado exitosamente:")
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
        description="Generador de CV con ReportLab (PDF directo)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  python generate_cv_reportlab.py "Globant" "IoT Edge Engineer"
  python generate_cv_reportlab.py "Google" "Senior Software Engineer"
  python generate_cv_reportlab.py "Microsoft" "Technical Lead"
        """
    )
    
    parser.add_argument("company", help="Nombre de la empresa objetivo")
    parser.add_argument("position", help="Nombre de la posición")
    parser.add_argument("--output", "-o", help="Nombre del archivo de salida")
    
    args = parser.parse_args()
    
    # Verificar dependencias
    try:
        import reportlab
    except ImportError as e:
        print("❌ Dependencias faltantes. Instala con:")
        print("   pip install reportlab")
        return
    
    generator = ReportLabCVGenerator()
    
    output_path = generator.generate_cv(args.company, args.position, args.output)
    
    if output_path:
        print(f"🎉 CV ReportLab generado en: {output_path}")
    else:
        print("❌ Error generando CV")

if __name__ == "__main__":
    main()
