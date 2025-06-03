ch = input("Convert (C)elsius to Fahrenheit or (F)ahrenheit to Celsius? ").strip().upper()

if ch == 'C':
    c = float(input("Enter temperature in Celsius: "))
    f = (c * 9/5) + 32
    print(f"{c}°C = {f}°F")
elif ch == 'F':
    f = float(input("Enter temperature in Fahrenheit: "))
    c = (f - 32) * 5/9
    print(f"{f}°F = {c}°C")
else:
    print("Enter correct choice!")