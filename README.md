# RpF - Repositorio de Formulaciones

RpF es un proyecto piloto de desarrollo de páginas estáticas para el contenido de cursos del departamento de ingeniería industrial de la Universidad de los Andes, liderado por la instructora Alfaima Solano para el curso Principios de Optimización (IIND-2103).

La idea es tener una página accesible por todos con escenarios de optimización que se prestan para la construcción de modelos de programación matemática lineales. Cada enunciado cuenta con una descripción del escenario y, para luego de que el estudiante haya intentado su propia implementación del modelo en _Python_, un modelo posible junto con su respectiva implementación haciendo uso de la librería _Pulp_.

Acceda a la página estática a través de este [enlace](https://alfaimasb.github.io/optimizacion/intro.html).

## Contribuir

Si tiene ideas o le gustaría ver cambios en el proyecto, no dude en diligenciar un _issue_.

Si gustaría contribuir al proyecto, realice un _Fork_ y haga sus cambios sugeridos. Una vez esté satisfecho con el resultado, vuelva a esta página y redacte un _Pull Request_ de su _Fork_ tanto para la rama 'master' como para la rama 'gh-pages'. Tenga en cuenta el siguiente procedimiento.

En su computador debe tener un ambiente virtual de _Python_ con los siguientes paquetes y sus dependencias. Recomendamos _Python 3.7_ con _Miniconda_ o _pipenv_. Si su sistema operativo es _Windows_, siga las instrucciones en este [enlace](https://jupyterbook.org/advanced/advanced.html?highlight=windows#working-on-windows) para trabajar con _Jupyter Book_.

 * Jupyter Book [(Proyect Home)](https://jupyterbook.org/intro.html) [(PyPI Install)](https://pypi.org/project/jupyter-book/)
 * Git [(Proyect Home)](https://git-scm.com/) [(Conda Install)](https://anaconda.org/anaconda/git)
 * ghp-import [(Conda install)](https://anaconda.org/conda-forge/ghp-import)

Recomendamos también usar _GitHub Desktop_ para hacer el manejo de versiones de su _Fork_.

 * Una vez tenga en su cuenta de _GitHub_ el _Fork_ del proyecto, clonelo a su computador.
 * Edite los archivos que consideres prudentes (Tenga en cuenta la documentación de _Jupyter Book_)
 * Bajor ninguna circunstancia edite los archivos de la carpeta '_build'. Este es un directorio derivado y se sobrescribirá con los cambios a los archivos .yml, .md y .ipynb.
 * Desde la terminal, active su ambiente virtual de _Python_ y dirijase al directorio donde clonó su proyecto (`$ cd path/to/../Github/optimizacion`).
 * El siguiente comanda construirá la página estática a partir de los archivos en el directorio:`jb build optimizacion` (si está en _Windows_, revise las instrucciones mencionadas anteriormente de la documentación).
 * Dirijase al directorio en '_build/html' dentro del proyecto y abra en su explorador web el archivo 'index.html'.
 * Verifique que no se haya roto ningún aspecto de la página y que se vean reflejado sus cambios.
 * Si hay errores o tiene cambios pendientes, realice sus cambios y vuelva a construir la página.
 * Haga _commit_ y _push_ de sus cambios a SU repositorio.
 * Desde la consola, ejecute el comando `ghp-import -n -p -f _build/html`
 * Ahora desde esta página del proyecto, realice los _pull request_ de su _Fork_ para las ramas 'master' y 'gp-pages'. Comente en buen detalle y de forma concisa sus cambios.

Algún dueño del proyecto evaluará su _PR_ y, según vea apropiado, aceptará, rechazará o sugerirá cambios.
