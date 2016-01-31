# Freie Amateurfunkrufzeichen in Deutschland

Es wird das [“Verzeichnis der zugeteilten deutschen Amateurfunkrufzeichen und
ihrer Inhaber (Rufzeichenliste)”](http://www.bundesnetzagentur.de/SharedDocs/Downloads/DE/Sachgebiete/Telekommunikation/Unternehmen_Institutionen/Frequenzen/Amateurfunk/Rufzeichenliste/Rufzeichenliste_AFU.pdf?__blob=publicationFile&v=10) benötigt.

Zum extrahieren der vergebenen Rufzeichen wird [pdfgrep](https://pdfgrep.org) benötigt.

Momentan existiert nur eine Ausgabe aller freien Klasse A Rufzeichen. Es werden die nicht zuteilbaren Suffixe laut BundesNetzAgentur Amtsblattverfügung Vfg Nr. 12/2005 geändert durch Vfg Nr. 34/2005 berücksichtigt. Weiterhin werden persönliche Rufzeichen nur noch mit zwei und drei Buchstaben-Suffix ausgegeben.

Die Idee stammt aus der Liste der freien össterreichischen Suffixe beim [Metalab](https://metalab.at/wiki/MetaFunk/Rufzeichen).

## Ausbau

### Weitere Rufzeichen

Klasse E Rufzeichen: ``/DO[1-9][A-Z]{2,3}/``

Klubstationen Klasse A (ohne 4-7-stelliges Suffix):
```
DA0[A-Z]{2,3}
DA[0,2,3][A-Z]{1}
D[B-D][0-9][A-Z]{1}
DF0[A-Z]{2,3}
D[F-H][0-9][A-Z]{1}
D[J-M][0-9][A-Z]{1}
DK0[A-Z]{2,3}
DL0[A-Z]{2,3}
DP[3-9][A-Z]{1}
D[Q-R][0-9][A-Z]{1}
```

Klubstationen Klasse E:
```
DA[7-9][A-Z]{1}
DN0[A-Z]{2,3}
DO0[A-Z]{1}
```

### Suche
  - Suche nach nicht vergebenen Rufzeichen
  - Vorschläge für Initialen oder Abkürzungen
