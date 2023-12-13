# Sequence Types

# Note: use print() to execute the examples. Comment out examples as needed to keep your Terminal
# output clean.

# Creating Lists
# 1. ✅ Create a list of 10 pet names
pet_names = [
    "Rose",
    "Meow Meow Beans",
    "Mr.Legumes",
    "Tom",
    "Luke",
    "Lea",
    "Lea",
    "Princess Grace",
    "Spot",
    "Tom",
    "Mini",
    "Paul",
]

# Reading Information From Lists
# 2. ✅ Return the first pet name
# print(pet_names[0])

# 3. ✅ Return all pet names beginning from the 3rd index
# print(pet_names[2:])

# 4. ✅ Return all pet names before the 3rd index
# print(pet_names[0:2])

# 5. ✅ Return all pet names beginning from the 3rd index and up to the 7th
# print(pet_names[2:6])

# 6. ✅ Find the index of a given element => .index()
# print(pet_names.index("Tom"))

# 7. ✅ Reverse the original list => .reverse()
# pet_names.reverse()
# print(pet_names)
# 8. ✅ Return the frequency of a given element => .count()
# print(pet_names.count("Tom"))

# Updating Lists
# 9. ✅ Change the first name to all uppercase letters => .upper()
# pet_names[0] = pet_names[0].upper()

# print(pet_names)

# 10. ✅ Append a new name to the list => .append()
# pet_names.append("Jacob")

# print(pet_names)

# 11. ✅ Add a new name at a specific index => .insert()
# pet_names.insert(2, "Jacob")

# print(pet_names)

# 12. ✅ Add two lists together => +
l1 = [1, 2, 3, 3, 3, 4, 4]
l2 = [3, 4]

l3 = l1 + l2
# print(l3)

# 13. ✅ Remove the final element from the list => .pop()
# pet_names.pop()

# print(pet_names)

# 14. ✅ Remove element by specific index => .pop()
# pet_names.pop(-2)

# print(pet_names)

# 15. ✅ Remove a specific element => .remove()
# pet_names.remove("Mini")
# print(pet_names)

# 16. ✅ Remove all pet names from the list => .clear()
# pet_names.clear()
# print(pet_names)

# Tuple
# 📚 Review:
# Mutable, Immutable <=> Changeable, Unchangeable

# 17. ✅ Create a Tuple of 10 pet ages => ()
pet_ages = (2, 2, 3, 10, 4, 5, 2, 4, 7, 1)

# 18. ✅ Print the first pet age => []
# print(pet_ages[0])

# Testing Mutability
# 19. ✅ Attempt to remove an element with ".pop" (should error)
# pet_ages.pop()

# 20. ✅ Attempt to change the first element (should error) => []
# pet_ages[0] = 5

# Tuple Methods
# 21. ✅ Return the frequency of a given element => .count()
# print(pet_ages.count(2))

# 22. ✅ Return the index of a given element  => .index()
# print(pet_ages.index(10))

# 23. ✅ Create a Range
# Note:  Ranges are primarily used in loops
# print(range(2, 10))

# Sets (Stretch Goal)
# 24. ✅ Create a set of 3 pet foods
pet_fav_food = {"house plants", "fish", "bacon"}
unique_names = set(pet_names)
# print(unique_names)
# Dictionaries
# Creating
# 25. ✅  Create a dictionary of pet information with the keys "name", "age" and "breed"
pet_info_rose = {"name": "Rose", "age": 11, "breed": "domestic long"}


# 26. ✅  Use dict to create a dictionary of pet information with the keys "name", "age" and "breed" => dict(...)
pet_info_spot = dict(name="Spot", age=25, breed="boxer")

# Reading
# 27. ✅ Print the pet attribute of "name" using bracket notation
# print(pet_info_rose["breed"])

# 28. ✅ Print the pet attribute of "age" using ".get"
# print(pet_info_rose.get("temperament"))
# Note: ".get" is preferred over bracket notation in most cases
# because it will return "None" instead of an error


# Updating
# 29. ✅ Update Rose's age to 12 => []
# pet_info_rose["age"] = 12

# print(pet_info_rose)

# 30. ✅ Update Spot's age to 26 => .update({...})
pet_info_spot.update({"age": 26, "name": "spot"})
# print(pet_info_spot)
# Deleting
# 31. ✅ Delete Rose's age using the "del" keyword => []
# del pet_info_rose["age"]

# print(pet_info_rose)

# 32. ✅ Delete Spot's age using ".pop"
pet_info_spot.pop("age")
# print(pet_info_spot)

# 33. ✅ Delete the last item for Rose using "popitem()"
pet_info_rose.popitem()
# print(pet_info_rose)

# Loops
pet_info = [
    {
        "name": "Rose",
        "age": 11,
        "breed": "domestic long-haired",
    },
    {
        "name": "Spot",
        "age": 25,
        "breed": "boxer",
    },
    {
        "name": "Meow Meow Beans",
        "age": 2,
        "breed": "domestic long-haired",
    },
    {
        "name": "Fran",
        "age": 1,
        "breed": "domestic long-haired",
    },
]

# 34. ✅ Loop through a range of 10 and print every number within the range
ra = range(10)
# for num in ra:
#     print(num)

# 35. ✅ Loop through a range between 50 and 60 that iterates by 2 and print every number
# for num in range(50, 60, 2):
#     print(num)

# 36. ✅ Loop through the "pet_info" list and print every dictionary
# for pet_dict in pet_info:
#     print(pet_dict)


# 37. ✅ Create a function that takes a list a parameter
# The function should use a "for" loop to loop through the list and print each item
# Invoke the function and pass it "pet_names" as an argument
# def print_elements(l):
#     for e in l:
#         print(e)


# print_elements(pet_names)


# 38. ✅ Create a function that takes a list as a parameter
# The function should define a counter and set it to 0
# Create a "while" loop
# The loop will continue as long as the counter is less than the length of the list
# Every loop should increase the count by 1
# Return the counter
def looper(l):
    counter = 0
    while counter < len(l):
        counter += 1
        # print(counter)

    return counter


# print(looper([1, 1, 1, 1]))
# 39. ✅ Create a function that updates the age of a given pet
# The function should take a list of "dictionaries", "name" and "age" as parameters
# Create an index variable and set it to 0
# Create a while loop
# The loop will continue so long as the list does not contain a name matching the "name" param
# and the index is less then the length of the list
# Every list will increase the index by 1
# If the dictionary containing a matching name is found, update the item's age with the new age
# Otherwise, return 'Pet not found'
def update_age(dicts, name, age):
    index = 0
    while index < len(dicts):
        if dicts[index].get("name") == name:
            dicts[index]["age"] = age
            return dicts[index]
        index += 1
    return "Pet not found"


# print(update_age(pet_info, "Spot", 20))


# map like
# 40. ✅ Use list comprehension to return a list containing every pet name from "pet_info" changed to uppercase
# print([pet_dict.get("name").upper() for pet_dict in pet_info])

# print(pet_info)
# find like
# 41. ✅ Use list comprehension to find a pet named spot

# print([pet_dict for pet_dict in pet_info if pet_dict.get("name") == "Spot"][0])
# filter like
# 42. ✅ Use list comprehension to find all of the pets under 3 years old
# print([pet_dict.get("name") for pet_dict in pet_info if pet_dict.get("age") < 3])

# 43. ✅ Create a generator expression matching the filter above
gen = (pet.get("name") for pet in pet_info if pet.get("age") < 3)

print(gen)

for name in gen:
    print(name)
