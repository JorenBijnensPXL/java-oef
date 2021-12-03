punt = int(input("behaalt resultaat op 20: "))
percent = punt*5

if percent < 60:
    graad = "onvoldoende"
elif percent < 70:
    graad = "voldoede"
elif percent < 80:
    graad = "onderscheiding"
elif percent < 90:
    graad = "grote onderscheiding"
else:
    graad = "grootste onderscheiding"

print(str(percent)+"%,", graad)