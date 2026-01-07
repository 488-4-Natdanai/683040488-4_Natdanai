from cat import Cat

cat1 = Cat("Milo", 3, "British Shorthair", "Gray")
cat2 = Cat.from_birth_year("Luna", 2015, "Siamese", "Cream")

print(cat1.meow())
print(cat1.play(2))
print(cat1.sleep(3))
print(cat1.eat(30))
print(cat1.get_status())

print()

print(cat2.meow())
print("Is Luna senior?", Cat.is_senior(cat2.age))
print("Recommended food:", Cat.calculate_healthy_food_amount(4), "grams")

print()

print("Species Info:", Cat.get_species_info())
