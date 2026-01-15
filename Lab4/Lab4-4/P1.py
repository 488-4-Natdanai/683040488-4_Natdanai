from room import Bedroom, Kitchen

print("----- Bedroom Test -----")
b1 = Bedroom(12, 10, 5)
print(b1.describe_room())
print("Bed size:", b1.bed_size, "ft")
print("Lighting:", b1.get_recommended_lighting(), "lumens/sq ft")
print("Area:", b1.calculate_area(), "sq ft")

print("\n----- Kitchen Test (with island) -----")
k1 = Kitchen(15, 12)
print(k1.describe_room())
print("Lighting:", k1.get_recommended_lighting(), "lumens/sq ft")
island, wall = k1.calculate_counter_space()
print("Island counter area:", island)
print("Wall counter area:", wall)

print("\n----- Kitchen Test (no island) -----")
k2 = Kitchen(15, 12, has_island=False)
print(k2.describe_room())
island, wall = k2.calculate_counter_space()
print("Island counter area:", island)
print("Wall counter area:", wall)
help(k2.calculate_counter_space)