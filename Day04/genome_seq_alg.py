DNA = "acatatacagatgttgttacgtcgcacggggagtcatccccgcctcgccgctagcccgacttgtgatagcctctaccacggtaccgaaacgtcttcgcta"

seq_to_find = "gcc"
seq_size = 5

# INPUT: dna - string containing a sequence of dna characters of unknown size
# find - the genome sequence to isolate in the dna string
# size - the size of each section of dna to search
# OUTPUT: count - number of times find occurs in each genomic subsequence in the dna
def count_genome_in_dna(dna, find, size):
    count = 0 # holds number of times the find string has been found
    pos = 0 # current position within the dna string
    len_find = len(find) # store the len of find so that I don't have to make repeated calls to len 

    # loop through the dna string
    while (pos < len(dna)):
        subseq_pos = pos # represents the position in the subsequence
        while (subseq_pos < (pos+size-len_find)):
            if (find == dna[subseq_pos:subseq_pos+len_find]):
                # if the characters at the current position in the substring are find, increment count
                count += 1
            subseq_pos += 1
        pos += size # increment to the next subsequence
    return count

# INPUT: filename - name of file to read dna string from. 
# The dna string in the file has to be a single line
# find - the genome sequence to isolate in the dna string
# size - the size of each section of dna to search
# OUTPUT: count - number of times find occurs in each genomic subsequence in the dna
def count_genome_in_file(filename, find, size):
    count = 0

    with open(filename, "rt") as dna:
        subseq = dna.read(size) # the subsequence of the dna to find the specific code
        len_find = len(find)
        while (subseq != ''): # keep going until end of file
            pos = 0 # position within the subsequence
            while (pos < (size - len_find)):
                if (find == subseq[pos:pos+len_find]):
                    count += 1
                pos += 1
            subseq = dna.read(size)
    return count

print(count_genome_in_dna(DNA, seq_to_find, seq_size))
print(count_genome_in_file("dna.txt", seq_to_find, seq_size))
