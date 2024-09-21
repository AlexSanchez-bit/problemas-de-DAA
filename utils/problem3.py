from enum import Enum
class SuspendedSignatures(Enum):
    P="POO"
    R="Recursividad"
    B="Both"
import random
def generate_random_example(students_number=None,classrooms=1,group_sizes=None):
    group_sizes = group_sizes if group_sizes is not None else random.randint(1,10)
    students_number = students_number if students_number is not None else random.randint(1,10)*group_sizes


    students_classrooms=[random.randint(0,classrooms) for _ in range(0,students_number)]
    students_signatures=[]
    for _ in range(0,students_number):
        rand = random.randint(0,1)
        if rand==0:
            students_signatures.append('P')
        elif rand ==1:
            students_signatures.append('R')
        else:
            students_signatures.append('B')


    return (students_number,students_classrooms,students_signatures,group_sizes)

