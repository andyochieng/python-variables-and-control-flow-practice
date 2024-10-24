# Ask the user for their age
age = int(input("Enter your age: "))

# Checking the age category
if age < 18:
    category = "You are a minor."
elif 18 <= age <= 65:
    category = "You are an adult."
elif age > 65:
    category = "You are a senior."
else:
    category = "Invalid age entered."

# Print the category
print(category)
