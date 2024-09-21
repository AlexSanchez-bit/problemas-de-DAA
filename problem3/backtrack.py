def backtrack_solution(students, students_classrooms, students_signatures, group_size):
    global group_formed
    group_formed = []
    ret = backtrack(students, students_classrooms, students_signatures, group_size, [], 0)
    return ret

group_formed = []
aula = []
exam = []
both = 0

def backtrack(students, students_classrooms, students_signatures, group_size, group, last_taken):
    global group_formed
    global aula
    global exam
    global both

    # Verificar si el grupo tiene el tamaño correcto
    if len(group) == group_size:
        if (all(students_classrooms[group[0]] == students_classrooms[stud] for stud in group) and
            all(students_signatures[group[0]] == students_signatures[stud] or students_signatures[stud] == 'B' for stud in group)):
            both += 1
        if all(students_classrooms[group[0]] == students_classrooms[stud] for stud in group):
            return 1
        if all(students_signatures[group[0]] == students_signatures[stud] for stud in group):
            return 1
        return 0  # Terminar la recursión si se ha alcanzado el tamaño del grupo

    total = 0
    for i in range(last_taken, students):
        group.append(i)  # Agregar el índice del estudiante
        total += backtrack(students, students_classrooms, students_signatures, group_size, group, i + 1)
        group.pop()  # Eliminar el último estudiante agregado

    return total
