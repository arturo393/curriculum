# 🚀 Generador CV Simple - Professional & ATS-Optimized

"""
CV Generator Simple - Una herramienta minimalista para generar CVs profesionales
Autor: Arturo Veras
Fecha: Enero 2025

Filosofía: Simplicidad > Complejidad
- Un script, una función, un resultado excelente
- Foco en ATS-optimization y profesionalismo
- Markdown → Google Docs → PDF workflow
"""

import os
import json
from datetime import datetime
from typing import Dict, List, Optional


class SimpleCVGenerator:
    """
    Generador simple de CV profesional optimizado para ATS
    
    Features:
    - Template moderno y limpio
    - Keywords relevantes para cada industria
    - Formato ATS-friendly
    - Output en Markdown listo para Google Docs
    """
    
    def __init__(self, template_type: str = "professional"):
        self.template_type = template_type
        self.current_date = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.output_dir = "output"
        self._ensure_output_dir()
    
    def _ensure_output_dir(self):
        """Crear directorio de output si no existe"""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def generate_cv(self, target_role: str = "iot-engineer", company: str = "tech-company") -> str:
        """
        Generar CV optimizado para rol específico
        
        Args:
            target_role: Tipo de rol (iot-engineer, firmware-dev, tech-lead, etc.)
            company: Tipo de empresa (tech-company, startup, consulting, etc.)
        
        Returns:
            Ruta del archivo generado
        """
        
        # Datos base (extraídos de anexos.md)
        personal_data = self._get_personal_data()
        
        # Template optimizado según rol
        cv_content = self._build_cv_template(personal_data, target_role, company)
        
        # Guardar archivo
        filename = f"cv_{target_role}_{company}_{self.current_date}.md"
        filepath = os.path.join(self.output_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(cv_content)
        
        print(f"✅ CV generado exitosamente: {filepath}")
        return filepath
    
    def _get_personal_data(self) -> Dict:
        """Datos personales base extraídos de anexos.md"""
        return {
            "name": "Arturo Veras Olivos",
            "title": "Ingeniero Civil Electrónico",
            "location": "Santiago, Chile",
            "phone": "+56 9 82413883",
            "email": "a.veras@gmail.com",
            "experience_years": "9+",
            "languages": {
                "Español": "Nativo",
                "Inglés": "B2 Upper Intermediate (técnico fluido)"
            }
        }
    
    def _build_cv_template(self, data: Dict, target_role: str, company: str) -> str:
        """Construir template profesional optimizado para ATS"""
        
        # Header profesional
        cv = f"""# {data['name']}
**{self._get_role_title(target_role)}**

📍 {data['location']} | 📞 {data['phone']} | ✉️ {data['email']}
🏆 {data['experience_years']} años de experiencia en desarrollo tecnológico

---

## 💼 PERFIL PROFESIONAL

{self._get_professional_summary(target_role)}

---

## 🛠️ COMPETENCIAS TÉCNICAS CLAVE

{self._get_key_skills(target_role)}

---

## 💼 EXPERIENCIA PROFESIONAL

{self._get_experience_section(target_role)}

---

## 🎯 PROYECTOS DESTACADOS

{self._get_featured_projects(target_role)}

---

## 🎓 EDUCACIÓN Y CERTIFICACIONES

{self._get_education_section()}

---

## 🌐 IDIOMAS

{self._get_languages_section(data['languages'])}

---

## 📊 LOGROS Y RECONOCIMIENTOS

{self._get_achievements_section()}

"""
        
        return cv
    
    def _get_role_title(self, target_role: str) -> str:
        """Título profesional optimizado según rol objetivo"""
        titles = {
            "iot-engineer": "Senior IoT Engineer & Embedded Systems Specialist",
            "firmware-dev": "Senior Firmware Developer & Embedded Systems Engineer",
            "tech-lead": "Technical Lead & Engineering Manager",
            "product-engineer": "Product Engineer & Innovation Specialist",
            "fullstack-iot": "Full-Stack IoT Developer & Systems Architect"
        }
        return titles.get(target_role, "Senior Embedded Systems Engineer")
    
    def _get_professional_summary(self, target_role: str) -> str:
        """Resumen profesional adaptado al rol objetivo"""
        
        base_summary = """Ingeniero Civil Electrónico con **9+ años de experiencia** desarrollando soluciones tecnológicas end-to-end, desde hardware embebido hasta aplicaciones empresariales. Especialista en **sistemas IoT críticos** y **firmware para microcontroladores STM32**, con experiencia comprobada en entornos industriales extremos."""
        
        role_specifics = {
            "iot-engineer": """
**Experiencia especializada en:**
• Arquitecturas IoT escalables (500K+ datos/día) con alta disponibilidad (99.9%+)
• Desarrollo firmware C/C++ para microcontroladores STM32 y comunicaciones LoRa
• Integración hardware-software con Python, MQTT, MongoDB y React
• Sistemas críticos para minería subterránea y monitoreo industrial""",
            
            "firmware-dev": """
**Expertise en desarrollo firmware:**
• Programación C/C++ para microcontroladores STM32 Cortex M0 en producción
• FreeRTOS, manejo de periféricos, interrupciones y optimización de código
• Comunicaciones embebidas: I2C, SPI, UART, LoRa, Bluetooth
• Desarrollo desde prototipo hasta producto en producción""",
            
            "tech-lead": """
**Liderazgo técnico demostrado:**
• Gestión de equipos multidisciplinarios y arquitecturas de sistemas complejos
• Planificación y coordinación de proyectos tecnológicos end-to-end
• Metodologías Agile y alineación técnico-comercial
• Experiencia en startup y scale-up con enfoque en resultados medibles""",
            
            "product-engineer": """
**Innovación y desarrollo de productos:**
• Visión 360° del ciclo de vida del producto tecnológico
• Alineación natural entre tecnología y objetivos de negocio
• Experiencia en I+D aplicada con reconocimientos (Fundación Copec UC)
• Productos en producción en múltiples industrias (minería, seguridad, energía)""",
            
            "fullstack-iot": """
**Desarrollo Full-Stack IoT:**
• Stack completo: STM32 firmware → Python backend → React frontend
• Arquitecturas distribuidas con Google Cloud, Docker y sistemas embebidos
• Instrumentación RF, MQTT, MongoDB y visualización en tiempo real
• Integración hardware-software para productos comerciales"""
        }
        
        return base_summary + "\n" + role_specifics.get(target_role, role_specifics["iot-engineer"])
    
    def _get_key_skills(self, target_role: str) -> str:
        """Competencias técnicas priorizadas según rol"""
        
        common_skills = {
            "programming": ["C/C++", "Python", "Java"],
            "embedded": ["STM32", "FreeRTOS", "ESP32", "Arduino"],
            "communications": ["LoRa", "MQTT", "Bluetooth", "TCP/IP"],
            "tools": ["Git", "Linux", "Docker", "Google Cloud"]
        }
        
        role_priorities = {
            "iot-engineer": {
                "primary": ["STM32", "Python", "LoRa", "MQTT", "React", "MongoDB"],
                "secondary": ["C/C++", "FreeRTOS", "Google Cloud", "Docker"],
                "tools": ["Git", "Linux", "Instrumentación RF"]
            },
            "firmware-dev": {
                "primary": ["C/C++", "STM32", "FreeRTOS", "I2C/SPI", "Bluetooth"],
                "secondary": ["ESP32", "Arduino", "LoRa", "UART"],
                "tools": ["Git", "IDE Embebido", "Debugging"]
            },
            "tech-lead": {
                "primary": ["Python", "Java", "Arquitectura de Sistemas", "Metodologías Agile"],
                "secondary": ["C/C++", "Docker", "Google Cloud", "MongoDB"],
                "tools": ["Git", "Project Management", "Team Leadership"]
            }
        }
        
        priority = role_priorities.get(target_role, role_priorities["iot-engineer"])
        
        return f"""### Tecnologías Principales
**{' • '.join(priority['primary'])}**

### Tecnologías Secundarias
{' • '.join(priority['secondary'])}

### Herramientas y Metodologías
{' • '.join(priority['tools'])}"""
    
    def _get_experience_section(self, target_role: str) -> str:
        """Experiencia profesional con énfasis según rol objetivo"""
        
        return """### **UQOMM SpA** | Encargado de Software y Firmware
**Septiembre 2021 - Presente (3+ años)** | Con Con, Chile
*Soluciones de comunicaciones para minería subterránea*

**Logros Clave:**
• **Sistema IoT crítico**: Desarrollé arquitectura completa para monitoreo de amplificadores en entornos mineros extremos
• **Firmware STM32**: Programación C/C++ para microcontroladores Cortex M0 con FreeRTOS y optimización de periféricos
• **Backend Python**: Sistema de captura de datos seriales, instrumentación RF y visualización en tiempo real
• **Stack tecnológico**: Python + React + MongoDB + MQTT para 500K+ datos/día con 99.9% disponibilidad
• **Administración**: Gestión de servidores Google Cloud, Linux y sistemas Odoo

### **BlackGPS** | Ingeniero de Hardware y Software
**Julio 2017 - Agosto 2021 (4+ años)** | Santiago, Chile
*Soluciones de seguridad y gestión de flotas*

**Logros Clave:**
• **Dispositivo anti-robo**: Diseño completo hardware/software con inhibidor GNSS/GSM para camiones
• **Backend Java**: Nuevas funcionalidades en SpringBoot para procesamiento GPS y CANBus
• **App Flutter**: Mejoras en aplicación móvil con comunicación Bluetooth
• **Soporte técnico**: Configuración dispositivos Teltonika, DCT Syrus, ERM Starlink

### **Proyectos de Innovación** | Fundador y Director Técnico
**2015 - 2017** | Viña del Mar, Chile

**Deuterio - Generadores de Hidrógeno:**
• **I+D aplicada**: Desarrollo de tecnología para generación eficiente de oxihidrógeno
• **Microcontroladores**: Programación de tren de pulsos y banco de pruebas automatizado
• **Reconocimiento**: Ganador concurso I+D Fundación Copec UC (2015)

**Prosismic SpA:**
• **Red de sensores**: Prototipo funcional para 80 sensores de detección temprana de sismos
• **Investigación**: Desarrollo de algoritmos de procesamiento de señales sísmicas"""
    
    def _get_featured_projects(self, target_role: str) -> str:
        """Proyectos destacados relevantes para el rol"""
        
        return """### **Sistema IoT Industrial - Minería Subterránea**
*STM32 • FreeRTOS • Python • LoRa • React*
- Arquitectura end-to-end para monitoreo crítico en entornos extremos
- **Impacto**: 500K+ puntos de datos/día, 99.9% disponibilidad
- Firmware optimizado para bajo consumo y alta confiabilidad

### **Dispositivo Anti-Robo Inteligente**
*Hardware Design • GNSS/GSM • Embedded Systems*
- Diseño completo desde concepto hasta producción
- Integración con sistemas de gestión de flotas existentes
- **Resultado**: Producto comercial en uso por empresas de logística

### **Red de Sensores Sísmicos**
*Sensor Networks • Signal Processing • IoT*
- Sistema distribuido para detección temprana de eventos sísmicos
- 80 nodos con comunicación inalámbrica y procesamiento en tiempo real
- **Innovación**: Algoritmos optimizados para reducir falsos positivos

### **Sistema de Instrumentación RF**
*Python • MQTT • Hardware Integration*
- Control automatizado de analizadores de espectro y generadores
- Mediciones precisas y visualización en tiempo real
- **Eficiencia**: Reducción 70% en tiempo de pruebas de laboratorio"""
    
    def _get_education_section(self) -> str:
        """Sección de educación y certificaciones"""
        
        return """### **Universidad Técnica Federico Santa María**
**Ingeniero Civil Electrónico** - Mención Computadores (2006-2014)
*Valparaíso, Chile*

**Memoria de Título:** "Implementación de un Generador de Rutas en un Sistema de Navegación de un Robot Móvil Cognitivo"

### **Certificaciones Relevantes**
• **Metodologías Ágiles** - HoruS Management Strategy (2022)
• **Scrum + Kanban** - eClass (2019) 
• **Diseño de Circuitos Integrados** - Synopsys, UTFSM (2017)"""
    
    def _get_languages_section(self, languages: Dict) -> str:
        """Sección de idiomas"""
        
        lang_list = []
        for lang, level in languages.items():
            lang_list.append(f"• **{lang}**: {level}")
        
        return "\n".join(lang_list)
    
    def _get_achievements_section(self) -> str:
        """Logros y reconocimientos"""
        
        return """• **Ganador I+D Aplicada** - Proyecto HH Motors, Fundación Copec UC (2015)
• **Sistemas Críticos** - 3+ años operando en minería subterránea sin fallas
• **Innovación Tecnológica** - 5+ productos desde concepto hasta producción
• **Liderazgo Técnico** - Gestión exitosa de proyectos multidisciplinarios
• **Participación EXPOTEC** - Exposición de Proyectos Tecnológicos, UTFSM (2015)"""


# =============================================================================
# CLI Interface Simple
# =============================================================================

def main():
    """Función principal con interfaz simple"""
    
    print("🚀 CV Generator Simple - Professional & ATS-Optimized")
    print("=" * 60)
    
    generator = SimpleCVGenerator()
    
    # Opciones disponibles
    roles = {
        "1": "iot-engineer",
        "2": "firmware-dev", 
        "3": "tech-lead",
        "4": "product-engineer",
        "5": "fullstack-iot"
    }
    
    companies = {
        "1": "tech-company",
        "2": "startup",
        "3": "consulting",
        "4": "automotive",
        "5": "industrial"
    }
    
    print("\n📋 Selecciona el tipo de rol objetivo:")
    for key, value in roles.items():
        print(f"  {key}. {value}")
    
    role_choice = input("\nOpción (1-5): ").strip()
    target_role = roles.get(role_choice, "iot-engineer")
    
    print("\n🏢 Selecciona el tipo de empresa:")
    for key, value in companies.items():
        print(f"  {key}. {value}")
    
    company_choice = input("\nOpción (1-5): ").strip()
    company_type = companies.get(company_choice, "tech-company")
    
    print(f"\n⚙️  Generando CV para: {target_role} en {company_type}")
    print("-" * 50)
    
    # Generar CV
    filepath = generator.generate_cv(target_role, company_type)
    
    print(f"\n✅ CV generado exitosamente!")
    print(f"📄 Archivo: {filepath}")
    print(f"\n💡 Próximos pasos:")
    print(f"   1. Revisar el archivo generado")
    print(f"   2. Copiar contenido a Google Docs")
    print(f"   3. Aplicar formato profesional")
    print(f"   4. Exportar como PDF")


if __name__ == "__main__":
    main()