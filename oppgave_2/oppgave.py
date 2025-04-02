
## OPPGAVETEKST ##

#Alice og Bob har utviklet en måte å sende kodede meldinger på. 
# De har først blitt enige om en kodenøkkel som består av de 29 bokstavene fra A til Å i en eller annen rekkefølge. 
# For å kryptere en bokstav x så bytter de den ut med bokstaven som er en plass til høyre for x i nøkkelen. 
# Dersom x var den siste bokstaven i nøkkelen blir den i stedet byttet ut med den første bokstaven i nøkkelen.
#For eksempel, hvis nøkkelen er OSYKQGEZHBLVRPXUCJMAWDTNFI
#Og meldingen som skal kodes er HEIBERITHVORDANHARDUDET
#Så blir den kryptert til BZOLZPONBRSPTWFBWPTCTZN
#Ettersom med denne nøkkelen blir H til B, E til Z, I til O, osv. 

#Skriv et program som knekker denne meldingen:
#ROFFXPZAOZPXKFÆRZNÆPPÆFEZPZP


# Krypteringsnøkkel 
nokkel = "OSYÅKQGEZHØBLVRPXUCJMAÆWDTNFI"

# Kryptert melding 
kryptert_melding = "ROFFXPZAOZPXKFÆRZNÆPPÆFEZPZP"

def dekrypter_melding(nokkel, kryptert_melding):

    #Skriv din løsning her
    
    return dekryptert_melding

# Dekrypter meldingen
dekryptert_melding = dekrypter_melding(nokkel, kryptert_melding)

# Skriv ut den dekrypterte meldingen
print(dekryptert_melding)
