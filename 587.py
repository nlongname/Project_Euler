# https://projecteuler.net/problem=587
# We have a series of circles touching each other horizontally, with a rectangle
# circumscribing that. We call the area between the leftmost circle and the
# lower-left corner of the rectangle L. We draw a line from the bottom-left
# to top-right corners of the rectangle, and take the area of the region
# below both that line and the leftmost circle. We want to know what proportion
# of L that area is.

import math

# a = n*b


def concave_triangle(n:int) -> float:
    # A lot of pencil-and-paper to prepare for this one
    # Area of L is (4-pi)/4 from the rectangle and circle area formulas
    # I'm splitting the area we're looking at in half based on the altitude
    # the left half is a right triangle, long leg a and short leg b
    # right half isn't a triangle, we'll use an integral
    # Assuming the formula of the first circle is x^2 + y^2 = 1, centered at
    # (0,0), with a=1+x, b=1+y. By similar triangles, we know that a = n*b
    # solving for b in terms of n, we get b = (n+1-sqrt(2n))/(n^2+1)
    # (we ignore the additive solution because of our quadrant)
    b = (n+1-math.sqrt(2*n))/(n**2+1)
    a = n*b
    left_half = 1/2 * a * b
    # integral from x to 0 between the lower half of the circle and y=-1
    right_half = (1-a) + 1/2 * ((a-1)*math.sqrt(1-(a-1)**2) + math.asin(a-1))
    L_area = (4-math.pi)/4
    return (left_half + right_half)/L_area

temp = 1/2
n = 1
while temp > .001:
    n += 1
    temp = concave_triangle(n)
print(n)
