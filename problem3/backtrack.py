
def backtrack_solution(students, students_classrooms, students_signatures, group_size):
    return backtrack(students, students_classrooms, students_signatures, group_size, [], 0)

def backtrack(students, students_classrooms, students_signatures, group_size, groups, last_taken):
    total_groups=0
    if last_taken == students:
        return 0

    groups.append([last_taken])
    groups_created=backtrack(students,students_classrooms,students_signatures,group_size,groups,last_taken+1)
    total_groups+=groups_created
    groups.pop()

    for group in groups:
        if(len(group)<group_size):
            if all(students_signatures[last_taken] == students_signatures[student] for student in group):
                group.append(last_taken)
                if len(group)==group_size:
                    total_groups+=1
                groups_created=backtrack(students,students_classrooms,students_signatures,group_size,groups,last_taken+1)
                total_groups+=groups_created
                group.pop()
                continue
            if all(students_classrooms[last_taken] == students_classrooms[student] for student in group):
                group.append(last_taken)
                if len(group)==group_size:
                    total_groups+=1
                groups_created=backtrack(students,students_classrooms,students_signatures,group_size,groups,last_taken+1)
                total_groups+=groups_created
                group.pop()
    return total_groups