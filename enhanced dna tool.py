# DNA Analysis Toolkit

dna = input("Enter DNA sequence: ").upper()

# Validation
valid = True
for base in dna:
    if base not in "ATGC":
        valid = False
        break

if not valid:
    print("Invalid DNA sequence! Use only A, T, G, C.")
else:
    length = len(dna)

    A = dna.count("A")
    T = dna.count("T")
    G = dna.count("G")
    C = dna.count("C")

    gc = ((G + C) / length) * 100

    rna = dna.replace("T", "U")

    reverse = dna[::-1]

    complement = ""
    for base in dna:
        if base == "A":
            complement += "T"
        elif base == "T":
            complement += "A"
        elif base == "G":
            complement += "C"
        elif base == "C":
            complement += "G"

    print("\n--- DNA Analysis ---")
    print("Sequence:", dna)
    print("Length:", length)
    print("A:", A)
    print("T:", T)
    print("G:", G)
    print("C:", C)
    print("GC Content:", round(gc, 2), "%")

    print("\n--- RNA ---")
    print(rna)

    print("\n--- Reverse ---")
    print(reverse)

    print("\n--- Complement ---")
    print(complement)