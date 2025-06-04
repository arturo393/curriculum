#!/bin/bash

# =============================================================================
# CV Generator Script - Arturo Veras
# Genera CVs especializados usando el sistema de templates
# =============================================================================

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Directorios
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEMPLATES_DIR="$SCRIPT_DIR/templates"
OUTPUT_DIR="$SCRIPT_DIR/generated"
SPECIALIZED_DIR="$TEMPLATES_DIR/specialized"

# Crear directorio de salida si no existe
mkdir -p "$OUTPUT_DIR"

# Función para mostrar ayuda
show_help() {
    echo -e "${BLUE}=== CV Generator - Arturo Veras ===${NC}"
    echo ""
    echo "Uso: $0 [TEMPLATE] [COMPANY] [POSITION]"
    echo ""
    echo -e "${YELLOW}Templates disponibles:${NC}"
    echo "  software        - Desarrollador de Software"
    echo "  firmware        - Desarrollador Firmware/Embebido"
    echo "  iot            - Especialista IoT/Industry 4.0"
    echo "  lead           - Technical Lead/Manager"
    echo "  startup        - Startup/Entrepreneurship"
    echo ""
    echo -e "${YELLOW}Ejemplos:${NC}"
    echo "  $0 software Google \"Senior Software Engineer\""
    echo "  $0 firmware Tesla \"Embedded Software Engineer\""
    echo "  $0 iot Siemens \"IoT Solutions Architect\""
    echo "  $0 lead Microsoft \"Engineering Manager\""
    echo "  $0 startup YCombinator \"Technical Co-Founder\""
    echo ""
    echo -e "${YELLOW}Opciones adicionales:${NC}"
    echo "  --list         - Lista todos los templates disponibles"
    echo "  --compile      - Compila automáticamente el PDF"
    echo "  --clean        - Limpia archivos temporales"
    echo "  --help         - Muestra esta ayuda"
}

# Función para listar templates
list_templates() {
    echo -e "${BLUE}=== Templates Disponibles ===${NC}"
    echo ""
    
    for template in "$SPECIALIZED_DIR"/*.tex; do
        if [[ -f "$template" ]]; then
            filename=$(basename "$template" .tex)
            template_name=${filename#cv_}
            
            # Extraer descripción del template
            description=$(grep -m1 "% Orientado a" "$template" | sed 's/% Orientado a //')
            
            echo -e "${GREEN}${template_name}${NC}"
            echo "  Archivo: $filename.tex"
            echo "  Descripción: $description"
            echo ""
        fi
    done
}

# Función para validar template
validate_template() {
    local template=$1
    local template_file="$SPECIALIZED_DIR/cv_${template}.tex"
    
    if [[ ! -f "$template_file" ]]; then
        echo -e "${RED}Error: Template '$template' no encontrado${NC}"
        echo "Archivo buscado: $template_file"
        echo ""
        echo -e "${YELLOW}Templates disponibles:${NC}"
        list_templates
        return 1
    fi
    
    return 0
}

# Función para generar CV
generate_cv() {
    local template=$1
    local company=$2
    local position=$3
    
    # Validar template
    if ! validate_template "$template"; then
        return 1
    fi
    
    # Crear nombre de archivo de salida
    local timestamp=$(date +"%Y%m%d_%H%M%S")
    local safe_company=$(echo "$company" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-zA-Z0-9]/_/g')
    local output_name="cv_${template}_${safe_company}_${timestamp}"
    local output_path="$OUTPUT_DIR/$output_name"
    
    echo -e "${BLUE}=== Generando CV ===${NC}"
    echo "Template: $template"
    echo "Company: $company"
    echo "Position: $position"
    echo "Output: $output_name"
    echo ""
    
    # Crear directorio temporal de trabajo
    mkdir -p "$output_path"
    
    # Copiar template especializado
    cp "$SPECIALIZED_DIR/cv_${template}.tex" "$output_path/main.tex"
    
    # Copiar template base y variables
    cp -r "$TEMPLATES_DIR/base/" "$output_path/"
    cp -r "$TEMPLATES_DIR/variables/" "$output_path/"
    
    # Crear archivo de configuración específica
    cat > "$output_path/job_config.tex" << EOF
% Configuración específica para esta postulación
% Generado automáticamente el $(date)

% Información de la postulación
\\newcommand{\\TARGETCOMPANY}{$company}
\\newcommand{\\TARGETPOSITION}{$position}
\\newcommand{\\GENERATIONDATE}{$(date +'%d de %B de %Y')}

% Personalización adicional (editar según necesidades)
\\newcommand{\\COVERLETTER}{true}  % true/false para generar carta de presentación
\\newcommand{\\LANGUAGE}{es}       % es/en para idioma
\\newcommand{\\COLORSCHEME}{blue}  % blue/green/red para esquema de colores
EOF
    
    echo -e "${GREEN}✓ Archivos generados en: $output_path${NC}"
    
    # Compilar si se solicita
    if [[ "$COMPILE" == "true" ]]; then
        compile_cv "$output_path"
    fi
    
    # Mostrar instrucciones
    echo ""
    echo -e "${YELLOW}=== Próximos pasos ===${NC}"
    echo "1. Editar personalización: $output_path/job_config.tex"
    echo "2. Compilar PDF: cd $output_path && pdflatex main.tex"
    echo "3. O usar: $0 --compile-path $output_path"
    echo ""
    
    return 0
}

# Función para compilar CV
compile_cv() {
    local cv_path=$1
    
    if [[ ! -d "$cv_path" ]]; then
        echo -e "${RED}Error: Directorio no encontrado: $cv_path${NC}"
        return 1
    fi
    
    echo -e "${BLUE}=== Compilando PDF ===${NC}"
    echo "Directorio: $cv_path"
    
    cd "$cv_path" || return 1
    
    # Compilar LaTeX (ejecutar dos veces para referencias)
    echo "Ejecutando pdflatex (1/2)..."
    pdflatex -interaction=nonstopmode main.tex > compile.log 2>&1
    
    echo "Ejecutando pdflatex (2/2)..."
    pdflatex -interaction=nonstopmode main.tex >> compile.log 2>&1
    
    if [[ -f "main.pdf" ]]; then
        echo -e "${GREEN}✓ PDF generado exitosamente: $cv_path/main.pdf${NC}"
        
        # Abrir PDF automáticamente en macOS
        if command -v open >/dev/null 2>&1; then
            echo "Abriendo PDF..."
            open "main.pdf"
        fi
    else
        echo -e "${RED}✗ Error al generar PDF${NC}"
        echo "Ver log de errores: $cv_path/compile.log"
        tail -20 "$cv_path/compile.log"
        return 1
    fi
    
    cd - > /dev/null
    return 0
}

# Función para limpiar archivos temporales
clean_temp_files() {
    echo -e "${BLUE}=== Limpiando archivos temporales ===${NC}"
    
    find "$OUTPUT_DIR" -name "*.aux" -delete
    find "$OUTPUT_DIR" -name "*.log" -delete
    find "$OUTPUT_DIR" -name "*.out" -delete
    find "$OUTPUT_DIR" -name "*.toc" -delete
    find "$OUTPUT_DIR" -name "*.synctex.gz" -delete
    
    echo -e "${GREEN}✓ Archivos temporales eliminados${NC}"
}

# Procesar argumentos
COMPILE=false

while [[ $# -gt 0 ]]; do
    case $1 in
        --help|-h)
            show_help
            exit 0
            ;;
        --list|-l)
            list_templates
            exit 0
            ;;
        --compile|-c)
            COMPILE=true
            shift
            ;;
        --compile-path)
            compile_cv "$2"
            exit $?
            ;;
        --clean)
            clean_temp_files
            exit 0
            ;;
        *)
            break
            ;;
    esac
done

# Validar argumentos principales
if [[ $# -lt 3 ]]; then
    echo -e "${RED}Error: Faltan argumentos${NC}"
    echo ""
    show_help
    exit 1
fi

# Ejecutar generación
generate_cv "$1" "$2" "$3"
exit $?
