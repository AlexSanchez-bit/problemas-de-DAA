
def count_sets(students, k):
    from collections import defaultdict
    from math import comb

    # Contar estudiantes por grupo y examen
    group_count = defaultdict(list)
    exam_count = defaultdict(list)
    combined_count = defaultdict(list)

    for student_id, (group, exam) in enumerate(students):
        group_count[group].append(student_id)
        exam_count[exam].append(student_id)
        combined_count[(group, exam)].append(student_id)

    total_sets = 0

    comb_aula=0
    comb_exam=0
    comb_comb=0
    # Contar grupos de tamaño k por aula
    for group, student_ids in group_count.items():
        count = len(student_ids)
        if count >= k:
            tmp = comb(count, k)
            total_sets += tmp
            comb_aula+=tmp

    # Contar grupos de tamaño k por examen
    for exam, student_ids in exam_count.items():
        count = len(student_ids)
        if count >= k:
            tmp = comb(count, k)
            total_sets += tmp
            comb_exam+=tmp

    # Contar grupos de tamaño k por aula y examen
    for (group, exam), student_ids in combined_count.items():
        count = len(student_ids)
        if count >= k:
            tmp = comb(count, k)
            total_sets -= tmp
            comb_comb+=tmp
    

    return total_sets
