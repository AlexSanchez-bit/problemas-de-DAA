
from collections import defaultdict
from math import comb
def count_sets(students, k):
    from collections import defaultdict

    # Paso 1: Identificar grupos y asignaturas únicas
    groups = set()
    exams = set()

    for student in students:
        group, exam = student
        groups.add(group)
        exams.add(1 if exam=='R' else 2)

    # Paso 2: Inicialización de la tabla de DP
    dp = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

    # Estado inicial: Hay exactamente 1 forma de seleccionar 0 estudiantes
    for group in groups:
        for exam in exams:
            dp[group][1 if exam=='R' else 2][0] = 1

    # Paso 3: Rellenar la tabla DP considerando cada estudiante
    for student in students:
        group, exam = student 
        for count in range(1, k + 1):
            # Actualizar DP considerando diferentes subproblemas
            dp[group][1 if exam=='R' else 2][count] = dp[group][0 if exam=='R' else 0][count - 1]
            dp[group][1 if exam=='R' else 2][count] += dp[group - 1][0 if exam=='R' else 0][count]
            dp[group][1 if exam=='R' else 2][count] += dp[group][(1 if exam=='R' else 2) - 1][count]
            dp[group][1 if exam=='R' else 2][count] -= dp[group - 1][ (1 if exam=='R' else 2)  - 1][count]

    # Paso 4: Obtener el resultado final sumando los casos de tamaño k
    result = 0
    for group in groups:
        for exam in exams:
            result += dp[group][1 if exam=='R' else 2][k]

    return result
