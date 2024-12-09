
#내 눈이 보이지않아 글을찾아 봐봐~ 나는~ 시력이 많이 안좋아~
#(? ?? ???않아~ 꽃을찾아 날아~ 나는~ 아주작은~ 애벌레~)

class Person:
    total_count = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.total_count += 1
    def introduce(self):
        print(f"제 이름은 {self.name}이고, 나이는 {self.age}살 입니다.")
p1 = Person('윤석열', 63)
p1.introduce()
p2 = Person('이재명', 61)
p2.introduce()
p3 = Person('문재인', 71)
p3.introduce()
"""
print(p3.total_count)
#-----------------------------오버라이딩-------------------------------#

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
    def run(self):
        print("저는 계엄선포 할 수 있어요.")
p1 = Person('윤석열', 63)
p1.introduce()
p2 = Person('이승엽', 61)
p2.introduce()
p3 = Person('이숭용', 71)
p3.introduce()
"""
class Student(Person):
    def __init__(self, name = '윤석열', age = '63'):
        super().__init__(self)
    def introduce(self):
        print(f"제 이름은 {self.name}이고, 나이는 비밀입니다.")
p1 = Person('윤석열', 63)
p1.introduce()
p2 = Person('이승엽', 61)
p2.introduce()
p3 = Person('이숭용', 71)
p3.introduce()

