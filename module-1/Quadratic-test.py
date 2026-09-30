while True:
    try:
        input_a = input("Enter the value of a: ")
        a = float(input_a)
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

while True:
    try:
        input_b = input("Enter the value of b: ")
        b = float(input_b)
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

while True:
    try:
        input_c = input("Enter the value of c: ")
        c = float(input_c)
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")


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