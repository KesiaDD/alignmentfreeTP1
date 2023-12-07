
# Alignment free - TP 1

L'objectif du TP est de comparer 5 especes de bactéries entre elles.
Vous trouverez les données en suivant [ce lien](https://we.tl/t-ACiDxJko7s)

## Composer le TP

Vous devez forker ce projet puis compléter ses fonctions.
Le rendu sera le dépot git dans lequel vous aurrez forké.

Le but est d'obtenir toutes les distances paire à paire des différentes bactéries.
Vous devez compléter le README pour y afficher la matrice des distances des bactéries.
Vous devez également y indiquer le temps 
d'exécution qu'il a fallu pour calculer cette matrice ainsi que l'espace mémoire maximale. Pour cela vous pouvez utiliser la commande ```/usr/bin/time -v```.

En observant les distances obtenues, que pouvez-vous dire des espèces présentes dans cet échantillon ?

## Réponse biologique
Dans la matrice de jaccard, on note une valeur maximale pour les fichiers 945 (Salmonella enterica subsp. enterica serovar Typhimurium str. 14028S substr. GXS275 ) et 785 ( Salmonella enterica subsp  enterica serovar Typhimurium str. LT2) ont une distance de jaccard de 0.9571 ces deux espèces sont donc très éloignées. 

L'espèce 695 (Aeromonas simiae strain A6 chromosome) possède les distances minimales avec toutes les autres espèces. C'est donc l'espèce la plus proches des autres. 

On peut conjecturer que 695 est une espèce ancestrale et que les autres sont des espèces dérivées qui ont subit des mutations. Les espèces les plus éloignées sont 945 et 785. 


## /usr/bin/time -v
 Command being timed: "/home/kesia/Documents/PHYG/C_main.py"
        User time (seconds): 108.34
        System time (seconds): 10.84
        Percent of CPU this job got: 100%
        Elapsed (wall clock) time (h:mm:ss or m:ss): 1:59.00
        Average shared text size (kbytes): 0
        Average unshared data size (kbytes): 0
        Average stack size (kbytes): 0
        Average total size (kbytes): 0
        Maximum resident set size (kbytes): 1545240
        Average resident set size (kbytes): 0
        Major (requiring I/O) page faults: 0
        Minor (reclaiming a frame) page faults: 4662061
        Voluntary context switches: 7
        Involuntary context switches: 1201
        Swaps: 0
        File system inputs: 0
        File system outputs: 16
        Socket messages sent: 0
        Socket messages received: 0
        Signals delivered: 0
        Page size (bytes): 4096
        Exit status: 0



