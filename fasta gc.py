import matplotlib.pyplot as plt

sequences = {}

with open("sample.fasta") as file:
    name = ""
    for line in file:
        line = line.strip()
        if line.startswith(">"):
            name = line
            sequences[name] = ""
        else:
            sequences[name] += line

gc_values = []

for name, seq in sequences.items():
    g = seq.count("G")
    c = seq.count("C")
    gc = ((g + c) / len(seq)) * 100
    gc_values.append(gc)
    print(name, "GC Content:", round(gc, 2), "%")

plt.bar(sequences.keys(), gc_values)
plt.xlabel("Sequences")
plt.ylabel("GC Content (%)")
plt.title("GC Content of Sequences")
plt.show()