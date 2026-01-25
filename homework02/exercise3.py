def percent_base(DNA_seq):
    length = len(DNA_seq)
    base_A = (DNA_seq.count("A") / length) * 100
    base_T = (DNA_seq.count("T") / length) * 100
    base_G = (DNA_seq.count("G") / length) * 100
    base_C = (DNA_seq.count("C") / length) * 100
    base_dict = {
        'A': f"{base_A:.2f}",
        'T': f"{base_T:.2f}",
        'G': f"{base_G:.2f}",
        'C': f"{base_C:.2f}"
    }

    print(base_dict)