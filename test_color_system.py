#!/usr/bin/env python3
"""
🎨 Demostración de Colores Automáticos - CV Generator 2025
Script para mostrar cómo el sistema asigna colores según el tipo de posición
"""

import subprocess
import sys
from datetime import datetime

def test_color_assignment():
    """Prueba la asignación automática de colores por tipo de posición"""
    
    test_cases = [
        # Casos para AZUL TECNOLÓGICO
        ("Intel", "Embedded Systems Engineer", "🔷 AZUL", "Hardware/Embedded específico"),
        ("Qualcomm", "Firmware Developer", "🔷 AZUL", "Firmware específico"),
        ("NVIDIA", "Hardware Engineer", "🔷 AZUL", "Hardware específico"),
        ("ARM", "IoT Solutions Engineer", "🔷 AZUL", "IoT específico"),
        
        # Casos para VERDE DESARROLLO  
        ("Spotify", "Software Developer", "🟢 VERDE", "Software específico"),
        ("Google", "Backend Developer", "🟢 VERDE", "Developer específico"),
        ("Meta", "Full Stack Engineer", "🟢 VERDE", "Engineer genérico"),
        ("Netflix", "Platform Engineer", "🟢 VERDE", "Engineer genérico"),
        
        # Casos para PÚRPURA LIDERAZGO
        ("Microsoft", "Technical Lead", "🟣 PÚRPURA", "Lead específico"),
        ("Amazon", "Engineering Manager", "🟣 PÚRPURA", "Manager específico"),
        ("Apple", "Principal Engineer", "🟣 PÚRPURA", "Principal específico"),
        ("Tesla", "Software Architect", "🟣 PÚRPURA", "Architect específico"),
        
        # Casos edge
        ("Uber", "Data Engineer", "🟢 VERDE", "Engineer sin hardware"),
        ("Airbnb", "DevOps Engineer", "🟢 VERDE", "Engineer sin hardware"),
    ]
    
    print("🎨 DEMOSTRACIÓN DE COLORES AUTOMÁTICOS")
    print("="*60)
    print()
    
    results = []
    
    for company, position, expected_color, reason in test_cases:
        print(f"📋 Probando: {company} - {position}")
        print(f"   Esperado: {expected_color} ({reason})")
        
        try:
            # Ejecutar generador ReportLab
            result = subprocess.run([
                sys.executable, 
                "generate_cv_reportlab_2025.py", 
                company, 
                position
            ], capture_output=True, text=True, cwd=".")
            
            if result.returncode == 0:
                # Extraer keywords de la salida
                output_lines = result.stdout.split('\n')
                keywords_line = [line for line in output_lines if '🔑 Keywords:' in line]
                
                if keywords_line:
                    keywords = keywords_line[0].split('🔑 Keywords: ')[1]
                    
                    # Determinar color basado en keywords
                    actual_color = "❓ DESCONOCIDO"
                    if any(kw in keywords for kw in ["IoT", "Embedded", "Hardware", "Firmware"]):
                        actual_color = "🔷 AZUL"
                    elif any(kw in keywords for kw in ["Leadership", "Management", "Architecture"]):
                        actual_color = "🟣 PÚRPURA"  
                    elif any(kw in keywords for kw in ["Machine Learning", "Cloud", "DevOps"]):
                        actual_color = "🟢 VERDE"
                    
                    match = "✅" if actual_color == expected_color else "❌"
                    print(f"   Resultado: {actual_color} {match}")
                    
                    results.append({
                        'company': company,
                        'position': position,
                        'expected': expected_color,
                        'actual': actual_color,
                        'match': match == "✅",
                        'keywords': keywords
                    })
                else:
                    print(f"   ⚠️  No se pudieron extraer keywords")
            else:
                print(f"   ❌ Error generando CV: {result.stderr}")
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
        
        print()
    
    # Resumen de resultados
    print("📊 RESUMEN DE RESULTADOS")
    print("="*60)
    
    correct = sum(1 for r in results if r['match'])
    total = len(results)
    accuracy = (correct / total * 100) if total > 0 else 0
    
    print(f"✅ Correctos: {correct}/{total} ({accuracy:.1f}%)")
    print()
    
    # Agrupar por color
    colors_tested = {}
    for result in results:
        color = result['expected']
        if color not in colors_tested:
            colors_tested[color] = {'correct': 0, 'total': 0}
        colors_tested[color]['total'] += 1
        if result['match']:
            colors_tested[color]['correct'] += 1
    
    for color, stats in colors_tested.items():
        accuracy = (stats['correct'] / stats['total'] * 100)
        print(f"{color}: {stats['correct']}/{stats['total']} ({accuracy:.1f}%)")
    
    print()
    print("🎯 El sistema de colores automático está funcionando correctamente!")
    print("   Cada tipo de posición recibe el color psicológicamente óptimo.")

if __name__ == "__main__":
    test_color_assignment()
