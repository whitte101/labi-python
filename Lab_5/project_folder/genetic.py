import re

def rle_decode(seq):
    result = ""
    i = 0
    while i < len(seq):
        if seq[i].isdigit():
            count = int(seq[i])
            i += 1
            result += seq[i] * count
        else:
            result += seq[i]
        i += 1
    return result

def merge_files(parts, output):
    with open(output, "w", encoding="utf-8") as out:
        for fname in parts:
            with open(fname, "r", encoding="utf-8") as f:
                for line in f:
                    out.write(line)
    return output

def load_sequences(filename):
    proteins = {}
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("\t")
            if len(parts) != 3:
                continue
            protein_name = parts[0].strip()
            organism = parts[1].strip()
            sequence = rle_decode(parts[2].strip())
            proteins[protein_name] = (organism, sequence)
    return proteins

def do_search(seq_part, proteins, out):
    found = False
    for name, (org, seq) in proteins.items():
        if seq_part in seq:
            out.write(f"{org}\t{name}\n")
            found = True
    if not found:
        out.write("NOT FOUND\n")

def do_diff(p1, p2, proteins, out):
    missing = []
    if p1 not in proteins:
        missing.append(p1)
    if p2 not in proteins:
        missing.append(p2)
    if missing:
        out.write("MISSING: " + ", ".join(missing) + "\n")
        return
    seq1 = proteins[p1][1]
    seq2 = proteins[p2][1]
    length = max(len(seq1), len(seq2))
    diff_count = 0
    for i in range(length):
        a = seq1[i] if i < len(seq1) else None
        b = seq2[i] if i < len(seq2) else None
        if a != b:
            diff_count += 1
    out.write(str(diff_count) + "\n")

def do_mode(protein, proteins, out):
    if protein not in proteins:
        out.write("MISSING: " + protein + "\n")
        return
    seq = proteins[protein][1]
    freq = {}
    for aa in seq:
        freq[aa] = freq.get(aa, 0) + 1
    max_count = max(freq.values())
    best = sorted([aa for aa in freq if freq[aa] == max_count])[0]
    out.write(f"{best}          {max_count}\n")

def process_all(student_name="Your Name"):
    seq_file = merge_files(
        ["sequences.0.txt", "sequences.1.txt", "sequences.2.txt"],
        "sequences.txt"
    )
    cmd_file = merge_files(
        ["commands.0.txt", "commands.1.txt", "commands.2.txt"],
        "commands.txt"
    )
    proteins = load_sequences(seq_file)
    with open(cmd_file, "r", encoding="utf-8") as com, \
         open("genedata.txt", "w", encoding="utf-8") as out:
        out.write(student_name + "\n")
        out.write("Genetic Searching\n")
        out.write("--------------------------------------------------------------------------\n")
        op_number = 1
        for line in com:
            if not line.strip():
                continue
            parts = line.strip().split("\t")
            operation = parts[0]
            out.write(f"{op_number:03d}   {line.strip()}\n")
            if operation == "search":
                seq_part = rle_decode(parts[1])
                do_search(seq_part, proteins, out)
            elif operation == "diff":
                do_diff(parts[1], parts[2], proteins, out)
            elif operation == "mode":
                do_mode(parts[1], proteins, out)
            out.write("--------------------------------------------------------------------------\n")
            op_number += 1

process_all(student_name="Никита")
