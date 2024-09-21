
def backtrack_solution(students, students_classrooms, students_signatures, group_size):
    global group_formed
    group_formed=[]
    ret = backtrack(students, students_classrooms, students_signatures, group_size, [], 0)
    print('total formados: ',group_formed)
    return ret

group_formed=[]
def backtrack(students,students_classrooms,students_signatures,group_size,group,last_taken):
    global group_formed
    if last_taken == students:
        return 0
    if(len(group)==group_size):
        group_formed.append(group)
        if(all(students_classrooms[group[0]]== students_classrooms[stud] for stud in group)):
            print('funciona aula ',group)

            return 1
        if(all(students_signatures[group[0]]== students_signatures[stud] or students_signatures[stud]=='B' for stud in group)):
            print('funciona grupo ',group)
            return 1
        print('no funciona: ',group)
        print([students_classrooms[stud] for stud in group])
        print([students_signatures[stud] for stud in group])
        return 0
    
    total=0
    group.append(last_taken)
    total+= backtrack(students,students_classrooms,students_signatures,group_size,group,last_taken+1)
    group.pop()
    total+= backtrack(students,students_classrooms,students_signatures,group_size,group,last_taken+1)

    return total
    