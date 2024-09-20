from problem3.backtrack import backtrack_solution
from utils.problem3 import generate_random_example


example = generate_random_example(students_number=9,classrooms=3,group_sizes=3)
print(example)
students,students_classrooms,students_signatures,group_sizes = example

resp_backtrack = backtrack_solution(students,students_classrooms,students_signatures,group_sizes)

print(resp_backtrack)

def main():
    pass