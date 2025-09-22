Explanation of My Calculator Program

Defining separate functions for each operation

I created individual functions for addition, subtraction, multiplication, and division. Each function handles one task. This makes the code cleaner, easier to understand, and reusable.

Making a loop to continuously take input from the user

I used a while True loop, so the calculator keeps running without restarting the program. The loop only stops when the user types "exit."

Handling errors, like division by zero or invalid input

In the divide function, I checked if the second number is zero to avoid a crash. I also used try-except, so invalid inputs, like letters instead of numbers, don’t break the program.

Using if __name__ == "__main__" to ensure the program runs properly when executed

This ensures the calculator runs only when the script is executed directly, not when it's imported. It makes the program more flexible and prevents unwanted execution in other files.
