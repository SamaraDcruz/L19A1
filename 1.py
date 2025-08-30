try:
    number = int("hello")
    print("Number is:", number)

except ValueError:
    print("❌ Oops! Cannot convert text into a number.")