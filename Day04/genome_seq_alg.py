DNA = "acatatacagatgttgttacgtcgcacggggagtcatccccgcctcgccgctagcccgacttgtgatagcctctaccacggtaccgaaacgtcttcgcta"

seq_to_find = "gcc"
seq_size = 5

def count_genome_in_dna(dna, find, size):
    count = 0
    pos = 0

    while (pos < len(dna)):
        