#!/usr/bin/env python3
"""
Data Parser - CV Suite 2025
Módulo centralizado para parsing de datos personales desde anexos.md
Autor: Arturo Veras González
"""

import re
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field


@dataclass
class PersonalData:
    """Estructura de datos personales"""
    # Información básica
    name: str = ""
    email: str = ""
    phone: str = ""
    location: str = ""
    
    # URLs y redes
    linkedin: str = ""
    github: str = ""
    portfolio: str = ""
    
    # Perfil profesional
    title: str = ""
    summary: str = ""
    
    # Experiencia laboral
    experience: List[Dict[str, Any]] = field(default_factory=list)
    
    # Educación
    education: List[Dict[str, Any]] = field(default_factory=list)
    
    # Skills y competencias
    technical_skills: List[str] = field(default_factory=list)
    soft_skills: List[str] = field(default_factory=list)
    languages: List[Dict[str, str]] = field(default_factory=list)
    
    # Certificaciones y logros
    certifications: List[Dict[str, Any]] = field(default_factory=list)
    projects: List[Dict[str, Any]] = field(default_factory=list)


class DataParser:
    """Parser centralizado para datos de anexos.md"""
    
    def __init__(self, data_file: Optional[Path] = None):
        """
        Inicializa el parser
        
        Args:
            data_file: Ruta al archivo anexos.md. Si es None, busca en directorio padre.
        """
        if data_file is None:
            # Buscar anexos.md en directorio padre del script
            current_dir = Path(__file__).parent
            data_file = current_dir.parent.parent / "anexos.md"
        
        self.data_file = data_file
        self._raw_content = ""
        
    def load_data(self) -> PersonalData:
        """
        Carga y parsea los datos desde anexos.md
        
        Returns:
            PersonalData: Estructura con todos los datos parseados
        """
        if not self.data_file.exists():
            print(f"⚠️  Archivo {self.data_file} no encontrado. Usando datos por defecto.")
            return self._get_default_data()
        
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                self._raw_content = f.read()
            
            return self._parse_content()
            
        except Exception as e:
            print(f"❌ Error leyendo {self.data_file}: {e}")
            return self._get_default_data()
    
    def _parse_content(self) -> PersonalData:
        """Parsea el contenido de anexos.md"""
        data = PersonalData()
        
        # Información básica
        data.name = self._extract_name()
        data.email = self._extract_email()
        data.phone = self._extract_phone()
        data.location = self._extract_location()
        
        # URLs y redes
        data.linkedin = self._extract_linkedin()
        data.github = self._extract_github()
        data.portfolio = self._extract_portfolio()
        
        # Perfil profesional
        data.title = self._extract_title()
        data.summary = self._extract_summary()
        
        # Experiencia
        data.experience = self._extract_experience()
        
        # Educación
        data.education = self._extract_education()
        
        # Skills
        data.technical_skills = self._extract_technical_skills()
        data.soft_skills = self._extract_soft_skills()
        data.languages = self._extract_languages()
        
        # Certificaciones y proyectos
        data.certifications = self._extract_certifications()
        data.projects = self._extract_projects()
        
        return data
    
    def _extract_name(self) -> str:
        """Extrae el nombre completo"""
        patterns = [
            r'# Arturo Veras ([\w\s]+)',
            r'Nombre:\s*([^\n]+)',
            r'# ([A-Z][\w\s]+ [A-Z][\w\s]+)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, self._raw_content, re.IGNORECASE)
            if match:
                return match.group(1).strip()
        
        return "Arturo Veras Olivos"
    
    def _extract_email(self) -> str:
        """Extrae el email"""
        pattern = r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})'
        match = re.search(pattern, self._raw_content)
        return match.group(1) if match else "a.veras@gmail.com"
    
    def _extract_phone(self) -> str:
        """Extrae el teléfono"""
        patterns = [
            r'\+56\s*9\s*\d{8}',
            r'\+56\s*\d{9}',
            r'(\+56\s*9\s*82413883)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, self._raw_content)
            if match:
                return match.group(0).replace(' ', ' ')
        
        return "+56 9 82413883"
    
    def _extract_location(self) -> str:
        """Extrae la ubicación"""
        patterns = [
            r'Ubicación:\s*([^\n]+)',
            r'Location:\s*([^\n]+)',
            r'(Santiago[^\n]*Chile)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, self._raw_content, re.IGNORECASE)
            if match:
                return match.group(1).strip()
        
        return "Santiago, Chile"
    
    def _extract_linkedin(self) -> str:
        """Extrae URL de LinkedIn"""
        pattern = r'linkedin\.com/in/([^\s\)]+)'
        match = re.search(pattern, self._raw_content)
        if match:
            return f"https://linkedin.com/in/{match.group(1)}"
        return "https://linkedin.com/in/arturoveras"
    
    def _extract_github(self) -> str:
        """Extrae URL de GitHub"""
        pattern = r'github\.com/([^\s\)]+)'
        match = re.search(pattern, self._raw_content)
        if match:
            return f"https://github.com/{match.group(1)}"
        return "https://github.com/arturo393"
    
    def _extract_portfolio(self) -> str:
        """Extrae URL del portfolio"""
        patterns = [
            r'Portfolio:\s*(https?://[^\s]+)',
            r'Website:\s*(https?://[^\s]+)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, self._raw_content, re.IGNORECASE)
            if match:
                return match.group(1)
        
        return "https://portfolio.arturoveras.dev"
    
    def _extract_title(self) -> str:
        """Extrae el título profesional principal"""
        patterns = [
            r'Título:\s*([^\n]+)',
            r'Ingeniero\s+([^\n]+)',
            r'(Senior\s+[^\n]+Engineer)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, self._raw_content, re.IGNORECASE)
            if match:
                return match.group(1).strip()
        
        return "Senior Software Engineer"
    
    def _extract_summary(self) -> str:
        """Extrae el resumen profesional"""
        patterns = [
            r'## Resumen\n([^#]+)',
            r'## Summary\n([^#]+)',
            r'Resumen:\s*([^\n]{50,})',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, self._raw_content, re.IGNORECASE | re.DOTALL)
            if match:
                return match.group(1).strip()
        
        return "Ingeniero de Software con experiencia en desarrollo de sistemas embebidos, IoT y arquitecturas distribuidas."
    
    def _extract_experience(self) -> List[Dict[str, Any]]:
        """Extrae experiencia laboral"""
        experience = []
        
        # Patrones para diferentes formatos de experiencia
        patterns = [
            r'### ([^#\n]+)\n.*?Empresa:\s*([^\n]+)\n.*?Período:\s*([^\n]+)\n.*?Responsabilidades:\s*\n((?:\*[^\n]+\n?)*)',
            r'#### ([^#\n]+) - ([^#\n]+)\n.*?\*\*Período:\*\*\s*([^\n]+)\n((?:\*[^\n]+\n?)*)',
        ]
        
        for pattern in patterns:
            matches = re.finditer(pattern, self._raw_content, re.IGNORECASE | re.DOTALL)
            for match in matches:
                position = match.group(1).strip()
                company = match.group(2).strip()
                period = match.group(3).strip()
                responsibilities_text = match.group(4).strip()
                
                # Extraer responsabilidades individuales
                responsibilities = [
                    resp.strip('* ').strip()
                    for resp in responsibilities_text.split('\n')
                    if resp.strip().startswith('*')
                ]
                
                experience.append({
                    'position': position,
                    'company': company,
                    'period': period,
                    'responsibilities': responsibilities
                })
        
        # Datos por defecto si no se encuentra nada
        if not experience:
            experience = [
                {
                    'position': 'Ingeniero de Software Senior',
                    'company': 'UQOMM',
                    'period': '2020 - Presente',
                    'responsibilities': [
                        'Desarrollo de sistemas IoT y embebidos',
                        'Arquitectura de microservicios',
                        'Liderazgo técnico de equipo'
                    ]
                },
                {
                    'position': 'Desarrollador Full Stack',
                    'company': 'BlackGPS',
                    'period': '2018 - 2020',
                    'responsibilities': [
                        'Desarrollo de aplicaciones web',
                        'Integración de sistemas GPS',
                        'Optimización de performance'
                    ]
                }
            ]
        
        return experience
    
    def _extract_education(self) -> List[Dict[str, Any]]:
        """Extrae información educativa"""
        education = []
        
        patterns = [
            r'### ([^#\n]+)\n.*?Institución:\s*([^\n]+)\n.*?Año:\s*([^\n]+)',
            r'#### ([^#\n]+) - ([^#\n]+)\n.*?Año:\s*([^\n]+)',
        ]
        
        for pattern in patterns:
            matches = re.finditer(pattern, self._raw_content, re.IGNORECASE | re.DOTALL)
            for match in matches:
                degree = match.group(1).strip()
                institution = match.group(2).strip()
                year = match.group(3).strip()
                
                education.append({
                    'degree': degree,
                    'institution': institution,
                    'year': year
                })
        
        # Datos por defecto
        if not education:
            education = [
                {
                    'degree': 'Ingeniero Civil Electrónico',
                    'institution': 'Universidad Técnica Federico Santa María',
                    'year': '2017'
                }
            ]
        
        return education
    
    def _extract_technical_skills(self) -> List[str]:
        """Extrae skills técnicas"""
        skills_section = re.search(r'## Skills Técnicas?\n(.*?)(?=##|$)', self._raw_content, re.IGNORECASE | re.DOTALL)
        
        if skills_section:
            skills_text = skills_section.group(1)
            skills = [
                skill.strip('* -').strip()
                for skill in skills_text.split('\n')
                if skill.strip() and ('*' in skill or '-' in skill)
            ]
            return skills
        
        # Skills por defecto
        return [
            'Python', 'JavaScript', 'C/C++', 'React', 'Node.js',
            'Docker', 'Kubernetes', 'AWS', 'PostgreSQL', 'MongoDB'
        ]
    
    def _extract_soft_skills(self) -> List[str]:
        """Extrae soft skills"""
        skills_section = re.search(r'## Soft Skills?\n(.*?)(?=##|$)', self._raw_content, re.IGNORECASE | re.DOTALL)
        
        if skills_section:
            skills_text = skills_section.group(1)
            skills = [
                skill.strip('* -').strip()
                for skill in skills_text.split('\n')
                if skill.strip() and ('*' in skill or '-' in skill)
            ]
            return skills
        
        return ['Liderazgo', 'Comunicación', 'Trabajo en equipo', 'Resolución de problemas']
    
    def _extract_languages(self) -> List[Dict[str, str]]:
        """Extrae idiomas"""
        languages_section = re.search(r'## Idiomas?\n(.*?)(?=##|$)', self._raw_content, re.IGNORECASE | re.DOTALL)
        
        languages = []
        if languages_section:
            languages_text = languages_section.group(1)
            # Buscar patrones como "Español - Nativo" o "English - Advanced"
            pattern = r'[\*\-]\s*([^:\-\n]+)[\:\-]\s*([^\n]+)'
            matches = re.finditer(pattern, languages_text)
            
            for match in matches:
                language = match.group(1).strip()
                level = match.group(2).strip()
                languages.append({'language': language, 'level': level})
        
        # Por defecto
        if not languages:
            languages = [
                {'language': 'Español', 'level': 'Nativo'},
                {'language': 'Inglés', 'level': 'Avanzado'}
            ]
        
        return languages
    
    def _extract_certifications(self) -> List[Dict[str, Any]]:
        """Extrae certificaciones"""
        cert_section = re.search(r'## Certificaciones?\n(.*?)(?=##|$)', self._raw_content, re.IGNORECASE | re.DOTALL)
        
        certifications = []
        if cert_section:
            cert_text = cert_section.group(1)
            # Buscar certificaciones
            lines = [line.strip('* -').strip() for line in cert_text.split('\n') if line.strip()]
            
            for line in lines:
                if line and not line.startswith('#'):
                    # Intentar separar nombre y emisor
                    if ' - ' in line:
                        name, issuer = line.split(' - ', 1)
                        certifications.append({'name': name.strip(), 'issuer': issuer.strip()})
                    else:
                        certifications.append({'name': line, 'issuer': ''})
        
        # Por defecto
        if not certifications:
            certifications = [
                {'name': 'HoruS Management Strategy', 'issuer': 'HoruS'},
                {'name': 'Desarrollo Ágil con Scrum + Kanban', 'issuer': 'Coursera'}
            ]
        
        return certifications
    
    def _extract_projects(self) -> List[Dict[str, Any]]:
        """Extrae proyectos destacados"""
        projects_section = re.search(r'## Proyectos?\n(.*?)(?=##|$)', self._raw_content, re.IGNORECASE | re.DOTALL)
        
        projects = []
        if projects_section:
            projects_text = projects_section.group(1)
            # Buscar proyectos con formato ### Nombre
            project_matches = re.finditer(r'### ([^#\n]+)\n(.*?)(?=###|$)', projects_text, re.DOTALL)
            
            for match in project_matches:
                name = match.group(1).strip()
                description = match.group(2).strip()
                
                projects.append({
                    'name': name,
                    'description': description[:200] + '...' if len(description) > 200 else description
                })
        
        return projects
    
    def _get_default_data(self) -> PersonalData:
        """Retorna datos por defecto cuando no se puede parsear anexos.md"""
        return PersonalData(
            name="Arturo Veras Olivos",
            email="a.veras@gmail.com",
            phone="+56 9 82413883",
            location="Santiago, Chile",
            linkedin="https://linkedin.com/in/arturoveras",
            github="https://github.com/arturo393",
            portfolio="https://portfolio.arturoveras.dev",
            title="Senior Software Engineer",
            summary="Ingeniero de Software con experiencia en desarrollo de sistemas embebidos, IoT y arquitecturas distribuidas.",
            experience=[
                {
                    'position': 'Ingeniero de Software Senior',
                    'company': 'UQOMM',
                    'period': '2020 - Presente',
                    'responsibilities': [
                        'Desarrollo de sistemas IoT y embebidos',
                        'Arquitectura de microservicios',
                        'Liderazgo técnico de equipo'
                    ]
                }
            ],
            education=[
                {
                    'degree': 'Ingeniero Civil Electrónico',
                    'institution': 'Universidad Técnica Federico Santa María',
                    'year': '2017'
                }
            ],
            technical_skills=['Python', 'JavaScript', 'C/C++', 'React', 'Node.js'],
            soft_skills=['Liderazgo', 'Comunicación', 'Trabajo en equipo'],
            languages=[
                {'language': 'Español', 'level': 'Nativo'},
                {'language': 'Inglés', 'level': 'Avanzado'}
            ],
            certifications=[
                {'name': 'HoruS Management Strategy', 'issuer': 'HoruS'},
                {'name': 'Desarrollo Ágil con Scrum + Kanban', 'issuer': 'Coursera'}
            ]
        )


# Función de conveniencia para uso rápido
def load_personal_data(data_file: Optional[Path] = None) -> PersonalData:
    """
    Función de conveniencia para cargar datos personales
    
    Args:
        data_file: Ruta opcional al archivo anexos.md
        
    Returns:
        PersonalData: Datos personales parseados
    """
    parser = DataParser(data_file)
    return parser.load_data()


if __name__ == "__main__":
    # Test del parser
    data = load_personal_data()
    print(f"✅ Datos cargados para: {data.name}")
    print(f"📧 Email: {data.email}")
    print(f"🏢 Experiencia: {len(data.experience)} trabajos")
    print(f"🎓 Educación: {len(data.education)} títulos")
    print(f"💪 Skills técnicas: {len(data.technical_skills)} items")