# Branch: Besoldungstabellen der Länder

Dieser Branch dient als Sammelzweig, um Besoldungstabellen der einzelnen Bundesländer per Pull Request strukturiert hinzuzufügen.

## Vorgehen für Pull Requests

1. Für jedes Bundesland einen eigenen PR erstellen.
2. Neue Tabelle unter `tables/` in einem eigenen Ordner anlegen.
3. Pro Tabelle die Dateien `Meta.csv`, `Table.csv` und `Adv.csv` ergänzen.
4. In `Meta.csv` mindestens `valid_from`, `name_de`, `name_en` und `link` pflegen.
5. Wenn nötig, verknüpfte Zulagen (`allowances`) und Zusatzrenten (`prv`) ergänzen.

## Empfohlene Benennung

- `tables/Beamte-<LAND>-A`
- `tables/Beamte-<LAND>-B`
- `tables/Beamte-<LAND>-W`
- `tables/Beamte-<LAND>-R`

Beispiele: `tables/Beamte-BY-A`, `tables/Beamte-NRW-B`.
