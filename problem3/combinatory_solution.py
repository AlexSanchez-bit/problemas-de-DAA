
def count_sets(students, k):
    from collections import defaultdict
    from math import comb

    # Contar estudiantes por grupo y examen
    group_count = defaultdict(int)
    exam_count = defaultdict(int)
    combined_count = defaultdict(int)

    for (group, exam) in students:
        group_count[group] = group_count[group] + 1
        exam_count[exam] = exam_count[exam] + 1
        combined_count[(group, exam)] = combined_count[(group, exam)] + 1

    total_sets = 0
    
    # Contar grupos de tamaño k por aula
    for count in group_count.values():
        if count >= k:
            tmp = comb(count, k)
            total_sets += tmp

    # Contar grupos de tamaño k por examen
    for count in exam_count.values():
        if count >= k:
            tmp = comb(count, k)
            total_sets += tmp

    # Contar grupos de tamaño k por aula y examen
    for count in combined_count.values():
        if count >= k:
            tmp = comb(count, k)
            total_sets -= tmp

    return total_sets
