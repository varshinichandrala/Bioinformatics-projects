# DNA Sequence Analysis Tool
sequence = input("Enter DNA sequence:").upper()
length = len(sequence)
A = sequence.count("A")
T = sequence.count("T")
G = sequence.count("G")
C = sequence.count("C")
gc =((G + C) / length) * 100

print("\n--- DNA Analysis Result ---")
print("sequence:", length)
print("Length:", length)
print("A:", A)
print("T:", T)
print("G:", G)
print("C:", C)
print("GC content:", round(gc, 2), "%")
