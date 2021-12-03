som_temperatuur = 0
hoogste_temperatuur = -273.15
aantal = 5

for i in range(aantal):
    tempratuur_dag = float(input("geef de temperatuur van de dag: "))
    som_temperatuur += tempratuur_dag

    if tempratuur_dag > hoogste_temperatuur:
        hoogste_temperatuur = tempratuur_dag

print("het was de afgelopen 10 dagen gemiddeld", str(som_temperatuur/aantal)+"°C")
print("de hoogste temeratuur van de afgelopen 10 dagen:", str(hoogste_temperatuur)+"°C")


