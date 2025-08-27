#!/usr/bin/env python3
"""
CV Suite Quick - Generador Rápido y Compacto
Genera CVs optimizados en 1-2 páginas con colores dinámicos
Autor: Arturo Veras González
Fecha: 2025
"""

import os
import sys
import subprocess

def main():
    """Función principal simplificada"""
    
    print("🎨 =" * 40)
    print("🚀 CV SUITE QUICK - GENERADOR COMPACTO")
    print("🎨 =" * 40)
    print()
    
    # Obtener parámetros
    if len(sys.argv) < 3:
        print("💡 Uso: python3 cv_suite_quick.py 'Empresa' 'Posición' [formato]")
        print("📝 Formatos: compact (default), html, both")
        print("📝 Ejemplo: python3 cv_suite_quick.py 'Intel' 'Embedded Engineer' both")
        print()
        print("🎨 COLORES AUTOMÁTICOS:")
        print("   🔵 Hardware/Embedded → Azul")
        print("   🟣 Leadership/Senior → Púrpura") 
        print("   🟢 Software/Developer → Verde")
        return
    
    company = sys.argv[1]
    position = sys.argv[2]
    format_type = sys.argv[3] if len(sys.argv) > 3 else 'compact'
    
    print(f"🏢 Empresa: {company}")
    print(f"💼 Posición: {position}")
    print(f"📄 Formato: {format_type}")
    print()
    
    # Predicción de colores
    company_lower = company.lower()
    position_lower = position.lower()
    
    if any(kw in f"{company_lower} {position_lower}" for kw in ['intel', 'hardware', 'embedded', 'iot']):
        color_prediction = "🔵 Azul (Hardware/Embedded)"
    elif any(kw in position_lower for kw in ['senior', 'lead', 'manager', 'director']):
        color_prediction = "🟣 Púrpura (Leadership)"
    elif any(kw in f"{company_lower} {position_lower}" for kw in ['spotify', 'software', 'developer']):
        color_prediction = "🟢 Verde (Software)"
    else:
        color_prediction = "🔵 Azul (Profesional)"
    
    print(f"🎨 Color predicho: {color_prediction}")
    print()
    
    # Generar CVs
    if format_type in ['compact', 'both']:
        print("🔄 Generando CV Compacto (1 página)...")
        try:
            result = subprocess.run(['python3', 'generate_cv_compact_2025.py', company, position], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                print("✅ CV Compacto generado exitosamente")
            else:
                print(f"❌ Error: {result.stderr}")
        except Exception as e:
            print(f"❌ Error: {e}")
        print()
    
    if format_type in ['html', 'both']:
        print("🔄 Generando CV HTML/CSS (1-2 páginas)...")
        try:
            result = subprocess.run(['python3', 'generate_cv_modern_fixed.py', company, position], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                print("✅ CV HTML/CSS generado exitosamente")
            else:
                print(f"❌ Error: {result.stderr}")
        except Exception as e:
            print(f"❌ Error: {e}")
        print()
    
    print("🎉 ¡Generación completada!")
    print()
    print("💡 Archivos generados:")
    print("   📁 generated_compact_2025/ (PDFs de 1 página)")
    print("   📁 generated_modern/ (HTML + PDF)")

if __name__ == "__main__":
    main()
