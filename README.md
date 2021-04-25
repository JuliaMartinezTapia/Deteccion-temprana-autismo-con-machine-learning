## Detección temprana de los trastornos del espectro autista (TEA) usando técnicas de machine learning
### Julia María Martínez Tapia
www.linkedin.com/in/juliamariamartineztapia

jmtcorreo@gmx.es


#### 31 de marzo de 2021

### Objetivo del proyecto

**El objetivo del presente trabajo es evaluar la utilidad de varios modelos de machine learning en la predicción temprana de casos de autismo.** 

**Premisas**:

+ A los efectos del presente proyecto se ha considerado mas perjudicial la obtención de falsos negativos que la obtención de falsos positivos.
Un falso negativo significa una persona que, sufriendo un TEA, es calificadas por el modelo como persona sin el trastorno y por tanto, una persona que puede no recibir un tratamiento médico que necesita para tener una calidad de vida aceptable.


**Es prioritario, por tanto, que el modelo de machine learning a implementar minimize la obtención de falsos negativos.**

+ Adicionalmente, dada la naturaleza del proyecto, las predicciones arrojadas por el algoritmo a implementar deben ser explicables, en el sentido de que sea posible determinar qué concretas variables han sido utilizadas para su realización y cual ha sido su relevancia a esos efectos.


**Por esta razón, se seleccionará el modelo de machine learning que maximize la precisión en la predicciones y la explicabilidad del resultado,  minimizando a su vez la obtención de falsos negativos.**


### Fuente de información


Fadi Fayez Thabtah, Department of Digital Technology, Manukau Institute of Technology, Auckland, New Zealand.

Los datos utilizados proceden de la fusión de tres datasets publicamente disponibles en el repositorio UCI.

+ Fadi Fayez Thabtah (2017), “Autistic Spectrum Disorder Screening Data for Adult” https://archive.ics.uci.edu/ml/machine-learning-databases/00426/

+ Fadi Fayez Thabtah (2017), “Autistic Spectrum Disorder Screening Data for children" https://archive.ics.uci.edu/ml/machine-learning-databases/00419/

+ Fadi Fayez Thabtah (2017), “Autistic Spectrum Disorder Screening Data for Adolescent” https://archive.ics.uci.edu/ml/machine-learning-databases/00420/

### Descripción del dataset

El dataset contiene 21 variables independientes, una columna target y 1100 registros.

Las variables independientes consisten en:

+ Diez variables consistentes en indicadores de comportamiento que señalan rasgos autistas (behavioural features);
+ Una variable denominada "screening_score" cuyos valores son la suma de los valores de los indicadores anteriormente mencionados, es decir, la puntuación obtenida en los indicadores, y,
+ por último, diez carácterísticas individuales que han probado su efectividad para detectar casos de TEA a partir de controles obtenidos de la ciencia del comportamiento.

Se puede encontrar más información sobre el dataset y las variables que contiene en este [enlace](https://www.kaggle.com/faizunnabi/autism-screening)

### Selección de variables

Para implementar los modelos de machine learning se ha eliminado la variable "screening_score", puesto que se corresponde exactamente con el sumatorio de las 10 variables indicadoras de comportamiento. Lógicamente tiene más sentido eliminar el screening_score y conservar las 10 variables que lo generan, que dan más información que su valor acumulado.

Por otra parte, resulta que el sumatorio de los valores de las 10 variables resultantes del cuestionario determina directamente la clase de las instancias, de forma que si tal sumatorio es 7 o superior, la clase de la instancia es 1 (es decir, autismo) y en caso contrario, la clase es 0 (no autismo). Por lo tanto, con el dataset completo realmente no es necesario implementar ningún modelo de machine learning, basta con atender a tal sumatorio.

Por ello, y considerando la enorme relevancia de la detección temprana en la capacidad de intervención en el desarrollo del trastorno, en este proyecto se ha tratado de reducir las variables del dataset indicadoras de comportamiento a aquellas que permiten su detección a menor edad, con el objetivo de favorecer la detección e intervención temprana.

**Por lo tanto, el objetivo final del proyecto ha sido la evaluar la utilidad de varios modelos de machine learning en la predicción de casos de autismo utilizando las variables de características individuales y aquellas variables indicadoras de comportamiento que permitan razonablemente su detección a menor edad, con el objetivo de favorecer la detección e intervención temprana del autismo.**

### Herramientas utilizadas

+ Notebook de Jupyter.
+ Numpy
+ Pandas
+ Matplotlib
+ Seaborn
+ Sklearn
+ Scipy
+ Tensorflow
+ Keras
+ Pickle

### Modelos de machine learning evaluados

- Logistic Regression
- Decision tree
- Random Forest Classifier (Bagging)
- ADA Boosting
- soft voting
- Neural network (deep learning)

##  Conclusión

La regresión logística es el modelo que mejor se ajusta a las premisas del proyecto:

+ Tiene un Accuracy razonable, en la posición 4º de los modelos evaluados.

+ Tiene el mejor Recall, y

+ Es un modelo razonablemente explicable.

