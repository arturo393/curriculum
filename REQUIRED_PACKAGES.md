# Paquetes LaTeX Requeridos

## Análisis de Dependencias

Basado en el análisis de los archivos `.tex` y los paquetes en `shared/`, estos son los paquetes LaTeX necesarios para compilar el curriculum:

### Paquetes Principales
- **moderncv** - Clase principal para el diseño del CV (incluida en `shared/`)
- **inputenc** - Codificación de caracteres UTF-8
- **fontenc** - Codificación de fuentes T1
- **lmodern** - Fuentes Latin Modern
- **graphicx** - Inclusión de gráficos
- **tikz** - Gráficos y diagramas vectoriales
- **geometry** - Configuración de márgenes de página

### Paquetes Auxiliares (en shared/)
- **moderntimeline** - Líneas de tiempo para CV
- **pdfpages** - Inclusión de páginas PDF
- **xpatch** - Modificaciones de comandos LaTeX
- **biblatex_modifications** - Modificaciones para bibliografías
- **cvitem_modifications** - Modificaciones personalizadas para elementos del CV

### Paquetes del Sistema (automáticos en moderncv.cls)
- **etoolbox** - Herramientas adicionales de LaTeX
- **ifthen** - Condicionales
- **xcolor** - Colores
- **ifxetex, ifluatex** - Detección de motor LaTeX
- **hyperref** - Enlaces e hipervínculos
- **url** - Formateo de URLs
- **fancyhdr** - Encabezados y pies de página
- **calc** - Cálculos de longitud
- **xparse** - Argumentos avanzados de comandos
- **microtype** - Microtipografía
- **tweaklist** - Ajustes de listas

## Instalación

### Para macOS con BasicTeX
```bash
sudo tlmgr install moderncv moderntimeline pdfpages xpatch biblatex geometry tikz
```

### Para distribuciones Linux completas (texlive-full)
Los paquetes ya están incluidos en la instalación completa.

### Para instalaciones mínimas de LaTeX
```bash
# Ubuntu/Debian
sudo apt-get install texlive-latex-base texlive-fonts-recommended texlive-latex-extra

# O instalar paquetes individuales:
sudo tlmgr install moderncv moderntimeline pdfpages xpatch biblatex geometry tikz inputenc fontenc lmodern graphicx
```

## Verificación
Para verificar que todos los paquetes están instalados, ejecuta:
```bash
./compile.sh esp
```

Si hay paquetes faltantes, LaTeX mostrará errores específicos indicando qué paquetes instalar.
