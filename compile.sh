#!/bin/bash
# Script para compilar los CVs en español e inglés
# Uso: ./compile.sh [esp|eng|all]

set -e

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Función para imprimir mensajes con color
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Función para compilar un CV
compile_cv() {
    local dir=$1
    local lang=$2
    
    print_status "Compilando CV en $lang..."
    
    if [ ! -d "$dir" ]; then
        print_error "Directorio $dir no encontrado"
        return 1
    fi
    
    cd "$dir"
    
    # Limpiar archivos auxiliares previos
    rm -f *.aux *.log *.out *.toc *.bbl *.blg *.fls *.fdb_latexmk
    
    # Compilar el documento principal
    if pdflatex main.tex; then
        print_status "Primera pasada completada para $lang"
        
        # Segunda pasada para resolver referencias
        if pdflatex main.tex; then
            print_status "Segunda pasada completada para $lang"
            
            # Si existe bibliografía, compilar con bibtex
            if [ -f "cvreferences.bib" ] || [ -f "publications.bib" ]; then
                print_status "Procesando bibliografía para $lang..."
                bibtex main || print_warning "Error en bibtex, continuando..."
                pdflatex main.tex
                pdflatex main.tex
            fi
            
            print_status "✓ CV en $lang compilado exitosamente"
            
            # Verificar que el PDF se creó
            if [ -f "main.pdf" ]; then
                print_status "PDF generado: $dir/main.pdf"
            else
                print_error "No se pudo generar el PDF"
                return 1
            fi
        else
            print_error "Error en segunda pasada de pdflatex para $lang"
            return 1
        fi
    else
        print_error "Error en primera pasada de pdflatex para $lang"
        return 1
    fi
    
    cd ..
}

# Función principal
main() {
    local option=${1:-all}
    
    # Verificar que LaTeX esté instalado
    if ! command -v pdflatex &> /dev/null; then
        print_error "pdflatex no está instalado en tu sistema."
        print_status "Por favor, instala LaTeX siguiendo las instrucciones en el README.md"
        print_status "Para macOS: brew install --cask basictex"
        print_status "Para Ubuntu: sudo apt-get install texlive-latex-base"
        exit 1
    fi
    
    print_status "Iniciando compilación de CVs..."
    
    case $option in
        esp)
            compile_cv "Arturo_Veras_CV_ESP" "español"
            ;;
        eng)
            compile_cv "Arturo_Veras_CV_ENG" "inglés"
            ;;
        all)
            compile_cv "Arturo_Veras_CV_ESP" "español"
            compile_cv "Arturo_Veras_CV_ENG" "inglés"
            ;;
        *)
            print_error "Opción no válida. Uso: $0 [esp|eng|all]"
            exit 1
            ;;
    esac
    
    print_status "Compilación completada."
}

# Verificar que estamos en el directorio correcto
if [ ! -d "shared" ] || [ ! -d "Arturo_Veras_CV_ESP" ] || [ ! -d "Arturo_Veras_CV_ENG" ]; then
    print_error "Este script debe ejecutarse desde el directorio raíz del repositorio curriculum"
    exit 1
fi

# Ejecutar función principal
main "$@"
