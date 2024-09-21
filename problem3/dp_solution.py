from collections import defaultdict

def count_valid_groups(n, k, m, students_groups, students_exams):
    # Diccionarios para contar estudiantes por grupo y examen
    group_count = defaultdict(lambda: defaultdict(int))  # group_count[group][exam]
    exam_count = defaultdict(int)  # exam_count[exam]
    
    # Contamos los estudiantes por grupo y examen
    for i in range(m):
        group = students_groups[i]
        exam = students_exams[i]
        group_count[group][exam] += 1
        exam_count[exam] += 1

    # Función para calcular combinaciones nCk
    def comb(n, k):
        if n < k:
            return 0
        if k == 0 or n == k:
            return 1
        result = 1
        for i in range(k):
            result = result * (n - i) // (i + 1)
        return result
    
    # Contador de grupos válidos
    total_groups = 0
    
    # 1. Contar grupos dentro de cada aula
    for group in group_count:
        for exam in group_count[group]:
            count_in_group_exam = group_count[group][exam]
            total_groups += comb(count_in_group_exam, k)
    
    # 2. Contar grupos por examen independientemente del aula
    for exam in exam_count:
        count_in_exam = exam_count[exam]
        total_groups += comb(count_in_exam, k)
    
    return total_groups

