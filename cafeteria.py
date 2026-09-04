import simpy
import random

def estudiante(env, numero, cafeteria, espera):
    llegada = env.now

    print(f"{env.now:.1f} min: Llega estudiante {numero}")

    with cafeteria.request() as turno:
        yield turno

        # Calcular espera
        tiempo_espera = env.now - llegada
        espera.append(tiempo_espera)

        print(f"{env.now:.1f} min: Atienden estudiante {numero}")

        # Tiempo de atención
        yield env.timeout(random.uniform(atencion_min, atencion_max))

        print(f"{env.now:.1f} min: Sale estudiante {numero}")


def llegadas(env):
    for i in range(1, estudiantes + 1):

        # Tiempo entre llegadas
        yield env.timeout(random.uniform(llegada_min, llegada_max))

        env.process(estudiante(env, i, cafeteria, esperas))


# -------------------------------
# DATOS
# -------------------------------

print("=== CAFETERÍA ESCOLAR ===")

estudiantes = int(input("Número de estudiantes: "))
llegada_min = float(input("Tiempo mínimo entre llegadas: "))
llegada_max = float(input("Tiempo máximo entre llegadas: "))
atencion_min = float(input("Tiempo mínimo de atención: "))
atencion_max = float(input("Tiempo máximo de atención: "))


# -------------------------------
# SIMULACIÓN
# -------------------------------

env = simpy.Environment()

# 1 persona puede ser atendida a la vez
cafeteria = simpy.Resource(env, capacity=1)

esperas = []

env.process(llegadas(env))
env.run()


# -------------------------------
# RESULTADO
# -------------------------------

promedio = sum(esperas) / len(esperas)

print("\n=== RESULTADOS ===")
print("Estudiantes atendidos:", estudiantes)
print(f"Tiempo promedio de espera: {promedio:.2f} minutos")