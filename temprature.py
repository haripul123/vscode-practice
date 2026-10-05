def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32
def celsius_to_kelvin(c):
    return c + 273.15
temp = float(input("Enter temperature in Celsius: "))
print(f"{temp}°C is {celsius_to_fahrenheit(temp)}°F")

print(f"{temp}°C is {celsius_to_kelvin(temp)} K")