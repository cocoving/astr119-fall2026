def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

a = get_float_input("Enter the value of a: ")
b = get_float_input("Enter the value of b: ")
c = get_float_input("Enter the value of c: ")

def Quadratic(a, b, c):
    if a == 0:
        print("This is not a quadratic equation.")
        return None
    denominator = 2 * a
    discriminate = b ** 2 - 4 * a * c
    if discriminate < 0:
        print("The equation has no real roots.")
        return None 
    elif discriminate == 0:
        root = -b / denominator
        return root
    else:
        root1 = (-b + discriminate ** 0.5) / denominator
        root2 = (-b - discriminate ** 0.5) / denominator
        return root1, root2 
print(Quadratic(a, b, c))