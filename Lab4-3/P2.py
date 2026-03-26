from University import Student, Professor, Administrator, UndergraduateStudent, GraduateStudent
from datetime import date
print("----- Professor Test -----")
p1 = Professor(
    name="Dr. Alan", age=45, birthdate="1979-01-01", bloodgroup="O", is_married=True
    , department="Computer Science", start_year=2010, professorship=3, admin_position=1)

p1.display_info()
print("\n----- Administrator Test -----")
a1 = Administrator(name="Ms. Linda", age=40,birthdate="1984-02-02", bloodgroup="A", is_married=True
                   , department="Finance", start_year=2015, admin_position=2)

a1.display_info()

print("\n----- Undergraduate Student Test -----")
u1 = UndergraduateStudent(name="Tom", age=20, birthdate="2005-03-03", bloodgroup="B", is_married=False, start_year=2023
                          , major="Game Design", level="undergraduate", club="Game Club", course_list=["Python", "OOP"], grade_list=[(3,"A"), (3,"B")])
u1.register_course("AI")
u1.display_info()

print("\n----- Graduate Student Test -----")
g1 = GraduateStudent(name="Sara", age=24, birthdate="2001-04-04", bloodgroup="AB", is_married=False, start_year=2024
                     , major="Computer Science", level="graduate", advisor_name="Dr. Alan", grade_list=[(3,"A"), (3,"A")])
g1.set_thesis_name("AI in Game Development")
g1.set_proposal_date(date(2025, 6, 1))
g1.display_info()

print("\n----- GPA Static Method Test -----")
credits = [3,3,2]
grades = ["A","B","A"]
print("Calculated GPA:", Student.calculate_gpa(credits, grades))
