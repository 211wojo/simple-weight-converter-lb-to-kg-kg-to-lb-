weight = float(input("Your weight: "))
unit = input("kg/lb?: ")


if unit == "kg":
    typ = "kg"
    typ2 = "lb"
    result= weight * 2.2
    
elif unit == "lb":
    typ = "lb"
    typ2 = "kg"
    result = weight / 2.2

print(weight, typ, "to", round(result), typ2)


