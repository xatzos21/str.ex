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



#  String basics 2

# Task 1 

#Create a variable called ```text``` to store the data:
#  ```Berlin is a world city of culture, politics, media and science.``` . 
# Your task is to print the length of the ```text``` variable on the screen. 

# * Your result should look like this:

# ```bash
# 63
# ```

text4 = "Berlin is a world city of culture, politics, media and science."

c = len(text4)
print(c)

# Task 2

# Reuse the variable called ```text```  and print
#  the first and the last characters on the screen. 

# * Your result should look like this:

# ```bash
# B .
# ```

e = (text4[:0]) + (text4[61:])
print(e)

# Task 3

#Reuse the variable called ```text```  and
#  print the first three characters in upper case.

# * Your result should look like this:

# ```bash
# First three characters: BER
#```

d = (text4[0:3])
print(d.capitalize())

# Task 4

# Create the variable called ```text``` with the following content: 
#  ```"Berlin is surrounded by the State of Brandenburg 
# and contiguous with Potsdam, Brandenburg's capital" ```, 
# then count how many times the letter  ```B ``` appears in the text.

# * Your result should look like this:

# ```bash
# B appears:  3  times
# ```

text5 = """Berlin is surrounded by the State of Brandenburg
 and contiguous with Potsdam, Brandenburg's capital"""

f = text5.count("b")
print("B appears: ", f, " times")

# Task 5

# Create a variable called ```text``` to store the data: 
# ```Berlin straddles the banks of the Spree, which flows into the Havel 
# (a tributary of the Elbe) in the western borough of Spandau.``` .
#  Your task is to print the last 10 characters of the ```text``` 
# variable on screen.

# * Your result should look like this:

# ```bash
# Last ten characters: f Spandau.
# ```

text6 = """Berlin straddles the banks of the Spree, which flows
 into the Havel (a tributary of the Elbe) in the western borough of Spandau."""

g = (text6[119:129])
print("Last ten characters : ", g)

# Task 6

#Create a variable called ```text``` to store the data: 
# ```---Python programming---``` . Your task is to remove the hyphen 
# (```-```) character from the string.

# * Your result should look like this:

# ```bash
# Python programming
# ```

text7 = "---Python programming---"

h = text7.strip("-")
print(h)

# Task 7

#Create two variables to store your first and your last name.
#  Your task is to concatenate the two variables using the appropriate
#  labels.

# * You should provide a single line print statement.

# * Your result should look like this:

# ```bash
# Firstname: Mary 
# Lastname: Mat
# ```

firstname = "Mary"
lastname = "mat"

print("Firstname: ", firstname)
print("Lastname: ", lastname)