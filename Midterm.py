import math

# Q1: Calculate the area of a circle
def area_of_circle(radius):
    area = radius**2 * math.pi
    
    return round(area, 2)

# Q2: Hollow Right Triangle
def hollow_right_triangle(n):
    result = ""

    if n >= 4:
        for i in range(n):
            if i == 0:
                result += "*"
            elif i == (n - 1):
                result += "*" * n
            else:
                result += "*"

                for j in range(i - 1):
                    result += " "

                result += "*"

            result += "\n"

        return result.strip()

    else:
        return "The triangle height should be at least 4."


# Q3: Inverted Pyramid
def inverted_pyramid(n):
    result = ""
    if n >= 3:
        for i in range(n - 1, -1, -1):
            for j in range(n - i - 1):
                result += " "
            for k in range(i * 2 + 1):
                result += "*"
            result += "\n"
    else:
        return "The pyramid height should be at least 3."
    return result.strip()


# ----------------------------------------------------------------
# print(area_of_circle(5))
# print()

# print(hollow_right_triangle(3))
# print()

# print(hollow_right_triangle(4))
# print()

# print(hollow_right_triangle(5))
# print()

# print(inverted_pyramid(3))
# print()

# print(inverted_pyramid(4))
# print()

# print(inverted_pyramid(5))
# print()
