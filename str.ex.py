#String basics 1

# Task-1

# Your task is to create a variable called `city` 
# to store the data: `London` , then print the content 
# of the `city` variable on the screen.

# - Your result should look like this:

# ```
# London
# ```

city = "London"
print(city)


# Task-2

# Your task is to create two variables, the first variable to be called `city`
#  and will store the data: `berlin` , and the second variable to be called `population` 
# and will store the data: `3645000`. Then print the content of the `city` 
# and `population` using a colon (`:`)  in between.  Make sure you capitalize 
# the content of the `city` variable.

# - Your result should look like this:

# ```
# Berlin: 3645000
# ```

city = "berlin: "
population = "3645000"
print(city.capitalize() + population)


# Task-3

# Your task is to create two variables, the first variable to be called `city`
#  and will store the data: `london` , and the second variable to be called 
# `population` and will store the data: `9000000`. Then print the content 
# of the `city` and `population` using their labels as shown in the output below. 
# Make sure you check if the content of the `city` is a text. Print 
# the appropriate results on screen as shown bellow.

# - Your result should look like this:

# ```
# City: London (True)
# Population: 9000000 
# ```

city = "London"
population =  "9000000"

a = city.isalpha()
print("City: London ", a)
print("Population: " + population)


# Task-4

# Create a variable called `text` to store the data: `Berlin is surrounded
#  by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital.` . 
# Your task is to check if  the word `capital`  is included in the text, if so, 
# print the index of the location inside the `text` string.

# - Your result should look like this:

# ```
# capital: 92
# ```

text1 = """Berlin is surrounded by the State of Brandenburg and 
contiguous with Potsdam, Brandenburg's capital."""

b = text1.index("capital")
print("capital: ", b)

# Task-5

#Create a variable called `text` to store the data: `Berlin straddles the banks
#  of the Spree, which flows into the Havel (a tributary of the Elbe) in the
#  western borough of Spandau.` . Your task is to split the content of the 
# `text` variable and store it in a list.

# - Your result should look like this:

# ```
# ['Berlin', 'straddles', 'the', 'banks', 'of', 'the', 'Spree,', 
# 'which', 'flows', 'into', 'the', 'Havel', '(a', 'tributary', 'of', 'the', 'Elbe)'
# , 'in', 'the', 'western', 'borough', 'of', 'Spandau.']
# ```

text = """Berlin straddles the banks of the Spree, which flows into the
 Havel (a tributary of the Elbe) in the western borough of Spandau."""
x = text.split()
print(x)


# Task-6

#Create a variable called `text` to store the data: `Berlin is surrounded 
# by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital.`
# . Your task is to replace the word `capital` with the phrase  `capital of Germany` .

# - Your result should look like this:

# ```
# Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, 
# Brandenburg's capital of Germany.
# ```

text3 = """Berlin is surrounded by the State of Brandenburg and 
contiguous with Potsdam, Brandenburg's capital."""

z = text3.replace('capital','capital of germany')
print(z)