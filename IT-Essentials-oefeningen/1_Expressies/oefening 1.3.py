tijd = 14
dagen_later = 535//24
uren_later = 535%24
print("het alarm gaat af over",dagen_later,"dagen om",uren_later + tijd,"uur")

dagen=0
for i in range(0,535):
    tijd = tijd + 1
    if (tijd==24):
        dagen=dagen+1
        tijd=0

print("het alarm gaat af over",dagen,"dagen om",tijd,"uur")


value1 = 5
value2 = 4
value3 = 5
for i in range(0,4):
    print(value3 / (value1 % value2))
    value1 = value1 + 1