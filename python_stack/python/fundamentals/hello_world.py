# 1. TASK: print "Hello World"
print("Hello World")

# 2. print "Hello Noelle!" with the name in a variable
name = "Sombat"
print("Hello", name)	# with a comma
print("Hello " + name)	# with a +

# 3. print "Hello 42!" with the number in a variable
num = 6
print("Hello", num)	# with a comma
print("Hello " + str(num))	# with a +	-- this one should give us an error!

# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "crab"
fave_food2 = "ramen"
print("I love to eat {} and {}.".format(fave_food1, fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}.") # with an f string