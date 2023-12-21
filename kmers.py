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


def get_reverse(codon): 
    """
    obtain the reverse codon
    """
    to_reverse = {"A": "T", "C":"G", "T":"A", "G":"C"}
    reverse = ''
    for ntd in codon:
        if ntd not in to_reverse.keys():
            break
        else:
            reverse = reverse + to_reverse[ntd]
    return reverse[::-1]

def stream_kmers(text, k):
    """
    on coupe le texte en mots de longueur k 
    traduire ces mots ntd par ntd (de str à binaire)
    on va faire un dictionnaire encodage
    A = 0 --> en bit 00 
    C = 1 --> en bit 01
    T = 2 --> en bit 10
    G = 3 --> en bit 11
    """
    # --- To complete ---
    encodage = {"A":0, "C": 1, "T":2, "G":3}
   
    for i in range(len(text)-k+1):
        kmer_mask = 0 
        kmer = text[i:i+k]
        for letter in kmer: 
            if letter not in encodage.keys(): 
                break
            else:
                kmer_mask <<= 2 
                kmer_mask |= encodage[letter]

        reverse_kmer_mask = 0 
        reverse_kmer = get_reverse(kmer)
        for r_letter in reverse_kmer: 
            reverse_kmer_mask <<= 2 
            reverse_kmer_mask |= encodage[r_letter]
            
        yield kmer_mask, reverse_kmer_mask

def main():
    pass
