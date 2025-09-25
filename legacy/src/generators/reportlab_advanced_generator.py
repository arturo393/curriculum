#!/usr/bin/env python3
"""
Advanced ReportLab Generator
Generador avanzado de PDFs con ReportLab siguiendo diseño moderno 2025
Migrado desde generate_cv_reportlab_2025.py a nueva arquitectura
"""

import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional

# ReportLab imports
try:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import cm, mm
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
        KeepTogether, Image
    )
    from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
    REPORTLAB_AVAILABLE = True
except ImportError:
    REPORTLAB_AVAILABLE = False

# Agregar path para imports
sys.path.append(str(Path(__file__).parent.parent))

from core.generator_base import BaseGenerator, GeneratorConfig
from core.data_parser import DataParser


class AdvancedReportLabGenerator(BaseGenerator):
    """Generador avanzado de CVs en PDF con ReportLab siguiendo tendencias 2025"""
    
    def __init__(self):
        super().__init__()
        self.generator_type = "reportlab_advanced"
        
        if REPORTLAB_AVAILABLE:
            self.setup_modern_styles()
    
    def get_dependencies(self) -> list:
        """Dependencias requeridas para ReportLab avanzado"""
        return ['reportlab']
    
    def validate_dependencies(self) -> bool:
        """Valida que ReportLab esté disponible"""
        if REPORTLAB_AVAILABLE:
            print(f"✅ ReportLab disponible")
            return True
        else:
            print(f"❌ ReportLab no disponible")
            print(f"💡 Instala: pip install reportlab")
            return False
    
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
            fontName='Helvetica'
        ))
        
        # Estilo de habilidades
        self.styles.add(ParagraphStyle(
            name='SkillTag',
            parent=self.styles['Normal'],
            fontSize=10,
            textColor=self.colors['primary'],
            fontName='Helvetica-Bold'
        ))
    
    def create_header(self, data: Dict[str, Any], config: GeneratorConfig) -> list:
        """Crea el header moderno del CV"""
        elements = []
        
        personal_info = data.get('personal_info', {})
        
        # Nombre principal
        name = personal_info.get('name', 'Arturo Veras González')
        elements.append(Paragraph(name, self.styles['ModernName']))
        
        # Título profesional personalizado
        title = f"{config.position} • Especialista en IoT • Desarrollador Full Stack"
        elements.append(Paragraph(title, self.styles['ProfessionalTitle']))
        
        # Información de contacto en tabla
        contact_data = [
            [
                personal_info.get('email', 'arturo@example.com'),
                personal_info.get('phone', '+56 9 8765 4321'),
                personal_info.get('linkedin', 'linkedin.com/in/arturo-veras'),
                personal_info.get('location', 'Santiago, Chile')
            ]
        ]
        
        contact_table = Table(contact_data, colWidths=[4.5*cm, 3.5*cm, 5*cm, 3.5*cm])
        contact_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('TEXTCOLOR', (0, 0), (-1, -1), self.colors['medium']),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ]))
        
        elements.append(contact_table)
        elements.append(Spacer(1, 8))
        
        return elements
    
    def create_experience_section(self, data: Dict[str, Any], config: GeneratorConfig) -> list:
        """Crea sección de experiencia profesional"""
        elements = []
        
        elements.append(Paragraph("EXPERIENCIA PROFESIONAL", self.styles['ModernSection']))
        
        experiences = data.get('experience', [])
        
        for exp in experiences:
            # Crear bloque de experiencia
            exp_elements = []
            
            # Empresa y posición
            company = exp.get('company', '')
            position = exp.get('position', '')
            period = exp.get('period', '')
            
            exp_elements.append(Paragraph(company, self.styles['CompanyName']))
            exp_elements.append(Paragraph(position, self.styles['PositionTitle']))
            exp_elements.append(Paragraph(period, self.styles['Period']))
            
            # Logros
            description = exp.get('description', '')
            if description:
                exp_elements.append(Paragraph(description, self.styles['Achievement']))
            
            # Logros adicionales si existen
            achievements = exp.get('achievements', [])
            for achievement in achievements:
                bullet_text = f"• {achievement}"
                exp_elements.append(Paragraph(bullet_text, self.styles['Achievement']))
            
            # Mantener juntos los elementos de experiencia
            elements.append(KeepTogether(exp_elements))
            elements.append(Spacer(1, 8))
        
        return elements
    
    def create_skills_section(self, data: Dict[str, Any], config: GeneratorConfig) -> list:
        """Crea sección de habilidades técnicas moderna"""
        elements = []
        
        elements.append(Paragraph("HABILIDADES TÉCNICAS", self.styles['ModernSection']))
        
        skills_data = data.get('skills', [])
        
        for skill_category in skills_data:
            category = skill_category.get('category', '')
            skills = skill_category.get('skills', [])
            
            if skills:
                # Título de categoría
                elements.append(Paragraph(f"<b>{category}:</b>", self.styles['Normal']))
                
                # Skills como tags
                skills_text = " • ".join(skills)
                elements.append(Paragraph(skills_text, self.styles['SkillTag']))
                elements.append(Spacer(1, 6))
        
        return elements
    
    def create_education_section(self, data: Dict[str, Any]) -> list:
        """Crea sección de educación"""
        elements = []
        
        elements.append(Paragraph("EDUCACIÓN", self.styles['ModernSection']))
        
        education = data.get('education', [])
        
        for edu in education:
            edu_elements = []
            
            degree = edu.get('degree', '')
            institution = edu.get('institution', '')
            period = edu.get('period', '')
            details = edu.get('details', '')
            
            edu_elements.append(Paragraph(degree, self.styles['CompanyName']))
            edu_elements.append(Paragraph(institution, self.styles['PositionTitle']))
            edu_elements.append(Paragraph(period, self.styles['Period']))
            
            if details:
                edu_elements.append(Paragraph(details, self.styles['Achievement']))
            
            elements.append(KeepTogether(edu_elements))
            elements.append(Spacer(1, 8))
        
        return elements
    
    def create_summary_section(self, data: Dict[str, Any], config: GeneratorConfig) -> list:
        """Crea sección de resumen profesional personalizado"""
        elements = []
        
        elements.append(Paragraph("PERFIL PROFESIONAL", self.styles['ModernSection']))
        
        # Resumen personalizado según empresa
        summary = self.generate_personalized_summary(config)
        elements.append(Paragraph(summary, self.styles['Normal']))
        elements.append(Spacer(1, 12))
        
        return elements
    
    def generate_personalized_summary(self, config: GeneratorConfig) -> str:
        """Genera resumen personalizado según la empresa objetivo"""
        company_lower = config.company.lower()
        
        base = "Ingeniero Civil Electrónico con 9+ años de experiencia desarrollando soluciones end-to-end"
        
        if "google" in company_lower:
            return f"{base}, especializado en sistemas escalables y tecnologías cloud-native. Experto en arquitecturas distribuidas que procesan millones de transacciones, con experiencia en machine learning aplicado y contribuciones open source."
        
        elif "microsoft" in company_lower:
            return f"{base}, especializado en ecosistema Microsoft y Azure. Experto en soluciones enterprise con integración cloud nativa, accessibility y productividad."
        
        elif "tesla" in company_lower:
            return f"{base}, especializado en sistemas de tiempo real y safety-critical. Experto en automotive protocols, sistemas autónomos y desarrollo rápido de productos."
        
        elif "globant" in company_lower:
            return f"{base}, especializado en IoT edge y sistemas embebidos. Experto en microcontroladores, RTOS y arquitecturas distribuidas para transformación digital."
        
        else:
            return f"{base}, con enfoque en {config.position.lower()} y tecnologías innovadoras. Experto en desarrollo de soluciones robustas y escalables."
    
    def generate_cv(self, config: GeneratorConfig) -> Optional[Path]:
        """Genera CV avanzado en PDF usando ReportLab"""
        try:
            # Validar dependencias
            if not self.validate_dependencies():
                return None
            
            # Crear directorio de salida
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            output_dir_name = f"cv_reportlab_advanced_{config.company.lower().replace(' ', '_')}_{timestamp}"
            output_path = self.output_dir / output_dir_name
            output_path.mkdir(parents=True, exist_ok=True)
            
            pdf_file = output_path / f"cv_{config.company.lower().replace(' ', '_')}_advanced.pdf"
            
            print(f"📄 Generando CV avanzado ReportLab para {config.company}")
            
            # Obtener datos
            data_parser = DataParser()
            data = data_parser.parse_anexos_md()
            
            # Crear documento PDF
            doc = SimpleDocTemplate(
                str(pdf_file),
                pagesize=A4,
                rightMargin=2*cm,
                leftMargin=2*cm,
                topMargin=1.5*cm,
                bottomMargin=1.5*cm
            )
            
            # Construir elementos del documento
            elements = []
            
            # Header
            elements.extend(self.create_header(data, config))
            
            # Resumen personalizado
            elements.extend(self.create_summary_section(data, config))
            
            # Experiencia
            elements.extend(self.create_experience_section(data, config))
            
            # Habilidades
            elements.extend(self.create_skills_section(data, config))
            
            # Educación
            elements.extend(self.create_education_section(data))
            
            # Construir PDF
            doc.build(elements)
            
            print(f"✅ CV avanzado ReportLab generado: {pdf_file}")
            
            # Abrir en macOS
            if sys.platform == "darwin":
                import subprocess
                subprocess.run(["open", str(pdf_file)])
            
            return pdf_file
            
        except Exception as e:
            print(f"❌ Error generando CV avanzado ReportLab: {e}")
            return None


# Registro del generador
if __name__ == "__main__":
    from core.generator_base import generator_registry
    
    generator = AdvancedReportLabGenerator()
    generator_registry.register(generator)
    
    # Test básico
    config = GeneratorConfig(
        company="Google",
        position="Senior Software Engineer",
        template_name="modern"
    )
    
    result = generator.generate_cv(config)
    if result:
        print(f"✅ Test exitoso: {result}")
    else:
        print("❌ Test fallido")