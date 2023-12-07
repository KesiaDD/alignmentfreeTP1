#!/usr/bin/env python

def kmer2str(val, k):
    """ Transform a kmer integer into a its string representation
    :param int val: An integer representation of a kmer
    :param int k: The number of nucleotides involved into the kmer.
    :return str: The kmer string formatted
    """
    letters = ['A', 'C', 'T', 'G']
    str_val = []
    for i in range(k):
        str_val.append(letters[val & 0b11])
        val >>= 2

    str_val.reverse()
    return "".join(str_val)

# def get_reverse(codon): 
#     to_reverse = {"A": "T", "C":"G", "T":"A", "G":"C"}
#     reverse = ''
#     for ntd in codon: 
#         reverse = reverse + to_reverse[ntd]
#     return reverse[::-1]

def stream_kmers(text, k):
    # --- To complete ---
    liste_kmers = []
    for i in range(len(text)-k+1):
        kmer = text[i:i+k]
        # if kmer in liste_kmers: 
        #     continue
        # else: 
        #     if get_reverse(kmer) not in liste_kmers: 
        #         liste_kmers.append(kmer)
        liste_kmers.append(kmer)
    return liste_kmers


def main():
    pass
