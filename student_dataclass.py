from dataclasses import dataclass

@dataclass

# creating class student
class Student:

    name:str
    college_id: int
    GPA: float

def main():
    #students added with name/id and gpa
    Omar = Student('Omar', 67895, 3.5)
    Abdi = Student('Abdi', 76906, 2.0)

    print(Omar)
    print(Abdi)
  

main() 