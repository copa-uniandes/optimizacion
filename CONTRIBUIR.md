# Contribuir

Si gustaría contribuir al proyecto, realice un _Fork_ y haga sus cambios sugeridos. Una vez esté satisfecho con el resultado, vuelva a la página del pryecto en GitHub y redacte un _Pull Request_ de su _Fork_ para la rama 'master'. Tenga en cuenta el siguiente procedimiento.

En su computador debe tener un ambiente virtual de _Python_ con los siguientes paquetes y sus dependencias. Recomendamos _Python 3.7_ con _Miniconda_ o _pipenv_. Si su sistema operativo es _Windows_, siga las instrucciones en este [enlace](https://jupyterbook.org/advanced/advanced.html?highlight=windows#working-on-windows) para trabajar con _Jupyter Book_.

 * Jupyter Book ([Proyecto](https://jupyterbook.org/intro.html)) (Sin paquete de Conda) ([PyPI](https://pypi.org/project/jupyter-book/))
 * Git ([Proyecto](https://git-scm.com/)) ([Conda](https://anaconda.org/anaconda/git)) (Sin paquete de PyPI)

Recomendamos también usar _GitHub Desktop_ para hacer el manejo de versiones de su _Fork_.

 * Una vez tenga en su cuenta de _GitHub_ el _Fork_ del proyecto, clonelo a su computador.
 * Edite los archivos que considere prudentes (Tenga en cuenta la documentación de _Jupyter Book_).
 * Desde la terminal, active su ambiente virtual de _Python_ y dirijase al directorio donde clonó su proyecto (`$ cd path/to/../Github/optimizacion`).
 * El siguiente comando construirá la página estática a partir de los archivos en el directorio:`jb build optimizacion` (si está en _Windows_, revise las instrucciones mencionadas anteriormente de la documentación).
 * Dirijase al directorio en '_build/html' dentro del proyecto y abra en su explorador web el archivo 'index.html'.
 * Verifique que no se haya roto ningún aspecto del libro y que se vean reflejados sus cambios.
 * Si hay errores o tiene cambios pendientes, realice sus cambios y vuelva a construir el libro para validarlos.
 * Haga _commit_ y _push_ de sus cambios a su repositorio.
 * Tenga en cuenta que, al hacer un _Fork_, puede también crear una página propia de 'GitHub Pages' que podrá actualizar automáticamente según el contenido actualizado de su rama 'master' (Vea '.github/workflows').
 * Ahora, desde el repositorio origen del proyecto en GitHub, realice el _pull request_ de su _Fork_ a la rama 'master' del repositorio origen, desde la rama de SU _Fork_ con los últimos cambios. Comente en buen detalle y de forma concisa sus cambios.
 * Es responsabilidad de cada quien aliviar los conflictos de su _PR_.

Algún dueño del proyecto evaluará su _PR_ y, según vea apropiado, aceptará, rechazará o sugerirá cambios.