import numpy as np

estudiantes = np.array([
    (101, "Juan Perez", 1, 4.5, 1989, True),
    (102, "Maria Gomez", 2, 3.8, 1995, False),
    (103, "Carlos Ruiz", 1, 4.2, 1988, True),
    (104, "Ana Lopez", 3, 4.7, 1990, False),
    (105, "Luis Martinez", 1, 3.9, 1987, True),
], dtype=[("codigo", "i4"), ("nombre", "U20"), ("carrera", "i4"), ("promedio", "f4"), ("año_ingreso", "i4"), ("condicional", "?")])

print("Códigos de carreras:")
print("1: Ingeniería")
print("2: Humanas")
print("3: Salud")

codigoCarrera = int(input("Ingrese el código numérico de la carrera a listar: "))

filtroCarrera = (estudiantes["carrera"] == codigoCarrera) & (estudiantes["promedio"] >= 4)
estudiantesFiltrados = estudiantes[filtroCarrera]

print(f"\nEstudiantes de la carrera {codigoCarrera} con promedio >= 4:")
for est in estudiantesFiltrados:
    print(f"Código: {est['codigo']}, Nombre: {est['nombre']}")
print(f"Total: {len(estudiantesFiltrados)} estudiantes")

filtroCondicionales = (estudiantes["año_ingreso"] < 1990) & (estudiantes["condicional"])
estudiantesCondicionales = estudiantes[filtroCondicionales]

print("\nEstudiantes que ingresaron antes de 1990 y están condicionales:")
for est in estudiantesCondicionales:
    print(f"Código: {est['codigo']}, Nombre: {est['nombre']}")
print(f"Total: {len(estudiantesCondicionales)} estudiantes")
