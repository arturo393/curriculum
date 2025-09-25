#!/usr/bin/env python3
"""
Color System - CV Suite 2025
Sistema centralizado de colores inteligente basado en psicología del color
Autor: Arturo Veras González
"""

from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass


class ColorCategory(Enum):
    """Categorías de color basadas en psicología"""
    TECHNOLOGY = "technology"
    LEADERSHIP = "leadership"
    CREATIVE = "creative"
    FINANCE = "finance"
    HEALTHCARE = "healthcare"
    EDUCATION = "education"
    CONSULTING = "consulting"
    STARTUP = "startup"
    GENERIC = "generic"


@dataclass
class ColorScheme:
    """Esquema de colores completo"""
    primary: str          # Color principal
    secondary: str        # Color secundario
    accent: str          # Color de acento
    text: str            # Color de texto
    background: str      # Color de fondo
    category: ColorCategory
    psychology: str      # Justificación psicológica


class ColorStrategy(ABC):
    """Estrategia abstracta para asignación de colores"""
    
    @abstractmethod
    def get_color_scheme(self, company: str, position: str) -> ColorScheme:
        """Obtiene esquema de colores para empresa y posición"""
        pass


class PsychologyColorStrategy(ColorStrategy):
    """Estrategia basada en psicología del color y tipo de empresa/rol"""
    
    def __init__(self):
        self._color_schemes = self._initialize_color_schemes()
        self._company_keywords = self._initialize_company_keywords()
        self._position_keywords = self._initialize_position_keywords()
    
    def get_color_scheme(self, company: str, position: str) -> ColorScheme:
        """
        Determina el esquema de colores basado en empresa y posición
        
        Args:
            company: Nombre de la empresa
            position: Título de la posición
            
        Returns:
            ColorScheme: Esquema de colores optimizado
        """
        category = self._determine_category(company, position)
        return self._color_schemes[category]
    
    def _determine_category(self, company: str, position: str) -> ColorCategory:
        """Determina la categoría basada en keywords de empresa y posición"""
        company_lower = company.lower()
        position_lower = position.lower()
        
        # Prioridad 1: Hardware/Embedded (Azul - Confianza técnica)
        hardware_keywords = ['intel', 'amd', 'nvidia', 'qualcomm', 'broadcom', 'arm']
        embedded_keywords = ['embedded', 'firmware', 'hardware', 'iot', 'microcontroller']
        
        if (any(keyword in company_lower for keyword in hardware_keywords) or
            any(keyword in position_lower for keyword in embedded_keywords)):
            return ColorCategory.TECHNOLOGY
        
        # Prioridad 2: Leadership (Púrpura - Autoridad y liderazgo)
        leadership_keywords = ['manager', 'director', 'lead', 'head', 'chief', 'vp', 'cto', 'ceo']
        
        if any(keyword in position_lower for keyword in leadership_keywords):
            return ColorCategory.LEADERSHIP
        
        # Prioridad 3: Software/Tech Modernas (Verde - Crecimiento)
        software_companies = ['google', 'microsoft', 'apple', 'meta', 'spotify', 'uber', 'airbnb']
        software_keywords = ['software', 'developer', 'engineer', 'programmer', 'fullstack', 'backend', 'frontend']
        
        if (any(keyword in company_lower for keyword in software_companies) or
            any(keyword in position_lower for keyword in software_keywords)):
            return ColorCategory.TECHNOLOGY
        
        # Prioridad 4: Startups (Naranja - Innovación)
        startup_keywords = ['startup', 'founder', 'entrepreneur']
        startup_companies = ['y combinator', 'techstars', 'accelerator']
        
        if (any(keyword in position_lower for keyword in startup_keywords) or
            any(keyword in company_lower for keyword in startup_companies)):
            return ColorCategory.STARTUP
        
        # Prioridad 5: Creative (Rosa/Magenta - Creatividad)
        creative_keywords = ['design', 'creative', 'ui', 'ux', 'designer', 'artist']
        creative_companies = ['adobe', 'figma', 'canva', 'dribbble']
        
        if (any(keyword in position_lower for keyword in creative_keywords) or
            any(keyword in company_lower for keyword in creative_companies)):
            return ColorCategory.CREATIVE
        
        # Prioridad 6: Finance (Azul oscuro - Estabilidad)
        finance_keywords = ['finance', 'banking', 'investment', 'analyst', 'accountant']
        finance_companies = ['goldman sachs', 'jp morgan', 'blackrock', 'vanguard']
        
        if (any(keyword in position_lower for keyword in finance_keywords) or
            any(keyword in company_lower for keyword in finance_companies)):
            return ColorCategory.FINANCE
        
        # Prioridad 7: Healthcare (Verde médico - Salud)
        healthcare_keywords = ['health', 'medical', 'doctor', 'nurse', 'pharma']
        healthcare_companies = ['pfizer', 'johnson', 'medtronic']
        
        if (any(keyword in position_lower for keyword in healthcare_keywords) or
            any(keyword in company_lower for keyword in healthcare_companies)):
            return ColorCategory.HEALTHCARE
        
        # Prioridad 8: Education (Azul académico - Conocimiento)
        education_keywords = ['teacher', 'professor', 'education', 'academic', 'university']
        education_companies = ['coursera', 'udemy', 'khan academy']
        
        if (any(keyword in position_lower for keyword in education_keywords) or
            any(keyword in company_lower for keyword in education_companies)):
            return ColorCategory.EDUCATION
        
        # Prioridad 9: Consulting (Gris profesional - Neutralidad)
        consulting_keywords = ['consultant', 'advisory', 'strategy']
        consulting_companies = ['mckinsey', 'bain', 'bcg', 'deloitte', 'pwc']
        
        if (any(keyword in position_lower for keyword in consulting_keywords) or
            any(keyword in company_lower for keyword in consulting_companies)):
            return ColorCategory.CONSULTING
        
        # Por defecto: Generic
        return ColorCategory.GENERIC
    
    def _initialize_color_schemes(self) -> Dict[ColorCategory, ColorScheme]:
        """Inicializa los esquemas de colores por categoría"""
        return {
            ColorCategory.TECHNOLOGY: ColorScheme(
                primary="#2563eb",      # Azul tecnológico
                secondary="#1e40af",    # Azul más oscuro
                accent="#3b82f6",       # Azul acento
                text="#1f2937",         # Gris oscuro
                background="#f8fafc",   # Gris muy claro
                category=ColorCategory.TECHNOLOGY,
                psychology="Azul transmite confianza, profesionalismo y estabilidad técnica. Ideal para roles tecnológicos."
            ),
            
            ColorCategory.LEADERSHIP: ColorScheme(
                primary="#7c3aed",      # Púrpura
                secondary="#5b21b6",    # Púrpura oscuro
                accent="#8b5cf6",       # Púrpura acento
                text="#374151",         # Gris
                background="#faf9fc",   # Blanco con tinte púrpura
                category=ColorCategory.LEADERSHIP,
                psychology="Púrpura representa autoridad, liderazgo y toma de decisiones estratégicas."
            ),
            
            ColorCategory.CREATIVE: ColorScheme(
                primary="#ec4899",      # Rosa/Magenta
                secondary="#be185d",    # Rosa oscuro
                accent="#f472b6",       # Rosa acento
                text="#1f2937",         # Gris oscuro
                background="#fdf2f8",   # Rosa muy claro
                category=ColorCategory.CREATIVE,
                psychology="Rosa/Magenta estimula la creatividad, innovación y pensamiento fuera de la caja."
            ),
            
            ColorCategory.FINANCE: ColorScheme(
                primary="#1e40af",      # Azul financiero
                secondary="#1e3a8a",    # Azul navy
                accent="#3b82f6",       # Azul acento
                text="#1f2937",         # Gris oscuro
                background="#f1f5f9",   # Azul muy claro
                category=ColorCategory.FINANCE,
                psychology="Azul oscuro transmite estabilidad, confianza y profesionalismo financiero."
            ),
            
            ColorCategory.HEALTHCARE: ColorScheme(
                primary="#059669",      # Verde médico
                secondary="#047857",    # Verde oscuro
                accent="#10b981",       # Verde acento
                text="#1f2937",         # Gris oscuro
                background="#f0fdf4",   # Verde muy claro
                category=ColorCategory.HEALTHCARE,
                psychology="Verde representa salud, crecimiento y bienestar. Asociado con medicina y cuidado."
            ),
            
            ColorCategory.EDUCATION: ColorScheme(
                primary="#1d4ed8",      # Azul académico
                secondary="#1e3a8a",    # Azul profundo
                accent="#3b82f6",       # Azul acento
                text="#1f2937",         # Gris oscuro
                background="#eff6ff",   # Azul muy claro
                category=ColorCategory.EDUCATION,
                psychology="Azul académico transmite conocimiento, sabiduría y confiabilidad educativa."
            ),
            
            ColorCategory.CONSULTING: ColorScheme(
                primary="#374151",      # Gris profesional
                secondary="#1f2937",    # Gris oscuro
                accent="#6b7280",       # Gris medio
                text="#111827",         # Negro suave
                background="#f9fafb",   # Gris muy claro
                category=ColorCategory.CONSULTING,
                psychology="Gris representa neutralidad, profesionalismo y objetividad consultiva."
            ),
            
            ColorCategory.STARTUP: ColorScheme(
                primary="#ea580c",      # Naranja innovación
                secondary="#c2410c",    # Naranja oscuro
                accent="#fb923c",       # Naranja acento
                text="#1f2937",         # Gris oscuro
                background="#fff7ed",   # Naranja muy claro
                category=ColorCategory.STARTUP,
                psychology="Naranja estimula innovación, energía y espíritu emprendedor."
            ),
            
            ColorCategory.GENERIC: ColorScheme(
                primary="#4f46e5",      # Índigo equilibrado
                secondary="#3730a3",    # Índigo oscuro
                accent="#6366f1",       # Índigo acento
                text="#1f2937",         # Gris oscuro
                background="#f8fafc",   # Gris muy claro
                category=ColorCategory.GENERIC,
                psychology="Índigo balanceado transmite profesionalismo versátil y adaptabilidad."
            )
        }
    
    def _initialize_company_keywords(self) -> Dict[str, ColorCategory]:
        """Keywords específicas de empresas conocidas"""
        return {
            # Tecnología Hardware
            'intel': ColorCategory.TECHNOLOGY,
            'amd': ColorCategory.TECHNOLOGY,
            'nvidia': ColorCategory.TECHNOLOGY,
            'qualcomm': ColorCategory.TECHNOLOGY,
            'broadcom': ColorCategory.TECHNOLOGY,
            'arm': ColorCategory.TECHNOLOGY,
            
            # Tecnología Software
            'google': ColorCategory.TECHNOLOGY,
            'microsoft': ColorCategory.TECHNOLOGY,
            'apple': ColorCategory.TECHNOLOGY,
            'meta': ColorCategory.TECHNOLOGY,
            'facebook': ColorCategory.TECHNOLOGY,
            'spotify': ColorCategory.TECHNOLOGY,
            'uber': ColorCategory.TECHNOLOGY,
            'airbnb': ColorCategory.TECHNOLOGY,
            'netflix': ColorCategory.TECHNOLOGY,
            
            # Finanzas
            'goldman sachs': ColorCategory.FINANCE,
            'jp morgan': ColorCategory.FINANCE,
            'blackrock': ColorCategory.FINANCE,
            'vanguard': ColorCategory.FINANCE,
            'morgan stanley': ColorCategory.FINANCE,
            
            # Consulting
            'mckinsey': ColorCategory.CONSULTING,
            'bain': ColorCategory.CONSULTING,
            'bcg': ColorCategory.CONSULTING,
            'deloitte': ColorCategory.CONSULTING,
            'pwc': ColorCategory.CONSULTING,
            'accenture': ColorCategory.CONSULTING,
            
            # Creative
            'adobe': ColorCategory.CREATIVE,
            'figma': ColorCategory.CREATIVE,
            'canva': ColorCategory.CREATIVE,
            'dribbble': ColorCategory.CREATIVE,
            
            # Healthcare
            'pfizer': ColorCategory.HEALTHCARE,
            'johnson & johnson': ColorCategory.HEALTHCARE,
            'medtronic': ColorCategory.HEALTHCARE,
            
            # Education
            'coursera': ColorCategory.EDUCATION,
            'udemy': ColorCategory.EDUCATION,
            'khan academy': ColorCategory.EDUCATION,
        }
    
    def _initialize_position_keywords(self) -> Dict[str, ColorCategory]:
        """Keywords específicas de posiciones"""
        return {
            # Leadership
            'manager': ColorCategory.LEADERSHIP,
            'director': ColorCategory.LEADERSHIP,
            'lead': ColorCategory.LEADERSHIP,
            'head': ColorCategory.LEADERSHIP,
            'chief': ColorCategory.LEADERSHIP,
            'vp': ColorCategory.LEADERSHIP,
            'cto': ColorCategory.LEADERSHIP,
            'ceo': ColorCategory.LEADERSHIP,
            'president': ColorCategory.LEADERSHIP,
            
            # Technology
            'engineer': ColorCategory.TECHNOLOGY,
            'developer': ColorCategory.TECHNOLOGY,
            'programmer': ColorCategory.TECHNOLOGY,
            'architect': ColorCategory.TECHNOLOGY,
            'embedded': ColorCategory.TECHNOLOGY,
            'firmware': ColorCategory.TECHNOLOGY,
            'hardware': ColorCategory.TECHNOLOGY,
            'software': ColorCategory.TECHNOLOGY,
            'fullstack': ColorCategory.TECHNOLOGY,
            'backend': ColorCategory.TECHNOLOGY,
            'frontend': ColorCategory.TECHNOLOGY,
            'devops': ColorCategory.TECHNOLOGY,
            'sre': ColorCategory.TECHNOLOGY,
            
            # Creative
            'designer': ColorCategory.CREATIVE,
            'creative': ColorCategory.CREATIVE,
            'ui designer': ColorCategory.CREATIVE,
            'ux designer': ColorCategory.CREATIVE,
            'artist': ColorCategory.CREATIVE,
            
            # Finance
            'analyst': ColorCategory.FINANCE,
            'accountant': ColorCategory.FINANCE,
            'finance': ColorCategory.FINANCE,
            'banking': ColorCategory.FINANCE,
            'investment': ColorCategory.FINANCE,
            
            # Healthcare
            'doctor': ColorCategory.HEALTHCARE,
            'nurse': ColorCategory.HEALTHCARE,
            'medical': ColorCategory.HEALTHCARE,
            'health': ColorCategory.HEALTHCARE,
            
            # Education
            'teacher': ColorCategory.EDUCATION,
            'professor': ColorCategory.EDUCATION,
            'instructor': ColorCategory.EDUCATION,
            'academic': ColorCategory.EDUCATION,
            
            # Consulting
            'consultant': ColorCategory.CONSULTING,
            'advisor': ColorCategory.CONSULTING,
            'strategy': ColorCategory.CONSULTING,
            
            # Startup
            'founder': ColorCategory.STARTUP,
            'entrepreneur': ColorCategory.STARTUP,
            'startup': ColorCategory.STARTUP,
        }


class SimpleColorStrategy(ColorStrategy):
    """Estrategia simple con colores fijos por empresa"""
    
    def __init__(self):
        self._simple_schemes = {
            'intel': ColorScheme(
                primary="#0071c5", secondary="#005a9f", accent="#4da6d9",
                text="#1f2937", background="#f8fafc", 
                category=ColorCategory.TECHNOLOGY,
                psychology="Azul Intel corporativo"
            ),
            'microsoft': ColorScheme(
                primary="#7c3aed", secondary="#5b21b6", accent="#8b5cf6",
                text="#374151", background="#faf9fc",
                category=ColorCategory.TECHNOLOGY,
                psychology="Púrpura Microsoft"
            ),
            'google': ColorScheme(
                primary="#4285f4", secondary="#1a73e8", accent="#669df6",
                text="#1f2937", background="#f8fafc",
                category=ColorCategory.TECHNOLOGY,
                psychology="Azul Google"
            )
        }
        
        # Fallback a estrategia psicológica
        self._fallback = PsychologyColorStrategy()
    
    def get_color_scheme(self, company: str, position: str) -> ColorScheme:
        """Obtiene esquema simple o fallback a psicológico"""
        company_key = company.lower().strip()
        
        if company_key in self._simple_schemes:
            return self._simple_schemes[company_key]
        
        return self._fallback.get_color_scheme(company, position)


class ColorSystem:
    """Sistema principal de gestión de colores"""
    
    def __init__(self, strategy: Optional[ColorStrategy] = None):
        """
        Inicializa el sistema de colores
        
        Args:
            strategy: Estrategia de colores a usar. Por defecto: PsychologyColorStrategy
        """
        self.strategy = strategy or PsychologyColorStrategy()
    
    def get_colors_for_job(self, company: str, position: str) -> ColorScheme:
        """
        Obtiene colores optimizados para empresa y posición
        
        Args:
            company: Nombre de la empresa
            position: Título de la posición
            
        Returns:
            ColorScheme: Esquema de colores completo
        """
        return self.strategy.get_color_scheme(company, position)
    
    def get_category_explanation(self, company: str, position: str) -> str:
        """Obtiene explicación psicológica de la elección de color"""
        scheme = self.get_colors_for_job(company, position)
        return f"{scheme.category.value.title()}: {scheme.psychology}"
    
    def set_strategy(self, strategy: ColorStrategy):
        """Cambia la estrategia de colores"""
        self.strategy = strategy
    
    def get_available_categories(self) -> List[ColorCategory]:
        """Obtiene todas las categorías disponibles"""
        return list(ColorCategory)
    
    def get_scheme_by_category(self, category: ColorCategory) -> ColorScheme:
        """Obtiene esquema de colores por categoría específica"""
        if isinstance(self.strategy, PsychologyColorStrategy):
            return self.strategy._color_schemes[category]
        else:
            # Fallback para otras estrategias
            temp_strategy = PsychologyColorStrategy()
            return temp_strategy._color_schemes[category]


# Funciones de conveniencia
def get_colors_for_job(company: str, position: str, strategy: str = "psychology") -> ColorScheme:
    """
    Función de conveniencia para obtener colores
    
    Args:
        company: Nombre de la empresa
        position: Título de la posición  
        strategy: Tipo de estrategia ("psychology" o "simple")
        
    Returns:
        ColorScheme: Esquema de colores
    """
    if strategy == "simple":
        color_strategy = SimpleColorStrategy()
    else:
        color_strategy = PsychologyColorStrategy()
    
    system = ColorSystem(color_strategy)
    return system.get_colors_for_job(company, position)


def predict_color_category(company: str, position: str) -> str:
    """
    Predice la categoría de color para una combinación empresa/posición
    
    Args:
        company: Nombre de la empresa
        position: Título de la posición
        
    Returns:
        str: Nombre de la categoría predicha
    """
    scheme = get_colors_for_job(company, position)
    return scheme.category.value


if __name__ == "__main__":
    # Test del sistema de colores
    test_cases = [
        ("Intel", "Embedded Systems Engineer"),
        ("Microsoft", "Senior Software Engineer"),
        ("Goldman Sachs", "Financial Analyst"),
        ("Startup XYZ", "Founder"),
        ("Adobe", "UX Designer")
    ]
    
    system = ColorSystem()
    
    print("🎨 Testing Color System")
    print("=" * 50)
    
    for company, position in test_cases:
        scheme = system.get_colors_for_job(company, position)
        print(f"\n🏢 {company} - {position}")
        print(f"   🎯 Categoría: {scheme.category.value}")
        print(f"   🎨 Color: {scheme.primary}")
        print(f"   🧠 Psicología: {scheme.psychology}")