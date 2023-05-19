#Vartotojo įvesties gavimas ir įrašymas į naują failą
new_file_name = input("Įveskite norimą naujo failo pavadinimą: ")
with open(new_file_name, 'w') as f:
    while True:
        line = input("Įveskite eilutę (Enter - baigti): ")
        if line == "":
            break
        f.write(line + '\n')