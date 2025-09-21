# 📝 GUÍA DE TIPOGRAFÍA Y MEJORES PRÁCTICAS PARA CVS 2025

## 🎯 **PRINCIPIOS FUNDAMENTALES**

### **1. Jerarquía Visual Clara**
```
📏 ESCALA TIPOGRÁFICA RECOMENDADA:
• Nombre: 20-24px (2rem-2.4rem)
• Subtítulo profesional: 12-14px (1rem-1.1rem) 
• Títulos de sección: 14-16px (1.05rem-1.1rem)
• Texto principal: 11-13px (0.9rem-1rem)
• Texto secundario: 9-11px (0.8rem-0.9rem)
• Contacto: 10-12px (0.85rem-0.95rem)
```

### **2. Interlineado (Line Height)**
```
📐 ESPACIADO VERTICAL:
• Texto principal: 1.4-1.6 (óptimo para lectura)
• Títulos: 1.2-1.3 (más compacto)
• Listas: 1.3-1.5 (facilita escaneo)
• Contacto: 1.2-1.4 (compacto pero legible)
```

### **3. Espaciado y Márgenes**
```
🔲 ESPACIOS RECOMENDADOS:
• Margen página: 1.5-2cm (0.5-0.75 pulgadas)
• Entre secciones: 16-24px (1rem-1.5rem)
• Después de títulos: 8-12px (0.5rem-0.75rem)
• Entre párrafos: 6-8px (0.4rem-0.5rem)
• Indentación: 12-16px (0.75rem-1rem)
```

## 🔤 **SELECCIÓN DE FUENTES**

### **Fuentes Profesionales Recomendadas:**

#### **📊 Para Roles Técnicos/Analíticos:**
```css
font-family: 'Inter', 'Roboto', 'Source Sans Pro', sans-serif;
```
- **Inter**: Moderna, muy legible, excelente para pantallas
- **Roboto**: Confiable, usada por Google, neutral
- **Source Sans Pro**: Diseñada para código, precisa

#### **🎨 Para Roles Creativos:**
```css
font-family: 'Montserrat', 'Poppins', 'Nunito Sans', sans-serif;
```
- **Montserrat**: Moderna, con personalidad
- **Poppins**: Amigable pero profesional
- **Nunito Sans**: Suave, humanística

#### **🏛️ Para Roles Corporativos/Ejecutivos:**
```css
font-family: 'Playfair Display', 'Crimson Text', Georgia, serif;
```
- **Playfair Display**: Elegante, para títulos
- **Crimson Text**: Clásica, muy legible
- **Georgia**: Serif web-safe, confiable

#### **🔧 Para Roles de Ingeniería:**
```css
font-family: 'JetBrains Mono', 'Fira Code', 'Source Code Pro', monospace;
```
- **Solo para acentos**: No usar para todo el CV
- **Ideal para**: URLs, código, datos técnicos

## 📐 **COMPOSICIÓN Y LAYOUT**

### **1. Estructura Visual**
```
📋 ORDEN DE INFORMACIÓN (TOP → BOTTOM):
1. Información personal (Header)
2. Resumen profesional 
3. Experiencia laboral
4. Habilidades técnicas
5. Educación
6. Certificaciones
7. Proyectos/Portfolio (opcional)
```

### **2. Densidad de Información**
```
📊 DISTRIBUCIÓN RECOMENDADA:
• 60-70%: Experiencia y logros
• 15-20%: Habilidades técnicas
• 10-15%: Educación y certificaciones
• 5-10%: Información personal y resumen
```

### **3. Uso del Color**
```
🎨 PSICOLOGÍA DEL COLOR EN CVS:

🔵 AZUL (#2563eb, #1e40af):
• Industrias: Tecnología, Finanzas, Salud
• Transmite: Confianza, profesionalismo, estabilidad
• Ideal para: Hardware, Embedded, Corporativo

🟢 VERDE (#059669, #047857):
• Industrias: Startups, Sostenibilidad, Crecimiento
• Transmite: Innovación, crecimiento, frescura
• Ideal para: Software, Desarrollo, Ambiental

🟣 PÚRPURA (#7c3aed, #6d28d9):
• Industrias: Liderazgo, Consultoría, Lujo
• Transmite: Creatividad, liderazgo, sofisticación
• Ideal para: Management, Strategy, Design

🔴 ROJO (#dc2626, #b91c1c):
• Industrias: Marketing, Ventas, Emergencias
• Transmite: Energía, urgencia, pasión
• Ideal para: Sales, Marketing, Startups

⚫ NEGRO/GRIS (#1f2937, #374151):
• Industrias: Legal, Arquitectura, Fashion
• Transmite: Elegancia, seriedad, minimalismo
• Ideal para: Ejecutivo, Legal, Creative
```

## 📏 **RESPONSIVE Y ADAPTABILIDAD**

### **1. Breakpoints para CVs Digitales**
```css
/* Mobile First para visualización */
@media (max-width: 768px) {
    font-size: 14px; /* Base más grande en móvil */
    line-height: 1.5;
    padding: 1rem;
}

/* Tablet/Desktop */
@media (min-width: 769px) {
    font-size: 13px; /* Más contenido en pantalla */
    line-height: 1.4;
    padding: 1.5rem;
}

/* Print/PDF */
@media print {
    font-size: 11px; /* Máximo aprovechamiento */
    line-height: 1.3;
    margin: 0.5in;
}
```

### **2. Optimización para ATS (Applicant Tracking Systems)**
```
🤖 REGLAS PARA ATS:
• Usar fuentes estándar (Arial, Helvetica, Times)
• Evitar tablas complejas
• No usar imágenes para texto
• Mantener estructura simple
• Usar formato de fecha consistente
• Incluir keywords relevantes
```

## 🎯 **APLICACIÓN EN NUESTRO SISTEMA**

### **Configuración Actual Optimizada:**
```css
:root {
    /* Tipografía profesional */
    --font-primary: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    --font-size-base: 13px;        /* Equilibrio perfecto */
    --line-height-base: 1.5;       /* Óptimo para lectura */
    
    /* Escala tipográfica */
    --font-size-name: 2.2rem;      /* 28.6px - Impactante */
    --font-size-title: 1.1rem;     /* 14.3px - Subtítulo */
    --font-size-section: 1.05rem;  /* 13.65px - Secciones */
    --font-size-text: 1rem;        /* 13px - Texto principal */
    --font-size-small: 0.9rem;     /* 11.7px - Secundario */
    
    /* Espaciado coherente */
    --spacing-xs: 0.5rem;   /* 6.5px */
    --spacing-sm: 0.75rem;  /* 9.75px */
    --spacing-md: 1rem;     /* 13px */
    --spacing-lg: 1.5rem;   /* 19.5px */
    --spacing-xl: 2rem;     /* 26px */
}
```

### **Mejores Prácticas Implementadas:**
✅ **Contraste**: Mínimo 4.5:1 para accesibilidad
✅ **Consistencia**: Sistema de espaciado coherente
✅ **Legibilidad**: Line-height optimizado por tipo de contenido
✅ **Jerarquía**: Escala tipográfica clara y lógica
✅ **Adaptabilidad**: Responsive para diferentes dispositivos

## 📊 **MÉTRICAS DE ÉXITO**

### **CV Efectivo debe lograr:**
- ⏱️ **6 segundos**: Tiempo promedio de revisión inicial
- 👁️ **Escaneo fácil**: Información clave visible inmediatamente
- 📄 **1-2 páginas**: Longitud óptima según estudios
- 🎯 **Keywords relevantes**: 70-80% de coincidencia con oferta
- 🔍 **ATS compatible**: 90%+ de parsing exitoso

## 🛠️ **HERRAMIENTAS RECOMENDADAS**

### **Para Verificar Tipografía:**
- **Contrast Checker**: Verificar accesibilidad
- **Type Scale**: Generar escalas armónicas
- **Google Fonts**: Selección y rendimiento
- **Font Pair**: Combinaciones efectivas

### **Para Testing:**
- **ATS Scanners**: Verificar compatibilidad
- **Mobile Preview**: Responsive testing
- **Print Preview**: Optimización para PDF

¿Te gustaría que ajuste algún aspecto específico de la tipografía actual?
