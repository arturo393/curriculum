# Currículum Vitae - Arturo Veras

Este repositorio contiene las versiones de mi Currículum Vitae en diferentes idiomas, gestionadas con LaTeX de manera optimizada y sin duplicación de código.

## 🏗️ Estructura Optimizada

El repositorio está organizado de manera eficiente para evitar duplicación de código:

```
curriculum/
├── shared/                          # Paquetes LaTeX compartidos
│   ├── moderncv/                   # Clase moderncv
│   ├── moderntimeline/             # Paquete timeline
│   ├── pdfpages/                   # Paquete pdfpages
│   ├── xpatch/                     # Paquete xpatch
│   ├── biblatex_modifications/     # Modificaciones biblatex
│   ├── cvitem_modifications/       # Modificaciones de elementos CV
│   └── template-*.tex              # Plantillas base
├── Arturo_Veras_CV_ESP/            # CV en español
│   ├── main.tex                    # Archivo principal
│   ├── coverletter.tex             # Carta de presentación
│   ├── cvreferences.bib            # Referencias
│   └── publications.bib            # Publicaciones
├── Arturo_Veras_CV_ENG/            # CV en inglés
│   ├── main.tex                    # Archivo principal
│   ├── coverletter.tex             # Cover letter
│   ├── cvreferences.bib            # References
│   └── publications.bib            # Publications
└── compile.sh                      # Script de compilación
```

## 📋 Versiones Disponibles

Actualmente, el CV está disponible en los siguientes idiomas:

* **Español (Spanish):**
  * [Ver CV en Español (PDF)](./Arturo_Veras_CV_ESP/main.pdf)
  * [Código Fuente (LaTeX)](./Arturo_Veras_CV_ESP/)
* **Inglés (English):**
  * [Ver CV en Inglés (PDF)](./Arturo_Veras_CV_ENG/main.pdf)
  * [Código Fuente (LaTeX)](./Arturo_Veras_CV_ENG/)

## 🔧 Compilación (LaTeX)

### Prerrequisitos

Necesitas tener LaTeX instalado en tu sistema. Aquí tienes las opciones según tu sistema operativo:

#### macOS
```bash
# Opción 1: MacTeX (completo, ~4GB)
# Descargar desde: https://www.tug.org/mactex/

# Opción 2: BasicTeX (ligero, ~100MB) + paquetes necesarios
brew install --cask basictex
sudo tlmgr update --self
sudo tlmgr install moderncv moderntimeline pdfpages xpatch biblatex geometry tikz

# Opción 3: Homebrew (TeX Live)
brew install --cask mactex-no-gui
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install texlive-full
# O instalación mínima:
sudo apt-get install texlive-latex-base texlive-fonts-recommended texlive-latex-extra
```

#### Windows
```bash
# Descargar e instalar MiKTeX desde: https://miktex.org/
# O TeX Live desde: https://www.tug.org/texlive/
```

### Método Rápido (Recomendado)

Una vez que tengas LaTeX instalado, usa el script de compilación incluido:

```bash
# Compilar ambas versiones
./compile.sh

# Compilar solo la versión en español
./compile.sh esp

# Compilar solo la versión en inglés
./compile.sh eng
```

### Método Manual

Si deseas compilar los archivos `.tex` manualmente:

```bash
# Para la versión en español
cd Arturo_Veras_CV_ESP
pdflatex main.tex
pdflatex main.tex  # Segunda pasada para referencias

# Para la versión en inglés
cd Arturo_Veras_CV_ENG
pdflatex main.tex
pdflatex main.tex  # Segunda pasada para referencias
```

Si utilizas bibliografías, puedes necesitar pasos adicionales:

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

## 📁 Contenido del Repositorio

* **`shared/`**: Contiene todos los paquetes LaTeX compartidos para evitar duplicación:
  * `moderncv/`: Clase principal para el diseño del CV
  * `moderntimeline/`: Paquete para líneas de tiempo
  * `pdfpages/`, `xpatch/`: Paquetes auxiliares
  * `*_modifications/`: Modificaciones personalizadas
  * `template-*.tex`: Plantillas base reutilizables
* **`Arturo_Veras_CV_ESP/`**: Archivos específicos de la versión en español
* **`Arturo_Veras_CV_ENG/`**: Archivos específicos de la versión en inglés
* **`compile.sh`**: Script automatizado de compilación
* **`.gitignore`**: Configurado para ignorar archivos auxiliares de LaTeX pero incluir PDFs finales
* **`CHANGELOG.md`**: Registro de cambios significativos en el CV
* **`RELEASE_NOTES.md`**: Notas detalladas sobre versiones

## ✨ Características

* **Sin duplicación de código**: Los paquetes LaTeX se almacenan una sola vez en `shared/`
* **Compilación automatizada**: Script `compile.sh` para compilar fácilmente una o ambas versiones
* **Estructura limpia**: Solo los archivos específicos del idioma en cada carpeta
* **Rutas relativas**: Los archivos `.tex` referencian automáticamente los paquetes compartidos
* **Control de versiones optimizado**: Menos archivos duplicados en el historial de Git

## 🚀 Mejoras Implementadas

### v1.1.0 - Optimización de Estructura
- ✅ Eliminación de duplicación de paquetes LaTeX
- ✅ Creación de carpeta `shared/` para paquetes comunes
- ✅ Script de compilación automatizado
- ✅ Actualización de rutas en archivos `.tex`
- ✅ README mejorado con documentación completa

## Contacto

Si tienes alguna pregunta o sugerencia, no dudes en contactarme.
(Aquí puedes añadir tu email o enlace a LinkedIn si lo deseas)