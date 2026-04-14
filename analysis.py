with open("multi.fasta", "r") as file:
    sequences = {}
    current_seq = ""
    for line in file:
        line = line.strip()
        if line.startswith(">"):
            current_seq = line
            sequences[current_seq] = ""
        else:
            sequences[current_seq] += line
for name, seq in sequences.items():
    length = len(seq)
    A = seq.count("A")
    T = seq.count("T")
    G = seq.count("G")
    C = seq.count("c")
    
    gc = ((G + C) / length) * 100
    
    print("\n", name)
    print("sequence:", seq)
    print("length:", length)
    print("A:", A)
    print("T:", T)
    print("G:", G)
    print("C:", C)
    print("GC Content:", round(gc, 2), "%")
