# åpner fil
f = open("input.txt")

# leser hver linje i fila og summerer kaloriene for hver alv
sum = 0
kalori_summer = []
for linje in f:
    if linje.strip():
        sum += int(linje.strip())
    else: 
        kalori_summer.append(sum)
        sum = 0
f.close()

# finner max kalorier og alvens posisjon i datafila
maks = 0
i = 0
indeks = 0
for sum in kalori_summer:
    i += 1
    if sum > maks:
        maks = sum
        indeks = i
print(f"Høyeste kalorisum: {maks} Indeks: {indeks}")

# reverserer lista og summerer de tre som har høyeste kaloriverdi
kalori_summer.sort(reverse=True)
sum_av_tre = kalori_summer[0] + kalori_summer[1] + kalori_summer[2]
print(f"Summen av kaloriene til de 3 som har mest: {sum_av_tre}")


