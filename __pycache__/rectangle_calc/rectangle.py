import calculate

length = float(input("enter the length of the rectangle: "))
width = float(input("enter the width of the rectangle: "))

area = calculate.area(length, width)
perimeter = calculate.perimeter(length, width)
                                
print(f"the area of the rectangle is: {area}")
print(f"the perimeter of the rectangle is {perimeter}")