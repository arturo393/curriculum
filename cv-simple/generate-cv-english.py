#!/usr/bin/env python3
# 🚀 CV Generator HTML English - One perfect page for PDF

"""
English CV Generator - Single Page HTML
- Genera CV en inglés optimizado para una página A4
- CSS inline para fácil exportación a PDF
- Sin dependencies externas
"""

from datetime import datetime


class CVGeneratorEnglish:
    """Simple English CV Generator optimized for one A4 page"""
    
    def __init__(self):
        self.personal_data = {
            "name": "Arturo Veras Olivos",
            "title": "Software Lead I+D | AI-Driven Architect",
            "location": "Santiago, Chile",
            "phone": "+56 9 82413883",
            "email": "a.veras@gmail.com",
            "experience_years": "12+",
            "linkedin": "linkedin.com/in/arturo-veras",
            "github": "github.com/arturo393"
        }
    
    def generate_html_cv(self) -> str:
        """Generates complete CV in HTML optimized for A4 page"""
        
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CV - {self.personal_data['name']}</title>
    <style>
        /* CSS optimized for A4 (210mm × 297mm) */
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
            max-width: 794px;
            max-height: 1123px;
            margin: 0 auto;
            padding: 15px;
        }}
        
        /* Print styles for perfect PDF */
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
        
        /* Sections */
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
        
        /* Experience */
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
        
        /* Lists */
        ul {{
            padding-left: 12px;
        }}
        
        li {{
            font-size: 10px;
            margin-bottom: 1px;
        }}
        
        /* Skills grid */
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
        
        /* Projects compact */
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
        
        /* Education compact */
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
        
        /* 2 column grid */
        .two-column {{
            display: grid;
            grid-template-columns: 1fr 1.4fr;
            gap: 12px;
        }}
        
        /* Achievements compact list */
        .achievements {{
            columns: 1;
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
            📍 {self.personal_data['location']} | 📞 {self.personal_data['phone']} | ✉️ {self.personal_data['email']} | 🏆 {self.personal_data['experience_years']} years experience
        </div>
    </div>

    <!-- PROFESSIONAL PROFILE -->
    <div class="section">
        <h2>Professional Profile</h2>
        <p>Electronic Civil Engineer with <strong>12 years of experience</strong> in the full cycle of technological products. Specialist in leading R&D teams using "AI-First" workflows (Copilot, Gemini, Agents), designing robust architectures from embedded firmware (STM32/C++) to full-stack software (Python, React). Strategic focus on manufacturing quality and customer-oriented solutions.</p>
    </div>

    <!-- TECHNICAL SKILLS -->
    <div class="section">
        <h2>Technical Skills</h2>
        <div class="skills-grid">
            <div class="skill-category">
                <h4>AI & Algorithms</h4>
                <ul>
                    <li><strong>GitHub Copilot</strong> (Expert)</li>
                    <li><strong>AI Agents & Workflows</strong></li>
                    <li>Gemini AI / LLMs Integration</li>
                    <li>Prompt Engineering</li>
                    <li>AI Decision Frameworks</li>
                </ul>
            </div>
            <div class="skill-category">
                <h4>Development & Architecture</h4>
                <ul>
                    <li><strong>Python / C / C++</strong></li>
                    <li><strong>Software Architecture</strong></li>
                    <li>Design & Testing Plans (Front/Back)</li>
                    <li>Microcontrollers (STM32, ESP32)</li>
                    <li>Firmware Design & Support</li>
                </ul>
            </div>
            <div class="skill-category">
                <h4>Cloud & Leadership</h4>
                <ul>
                    <li>Google Cloud (GCP)</li>
                    <li>R&D Team Leadership</li>
                    <li>IT Area Management</li>
                    <li>Docker / Linux / Git</li>
                    <li>React / MongoDB / Odoo</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- PROFESSIONAL EXPERIENCE -->
    <div class="section">
        <h2>Professional Experience</h2>
        
        <div class="job">
            <div class="job-title">UQOMM SpA — Software Lead I+D | AI, Software & Firmware Architect</div>
            <div class="job-details">September 2021 – Present (4 years 6 months) | Con Con, Chile | Mining Communications</div>
            <div class="job-achievements">
                • <strong>Team Leadership:</strong> Built and directed a team of 3 engineers, fostering autonomy, project ownership, and soft skills development.<br>
                • <strong>Full AI Workflows:</strong> Implemented accelerated development methodologies with Copilot and AI agents for massive refactoring and solution research.<br>
                • <strong>Strategic Architecture:</strong> Developed technical design and testing plans prior to implementation, ensuring robustness in firmware, software, and frontend.<br>
                • <strong>Quality & Production:</strong> Defined manufacturing test guidelines and ensured end-to-end customer-oriented product quality.<br>
                • <strong>IT Management:</strong> Comprehensive management of the IT area along with the software team, ensuring operational continuity and security.<br>
                • <strong>Multistack Support:</strong> Expert guidance in firmware design for new hardware and complex underground systems architecture.
            </div>
        </div>
        
        <div class="job">
            <div class="job-title">BlackGPS — Senior Hardware & Software Engineer</div>
            <div class="job-details">July 2017 – August 2021 (4+ years) | Santiago, Chile | Fleet Security Solutions</div>
            <div class="job-achievements">
                • <strong>Anti-Theft Device:</strong> Complete hardware/software design with GNSS/GSM inhibitor and GPS tracking<br>
                • <strong>Firmware Development:</strong> Real-time systems with FreeRTOS, production-grade code in C/C++<br>
                • <strong>Backend Architecture:</strong> SpringBoot Java implementation for GPS and CANBus data processing<br>
                • <strong>Mobile Application:</strong> Flutter app improvements with Bluetooth communication and remote commands<br>
                • <strong>Technical Support:</strong> Device configuration for 100+ fleet management customers (Teltonika, DCT Syrus, ERM Starlink)
            </div>
        </div>
    </div>

    <!-- FEATURED PROJECTS -->
    <div class="section">
        <h2>Featured Projects</h2>
        
        <div class="project">
            <div class="project-title">Industrial IoT Diagnostics — Underground Mining</div>
            <div class="project-tech">STM32 • FreeRTOS • Python • LoRa • React • MongoDB • MQTT</div>
            <div class="project-description"><strong>Impact:</strong> Remote diagnostics platform eliminated on-site visits, reducing operational costs and improving response time</div>
        </div>
        
        <div class="project">
            <div class="project-title">Anti-Theft RF Inhibitor Device</div>
            <div class="project-tech">STM32 • GNSS/GSM • SpringBoot • Java • CANBus</div>
            <div class="project-description"><strong>Outcome:</strong> Production-grade device from R&D to market deployment across logistics industry</div>
        </div>
        
        <div class="project">
            <div class="project-title">RF Instrumentation & Automation</div>
            <div class="project-tech">Python • Signal Processing • Lab Equipment Integration</div>
            <div class="project-description"><strong>Achievement:</strong> Automated RF test benches, reducing testing time by 80% through intelligent instrumentation</div>
        </div>
    </div>

    <!-- EDUCATION & LANGUAGES (2 columns) -->
    <div class="two-column">
        <div class="section">
            <h2>Education</h2>
            <div class="education-item">
                <div class="education-degree">Electrical Engineer</div>
                <div class="education-details">Federico Santa María Technical University (2006-2014)<br>Valparaíso, Chile</div>
            </div>
            <div class="education-item">
                <div class="education-degree">Certifications</div>
                <div class="education-details">• Agile Methodologies (2022)<br>• Scrum + Kanban (2019)<br>• Integrated Circuit Design (2017)</div>
            </div>
        </div>
        
        <div class="section">
            <h2>Languages & Achievements</h2>
            <div style="margin-bottom: 8px;">
                <p><strong>Spanish:</strong> Native</p>
                <p><strong>English:</strong> B1-B2 Intermediate (technical fluency)</p>
                <ul style="font-size: 9px; margin-top: 3px; margin-bottom: 0;">
                    <li>Advanced technical documentation reading</li>
                    <li>Functional speaking for technical meetings</li>
                    <li>Working towards C1 proficiency</li>
                </ul>
            </div>
            <div>
                <ul class="achievements">
                    <li>Winner I+D Applied Research Award — Copec UC Foundation (2015)</li>
                    <li>5+ specialized firmware implementations: headend, LoRa, telemetry, tag systems</li>
                    <li>Full-stack architecture: hardware → firmware → backend → frontend → cloud</li>
                    <li>Agile/Scrum methodologies (4+ years) • Git Flow workflows (3+ years)</li>
                    <li>Available: Mon-Fri 18:00-20:00 UTC-3 for interviews</li>
                </ul>
            </div>
        </div>
    </div>
</body>
</html>"""
        
        return html_content
    
    def save_cv(self, output_dir: str = "output") -> str:
        """Save CV to HTML and return filepath"""
        import os
        
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"cv_arturo_veras_english_{timestamp}.html"
        filepath = os.path.join(output_dir, filename)
        
        html_content = self.generate_html_cv()
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return filepath


def main():
    """Main function"""
    print("🚀 English CV Generator HTML - One perfect page for PDF")
    print("=" * 60)
    
    generator = CVGeneratorEnglish()
    filepath = generator.save_cv()
    
    print(f"✅ English CV generated successfully!")
    print(f"📄 File: {filepath}")
    print(f"\n💡 How to export to PDF:")
    print(f"   1. Open {filepath} in your browser")
    print(f"   2. Ctrl+P / Cmd+P (Print)")
    print(f"   3. Select 'Save as PDF'")
    print(f"   4. Set margins to minimum")
    print(f"   5. Done! Professional one-page CV")


if __name__ == "__main__":
    main()
