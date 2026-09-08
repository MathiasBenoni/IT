from os import replace


while True:

  

  try:
    num_1_as_string = input("Skriv inn et tall: ")
    num_1_processed = num_1_as_string.replace(",", ".")
    num_1 = float(num_1_processed)

    num_2_as_string = input("Skriv inn et annet tall: ")
    num_2_processed = num_2_as_string.replace(",", ".")
    num_2 = float(num_2_processed)
    
    total = num_1 + num_2

  except:
    break

  else:
    print(f"{num_1_as_string} og {num_2_as_string} er {total}")