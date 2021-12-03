output = ""
percent_maan = 16.5
percent_jupiter = 253.7
percent_mars = 37.8

for gewicht in range(50,121,5):
    output += ("\nAarde: " + str(gewicht) + "\n" +"Maan: " + str(gewicht / 100 * percent_maan) + "\n" + "Jupiter: " + str(gewicht / 100 * percent_jupiter) + "\n" + "Mars: " + str(gewicht / 100 * percent_mars) + "\n")
print(output)