# **Práctica 2: Pre-procesamiento del dataset**

La presente práctica tiene como objetivo realizar el pre-procesamiento de un conjunto de datos, partiendo de su exploración y detallando las siguientes etapas:
* Contexto y Procedencia.
* Estructura (y su verificación).
* Análisis de calidad de los datos.
* Análisis de una selección de atributos particulares.
* Limpieza
* Aumento de datos.
* Extracción de características.
* Reducción de dimensionalidad.
* Selección de características.

Para ejecutar el siguiente proyecto, descargar las siguientes bibliotecas de python

```bash
pip install pandas numpy matplotlib seaborn scipy "scikit-learn>=1.8,<2" jupyter
```

El conjunto de datos utilizado fue [Diabetes 130-US Hospitals for Years 1999-2008](https://archive.ics.uci.edu/dataset/296/diabetes-130-us-hospitals-for-years-1999-2008), del *UCI Machine Learning Repository* (licencia CC BY 4.0), y se puede descargar a través de su página:
https://archive.ics.uci.edu/dataset/296/diabetes-130-us-hospitals-for-years-1999-2008

Lo siguiente es descomprimir el archivo del conjunto de datos, justo en la carpeta dónde se encuentre este notebook. D

Ejecutar las celdas en orden. La semilla (`ran = 66`) fija las particiones y los procesos aleatorios, por lo que los resultados son reproducibles.