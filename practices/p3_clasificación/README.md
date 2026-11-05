# **Práctica 3: Tarea de clasificación**

La presente práctica tiene como objetivo construir un clasificador que prediga, al cierre del primer semestre, la situación que tendrá un estudiante al final de la duración normal de su carrera: graduado (`graduate`), desertor (`dropout`) o todavía inscrito (`enrolled`). Se comparan cinco clasificadores (árbol de decisión, Naive Bayes, k vecinos más cercanos, máquinas de soporte vectorial y regresión logística), con el F1 macro como métrica principal, a lo largo de las siguientes etapas:
* Descripción del conjunto de datos.
* Preprocesamiento por clasificador, dentro de un `Pipeline`.
* Optimización de hiperparámetros con búsqueda bayesiana (Optuna) y validación cruzada estratificada.
* Comparación de los clasificadores.
* Matriz de confusión y análisis de la clase desertor.
* Estimación con datos del cierre del segundo semestre.
* Clasificador final y predicciones.
* Discusión y conclusiones.

## Conjunto de datos

El conjunto de datos utilizado fue [Predict Students' Dropout and Academic Success](https://archive.ics.uci.edu/dataset/697), del *UCI Machine Learning Repository* (licencia CC BY 4.0), recopilado por Realinho *et al.* (2022). Contiene a 4,424 estudiantes de licenciatura del Instituto Politécnico de Portalegre, en Portugal, que ingresaron entre los ciclos 2008/09 y 2018/19, y se distribuye en dos archivos de la carpeta `datos/` del repositorio del curso:
* `desercion-entrenamiento.csv`: 3,539 estudiantes con un identificador (`id`), sus 36 atributos y la variable objetivo `Target` (Graduate 1,767, Dropout 1,137 y Enrolled 635).
* `desercion-prueba.csv`: 885 estudiantes con su `id` y únicamente los 30 atributos que se conocen al cierre del primer semestre, sin `Target` ni los seis atributos del segundo semestre.

Los atributos describen la inscripción del estudiante (perfil, antecedentes académicos y situación socioeconómica), los indicadores macroeconómicos del año de ingreso y su desempeño en el primer y segundo semestres. De ellos, 9 son nominales codificados como números enteros, 8 binarios, 1 ordinal y 18 numéricos. No hay valores faltantes ni registros duplicados. El significado de cada código se encuentra en la ficha del conjunto de datos en UCI.

## Requisitos

Para ejecutar el proyecto, instalar las siguientes bibliotecas de python, en las versiones con las que se ejecutó el notebook:

```bash
pip install numpy==2.5.2 pandas==3.0.5 matplotlib==3.11.0 scikit-learn==1.9.0 optuna==5.0.0 jupyter
```

Con otras versiones de scikit-learn u Optuna, la búsqueda de hiperparámetros puede seguir un camino distinto y llegar a resultados ligeramente diferentes.

## Instrucciones de uso

Lo siguiente es colocar los dos archivos del conjunto de datos en una carpeta `data/`, en la misma carpeta donde se encuentre el notebook. 

Ejecutar las celdas en orden (o *Restart & Run All*). La semilla (`ran = 42`) fija los pliegues de la validación cruzada y la búsqueda de hiperparámetros, por lo que los resultados son reproducibles. La optimización de los cinco clasificadores tarda alrededor de 15 minutos, la mayor parte en el SVM y la regresión logística.

Al terminar, el notebook genera el archivo `predicciones.csv`, en la misma carpeta que el notebook. Es el único archivo de resultados del proyecto y contiene las predicciones del clasificador final para los 885 estudiantes de prueba, con exactamente dos columnas: `id` y `Target`, cuyos valores son `dropout`, `enrolled` o `graduate`.