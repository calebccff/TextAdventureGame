def intInput(prompt, min, max):
    try:
        val = input(prompt)
        if(val > min and val <= max):
            return val
        else:
            print("Make sure that the number you entered is in the specified range")
    except ValueError:
        print("Enter a number")