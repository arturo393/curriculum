#!/usr/bin/env python3
# 🚀 CV Generator HTML - Una página perfecta para PDF

"""
CV Generator HTML Simple
- Genera CV en HTML optimizado para una página A4
- CSS inline para fácil exportación a PDF
- Sin dependencies externas
"""

from datetime import datetime


class CVGeneratorHTML:
    """Generador simple de CV en HTML de una página"""
    
    def __init__(self):
        self.personal_data = {
            "name": "Arturo Veras Olivos",
            "title": "Ingeniero Civil Electrónico",
            "location": "Santiago, Chile",
            "phone": "+56 9 82413883",
            "email": "a.veras@gmail.com",
            "experience_years": "12+",
        }
    
    def generate_html_cv(self) -> str:
        """Generar CV completo en HTML optimizado para una página A4"""
        
        html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CV - {self.personal_data['name']}</title>
    <style>
        /* CSS optimizado para una página A4 (210mm × 297mm) */
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-size: 11px;
            line-height: 1.3;
            color: #333;
            background: #fff;
            max-width: 794px; /* A4 width in pixels (210mm) */
            max-height: 1123px; /* A4 height in pixels (297mm) */
            margin: 0 auto;
            padding: 15px;
        }}
        
        /* Print styles para PDF perfecto */
        @media print {{
            body {{
                margin: 0;
                padding: 15px;
                font-size: 10px;
            }}
            @page {{
                size: A4;
                margin: 10mm;
            }}
        }}
        
        /* Header */
        .header {{
            text-align: center;
            border-bottom: 2px solid #2c3e50;
            padding-bottom: 8px;
            margin-bottom: 12px;
        }}
        
        .header h1 {{
            font-size: 22px;
            font-weight: 700;
            color: #2c3e50;
            margin-bottom: 2px;
        }}
        
        .header .subtitle {{
            font-size: 14px;
            color: #34495e;
            font-weight: 500;
            margin-bottom: 6px;
        }}
        
        .header .contact {{
            font-size: 10px;
            color: #7f8c8d;
        }}
        
        /* Secciones */
        .section {{
            margin-bottom: 10px;
        }}
        
        .section h2 {{
            font-size: 13px;
            font-weight: 600;
            color: #2c3e50;
            border-bottom: 1px solid #bdc3c7;
            padding-bottom: 2px;
            margin-bottom: 6px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        
        .section p, .section li {{
            margin-bottom: 4px;
        }}
        
        /* Experiencia */
        .job {{
            margin-bottom: 8px;
        }}
        
        .job-title {{
            font-weight: 600;
            color: #2c3e50;
            font-size: 11px;
        }}
        
        .job-details {{
            font-size: 10px;
            color: #7f8c8d;
            font-style: italic;
            margin-bottom: 3px;
        }}
        
        .job-achievements {{
            font-size: 10px;
            line-height: 1.2;
        }}
        
        /* Listas */
        ul {{
            padding-left: 12px;
        }}
        
        li {{
            font-size: 10px;
            margin-bottom: 1px;
        }}
        
        /* Skills en columnas */
        .skills-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            gap: 8px;
            font-size: 10px;
        }}
        
        .skill-category {{
            background: #f8f9fa;
            padding: 6px;
            border-radius: 3px;
        }}
        
        .skill-category h4 {{
            font-size: 10px;
            font-weight: 600;
            color: #2c3e50;
            margin-bottom: 3px;
        }}
        
        /* Proyectos compactos */
        .project {{
            margin-bottom: 6px;
            border-left: 2px solid #3498db;
            padding-left: 6px;
        }}
        
        .project-title {{
            font-weight: 600;
            font-size: 10px;
            color: #2c3e50;
        }}
        
        .project-tech {{
            font-size: 9px;
            color: #7f8c8d;
            font-style: italic;
        }}
        
        .project-description {{
            font-size: 10px;
            margin-top: 2px;
        }}
        
        /* Educación compacta */
        .education-item {{
            margin-bottom: 4px;
        }}
        
        .education-degree {{
            font-weight: 600;
            font-size: 10px;
        }}
        
        .education-details {{
            font-size: 9px;
            color: #7f8c8d;
        }}
        
        /* Grid de 2 columnas para secciones compactas */
        .two-column {{
            display: grid;
            grid-template-columns: 1fr 1.4fr;
            gap: 12px;
        }}
        
        /* Logros en lista compacta */
        .achievements {{
            columns: 2;
            column-gap: 12px;
            font-size: 10px;
        }}
        
        .achievements li {{
            margin-bottom: 2px;
            break-inside: avoid;
        }}
    </style>
</head>
<body>
    <!-- HEADER -->
    <div class="header">
        <h1>{self.personal_data['name']}</h1>
        <div class="subtitle">Software Lead I+D | AI-Driven Architect | Electronic Civil Engineer</div>
        <div class="contact">
            📍 {self.personal_data['location']} | 📞 {self.personal_data['phone']} | ✉️ {self.personal_data['email']} | 🏆 {self.personal_data['experience_years']} años de experiencia
        </div>
    </div>

    <!-- PERFIL PROFESIONAL -->
    <div class="section">
        <h2>Perfil Profesional</h2>
        <p>Ingeniero Civil Electrónico con <strong>12 años de experiencia</strong> en el ciclo completo de productos tecnológicos. Especialista en liderar equipos de I+D bajo flujos de trabajo "AI-First" (Copilot, Gemini, Agentes), diseñando arquitecturas robustas que abarcan desde firmware embebido (STM32/C++) hasta software full-stack (Python, React). Enfoque estratégico en calidad de fabricación y soluciones orientadas al cliente.</p>
    </div>

    <!-- COMPETENCIAS TÉCNICAS (Grid de 3 columnas) -->
    <div class="section">
        <h2>Competencias Técnicas</h2>
        <div class="skills-grid">
            <div class="skill-category">
                <h4>IA & Algoritmos</h4>
                <ul>
                    <li><strong>GitHub Copilot</strong> (Avanzado)</li>
                    <li><strong>IA Agents & Workflows</strong></li>
                    <li>Gemini AI / LLMs Integration</li>
                    <li>Prompts Engineering</li>
                    <li>IA Frameworks de decisión</li>
                </ul>
            </div>
            <div class="skill-category">
                <h4>Desarrollo & Arquitectura</h4>
                <ul>
                    <li><strong>Python / C / C++</strong></li>
                    <li><strong>Software Architecture</strong></li>
                    <li>Planificación & Test (Frontend/Backend)</li>
                    <li>Microcontroladores (STM32, ESP32)</li>
                    <li>Firmware Design & Firmware Support</li>
                </ul>
            </div>
            <div class="skill-category">
                <h4>Cloud, DevOps & Liderazgo</h4>
                <ul>
                    <li>Google Cloud (GCP)</li>
                    <li>Liderazgo de equipos (I+D)</li>
                    <li>Gestión de área TI</li>
                    <li>Docker / Linux / Git</li>
                    <li>React / MongoDB / Odoo</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- EXPERIENCIA PROFESIONAL -->
    <div class="section">
        <h2>Experiencia Profesional</h2>
        
        <div class="job">
            <div class="job-title">UQOMM SpA - Software Lead I+D | Arquitecto de IA, Software & Firmware</div>
            <div class="job-details">Septiembre 2021 - Presente (4 años 6 meses) | Con Con, Chile | Comunicaciones para minería subterránea</div>
            <div class="job-achievements">
                • <strong>Liderazgo de Equipo:</strong> Creación y dirección de un equipo de 3 ingenieros, fomentando la autonomía, responsabilidad por proyectos y habilidades blandas.<br>
                • <strong>Flujos Full IA:</strong> Implementación de metodologías de desarrollo acelerado con Copilot y agentes de IA para refactorización masiva e investigación de soluciones.<br>
                • <strong>Arquitectura Estratégica:</strong> Diseño de planes técnicos y planes de test antes de la implementación, asegurando robustez en firmware, software y frontend.<br>
                • <strong>Calidad & Producción:</strong> Definición de lineamientos para pruebas de fabricación y aseguramiento de calidad del producto final orientado al cliente.<br>
                • <strong>Gestión TI:</strong> Administración integral del área de TI junto al equipo de software, garantizando continuidad operativa y seguridad.<br>
                • <strong>Apoyo Multistack:</strong> Soporte experto en diseño de firmware para nuevos hardware y arquitectura de sistemas complejos bajo tierra.
            </div>
        </div>
        
        <div class="job">
            <div class="job-title">BlackGPS - Ingeniero de Hardware y Software</div>
            <div class="job-details">Julio 2017 - Agosto 2021 (4+ años) | Santiago, Chile</div>
            <div class="job-achievements">
                • <strong>Dispositivo anti-robo:</strong> Diseño completo hardware/software con inhibidor GNSS/GSM<br>
                • <strong>Firmware con FreeRTOS:</strong> Desarrollo en C/C++ para sistema de tiempo real<br>
                • <strong>Backend Java:</strong> Nuevas funcionalidades en SpringBoot para procesamiento GPS y CANBus<br>
                • <strong>App Flutter:</strong> Mejoras en aplicación móvil con comunicación Bluetooth<br>
                • <strong>Soporte técnico:</strong> Configuración dispositivos Teltonika, DCT Syrus, ERM Starlink
            </div>
        </div>
    </div>

    <!-- PROYECTOS DESTACADOS -->
    <div class="section">
        <h2>Proyectos Destacados</h2>
        
        <div class="project">
            <div class="project-title">Sistema IoT Industrial - Minería Subterránea</div>
            <div class="project-tech">STM32 • FreeRTOS • Python • LoRa • React • MongoDB • MQTT</div>
            <div class="project-description"><strong>Impacto:</strong> Plataforma de diagnóstico remoto eliminó visitas en sitio, reduciendo costos operacionales significativamente</div>
        </div>
        
        <div class="project">
            <div class="project-title">Dispositivo Anti-Robo RF Inhibidor</div>
            <div class="project-tech">STM32 • GNSS/GSM • SpringBoot • Java • CANBus</div>
            <div class="project-description"><strong>Logro:</strong> Dispositivo grado producción desde R&D hasta despliegue en mercado logístico</div>
        </div>
        
        <div class="project">
            <div class="project-title">Instrumentación & Automatización RF</div>
            <div class="project-tech">Python • Procesamiento de Señales • Integración Equipos Lab</div>
            <div class="project-description"><strong>Resultado:</strong> Automatización de bancos de prueba RF, reduciendo tiempo de testing en 80%</div>
        </div>
    </div>

    <!-- EDUCACIÓN Y IDIOMAS/LOGROS (2 columnas con más espacio para idiomas/logros) -->
    <div class="two-column">
        <div class="section">
            <h2>Educación</h2>
            <div class="education-item">
                <div class="education-degree">Ingeniero Civil Electrónico</div>
                <div class="education-details">Universidad Técnica Federico Santa María (2006-2014)</div>
            </div>
            <div class="education-item">
                <div class="education-degree">Certificaciones</div>
                <div class="education-details">• Metodologías Ágiles (2022)<br>• Scrum + Kanban (2019)<br>• Diseño Circuitos Integrados (2017)</div>
            </div>
        </div>
        
        <div class="section">
            <h2>Idiomas & Logros Profesionales</h2>
            <div style="margin-bottom: 8px;">
                <p><strong>Español:</strong> Nativo</p>
                <p><strong>Inglés:</strong> B1-B2 Intermedio (fluidez técnica)</p>
                <ul style="font-size: 9px; margin-top: 3px; margin-bottom: 0;">
                    <li>Lectura avanzada de documentación técnica</li>
                    <li>Comunicación funcional para reuniones técnicas</li>
                    <li>Objetivo: alcanzar nivel C1</li>
                </ul>
            </div>
            <div>
                <ul class="achievements" style="columns: 1; column-gap: 0;">
                    <li style="margin-bottom: 3px;">Ganador I+D Aplicada - Fundación Copec UC (2015)</li>
                    <li style="margin-bottom: 3px;">Desarrollo de 5+ firmwares especializados: headend, LoRa master-remoto, telemetría, sistema tags y leak feeder</li>
                    <li style="margin-bottom: 3px;">Innovación Tecnológica - 5+ productos llevados hasta producción comercial</li>
                    <li style="margin-bottom: 3px;">Liderazgo Técnico - Gestión exitosa de proyectos multidisciplinarios</li>
                </ul>
            </div>
        </div>
    </div>
</body>
</html>"""
        
        return html_content
    
    def save_cv(self, output_dir: str = "output") -> str:
        """Guarda el CV en HTML y devuelve la ruta"""
        import os
        
        # Crear directorio si no existe
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Generar nombre único
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"cv_arturo_veras_{timestamp}.html"
        filepath = os.path.join(output_dir, filename)
        
        # Guardar archivo
        html_content = self.generate_html_cv()
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return filepath


def main():
    """Función principal simplificada"""
    print("🚀 CV Generator HTML - Una página perfecta para PDF")
    print("=" * 50)
    
    generator = CVGeneratorHTML()
    filepath = generator.save_cv()
    
    print(f"✅ CV generado exitosamente!")
    print(f"📄 Archivo: {filepath}")
    print(f"\n💡 Cómo exportar a PDF:")
    print(f"   1. Abrir {filepath} en navegador")
    print(f"   2. Ctrl+P / Cmd+P (Imprimir)")
    print(f"   3. Seleccionar 'Guardar como PDF'")
    print(f"   4. Configurar márgenes mínimos")
    print(f"   5. ¡Listo! CV profesional en una página")


if __name__ == "__main__":
    main()