# **Práctica 4: Meta aprendizaje**

La presente práctica tiene como objetivo medir cuánto ganan los ensambles sobre clasificadores individuales ya bien ajustados y buscar el mejor modelo para un segundo problema. Se divide en dos partes:

* Parte 1, deserción estudiantil: a partir de los cinco clasificadores optimizados de la Práctica 3 (árbol de decisión, Naive Bayes, kNN, SVM y regresión logística), con el mismo preprocesamiento y los mismos pliegues, se estudian:
  * Bagging de árboles sin límite de profundidad (varianza).
  * AdaBoost con tocones (sesgo).
  * La correlación de los errores de los cinco modelos y su combinación con votación dura, votación suave y *stacking*.
  * Random Forest y Extra-Trees optimizados.
  * LightGBM y CatBoost optimizados.
  * La comparación de todos los modelos y la matriz de confusión del mejor.
* Parte 2, Bank Marketing: búsqueda del mejor modelo bajo un protocolo de validación cruzada fijo, comparando estrategias de balanceo de clases (pesos por clase y ajuste del umbral de decisión), LightGBM optimizado, Random Forest, CatBoost y votación suave. El mejor modelo se entrena con todos los datos y se guarda con `joblib`.

## Conjuntos de datos

### Deserción estudiantil (Parte 1)

El conjunto [Predict Students' Dropout and Academic Success](https://archive.ics.uci.edu/dataset/697), del *UCI Machine Learning Repository* (licencia CC BY 4.0), fue recopilado por Realinho *et al.* (2022). Reúne a estudiantes de licenciatura del Instituto Politécnico de Portalegre, en Portugal, que ingresaron entre los ciclos 2008/09 y 2018/19. Se utiliza únicamente `desercion-entrenamiento.csv`, de la carpeta `datos/` del repositorio del curso: 3,539 estudiantes con sus 36 atributos y la variable objetivo `Target` (Graduate 1,767, Dropout 1,137 y Enrolled 635).

Igual que en la Práctica 3, se usan los 30 atributos que se conocen al cierre del primer semestre:

* 9 nominales codificados como números enteros.
* 8 binarios.
* 1 ordinal.
* 12 numéricos.

No hay valores faltantes ni registros duplicados.

### Bank Marketing (Parte 2)

El conjunto [Bank Marketing](https://archive.ics.uci.edu/dataset/222), del *UCI Machine Learning Repository* (licencia CC BY 4.0), fue recopilado por Moro *et al.* (2014). Reúne las campañas de mercadotecnia telefónica de un banco portugués realizadas entre mayo de 2008 y noviembre de 2010, en las que se ofrecía a cada cliente un depósito a plazo. Se utiliza el archivo `bank-additional-full.csv`, con 41,188 llamadas separadas por punto y coma. La variable objetivo `y` indica si el cliente contrató el depósito (`yes`, 4,640 llamadas, 11.3%) y se codifica como 1 (yes) y 0 (no).

Se elimina `duration`, la duración de la llamada, que solo se conoce al terminar la llamada. Quedan 19 atributos, que describen:

* Al cliente.
* El último contacto de la campaña.
* Las campañas anteriores.
* El contexto socioeconómico.

De ellos, 10 son categóricos y 9 numéricos. Los valores faltantes se codifican como la categoría `unknown` en los atributos categóricos y como 999 en `pdays`, cuando el cliente no había sido contactado antes. Los registros están ordenados por fecha.

## Requisitos

Para ejecutar el proyecto, instalar las siguientes bibliotecas de python, en las versiones con las que se ejecutó el notebook:

```bash
pip install numpy==2.5.2 pandas==3.0.5 matplotlib==3.11.0 scikit-learn==1.9.0 lightgbm==4.6.0 catboost==1.2.10 jupyter
```

Con otras versiones de scikit-learn, LightGBM o CatBoost, los resultados pueden ser ligeramente diferentes.

## Instrucciones de uso

Ejecutar las celdas en orden. Las semillas fijan los pliegues de la validación cruzada y las búsquedas de hiperparámetros, por lo que los resultados son reproducibles:

* En la Parte 1, la semilla es `ran = 42`
* En la Parte 2, los pliegues usan `random_state=2026`

La ejecución completa tarda alrededor de 45 minutos con dos núcleos, la mayor parte en las búsquedas de hiperparámetros.

Al terminar, el notebook genera el archivo `.joblib`, en la misma carpeta que el notebook. Es el único archivo de resultados del proyecto y contiene el modelo final de Bank Marketing: un *pipeline* con la codificación *one-hot*, LightGBM optimizado y el umbral de decisión ajustado para maximizar el F1 macro, entrenado con todas las llamadas. Recibe un DataFrame con los 19 atributos de `bank-additional-full.csv` (sin `duration` ni `y`) y predice 1 o 0:

```python
import joblib
import pandas as pd

modelo = joblib.load('"...".joblib')
banco = pd.read_csv('data/bank-additional-full.csv', sep=';')
predicciones = modelo.predict(banco.drop(columns=['duration', 'y']))
```

