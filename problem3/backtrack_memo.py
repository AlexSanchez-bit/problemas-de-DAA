
group_formed = []
memo = {}
def backtrack_solution(students, students_classrooms, students_signatures, group_size):
    global group_formed, memo
    group_formed = []
    memo = {}
    backtrack(students, students_classrooms, students_signatures, group_size, [], 0)
    print(group_formed)

def backtrack(students, students_classrooms, students_signatures, group_size, group, last_taken):
    global group_formed, memo
    
    # Convierte el estado actual (grupo y last_taken) en una clave para memoización
    state = (tuple(group), last_taken)
    
    # Verifica si ya se ha calculado este estado
    if state in memo:
        return memo[state]
    
    if len(group) == group_size:
        if (all(students_classrooms[group[0]] == students_classrooms[stud] for stud in group) or
            all(students_signatures[group[0]] == students_signatures[stud] or students_signatures[stud] == 'B' for stud in group)):
            group_formed.append(group[:])
            memo[state] = 1  # Guarda el resultado en el memo
            return 1
        memo[state] = 0  # Si no es válido, también lo guardamos
        return 0

    total = 0
    for i in range(last_taken, students):
        if len(group) < group_size:
            group.append(i)
            total += backtrack(students, students_classrooms, students_signatures, group_size, group, i + 1)
            group.pop()
    
    memo[state] = total  # Guarda el resultado total de este estado
    return total

