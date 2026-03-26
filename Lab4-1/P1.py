from datetime import datetime, timedelta
from cat import Cat

cat1 = Cat("Milo", "British Shorthair", 2, "Alice")
cat2 = Cat("Luna", "Siamese", 3, "Bob")
cat3 = Cat("Oreo", "Persian", 1, "Chris")

print("First cat date_in:")
print(cat1.get_time_in())

cat1.greet()
print()

print("Second cat date_out (before):")
print(cat2.get_time_out())

new_date_out = datetime.now() + timedelta(days=2)
cat2.set_time_out(new_date_out)

print("Second cat date_out (after +2 days):")
print(cat2.get_time_out())
print()

cat3.owner = "David"
cat3.age = 2

cat1.print_cat()
cat2.print_cat()
cat3.print_cat()

print("Total number of cats:", Cat.get_num())
Cat.reset_cat()
print("Total number of cats after reset:", Cat.get_num())
