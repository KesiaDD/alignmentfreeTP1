from loading import load_directory
from kmers import stream_kmers, kmer2str
import pandas as pd


def jaccard(fileA, fileB, k):
    j = 0
    # --- To complete ---
    
    commun = set()
    kmers_A = stream_kmers(fileA[0],k)
    kmers_B = stream_kmers(fileB[0],k)
    # print("type(kmers a et B)", type(kmers_A), type(kmers_B))
    # print(kmers_A[:10])

    unique_kmers = set(kmers_A + kmers_B)
    set_A = set(kmers_A)
    set_B = set(kmers_B)

    if (set_A & set_B): 
        commun = (set_A & set_B)
    
    j = len(commun)/len(unique_kmers)
    # print(f"pour {fileA} et {fileB} on a {j}")

    return j



if __name__ == "__main__":
    # Load all the files in a dictionary
    files = load_directory("data")
    k = 21
    
    filenames = list(files.keys())
    Matrice_jaccard = pd.DataFrame(columns=filenames, index = filenames)
    for i in range(len(files)):
        print(i,"-------------------------")
        for j in range(i+1, len(files)):
            print(j, "=========================")
            
            # --- Complete here ---
            j_index = jaccard(files[filenames[i]], files[filenames[j]], k)
            Matrice_jaccard[filenames[i]][filenames[j]] = j_index
           
            # print(filenames[i], filenames[j], j_index)
print('la MATRICE')
print(Matrice_jaccard)
print(Matrice_jaccard.max().max())