def greet(name):
    return f"Hey {name}!"
print(greet('joe'))

def age_in_dog_years(age):
    return age * 7

print(age_in_dog_years(28))

def concat(w1, w2):
    return w1+w2
print(concat("da","nk"))

def uppercase_and_reverse(input):
    return input.upper()[::-1]
print(uppercase_and_reverse("Do not go gentle into that good night."))