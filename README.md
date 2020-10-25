# RpF - Repositorio de Formulaciones

RpF es un proyecto piloto de desarrollo de páginas estáticas para el contenido de cursos del departamento de ingeniería industrial de la Universidad de los Andes, liderado por la instructora Alfaima Solano para el curso Principios de Optimización (IIND-2103).

La idea es tener una página accesible por todos con escenarios de optimización que se prestan para la construcción de modelos de programación matemática lineal-entera. Cada enunciado cuenta con una descripción del escenario y, para luego de que el estudiante haya intentado su propia implementación del modelo en _Python_, un modelo posible junto con su respectiva implementación haciendo uso de la librería _PuLP_.

Acceda a la página estática a través de este [enlace](https://alfaimasb.github.io/optimizacion/intro.html).

## Contribuir

Si tiene ideas o le gustaría ver cambios en el proyecto, no dude en diligenciar un _issue_.

Si gustaría contribuir al proyecto, realice un _Fork_ y haga sus cambios sugeridos. Una vez esté satisfecho con el resultado, vuelva a esta página y redacte un _Pull Request_ de su _Fork_ para la rama 'master'. Tenga en cuenta el siguiente procedimiento.

En su computador debe tener un ambiente virtual de _Python_ con los siguientes paquetes y sus dependencias. Recomendamos _Python 3.7_ con _Miniconda_ o _pipenv_. Si su sistema operativo es _Windows_, siga las instrucciones en este [enlace](https://jupyterbook.org/advanced/advanced.html?highlight=windows#working-on-windows) para trabajar con _Jupyter Book_.

 * Jupyter Book ([Proyecto](https://jupyterbook.org/intro.html)) (Sin paquete de Conda) ([PyPI](https://pypi.org/project/jupyter-book/))
 * Git ([Proyecto](https://git-scm.com/)) ([Conda](https://anaconda.org/anaconda/git)) (Sin paquete de PyPI)

Recomendamos también usar _GitHub Desktop_ para hacer el manejo de versiones de su _Fork_.

 * Una vez tenga en su cuenta de _GitHub_ el _Fork_ del proyecto, clonelo a su computador.
 * Edite los archivos que consideres prudentes (Tenga en cuenta la documentación de _Jupyter Book_)
 * Desde la terminal, active su ambiente virtual de _Python_ y dirijase al directorio donde clonó su proyecto (`$ cd path/to/../Github/optimizacion`).
 * El siguiente comanda construirá la página estática a partir de los archivos en el directorio:`jb build optimizacion` (si está en _Windows_, revise las instrucciones mencionadas anteriormente de la documentación).
 * Dirijase al directorio en '_build/html' dentro del proyecto y abra en su explorador web el archivo 'index.html'.
 * Verifique que no se haya roto ningún aspecto de la página y que se vean reflejado sus cambios.
 * Si hay errores o tiene cambios pendientes, realice sus cambios y vuelva a construir la página para validarlos.
 * Haga _commit_ y _push_ de sus cambios a SU repositorio.
 * Tenga en cuenta que al hacer un _Fork_ está también creando una página de 'GitHub Pages' que se actualizará automáticamente según el contenido actualizado de su rama 'master'.
 * Ahora, desde el hogar del proyecto en GitHub, realice los _pull request_ de su _Fork_ para la rama 'master' desde la rama 'master' de SU _Fork_. Comente en buen detalle y de forma concisa sus cambios.

Algún dueño del proyecto evaluará su _PR_ y, según vea apropiado, aceptará, rechazará o sugerirá cambios.

## Enlaces
 * [Universidad de los Andes](https://uniandes.edu.co/)
 * [Facultad de Ingeniería](https://ingenieria.uniandes.edu.co/)
 * [Departamento de Ingeniería Industrial](https://industrial.uniandes.edu.co/)

## Disclaimer

Este proyecto está en sus primeras etapas de desarrollo y, por lo tanto, puede tener errores o inconsistencias. Apreciamos cualquier aporte que puedan hacer para mejorar el contenido.
