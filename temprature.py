def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

temp = float(input("Enter temperature in Celsius: "))
print(f"{temp}°C is {celsius_to_fahrenheit(temp)}°F")