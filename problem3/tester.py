from problem3.backtrack import backtrack_solution
from problem3.combinatory_solution import count_sets
from utils.problem3 import generate_random_example
from problem3.flux import Grafo
import random


def main():

    good=0
    total=1000
    for _ in range(0,total):
        example = generate_random_example(students_number=random.randint(10,20),classrooms=random.randint(3,10),group_sizes=random.randint(1,10))
        print(example)
        students,students_classrooms,students_signatures,group_sizes = example
        estudiantes = [
            (students_classrooms[student],students_signatures[student]) for student in range(students)
        ]
        resp_backtrack = backtrack_solution(students,students_classrooms,students_signatures,group_sizes)
        print('Conjuntos Validos por backtrack',resp_backtrack)
        c_sets=count_sets(estudiantes,group_sizes)
        print('dinamic sets: ',c_sets)
        good+= 1 if c_sets == resp_backtrack else 0
    print((good/total)*100 ,'% test passed')