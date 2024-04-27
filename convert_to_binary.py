def binary():
    numero = int(input("Inserisci numero: "))
    numero_bin = bin(numero)
    print("Binary numero di", numero, "fa: ", numero_bin[2::])
binary()