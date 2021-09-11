# T2A1 - Workbook

## **1.** *if statements*
    are found commonly throughout coding languages and are a significant part of those languages.

    If statements will allow the programmer to express a line of code individually, executing one line at a time.

*eg.*
```python
temperature = 25
if temperature < 10:
    print("Turn on the heater!")
```
    Here we see that we set the temperature as a variable with the value assigned to 25. 
    Now if the temperature goes below 10, it will tell us to turn the heater on because it has become too cold.

    We can expand upon it by adding together an if and else statement to reduce clutter and complication in the structure of our code.

*eg.* 
```python
temperature = 25
if temperature < 10:
    print("Turn on the heater!")
elif temperature > 25:
    print("Turn on the AC!")
```

    If our temperature goes below 10, we get the "Turn on the heater!" message, else we will run our new message if the temperature is above 25; "Turn on the AC!". 
    From this we can understand that if the first statement isn't true, then we will run the next statement in order. 
    If we wanted to safeguard more temperature zones we could add more elif statements into our code.

## *for statements*
    are the most commonly used code for iterations which contain a dictionary, list, tuple, set or string. 
    The main aim of a for loop is to execute code a specified amount of times and given a condition is met.
    One of the most interesting factors for for loops is that the coder can choose one object from a list and iterate over it.

*eg.*
```python
colors = ["red", "green", "blue"]
for x in colors:
    print(x)
```
    This code will find the first string we entered "red", this is counted as one iteration, and print it on its own line. 
    It then moves to the next of its iteration and proceeds to the next string "green", and prints on a new line. 
    This continues until all our strings have been printed. 
    This is because 'x' is being considered as each individual string and one iteration is performed for each string in our list.

    The complexity of for loops can be pushed much further than this.
    Nested for loops will allow us to iterate over something, then perform a separate iteration over another.

*eg.*
```python
numbers = ["one", "two", "three"]
obj = ["cookie!"]

for x in numbers:
    for y in obj:
        print(x, y)
print("ah ah ah")
```

    The example of nested loops shows two possible code executions that will have iterations. 
    Each time the first or outer loop has an iteration, it will be followed by the nested or inner loop iteration. 
    This will continue until the last item in the list has been met in the outer loop.
    Here our output will be: 
    one cookie! 
    two cookie! 
    three cookie! 
    ah ah ah

## **2.** *Type Coercion*

    Put simply, Python doesn't support type coercion as of Python 3.0.
    Instead, Python has a set of rules that apply when attempting to convert different data types.
    Following the rules are key as not all data types will just magically convert like in other languages.
    The most common way for Python to help the programmer is by using built-in dunder(double underscore) methods. 
    These are often overlooked because of their simplistic look, but under the hood they are doing some serious work. 
    It would be difficult for Python to concatenate code without specific ways of going about it. 

***Strings***

    are immutable, and for good reason! If strings were mutable, we would have many issues of repetition in our code, especially when printing strings. 
    When strings are concatenated they must be assigned to a variable. 
    If this process didn't exist, there would be multiple overlaps or even errors in code because of the strings assigned to the same variables. 
    With strings being immutable, we avoid the repetition of strings in our variables. 
    
    Where one issue is solved, another can arise. 
    TypeErrors happen because of the programmer attempting to concatenate a string with a non string type. 
    Luckily, Python has a few ways around type conversion. 
    There are methods that can assist with conversion, one example being .join(), which will convert a list to a string. 

    A very common example of converting integers to strings is by using the str() method, which is another built-in Python method.

*eg.*
```python
x = 5
y = 5
z = x + y

print(str(z))
```
    Even though the print statement looks identical, behind the scenes there is a type conversion happening.
    Originally we would be printing an integer as "z". But, by adding str(z), type conversion occurs, converting it into the string "10". 
    The same is true if we wanted to convert a string to an integer with int(z).

*eg.*
```python
print(int("10"))
```
    The int() method takes two arguments, however only the first is needed for the conversion to take place. 
    int()'s second argument is to define a base number and is purely optional to imply. 

***Integers and floats***

    When we try to add an integer and float together, we will in fact get the total. But Python doesn't have type coercion, so how?
    Using x + y as an example, Python will read + as x.__add__(y). 
    Integers cannot be added to a float, it tells Python that it doesn't know how to add itself to a float.

    Python will now call a new dunder add method called __radd__. This will pass the float to the integer instead. 
    Our equation now looks like this in Python: y.__radd__(x). 
    Python will attempt to first __add__ them together, if it returns 'NotImplemented', Python knows that one value doesn't know how to be added to the other. 

*eg.*
```python
a = 8
b = 2.5
a + b = c
print(c)
```
Lets look behind the scenes:
```python
a + b = c
a.__add__(b)
NotImplemented ("Remember this is what Python sees")
"The Switch"
b + a = c
b.__radd__(a)

print(c)
10.5
```
    The answer will return 10.5, but why?

    It now attempts a switch, calling __radd__ instead of raising a TypeError. 
    Our integer(x) can now be added to our float(y) and the code will not return any errors.

## **3.** *Pass By Value*

    What in seems like a war between programmers, we have the concept of pass by value.
    Simply, pass by value is defined as when we create a function and give it a value, the function is given a copy of the argument passed by the called statement. 
    The original object will stay unchanged, and instead all changes made are sent to it's copy which are stored at a different location in the memory.

    Another way of saying this is that the value is passed directly to the value's argument of the function, creating a copy of that variable. 
    If changes are made to the copy variable from outside the function, it won't effect the value, keeping the original value unmodified. 

*eg.*
```python
colors = {'R': 255, 'G': 255, 'B': 255}

def new(colors):
    colors = ["R: Red", "G: Green", "B: Blue"]

    print(f"Inner function {colors}")
    return 

new(colors)
print(f"Outer function: {colors}")
```

    In this code we see a variable dictionary named colors in the outer scope. 
    We then create a function called new(colors) and give it a variable colors.
    Printing our function (from within the function) will return our colors different to the outer scope variable. 


## **4.**

## **5.** *Analysis*
```python
 def convert_celcius_to_fahrenheit
    celsius = input()
    fahrenheit = (celsius * 9 / 5) + 32
    print("The result is: " + fahrenheit) 
    convert_celcius_to_fahrenheit()
```
### **a.**
    - Indentation errors on every line.
    - Syntax Error for function.
    - No error, but input will run empty.
    - TypeError, Input needs to call for an integer instead of a string.

### **b.** 
    Each line has an extra indentation. Known as "whitespace", Python critically evaluates where whitespace is placed within code. 
    This means that code blocks in Python will be denoted by their indentation.
    Indentation helps provide a cleaner, more uniformed code and will yield different results if not used correctly. 
    
    An indented code block will be preceded with a colon(:) on the previous line of code. 
    Which leads us nicely into our next error..

```python
# Bad
 def convert_celcius_to_fahrenheit
```
```python
# Good
def convert_celcius_to_fahrenheit():
```
    To create a function, there is a process to follow. def function_name():
    The reason parentheses are required to create a function is so that arguments or parameters for the function can be added inside them (). 
    An error occurs if no parentheses are added to handle arguments.

    Attempts to create a function called convert_celcius_to_fahrenheit. 
    To successfully assign a name to the function and have code assigned to the name, a colon(:) must be added to the end of the function name.

```python
# Bad
celsius = input()
```
```python
# Good
celsius = int(input("Please enter an integer in celcius: "))
```
    Taking input() from a user needs to be an easy to understand and guided experience. 
    Throwing an empty input to a user will not allow them to understand what they are meant to add in.
    So, we add a string that is easy to understand.

    Because input() takes a string from the user, it will be saved as a string. 
    This will cause a conflict with our code when trying to use a formula later on.
    When we take the user input which we know it will be a number, we can force it to accept it in a method we choose.
    If we change it to int(input()), we can accept integers without the conflict of a string.

```python
# Bad
print("The result is: " + fahrenheit) 
```
```python
# Good
print(f"The result is: {fahrenheit}")
```

    By changing the print code to an f-string, we can easily add code within the {} that will call for a previously written function. 
    The f-string allows us to add any amount of functions to the printed string with no conflicts or additional coding needed besides the {}.

## **6.** *Analysis*
```python
 for number in range(1, 100):
     message = ''
     if number % 3 != 0:
     message =+ "Fizz"
     if number % 5 != 0:
     message =+ "Buzz"
     if number % 5 == 0 or number % 3 != 0:
     number =+ str(number)
     print(message)
```
### **a.**
    - Indentation Error
    - Indentation Error / Code block
    - Type Error +=
    - Type Error string
    - if statments to elif
    - Removed message = ""
    - Removed number =+ str(number)
    - Changed 3 != 0 to 3 == 0
    - Changed or to and
    - Changed print(message) to print(number)
    - Changed all message to number
    - Added new line if % by 3 and 5: FizzBuzz

### **b.**
```python
# Bad
 for number in range(1, 100):
```
    Indentation must be fixed for this line. Whitespace creating an error. Backspaced.

```python
# Bad
message = ''
```
```python
# Good
if number % 3 and number % 5:
```
    All lines in the codeblock have indentation errors. Needed to remove whitespace.
    This variable isn't needed. Instead we can write a code that will say if we reach a number that is % 3 and 5, we can print FizzBuzz.

```python
# Bad
Multiple if statements
```
    Bad to continue using if statements when inside the same codeblock. 
    Replace if with elif(else if) if we want it to do another action if the first condition isn't met.

```python
# Bad
Remove message =+ "Fizz"
Remove message =+ "Buzz"
```
    Incorrect format +=. 
    The code here isn't needed at all as we replaced it above.
    The goal was to get FizzBuzz printed on the same line, however it was a pointless addition with errors.

```python
# Bad
number =+ str(number)
```
    Incorrect format +=.
    This code contained indent and type errors.

```python
# Bad
if number % 5 == 0 or number % 3 != 0:
```
```python
# Good
elif number % 5 == 0 and number % 3 == 0:
```
    Changed if to elif for proper structure. 
    Changed or to and. We want both to be true instead of just possibly one.
    Changed != to ==. We want % 3 to equal in order to print the correct statement.
```python
# Bad
if number % 5 == 0 or number % 3 != 0:
number =+ str(number)
```
```python
# Good
print(number)
```
    print(message) changed to print(number) because we want to iterate through the numbers in our range. 

```python
# Final
for number in range(1, 100):
    if number % 3 and number % 5:
        print("FizzBuzz")
    elif number % 3 != 0:
        print("Fizz")
    elif number % 5 != 0:
        print("Buzz")
    elif number % 5 == 0 and number % 3 == 0:
        print(number)
```

## **7.**

![Flowchart](flownew.png)

function to find primes:
    create a variable to hold list of primes
    for a number NUM in range of 0 to 100 with increments of 1
        if the number NUM is greater than 1
            for a iterator I in range of 2 to number NUM
                if number NUM is divisible by iterator I
                    break out of loop
                else increase iterator by 1
            if loop is not broken
                add number NUM to list of primes
    return list of primes

```python
def find_primes():
    prime_list = []
    for num in range(0, 100 + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
                else:
                    continue
            else:
                prime_list.append(num)
    return prime_list
```

## **8.** 
*Merge Sort*

    Merge sort is considered a divide and conquer algorithm. 
    The divide and conque algorithm can be three sections to be explained.
    The first is to divide, creating sub like smaller problems.
    Mergesort is called to divide the array recursively until the size becomes one.
    Then we conquer, calling in relation to the problems until solved. 
    And finally we combine the sub problems which we aim to get a solution to the final problem.
    Merge sort (fn. merge()) divides an array into halves creating sub arrays. 
    It follows by sorting and merging the two newly sorted halves, which the function is called for.

    To recap: Mergesort will be called to continually divide the array by half, until each problem is its own.
    It will read the numbers and sort them into new parts. Followed by dividing again and finding the new solution. 
    Finally merging the array together at the end.

    Merge sort is much slower calculating smaller inputs compared to other sorting algorithms. 
    It requires additional memory space of BigO(n) to utilise the temporary array. 
    Merge sort has sequential data access, meaning the need for random access is low.
    Seen as good and bad, it will always go through its entire process of divide and conquer, even if the array it's given has already been sorted.

*Bubble Sort*

    Bubble sort is considered to be the most basic and simple of the sorting algorithms.
    The method used is to contiually swap adjacent elements, if they are found to be in the wrong order.
    It does this in passes, passing elements, swapping and passing again.
    If an element is found to be swapped, it will continue to pass until a final pass is found with no swaps required.
    Regardless of if the array is sorted or not, Bubble sort will run on BigO(n^2). 
    Since nested loops are linked to BigO(n^2), we know to expect an inner and outer loop.
    Bubble sort can be used in BigO(n) where two elements require sorting and is often used for simplicity.

    To recap: Bubble sort will continually move the largest element to the right, while moving the lowest to the left.
    It will continue to run until a pass where no element was swapped has been accomplished.
    Once it passes with all adjacent elements unchanged, it will complete.


## **9.** 

    Because Bubble and Merge sort are so different in how they 




ref:
https://docs.python.org/2.5/ref/coercion-rules.html
https://www.pythonmorsels.com/topics/type-coercion/
https://careerkarma.com/blog/python-string-to-int/
https://www.geeksforgeeks.org/dunder-magic-methods-python/
https://realpython.com/python-string-split-concatenate-join/
https://pythonguides.com/python-pass-by-reference-or-value/
https://www.geeksforgeeks.org/pass-by-reference-vs-value-in-python/
https://clouds.eos.ubc.ca/~phil/courses/atsc301_private/whirlwind/02-Basic-Python-Syntax.html
https://www.tutorialspoint.com/python/python_functions.htm
https://www.geeksforgeeks.org/merge-sort/
https://www.programiz.com/dsa/bubble-sort
https://www.geeksforgeeks.org/bubble-sort/
