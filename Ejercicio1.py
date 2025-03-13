import numpy as np

num_candidatos = 30
num_estudiantes = 5000

votos = np.random.randint(1, num_candidatos + 1, num_estudiantes)

conteo_votos = np.zeros(num_candidatos, dtype=int)  
for voto in votos:
    conteo_votos[voto - 1] += 1  

candidatos = np.arange(1, num_candidatos + 1)

resultados = np.column_stack((candidatos, conteo_votos))

resultados_ordenados = resultados[np.argsort(-conteo_votos)]

print("Candidato  Votos")
for candidato, votos in resultados_ordenados:
    print(f"{int(candidato):9}  {int(votos):5}")
