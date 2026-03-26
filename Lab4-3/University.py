from datetime import date, datetime

class Person:
    _running_id = 1

    def __init__(self, name, age, birthdate, bloodgroup, is_married):
        self.name = name
        self.age = age
        self._birthdate = birthdate
        self.__bloodgroup = bloodgroup
        self.__is_married = is_married
        self._id = self.__generate_id()

    def __generate_id(self):
        year = datetime.now().year
        pid = f"{year}{Person._running_id:03d}"
        Person._running_id += 1
        return pid

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"ID: {self._id}")


class Staff(Person):
    def __init__(self, name, age, birthdate, bloodgroup, is_married,
                 department, start_year, salary=0):
        super().__init__(name, age, birthdate, bloodgroup, is_married)
        self.department = department
        self.start_year = start_year
        self.tenure_year = self.__calculate_tenure()
        self.__salary = salary

    def __calculate_tenure(self):
        return datetime.now().year - self.start_year

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")
        print(f"Tenure: {self.tenure_year}")
        print(f"Salary: {self.__salary}")


class Student(Person):
    def __init__(self, name, age, birthdate, bloodgroup, is_married,
                 start_year, major, level, grade_list=None):
        super().__init__(name, age, birthdate, bloodgroup, is_married)
        self.start_year = start_year
        self.major = major
        self.level = level
        self.grade_list = grade_list or []
        self.gpa = self.calculate_instance_gpa()
        self.__graduation_date = self.__calculate_graduation_date()

    @staticmethod
    def calculate_gpa(credit_list, grade_list):
        grade_map = {"A":4,"B":3,"C":2,"D":1,"F":0}
        total = 0
        credits = 0
        for c,g in zip(credit_list, grade_list):
            total += c * grade_map[g]
            credits += c
        return total / credits if credits else 0

    def calculate_instance_gpa(self):
        if not self.grade_list:
            return 0
        credit = [c for c,g in self.grade_list]
        grade = [g for c,g in self.grade_list]
        return Student.calculate_gpa(credit, grade)

    def __calculate_graduation_date(self):
        if self.level == "undergraduate":
            return date(self.start_year + 4, 1, 1)
        return date(self.start_year + 2, 1, 1)

    def display_info(self):
        super().display_info()
        print(f"Major: {self.major}")
        print(f"Level: {self.level}")
        print(f"GPA: {self.gpa:.2f}")


class Professor(Staff):
    def __init__(self, name, age, birthdate, bloodgroup, is_married,
                 department, start_year, professorship, admin_position=0):
        super().__init__(name, age, birthdate, bloodgroup, is_married,
                         department, start_year)
        self.professorship = professorship
        self.admin_position = admin_position
        self.set_salary()

    def set_salary(self):
        salary = 30000 + self.tenure_year*1000 + self.professorship*10000 + self.admin_position*10000
        super().set_salary(salary)

    def display_info(self):
        super().display_info()
        print(f"Professorship: {self.professorship}")
        print(f"Admin Position: {self.admin_position}")


class Administrator(Staff):
    def __init__(self, name, age, birthdate, bloodgroup, is_married,
                 department, start_year, admin_position):
        super().__init__(name, age, birthdate, bloodgroup, is_married,
                         department, start_year)
        self.admin_position = admin_position
        self.set_salary()

    def set_salary(self):
        salary = 15000 + self.tenure_year*800 + self.admin_position*5000
        super().set_salary(salary)

    def display_info(self):
        super().display_info()
        print(f"Admin Position Level: {self.admin_position}")


class UndergraduateStudent(Student):
    def __init__(self, name, age, birthdate, bloodgroup, is_married,
                 start_year, major, level, club=None, course_list=None, grade_list=None):
        super().__init__(name, age, birthdate, bloodgroup, is_married,
                         start_year, major, level, grade_list)
        self.club = club
        self.course_list = course_list or []

    def register_course(self, course):
        self.course_list.append(course)

    def display_info(self):
        super().display_info()
        print(f"Club: {self.club}")
        print(f"Courses: {self.course_list}")


class GraduateStudent(Student):
    def __init__(self, name, age, birthdate, bloodgroup, is_married,
                 start_year, major, level, advisor_name, grade_list=None):
        super().__init__(name, age, birthdate, bloodgroup, is_married,
                         start_year, major, level, grade_list)
        self.advisor_name = advisor_name
        self.thesis_name = None
        self.__proposal_date = None
        self._Student__graduation_date = self.expected_graduation_date()

    def expected_graduation_date(self):
        if self.__proposal_date:
            return self.__proposal_date.replace(year=self.__proposal_date.year + 1)
        return date.today().replace(year=date.today().year + 2)

    def set_thesis_name(self, name):
        self.thesis_name = name

    def set_proposal_date(self, pdate):
        self.__proposal_date = pdate
        self._Student__graduation_date = self.expected_graduation_date()

    def get_proposal_date(self):
        return self.__proposal_date

    def display_info(self):
        super().display_info()
        print(f"Advisor: {self.advisor_name}")
        print(f"Thesis: {self.thesis_name}")
        print(f"Proposal Date: {self.__proposal_date}")
