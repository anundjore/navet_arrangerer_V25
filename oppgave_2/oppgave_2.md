# Oppgave 2: Kryptert melding

Alice og Bob har utviklet en metode for å sende kodede meldinger. De har blitt enige om en kodenøkkel som består av de 29 bokstavene fra A til Å i en tilfeldig rekkefølge.

## Krypteringsmetode
For å kryptere en bokstav `x`, byttes den ut med bokstaven som er én plass til høyre i nøkkelen. Dersom `x` er den siste bokstaven i nøkkelen, byttes den ut med den første bokstaven i nøkkelen.

### Eksempel
Hvis nøkkelen er:
```
OSYKQGEZHBLVRPXUCJMAWDTNFI
```

Og meldingen som skal kodes er:
```
HEIBERITHVORDANHARDUDET
```

Så blir den kryptert til:
```
BZOLZPONBRSPTWFBWPTCTZN
```

Ettersom med denne nøkkelen blir H til B, E til Z, I til O, osv.

## Oppgave
Skriv et program som dekrypterer følgende melding:
```
ÆHRRXCQVHQCÆQKFKQLMSXFRSÆQMSCCSREQCQC
```

**Lykke til! Vis frem løsningen din til oss på Awk når du er ferdig for å være med i trekningen av premier!**

