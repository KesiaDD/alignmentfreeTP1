#!/usr/bin/env python

from loading import load_directory
from kmers import stream_kmers, kmer2str
import pandas as pd
from collections import Counter
from xorshift import xorshift128

def jaccard(fileA, fileB, k):
    kmers_A = Counter(min(kmer) for seqA in fileA for kmer in stream_kmers(seqA, k))
    kmers_B = Counter(min(kmer) for seqB in fileB for kmer in stream_kmers(seqB, k))

    common_kmers = set(kmers_A.keys()) & set(kmers_B.keys())
    common_elem = sum(min(kmers_A[kmer], kmers_B[kmer]) for kmer in common_kmers)

    total = sum(kmers_A.values()) + sum(kmers_B.values()) - common_elem

    j = common_elem / total
    print("j =", j)

    return j



if __name__ == "__main__":
    # Load all the files in a dictionary

    # files = load_directory("datatoy")
    # k = 5 

    files = load_directory("data")
    k = 21
    
    filenames = list(files.keys())
    Matrice_jaccard = pd.DataFrame(columns=filenames, index = filenames)
    for i in range(len(files)):
        print(i, '--------------------------------')
        for j in range(i+1, len(files)):
            print(j, '=====================================')
          
            j_index = jaccard(files[filenames[i]], files[filenames[j]], k)
            Matrice_jaccard[filenames[i]][filenames[j]] = j_index
            print(filenames[i], filenames[j], j_index)
    print('la MATRICE')
    print(Matrice_jaccard)


