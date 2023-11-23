students = [(100,'Manas',19,'Male',('c++','c','python')),(101,'Nandini',19,'Female',('c++','c','python','HTML')),
            (100,'Aryan',69,'Male',('Maths','c','English')),(100,'Aru',19,'Female',('English','Maths','python')),
            (100,'Vasu',19,'Male',('Physics','Chemistry','Maths'))]
def age(students):
    total=sum(student[2] for student in students)
    return total/len(students)
print("average age: ", age(students))
'''def most_sub(students):
    return max(students,key=lambda x: len(x'''
