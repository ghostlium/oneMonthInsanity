bill = float(input("What is your bill? ").replace("$",""))
tipPercent = float(input("What percent do you want your tip to be? ").replace("%",""))

tip = bill*tipPercent/100

print(f"Tip {tip:.2f}!")

