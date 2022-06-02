# --- DNA to protein ---

# --- Open 3 files ---

# File has sequences of DNA
dna_file = open("DNA", "r+")
# Empty file for mRNA sequences
mRNA_file = open("mRNA_Sequence", "w")
# Empty file for proteins sequences
protein_file = open("protein", "r+")
seq_DNA = dna_file.read()
# Function for transcription process
def transcription(dna):
    mRNA = " "
    # Make mRNA sequences
    for i in dna:
        if i == 'A':
            mRNA += 'U'

        elif i == 'T':
            mRNA += 'A'

        elif i == 'C':
            mRNA += 'G'

        elif i == 'G':
            mRNA += 'C'

        elif i == ' ':
            mRNA += ' '

        else:
            print("Invalid")
    return mRNA

seq_mRNA = transcription(seq_DNA)
# Put sequences of mRNA in mRNA file
mRNA_file.write(seq_mRNA)

# Function to get proteins
def translate(seq):
    # Dictionary has proteins codons
    table = {
        'ATA': ' Ile ', 'ATC': ' Ile ', 'ATT': ' Ile ', 'ATG': ' Met ',
        'ACA': ' Thr ', 'ACC': ' Thr ', 'ACG': ' Thr ', 'ACT': ' Thr ',
        'AAC': ' Asn ', 'AAT': ' Asn ', 'AAA': ' Lys ', 'AAG': ' Lys ',
        'AGC': ' Ser ', 'AGT': ' Ser ', 'AGA': ' Arg ', 'AGG': ' Arg ',
        'CTA': ' Leu ', 'CTC': ' Leu ', 'CTG': ' Leu ', 'CTT': ' Leu ',
        'CCA': ' Pro ', 'CCC': ' Pro ', 'CCG': ' Pro ', 'CCT': ' Pro ',
        'CAC': ' His ', 'CAT': ' His ', 'CAA': ' Gin ', 'CAG': ' Gin ',
        'CGA': ' Arg ', 'CGC': ' Arg ', 'CGG': ' Arg ', 'CGT': ' Arg ',
        'GTA': ' Val ', 'GTC': ' Val ', 'GTG': ' Val ', 'GTT': ' Val ',
        'GCA': ' Ala ', 'GCC': ' Ala ', 'GCG': ' Ala ', 'GCT': ' Ala ',
        'GAC': ' Asp ', 'GAT': ' Asp ', 'GAA': ' Glu ', 'GAG': ' Glu ',
        'GGA': ' Gly ', 'GGC': ' Gly ', 'GGG': ' Gly ', 'GGT': ' Gly ',
        'TCA': ' Ser ', 'TCC': ' Ser ', 'TCG': ' Ser ', 'TCT': ' Ser ',
        'TTC': ' Phe ', 'TTT': ' Phe ', 'TTA': ' Leu ', 'TTG': ' Leu ',
        'TAC': ' Tyr  ', 'TAT': ' Tyr  ', 'TAA': '-', 'TAG': '-',
        'TGC': ' Cys ', 'TGT': ' Cys ', 'TGA': '_', 'TGG': ' Trp ',
    }
    protein = ""
    if len(seq) % 3 == 0:
        for i in range(0, len(seq), 3):
            codon = seq[i:i + 3]
            protein += table[codon]
        return protein

seq_protein = translate(seq_DNA)
# Put proteins sequences in protein file
protein_file.write(seq_protein)
# Close all file
mRNA_file.close()
protein_file.close()
dna_file.close()
# --- End of the project ---