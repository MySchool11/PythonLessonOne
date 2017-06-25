__author__ = 'Mr Bancroft'                      # Not needed just nice to show authorship

print("The first lesson in Python")                 # print statement to output text
print(1 + 2)                                        # Python is clever enough to convert integers to text after adding
print(7 * 6)                                        # Python will use the * as multiply as it knows integers are here
print("Hello" * 6)                                  # Python will print hello six times as the * is now used on a string
print()                                             # Just print a blank line
print("I said 'test it first'")                     # Python will print the ' characters as Print used " characters
print('I said "test it first"')                     # Same again, only different :-)
print("I said \"test it first\"")                   # Same again, only using the escape character \ to ignore "
print("I said \"test it first\"\n" * 2)             # Same as last 2 using \n to place a newline between each
# IF you start a string with " you need to finish it with " same with '
print("Concatenate (join)" + " strings")            # Python knows the + means to join the strings together
saying = "I said 'Test it first'"                   # create a variable holding the saying called saying!
print(saying+" that's what I said")                 # Print the string in saying and join more text at the end
isaid = "that's what I said"                        # create a variable to hold the text from the above example
print(saying+" "+isaid)                             # Print the strings in the variables together with a space between
numberOfTimes = 2                                   # A variable holding the integer 6, the name is in camelCase
print((saying+" "+isaid+"\n")*numberOfTimes)        # Prints the same as line 10 but using variables instead
# Adding these comments to your code, is always a good idea. It helps others (and you) to know what code does, you will
# forget at some point - especially after you write your 100th program :-).
'''
I really should have used a multiline
comment to write the
previous comment as # is reserved for single line comments
really
OK? Good
'''
