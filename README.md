# simulacion-cafeteria
Simulación de una cafetería escolar usando Python y SimPy
# Simulación de una Cafetería Escolar
#DE LA CRUZ OJEDA AARON
#GONZALEZ POOL JARED ARTURO
## Descripción

Este programa realiza una **simulación de una cafetería escolar** utilizando la biblioteca **SimPy de Python**.

El objetivo es representar el comportamiento de un grupo de estudiantes que llegan a una cafetería, esperan su turno para ser atendidos, reciben atención y finalmente salen del establecimiento.

La simulación utiliza una **cola de espera con un solo servidor**, es decir, solamente un estudiante puede ser atendido a la vez.

---

## Funcionamiento del programa

El programa solicita al usuario los siguientes datos:

* Número de estudiantes.
* Tiempo mínimo entre llegadas.
* Tiempo máximo entre llegadas.
* Tiempo mínimo de atención.
* Tiempo máximo de atención.

A partir de estos valores, el programa genera tiempos aleatorios para representar un escenario más realista.

### Flujo de la simulación

```text
Inicio
  ↓
Ingresar datos de la simulación
  ↓
Llegan los estudiantes
  ↓
¿La cafetería está disponible?
  ↓
 ┌───────────────┐
 │      NO       │ → El estudiante espera en la cola
 └───────────────┘
  ↓ SÍ
El estudiante es atendido
  ↓
Se registra el tiempo de espera
  ↓
Tiempo aleatorio de atención
  ↓
El estudiante sale
  ↓
¿Quedan estudiantes?
  ↓
 ┌───────┐
 │  SÍ   │ → Continúa la simulación
 └───────┘
  ↓ NO
Calcular promedio de espera
  ↓
Mostrar resultados
  ↓
Fin
```

---

## Algoritmo

El programa está dividido principalmente en dos procesos.

### 1. Proceso `estudiante()`

Esta función representa a cada estudiante.

Cuando un estudiante llega:

1. Se registra el momento de llegada.
2. Solicita acceso al recurso de la cafetería.
3. Si el recurso está ocupado, permanece esperando.
4. Cuando puede ser atendido, se calcula cuánto tiempo esperó.
5. Se genera un tiempo aleatorio de atención.
6. Al terminar, el estudiante abandona la cafetería.

El tiempo de atención se obtiene mediante:

```python
random.uniform(atencion_min, atencion_max)
```

Esto genera un valor aleatorio entre el tiempo mínimo y máximo establecido.

---

### 2. Proceso `llegadas()`

Esta función controla la llegada de los estudiantes.

Para cada estudiante:

1. Se genera un tiempo aleatorio entre llegadas.
2. Se espera ese tiempo.
3. Se crea el proceso correspondiente al estudiante.

Se utiliza:

```python
random.uniform(llegada_min, llegada_max)
```

para generar los intervalos aleatorios de llegada.

---

## Recurso de la cafetería

La cafetería se representa mediante un recurso de SimPy:

```python
cafeteria = simpy.Resource(env, capacity=1)
```

El valor `capacity=1` significa que **solo un estudiante puede ser atendido simultáneamente**.

Los demás estudiantes deben esperar hasta que el recurso quede disponible.

Esto permite simular una situación de **fila única con un servidor**.

---

## Tiempo de espera

Para cada estudiante se calcula el tiempo que permanece esperando antes de ser atendido.

La fórmula utilizada por el programa es:

```python
tiempo_espera = env.now - llegada
```

Donde:

* `env.now` representa el momento en que comienza la atención.
* `llegada` representa el momento en que llegó el estudiante.

Todos los tiempos de espera se almacenan en la lista:

```python
esperas = []
```

---

## Resultado

Al finalizar la simulación, se calcula el promedio de espera de los estudiantes:

```python
promedio = sum(esperas) / len(esperas)
```

Finalmente, se muestran:

* Número de estudiantes atendidos.
* Tiempo promedio de espera en minutos.

Ejemplo de salida:

```text
=== RESULTADOS ===
Estudiantes atendidos: 10
Tiempo promedio de espera: 2.47 minutos
```

---

## Tecnologías utilizadas

* Python
* SimPy
* Random

### Librerías

```python
import simpy
import random
```

---

## Ejecución

### 1. Instalar Python

Es necesario tener Python instalado en el equipo.

### 2. Instalar SimPy

Desde la terminal se puede instalar con:

```bash
pip install simpy
```

### 3. Ejecutar el programa

Guardar el código, por ejemplo, como:

```text
cafeteria.py
```

Después ejecutar:

```bash
python cafeteria.py
```

### 4. Introducir los datos

El programa solicitará los valores necesarios, por ejemplo:

```text
=== CAFETERÍA ESCOLAR ===
Número de estudiantes: 10
Tiempo mínimo entre llegadas: 1
Tiempo máximo entre llegadas: 3
Tiempo mínimo de atención: 2
Tiempo máximo de atención: 5
```

---

## Objetivo de la simulación

El propósito de este programa es **analizar el comportamiento de una fila de estudiantes en una cafetería**, utilizando eventos discretos y tiempos aleatorios.

La simulación permite observar cómo los tiempos de llegada y atención afectan directamente al tiempo que los estudiantes permanecen esperando.

---

## Conclusión

El programa permite representar de manera sencilla el funcionamiento de una cafetería con un solo punto de atención. Mediante SimPy se pueden controlar las llegadas, la formación de la fila, la atención y la salida de los estudiantes, obteniendo como resultado el **tiempo promedio de espera**.

Esto demuestra cómo la simulación puede utilizarse para analizar y comprender el comportamiento de sistemas que involucran **colas, recursos limitados y tiempos variables**.
