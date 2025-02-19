#!/usr/bin/env python3.6
# Prompts the user for a message to echo.
# Prompts the user for the number of times to repeat the message. If no response is given, then the count should default to 1.
# Defines a function that takes a message and count then prints the message that many times.

message = input("Enter a message: ")
count = input("Number of repeats [1]: ").strip()

if count:
    count = int(count)
else:
    count = 1

def multi_echo(message, count):
    while count > 0:
        print(message)
        count -= 1

multi_echo(message, count)
