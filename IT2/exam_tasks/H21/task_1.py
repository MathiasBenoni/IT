k_verdi = input("70 - 250: ")

try:
    k_verdi = int(k_verdi)

    if 70 <= k_verdi <= 79:
        print("2,2 poeng")
    elif 80 <= k_verdi <= 99:
        print("2 poeng")
    elif 100 <= k_verdi <= 169:
        print("1,8 poeng")
    elif 170 <= k_verdi <= 250:
        print("1,2 poeng")
    else:
        print("NO")

except ValueError:
    print("NO")