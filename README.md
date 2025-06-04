# Currículum Vitae - Arturo Veras

Este repositorio contiene las versiones de mi Currículum Vitae en diferentes idiomas, gestionadas con LaTeX.

## Versiones Disponibles

Actualmente, el CV está disponible en los siguientes idiomas:

* **Español (Spanish):**
  * [Ver CV en Español (PDF)](./Arturo_Veras_CV_ESP/nombre_del_archivo_cv_esp.pdf)
  * [Código Fuente (LaTeX)](./Arturo_Veras_CV_ESP/)
* **Inglés (English):**
  * [Ver CV en Inglés (PDF)](./Arturo_Veras_CV_ENG/nombre_del_archivo_cv_eng.pdf)
  * [Código Fuente (LaTeX)](./Arturo_Veras_CV_ENG/)

**Nota:** Por favor, reemplaza `nombre_del_archivo_cv_esp.pdf` y `nombre_del_archivo_cv_eng.pdf` con los nombres reales de tus archivos PDF una vez que los subas.

## Compilación (LaTeX)

Si deseas compilar los archivos `.tex` tú mismo, necesitarás una distribución de LaTeX instalada (como TeX Live, MiKTeX, o MacTeX).

La compilación generalmente se realiza con el comando:

```bash
pdflatex tu_archivo.tex
```

Podrías necesitar ejecutar el comando varias veces para resolver referencias cruzadas o bibliografías. Si se utiliza `bibtex` o `biber` para la bibliografía, los comandos serían algo como:

```bash
pdflatex tu_archivo.tex
bibtex tu_archivo # o biber tu_archivo
pdflatex tu_archivo.tex
pdflatex tu_archivo.tex
```

Si se utilizan paquetes específicos o un motor de LaTeX diferente (como XeLaTeX o LuaLaTeX), asegúrate de tenerlos instalados y utiliza el comando apropiado.

## Contenido del Repositorio

* `.gitignore`: Configurado para ignorar archivos auxiliares de LaTeX y otros archivos temporales, pero para incluir los PDFs finales.
* `CHANGELOG.md`: Registro de cambios significativos en el CV o en la estructura del repositorio.
* `RELEASE_NOTES.md`: Notas sobre las "versiones" del CV.
* `Arturo_Veras_CV_ESP/`: Carpeta con la versión en español (código fuente LaTeX y PDF).
* `Arturo_Veras_CV_ENG/`: Carpeta con la versión en inglés (código fuente LaTeX y PDF).

## Contacto

Si tienes alguna pregunta o sugerencia, no dudes en contactarme.
(Aquí puedes añadir tu email o enlace a LinkedIn si lo deseas)