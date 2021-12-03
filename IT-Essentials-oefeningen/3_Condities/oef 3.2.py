brutoloon = float(input("geef het brutoloon: "))
print()
print("het brutoloon is:", brutoloon)

vakantiegeld = brutoloon / 100 * 5
print("het vakantiegeld is:", vakantiegeld,"euro")

if vakantiegeld >= 350:
    jaarlijkse_bijdrage = 350 / 100 * 8
else:
    jaarlijkse_bijdrage = vakantiegeld / 100 * 8

print("de jaarlijkse bijdrage is:", jaarlijkse_bijdrage,"euro")
