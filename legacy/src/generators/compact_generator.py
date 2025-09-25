#!/usr/bin/env python3
"""
Compact Generator - CV Suite 2025  
Generador de CVs compactos en PDF usando ReportLab optimizado para 1 página
Autor: Arturo Veras González
"""

import sys
from pathlib import Path
from typing import List, Optional, Dict, Any
from datetime import datetime

# Imports desde core
sys.path.append(str(Path(__file__).parent.parent))
from core.generator_base import BaseGenerator, GeneratorConfig
from core.data_parser import PersonalData


class CompactGenerator(BaseGenerator):
    """Generador de CVs compactos optimizados para 1 página"""
    
    def __init__(self):
        super().__init__("compact")
    
    def generate_cv(self, config: GeneratorConfig) -> Optional[Path]:
        """
        Genera CV compacto en PDF usando ReportLab
        
        Args:
            config: Configuración del generador
            
        Returns:
            Path: Archivo PDF generado
        """
        if not self.validate_dependencies():
            print("❌ Error: ReportLab no está instalado")
            print("💡 Instala con: pip install reportlab")
            return None
        
        if not self.validate_config(config):
            return None
        
        try:
            self.log_generation_start(config)
            
            # Crear directorio de salida
            output_dir = self.create_output_directory(config)
            
            # Obtener contexto de personalización
            context = self.get_customization_context(config)
            
            # Generar PDF
            pdf_file = self._generate_pdf(context, output_dir)
            
            self.log_generation_success(output_dir)
            return pdf_file
            
        except Exception as e:
            self.log_generation_error(e)
            return None
    
    def _generate_pdf(self, context: Dict[str, Any], output_dir: Path) -> Path:
        """Genera el PDF usando ReportLab"""
        from reportlab.lib.pagesizes import A4, letter
        from reportlab.lib import colors
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import inch, mm
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
        from reportlab.platypus.flowables import HRFlowable
        from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
        from reportlab.pdfgen import canvas
        from reportlab.lib.utils import ImageReader
        
        # Archivo de salida
        pdf_file = output_dir / "cv_compact.pdf"
        
        # Configuración del documento
        doc = SimpleDocTemplate(
            str(pdf_file),
            pagesize=A4,
            rightMargin=15*mm,
            leftMargin=15*mm,
            topMargin=12*mm,
            bottomMargin=12*mm
        )
        
        # Obtener datos
        personal = context['personal']
        colors_scheme = context['colors']
        
        # Convertir color hex a RGB
        primary_color = self._hex_to_rgb(colors_scheme['primary'])
        accent_color = self._hex_to_rgb(colors_scheme['accent'])
        
        # Crear estilos personalizados
        styles = self._create_styles(primary_color, accent_color)
        
        # Construir contenido
        story = []
        
        # Header con información personal
        story.extend(self._build_header(personal, context, styles, primary_color))
        
        # Spacer pequeño
        story.append(Spacer(1, 3*mm))
        
        # Resumen profesional
        story.extend(self._build_summary(personal, styles))
        
        # Experiencia laboral
        story.extend(self._build_experience(personal, styles, primary_color))
        
        # Skills técnicas
        story.extend(self._build_skills(personal, styles, accent_color))
        
        # Educación
        story.extend(self._build_education(personal, styles, primary_color))
        
        # Certificaciones si existen
        if personal.certifications:
            story.extend(self._build_certifications(personal, styles, accent_color))
        
        # Footer con información de generación
        story.extend(self._build_footer(context, styles))
        
        # Generar PDF
        doc.build(story)
        
        print(f"   📄 PDF: {pdf_file.name}")
        return pdf_file
    
    def _hex_to_rgb(self, hex_color: str) -> tuple:
        """Convierte color hex a tupla RGB para ReportLab"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16)/255.0 for i in (0, 2, 4))
    
    def _create_styles(self, primary_color: tuple, accent_color: tuple):
        """Crea estilos personalizados para el documento"""
        styles = getSampleStyleSheet()
        
        # Estilo para nombre
        styles.add(ParagraphStyle(
            name='CustomName',
            parent=styles['Heading1'],
            fontSize=18,
            spaceAfter=2*mm,
            textColor=colors.Color(*primary_color),
            fontName='Helvetica-Bold',
            alignment=TA_LEFT
        ))
        
        # Estilo para título/posición
        styles.add(ParagraphStyle(
            name='CustomTitle',
            parent=styles['Heading2'],
            fontSize=12,
            spaceAfter=1*mm,
            textColor=colors.Color(*accent_color),
            fontName='Helvetica',
            alignment=TA_LEFT
        ))
        
        # Estilo para secciones
        styles.add(ParagraphStyle(
            name='SectionHeader',
            parent=styles['Heading3'],
            fontSize=11,
            spaceBefore=4*mm,
            spaceAfter=2*mm,
            textColor=colors.Color(*primary_color),
            fontName='Helvetica-Bold',
            borderWidth=0,
            borderColor=colors.Color(*accent_color),
            borderPadding=0
        ))
        
        # Estilo para contenido
        styles.add(ParagraphStyle(
            name='CustomBody',
            parent=styles['Normal'],
            fontSize=9,
            spaceAfter=1*mm,
            fontName='Helvetica',
            alignment=TA_JUSTIFY,
            leading=11
        ))
        
        # Estilo para items de lista
        styles.add(ParagraphStyle(
            name='ListItem',
            parent=styles['Normal'],
            fontSize=8.5,
            spaceAfter=0.5*mm,
            fontName='Helvetica',
            leftIndent=4*mm,
            bulletIndent=2*mm,
            leading=10
        ))
        
        # Estilo para información de contacto
        styles.add(ParagraphStyle(
            name='Contact',
            parent=styles['Normal'],
            fontSize=8,
            fontName='Helvetica',
            alignment=TA_RIGHT
        ))
        
        return styles
    
    def _build_header(self, personal: PersonalData, context: Dict, styles, primary_color: tuple):
        """Construye el header con información personal"""
        from reportlab.platypus import Table, TableStyle
        from reportlab.lib import colors
        
        story = []
        
        # Información personal en tabla de 2 columnas
        header_data = [
            [
                Paragraph(f"<b>{personal.name}</b>", styles['CustomName']),
                Paragraph(f"📧 {personal.email}<br/>📱 {personal.phone}<br/>📍 {personal.location}", styles['Contact'])
            ],
            [
                Paragraph(f"{context['position']}", styles['CustomTitle']),
                Paragraph(f"💼 {context['company']}<br/>🔗 <link href='{personal.linkedin}'>LinkedIn</link><br/>💻 <link href='{personal.github}'>GitHub</link>", styles['Contact'])
            ]
        ]
        
        header_table = Table(header_data, colWidths=[120*mm, 65*mm])
        header_table.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('RIGHTPADDING', (0, 0), (-1, -1), 0),
            ('TOPPADDING', (0, 0), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 1*mm),
        ]))
        
        story.append(header_table)
        
        # Línea separadora
        from reportlab.platypus.flowables import HRFlowable
        story.append(HRFlowable(width="100%", thickness=1, color=colors.Color(*primary_color)))
        
        return story
    
    def _build_summary(self, personal: PersonalData, styles):
        """Construye sección de resumen profesional"""
        story = []
        
        story.append(Paragraph("<b>💡 PERFIL PROFESIONAL</b>", styles['SectionHeader']))
        story.append(Paragraph(personal.summary, styles['CustomBody']))
        
        return story
    
    def _build_experience(self, personal: PersonalData, styles, primary_color: tuple):
        """Construye sección de experiencia laboral"""
        from reportlab.platypus import Table, TableStyle
        from reportlab.lib import colors
        
        story = []
        
        story.append(Paragraph("<b>💼 EXPERIENCIA LABORAL</b>", styles['SectionHeader']))
        
        for exp in personal.experience:
            # Header de experiencia en tabla
            exp_header = Table([
                [
                    Paragraph(f"<b>{exp['position']}</b>", styles['CustomBody']),
                    Paragraph(f"<b>{exp['company']}</b> | {exp['period']}", styles['Contact'])
                ]
            ], colWidths=[120*mm, 65*mm])
            
            exp_header.setStyle(TableStyle([
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('LEFTPADDING', (0, 0), (-1, -1), 0),
                ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                ('TOPPADDING', (0, 0), (-1, -1), 0),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 0.5*mm),
            ]))
            
            story.append(exp_header)
            
            # Responsabilidades
            for resp in exp['responsibilities'][:4]:  # Limitar a 4 items por espacio
                story.append(Paragraph(f"▸ {resp}", styles['ListItem']))
            
            story.append(Spacer(1, 1*mm))
        
        return story
    
    def _build_skills(self, personal: PersonalData, styles, accent_color: tuple):
        """Construye sección de skills técnicas"""
        from reportlab.platypus import Table, TableStyle
        from reportlab.lib import colors
        
        story = []
        
        story.append(Paragraph("<b>🛠️ COMPETENCIAS TÉCNICAS</b>", styles['SectionHeader']))
        
        # Agrupar skills en filas de 4-5 items
        skills = personal.technical_skills[:15]  # Limitar por espacio
        skill_rows = []
        
        for i in range(0, len(skills), 4):
            row = skills[i:i+4]
            # Completar fila si es necesario
            while len(row) < 4:
                row.append("")
            skill_rows.append(row)
        
        if skill_rows:
            skills_table = Table(skill_rows, colWidths=[46*mm]*4)
            skills_table.setStyle(TableStyle([
                ('FONTSIZE', (0, 0), (-1, -1), 8),
                ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
                ('TEXTCOLOR', (0, 0), (-1, -1), colors.Color(*accent_color)),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('LEFTPADDING', (0, 0), (-1, -1), 2*mm),
                ('RIGHTPADDING', (0, 0), (-1, -1), 2*mm),
                ('TOPPADDING', (0, 0), (-1, -1), 1*mm),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 1*mm),
                ('BACKGROUND', (0, 0), (-1, -1), colors.Color(0.95, 0.95, 0.95)),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.Color(*accent_color)),
                ('ROUNDEDCORNERS', [2, 2, 2, 2]),
            ]))
            
            story.append(skills_table)
        
        return story
    
    def _build_education(self, personal: PersonalData, styles, primary_color: tuple):
        """Construye sección de educación"""
        from reportlab.platypus import Table, TableStyle
        from reportlab.lib import colors
        
        story = []
        
        story.append(Paragraph("<b>🎓 EDUCACIÓN</b>", styles['SectionHeader']))
        
        for edu in personal.education:
            edu_table = Table([
                [
                    Paragraph(f"<b>{edu['degree']}</b>", styles['CustomBody']),
                    Paragraph(f"{edu['institution']} | {edu['year']}", styles['Contact'])
                ]
            ], colWidths=[120*mm, 65*mm])
            
            edu_table.setStyle(TableStyle([
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('LEFTPADDING', (0, 0), (-1, -1), 0),
                ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                ('TOPPADDING', (0, 0), (-1, -1), 0),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 1*mm),
            ]))
            
            story.append(edu_table)
        
        return story
    
    def _build_certifications(self, personal: PersonalData, styles, accent_color: tuple):
        """Construye sección de certificaciones"""
        story = []
        
        story.append(Paragraph("<b>🏆 CERTIFICACIONES</b>", styles['SectionHeader']))
        
        for cert in personal.certifications[:6]:  # Limitar por espacio
            cert_text = cert['name']
            if cert.get('issuer'):
                cert_text += f" - {cert['issuer']}"
            story.append(Paragraph(f"▸ {cert_text}", styles['ListItem']))
        
        return story
    
    def _build_footer(self, context: Dict, styles):
        """Construye footer con información de generación"""
        from reportlab.platypus import Spacer
        
        story = []
        
        story.append(Spacer(1, 3*mm))
        
        footer_text = f"<i>🎨 {context['meta']['color_explanation']} | Generado el {context['meta']['generated_at'][:10]} para {context['company']}</i>"
        story.append(Paragraph(footer_text, styles['Contact']))
        
        return story
    
    def get_supported_templates(self) -> List[str]:
        """Retorna templates soportados"""
        return ["compact", "minimal", "professional"]
    
    def validate_dependencies(self) -> bool:
        """Valida dependencias del generador compacto"""
        try:
            import reportlab
            print("   ✅ reportlab: OK")
            return True
        except ImportError:
            print("   ❌ reportlab: Missing")
            print("   💡 Install with: pip install reportlab")
            return False
    
    def _get_template_extension(self) -> str:
        """Extensión de templates para ReportLab"""
        return "py"  # Templates son scripts Python


def main():
    """Función principal para uso directo del generador"""
    if len(sys.argv) < 3:
        print("💡 Uso: python compact_generator.py 'Empresa' 'Posición'")
        print("📝 Ejemplo: python compact_generator.py 'Intel' 'Embedded Engineer'")
        return
    
    company = sys.argv[1]
    position = sys.argv[2]
    
    # Crear configuración
    config = GeneratorConfig(
        company=company,
        position=position,
        template_name="compact"
    )
    
    # Generar CV
    generator = CompactGenerator()
    output_path = generator.generate_cv(config)
    
    if output_path:
        print(f"🎉 CV compacto generado exitosamente: {output_path}")
        
        # Abrir PDF si está disponible
        import subprocess
        import sys
        if sys.platform == "darwin":  # macOS
            subprocess.run(["open", str(output_path)])
        elif sys.platform == "linux":  # Linux
            subprocess.run(["xdg-open", str(output_path)])
        elif sys.platform == "win32":  # Windows
            subprocess.run(["start", str(output_path)], shell=True)
    else:
        print("❌ Error generando CV compacto")


if __name__ == "__main__":
    main()