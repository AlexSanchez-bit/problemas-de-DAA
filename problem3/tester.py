from problem3.backtrack import backtrack_solution
from problem3.dp_solution import count_valid_groups
from utils.problem3 import generate_random_example


example = generate_random_example(students_number=9,classrooms=3,group_sizes=3)
print(example)
students,students_classrooms,students_signatures,group_sizes = example

resp_backtrack = backtrack_solution(students,students_classrooms,students_signatures,group_sizes)

print('Conjuntos Validos por backtrack',resp_backtrack)

result = count_valid_groups(3, group_sizes, students, students_classrooms, students_signatures)
print(f'Número total de conjuntos válidos dp: {result}')

def main():
    pass