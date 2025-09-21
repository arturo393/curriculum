#!/usr/bin/env python3
"""
Markdown Generator - CV Suite 2025
Generador simple y rápido de CVs en formato Markdown
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


class MarkdownGenerator(BaseGenerator):
    """Generador simple de CVs en formato Markdown"""
    
    def __init__(self):
        super().__init__("markdown")
    
    def generate_cv(self, config: GeneratorConfig) -> Optional[Path]:
        """
        Genera CV en formato Markdown
        
        Args:
            config: Configuración del generador
            
        Returns:
            Path: Archivo Markdown generado
        """
        if not self.validate_config(config):
            return None
        
        try:
            self.log_generation_start(config)
            
            # Crear directorio de salida
            output_dir = self.create_output_directory(config)
            
            # Obtener contexto de personalización
            context = self.get_customization_context(config)
            
            # Generar Markdown
            md_file = self._generate_markdown(context, output_dir)
            
            # Intentar generar PDF si pandoc está disponible
            pdf_file = self._generate_pdf_with_pandoc(md_file, output_dir)
            
            self.log_generation_success(output_dir)
            return md_file
            
        except Exception as e:
            self.log_generation_error(e)
            return None
    
    def _generate_markdown(self, context: Dict[str, Any], output_dir: Path) -> Path:
        """Genera el archivo Markdown"""
        personal = context['personal']
        colors = context['colors']
        
        # Construir contenido Markdown
        md_content = self._build_markdown_content(context)
        
        # Escribir archivo
        md_file = output_dir / "cv.md"
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        print(f"   📄 Markdown: {md_file.name}")
        return md_file
    
    def _build_markdown_content(self, context: Dict[str, Any]) -> str:
        """Construye el contenido completo del CV en Markdown"""
        personal = context['personal']
        company = context['company']
        position = context['position']
        colors = context['colors']
        meta = context['meta']
        
        md = []
        
        # Header principal
        md.append(f"# {personal.name}")
        md.append(f"## {position}")
        md.append(f"### {company}")
        md.append("")
        
        # Información de contacto
        md.append("---")
        md.append("")
        md.append("**Contacto:**")
        md.append(f"- 📧 **Email:** {personal.email}")
        md.append(f"- 📱 **Teléfono:** {personal.phone}")
        md.append(f"- 📍 **Ubicación:** {personal.location}")
        md.append(f"- 💼 **LinkedIn:** [{personal.linkedin}]({personal.linkedin})")
        md.append(f"- 💻 **GitHub:** [{personal.github}]({personal.github})")
        if personal.portfolio:
            md.append(f"- 🌐 **Portfolio:** [{personal.portfolio}]({personal.portfolio})")
        md.append("")
        
        # Resumen profesional
        md.append("---")
        md.append("")
        md.append("## 💡 Perfil Profesional")
        md.append("")
        md.append(personal.summary)
        md.append("")
        
        # Experiencia laboral
        md.append("## 💼 Experiencia Laboral")
        md.append("")
        
        for exp in personal.experience:
            md.append(f"### {exp['position']}")
            md.append(f"**{exp['company']}** | *{exp['period']}*")
            md.append("")
            
            if exp.get('responsibilities'):
                for resp in exp['responsibilities']:
                    md.append(f"- {resp}")
                md.append("")
        
        # Skills técnicas
        if personal.technical_skills:
            md.append("## 🛠️ Competencias Técnicas")
            md.append("")
            
            # Agrupar skills en categorías si es posible
            all_skills = personal.technical_skills
            
            # Skills en formato de badges/pills
            skill_lines = []
            for i in range(0, len(all_skills), 5):
                skill_group = all_skills[i:i+5]
                skill_badges = [f"`{skill}`" for skill in skill_group]
                skill_lines.append(" ".join(skill_badges))
            
            for line in skill_lines:
                md.append(line)
                md.append("")
        
        # Educación
        if personal.education:
            md.append("## 🎓 Educación")
            md.append("")
            
            for edu in personal.education:
                md.append(f"### {edu['degree']}")
                md.append(f"**{edu['institution']}** | *{edu['year']}*")
                md.append("")
        
        # Certificaciones
        if personal.certifications:
            md.append("## 🏆 Certificaciones")
            md.append("")
            
            for cert in personal.certifications:
                cert_text = f"- **{cert['name']}"
                if cert.get('issuer'):
                    cert_text += f"** - {cert['issuer']}"
                else:
                    cert_text += "**"
                md.append(cert_text)
            md.append("")
        
        # Idiomas
        if personal.languages:
            md.append("## 🌍 Idiomas")
            md.append("")
            
            for lang in personal.languages:
                md.append(f"- **{lang['language']}:** {lang['level']}")
            md.append("")
        
        # Proyectos destacados (si existen)
        if personal.projects:
            md.append("## 🚀 Proyectos Destacados")
            md.append("")
            
            for project in personal.projects[:3]:  # Solo primeros 3
                md.append(f"### {project['name']}")
                md.append(project['description'])
                md.append("")
        
        # Footer con información de generación
        md.append("---")
        md.append("")
        md.append("**Información de Generación:**")
        md.append(f"- 🎨 Categoría de color: {colors['category'].title()}")
        md.append(f"- 🧠 Psicología: {colors['psychology']}")
        md.append(f"- 📅 Generado: {meta['generated_at'][:10]}")
        md.append(f"- 🎯 Personalizado para: {company}")
        md.append("")
        
        return "\n".join(md)
    
    def _generate_pdf_with_pandoc(self, md_file: Path, output_dir: Path) -> Optional[Path]:
        """Intenta generar PDF usando pandoc"""
        try:
            import subprocess
            
            pdf_file = output_dir / "cv.pdf"
            
            # Comando pandoc con opciones de formato
            cmd = [
                "pandoc",
                str(md_file),
                "-o", str(pdf_file),
                "--pdf-engine=wkhtmltopdf",
                "--margin-top=20mm",
                "--margin-bottom=20mm",
                "--margin-left=20mm",
                "--margin-right=20mm",
                "--encoding=UTF-8"
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0 and pdf_file.exists():
                print(f"   📄 PDF: {pdf_file.name}")
                return pdf_file
            else:
                print(f"   ⚠️  pandoc error: {result.stderr}")
                return None
                
        except FileNotFoundError:
            print("   ⚠️  pandoc no disponible - solo Markdown generado")
            return None
        except Exception as e:
            print(f"   ⚠️  Error con pandoc: {e}")
            return None
    
    def get_supported_templates(self) -> List[str]:
        """Retorna templates soportados"""
        return ["simple", "minimal", "clean", "professional"]
    
    def validate_dependencies(self) -> bool:
        """Valida dependencias del generador Markdown"""
        # Markdown no requiere dependencias especiales
        print("   ✅ Markdown: OK (sin dependencias)")
        
        # Verificar pandoc opcional
        try:
            import subprocess
            result = subprocess.run(["pandoc", "--version"], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                print("   ✅ pandoc: OK (PDF generation available)")
            else:
                print("   ⚠️  pandoc: Available but error")
        except FileNotFoundError:
            print("   ⚠️  pandoc: Missing (Markdown only)")
        
        return True
    
    def _get_template_extension(self) -> str:
        """Extensión de templates Markdown"""
        return "md"
    
    def create_simple_template(self) -> Path:
        """Crea un template simple para edición manual"""
        template_dir = self.templates_dir / "markdown"
        template_dir.mkdir(exist_ok=True)
        
        template_file = template_dir / "simple_template.md"
        
        template_content = """# [Tu Nombre]
## [Posición Objetivo]
### [Empresa Objetivo]

---

**Contacto:**
- 📧 **Email:** [tu.email@ejemplo.com]
- 📱 **Teléfono:** [+56 9 XXXX XXXX]
- 📍 **Ubicación:** [Tu Ciudad, País]
- 💼 **LinkedIn:** [https://linkedin.com/in/tu-perfil]
- 💻 **GitHub:** [https://github.com/tu-usuario]

---

## 💡 Perfil Profesional

[Describe tu perfil profesional aquí. Incluye tu experiencia clave, especializaciones y valor que aportas.]

## 💼 Experiencia Laboral

### [Posición 1]
**[Empresa 1]** | *[Fecha Inicio] - [Fecha Fin]*

- [Responsabilidad/logro 1]
- [Responsabilidad/logro 2]
- [Responsabilidad/logro 3]

### [Posición 2]
**[Empresa 2]** | *[Fecha Inicio] - [Fecha Fin]*

- [Responsabilidad/logro 1]
- [Responsabilidad/logro 2]

## 🛠️ Competencias Técnicas

`Skill 1` `Skill 2` `Skill 3` `Skill 4` `Skill 5`

`Skill 6` `Skill 7` `Skill 8` `Skill 9` `Skill 10`

## 🎓 Educación

### [Título/Grado]
**[Institución]** | *[Año]*

## 🏆 Certificaciones

- **[Certificación 1]** - [Emisor]
- **[Certificación 2]** - [Emisor]

## 🌍 Idiomas

- **Español:** Nativo
- **Inglés:** [Nivel]

---

**Información de Generación:**
- 📅 Generado: [Fecha]
- 🎯 Personalizado para: [Empresa]
"""
        
        with open(template_file, 'w', encoding='utf-8') as f:
            f.write(template_content)
        
        print(f"✅ Template creado: {template_file}")
        return template_file


def main():
    """Función principal para uso directo del generador"""
    if len(sys.argv) < 3:
        print("💡 Uso: python markdown_generator.py 'Empresa' 'Posición' [opciones]")
        print("📝 Ejemplo: python markdown_generator.py 'Google' 'Software Engineer'")
        print("🛠️  Opciones:")
        print("   --template: Crear template simple para editar")
        return
    
    # Verificar opción de template
    if "--template" in sys.argv:
        generator = MarkdownGenerator()
        generator.create_simple_template()
        return
    
    company = sys.argv[1]
    position = sys.argv[2]
    
    # Crear configuración
    config = GeneratorConfig(
        company=company,
        position=position,
        template_name="simple"
    )
    
    # Generar CV
    generator = MarkdownGenerator()
    output_path = generator.generate_cv(config)
    
    if output_path:
        print(f"🎉 CV Markdown generado exitosamente: {output_path}")
        print()
        print("💡 Próximos pasos:")
        print("   1. Revisa el archivo Markdown generado")
        print("   2. Edita manualmente si necesitas ajustes")
        print("   3. Convierte a PDF con: pandoc cv.md -o cv_final.pdf")
    else:
        print("❌ Error generando CV Markdown")


if __name__ == "__main__":
    main()