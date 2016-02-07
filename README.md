# Freie Amateurfunkrufzeichen in Deutschland

Es wird das [“Verzeichnis der zugeteilten deutschen Amateurfunkrufzeichen und
ihrer Inhaber (Rufzeichenliste)”](http://www.bundesnetzagentur.de/SharedDocs/Downloads/DE/Sachgebiete/Telekommunikation/Unternehmen_Institutionen/Frequenzen/Amateurfunk/Rufzeichenliste/Rufzeichenliste_AFU.pdf?__blob=publicationFile&v=10) benötigt.

Zum extrahieren der vergebenen Rufzeichen wird [pdfgrep](https://pdfgrep.org) in mindestens Version 1.4.0 benötigt.

Momentan existiert nur eine Ausgabe aller freien Klasse E Rufzeichen. Es werden die nicht zuteilbaren Suffixe laut BundesNetzAgentur [Amtsblattverfügung Vfg Nr. 12/2005 geändert durch Vfg Nr. 34/2005](https://www.bundesnetzagentur.de/SharedDocs/Downloads/DE/Sachgebiete/Telekommunikation/Unternehmen_Institutionen/Frequenzen/Amateurfunk/AmtsblattverfuegungenAFu/Vfg122005ge228ndertdurcId1833pdf.pdf?__blob=publicationFile&v=4) berücksichtigt. Weiterhin werden persönliche Rufzeichen nur noch mit zwei und drei Buchstaben-Suffix ausgegeben.

Die ausgegebene Liste ist keine Gewähr darauf, dass ein Rufzeichen tatsächlich verfügbar ist. Nach Rückgabe eines Rufzeichens oder dem Tod des vorherigen Inhabers, ist ein Rufzeichen für eine gewissen Zeit gesperrt. Letzten Endes ist es Ermessenssache der BundesNetzAgentur, ob ein Rufzeichen vergeben werden kann. Die [Dienstleistungzentren Amteurfunkverwaltung](http://www.bundesnetzagentur.de/DE/Sachgebiete/Telekommunikation/Unternehmen_Institutionen/Frequenzen/SpezielleAnwendungen/Amateurfunk/amateurfunk_node.html) geben hier weitere Auskunft.

Die Idee stammt aus der Liste der freien österreichischen Suffixe beim [Metalab](https://metalab.at/wiki/MetaFunk/Rufzeichen).

## Ausbau / TODO

### Code
  - ~~Rufzeichenlisten PDF runterladen~~
  - generierte Textliste der vergebenen Rufzeichen zwischenspeichern und nicht jedes Mal neu aus dem PDF generieren
  - bessere Effizienz durch Listencompare statt Iteration mit Regular Expressions

### Suche
  - Suche nach nicht vergebenen Rufzeichen
  - Vorschläge für Initialen oder Abkürzungen

### Regular Expressions für Rufzeichensuchen

Klasse A Rufzeichen: ``/D([CDGHJ][0-9]|[BFKLM][1-9])[A-Z]{2,3}/``

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

