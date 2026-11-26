# **Proyecto: Selección del mejor frame con parámetros posturales para la estimación de pose en perros**

Para analizar la conducta de un perro a partir de video, se estima su pose en cada frame con SuperAnimal-Quadruped y se eligen los frames cuya pose es más confiable. Hasta ahora, esa elección se basa solo en la *likelihood* de los keypoints, que es la confianza del propio modelo: un frame puede tener una likelihood alta y, aun así, un esqueleto imposible.

En este proyecto se construye un score que combina la likelihood con los ángulos posturales de Ferres et al. y con proporciones de longitud de hueso, y se ajusta con Optuna para elegir los frames con menor error real respecto a la corrección manual.

El *notebook* `nb_proyecto_parametros_KP.ipynb` sigue el orden datos, exploración, preprocesamiento y partición, modelado, evaluación y conclusiones. En la exploración se eligen tres razas y dos videos por raza, y la evaluación deja fuera un video a la vez, con un estudio de ablación por grupo y por parámetro. Todo el modelado y la evaluación se repiten en tres baterías de seis videos, dos por raza, con los videos de calidad alta, media y baja según la exploración.

## Datos

Los datos provienen del proyecto de pose canina del grupo: videos de 10 razas del grupo 1 de la FCI (perros de pastor y boyeros), con 12 videos por raza. Cada video se procesó con SuperAnimal-Quadruped, adaptado al propio video sin etiquetas manuales, y de cada uno se extrajeron 24 frames que se corrigieron a mano. Por video hay tres fuentes:

* `1_superanimal`: un JSON con la predicción de todos los frames del video, con hasta dos detecciones por frame, cada una con su caja `[x, y, ancho, alto]`, el score de la caja y 39 keypoints (x, y, likelihood). La sección 1 verifica los JSON de los 120 videos; a partir de la sección 2.2 solo se usan los de Australian Cattle Dog, German Shepherd Dog y Shetland Sheepdog (36 archivos, 105 MB). Con solo esos 36, el notebook se ejecuta igual y únicamente cambia el inventario de la sección 1.
* `1_dlc`: un CSV de DeepLabCut (`CollectedData_sys.csv`) con los 24 frames seleccionados y sus 24 keypoints, para los 120 videos (3.4 MB).
* `1_dlc_hand_corrected`: los mismos frames corregidos a mano, con la misma estructura (2.7 MB). Un punto vacío indica que el anotador lo consideró ocluido.

Por su tamaño, la carpeta `data/` no se incluye en el repositorio (está en `.gitignore`) y los datos se solicitan al autor.

## Requisitos

Para ejecutar el proyecto, instalar las siguientes bibliotecas de python, en las versiones con las que se ejecutó el notebook:

```bash
pip install numpy==2.5.3 pandas==3.0.5 matplotlib==3.11.2 scipy==1.18.1 optuna==4.5.0 jupyter
```

## Referencias

Akiba, T., Sano, S., Yanase, T., Ohta, T., & Koyama, M. (2019). Optuna: A next-generation hyperparameter optimization framework. En *Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining* (pp. 2623-2631). https://doi.org/10.1145/3292500.3330701

Ferres, K., Schloesser, T., & Gloor, P. A. (2022). Predicting dog emotions based on posture analysis using DeepLabCut. *Future Internet, 14*(4), 97. https://doi.org/10.3390/fi14040097
