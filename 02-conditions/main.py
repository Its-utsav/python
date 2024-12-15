# 1. Age Group Categorization
# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

age = int(input('Enter age: '))
age_group = None

if age < 13 : age_group = 'child'
elif age > 13 and age < 19 : age_group = "Teenager"
elif age > 20 and age < 59 : age_group = "Adult"
else: age_group = "senior"

# 2. Movie Ticket Pricing
# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.
age = 12
day = "Wednesday"

price = 12 if age > 18 else 8
if day == "Wednesday": price -=2 
# 3. Grade Calculator
# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

score = 69
grade = None
if score >= 0 and score <= 100:
    if score > 90 and score<= 100: grade = 'A'
    elif score > 80 and score <= 89: grade = 'B'
    elif score > 70 and score <= 79: grade = 'C'
    elif score > 60 and score <= 69: grade = 'D'
    else: grade = 'F'



# 4. Fruit Ripeness Checker
# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

fruit = "Banana"
color = "Green"

if fruit == "Banana":
    if color == "Green": print("Unripe")
    elif color == "Yellow" : print("Ripe")
    elif color == "Brown" : print("Overripe")

# 5. Weather Activity Suggestion
# Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

weather = "Sunny"
if weather == "Sunny": activity = "Go for a walk"
elif weather == "Rainy" : activity = "Read a book"
elif weather == "Snowy" : activity = "Build a snowman"

# 6. Transportation Mode Selection
# Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).
distance = 3
transport_type = None
if distance <3 : transport_type = "Walk"
elif distance > 3 and distance < 15 : transport_type = "Bike"
elif distance > 15: transport_type = "Car"

# 7. Coffee Customization
# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

order_size = "Medium"
extra_shot = True

if extra_shot:
    coffee = order_size + "Extra coffee"
else:
    coffee = order_size + "Coffee"

# 8. Password Strength Checker
# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

pass_word = "123"
strength = None

if len(pass_word) < 6: strength = "Weak"
elif len(pass_word) > 6 and len(pass_word) : strength = "Medium"
elif len(pass_word) > 10: strength = "Strong"



# 9. Leap Year Checker
# Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

# year = 2100
# is_Leap = False
# if (year % 4 ==0 and year % 100 !=0 ) and year % 400 == 0 : is_Leap = True
# print(is_Leap)

#  10. Pet Food Recommendation
# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

pet_species = "Dog"
age = 2

if pet_species =="Dog" :
    if age < 2: food = "Puppy food"
    else: food = "Senior Puppy food"
    
elif pet_species == "Cat":
    if age > 5: food = "Senior cat food"
    else: food = "Cat food"
else:
    print("incorrect pet")