# Brutto-Netto-Gehaltsrechner - (Gross Net Salary Calculator)

- [Brutto-Netto-Gehaltsrechner - (Gross Net Salary Calculator)](#brutto-netto-gehaltsrechner---gross-net-salary-calculator)
  - [:de: Deutsch](#de-deutsch)
    - [Einführung](#einführung)
    - [Ordnerstruktur](#ordnerstruktur)
    - [Tabellenbeschreibungen](#tabellenbeschreibungen)
      - [Entgelttabellen](#entgelttabellen)
      - [Zusatzrentenversicherung](#zusatzrentenversicherung)
      - [Zulagen-Tabellen](#zulagen-tabellen)
    - [Einrichten einer neuen Entgelttabelle](#einrichten-einer-neuen-entgelttabelle)
    - [Einrichtung einer neuen Zusatzrentenversicherung](#einrichtung-einer-neuen-zusatzrentenversicherung)
    - [Einrichten einer neuen Zulagentabelle](#einrichten-einer-neuen-zulagentabelle)
    - [Verknüpfung der Entgelttabelle, der Zusatzrentenversicherung und der Zulagen](#verknüpfung-der-entgelttabelle-der-zusatzrentenversicherung-und-der-zulagen)
  - [:uk: English](#uk-english)
    - [Introduction](#introduction)
    - [Folder Structure](#folder-structure)
    - [Table Descriptions](#table-descriptions)
      - [Remuneration Tables](#remuneration-tables)
      - [Supplementary Pension Insurance](#supplementary-pension-insurance)
      - [Allowance Tables](#allowance-tables)
    - [Setting up a New Remuneration Table](#setting-up-a-new-remuneration-table)
    - [Setting up a New Supplementary Pension Insurance](#setting-up-a-new-supplementary-pension-insurance)
    - [Setting up a New Allowance Table](#setting-up-a-new-allowance-table)
    - [Linking the Remunerations Table, Supplementary Pension Insurance, and Allowances](#linking-the-remunerations-table-supplementary-pension-insurance-and-allowances)


## :de: Deutsch

### Einführung 

Willkommen im Repository des Brutto-Netto-Gehaltsrechners! Dieses Open-Source-Projekt wurde speziell für Angestellte des öffentlichen Dienstes in Deutschland entwickelt, um ihr Nettogehalt zu ermitteln. Das Repository speichert die notwendigen Daten und den Sourcecode, der von der Website https://lohntastik.de/od-rechner/tv-gehaltsrechner verwendet wird, die das Bruttogehalt auf der Grundlage der in diesem Repository gespeicherten Informationen berechnet. Es enthält eine umfangreiche Sammlung von Daten, darunter Source Codes, Entgelttabellen, Progressionstabellen, Zulagenoptionen, Angaben zur privaten Rentenversicherung und mehr. Wir freuen uns über Beiträge aus der Community, um dieses wichtige Instrument zu erweitern und zu verbessern. Wenn Sie Interesse haben, einen Beitrag zu leisten, lesen Sie bitte die nachstehende Beschreibung, um loszulegen.

### Ordnerstruktur

Die Ordnerstruktur für die Speicherung der Entgelttabelleninformationen sieht wie folgt aus:

```
- tables Ordner
  └── remuneration_name Ordner
      ├── Adv.csv
      ├── Table.csv
      └── Meta.csv
- prv Ordner
  └── prv_name Ordner
      ├── Meta.csv
- allowances Ordner
  └── allowance_name Ordner
      ├── Table.csv
      └── Meta.csv
```


- Der Ordner `tables` enthält alle Entgelttabellen.
- Jede Entgelttabelle wird in einem eigenen Ordner unter dem Ordner `tables` gespeichert.
- Der Ordnername für jede Entgelttabelle sollte angegeben werden und wird später im Brutto-Netto-Gehaltsrechner verwendet.
- Der Ordner mit den Entgelttabellen enthält drei Dateien: `Adv.csv`, `Table.csv`, und `Meta.csv`.
- Im Ordner `prv` werden die Informationen zu den Pensionsplänen für den öffentlichen Sektor gespeichert.
- Jeder Pensionsplan sollte seinen eigenen Ordner unter dem Ordner `prv` haben.
- Der Ordnername für jeden Pensionsplan sollte unter dem Schlüsselwort `prv` in der Datei `Meta.csv` für die Entgelttabellen angegeben und verwendet werden.
- Der Ordner `prv_name` enthält eine "Meta.csv"-Datei mit den entsprechenden Informationen.
- Der Ordner `allowances` enthält die Informationen zu den Zulagen.
- Für jede Zulage sollte ein eigener Ordner unter dem Ordner `allowances` angelegt werden.
- Der Name des Ordners für jede Zulage sollte unter dem Schlüsselwort `allowances` in der Datei `Meta.csv` für die Entgelttabellen angegeben und verwendet werden.
- Der Ordner `allowances` enthält eine Datei "Table.csv" und eine Datei "Meta.csv".

### Tabellenbeschreibungen

#### Entgelttabellen

1. `Adv.csv`: Stufenlaufzeit mit Angabe der Anzahl der Jahre, die für den Aufstieg in die nächste Stufe für jede Kombination aus Entgeltgruppe und Stufe erforderlich sind.

  Feldbeschreibungen:
  - Die erste Spalte enthält die Namen der Entgeltgruppen.
  - Die erste Zeile enthält die Namen der Stufen.
  - Die anderen Zellen enthalten die Anzahl der Jahre, die in einer bestimmten Stufe verbracht werden müssen, um in die nächste Stufe aufzusteigen.

  Beispiel:
  ```csv
  T,1,2,3,4,5,6
  18,1,3,4,4,5,
  17,1,3,4,4,5,
  ```

  In der 18. Entgeltgruppe dauert es beispielsweise 1 Jahr, um von der Stufe 1 in die Stufe 2 aufzusteigen, 3 Jahre, um von der Stufe 2 in die Stufe 3 aufzusteigen, und so weiter.

2. `Table.csv`: Enthält das monatliche Bruttogehalt für jede Kombination aus Entgeltgruppe und Stufe.

  Feldbeschreibungen:
  - Die erste Spalte enthält die Namen der Entgeltgruppen.
  - Die erste Zeile enthält die Namen der Stufen.
  - Die anderen Zellen enthalten das monatliche Bruttogehalt für jede Kombination aus Entgeltgruppe und Dienstaltersstufe.

  Beispiel:
  ```csv
  T,1,2,3,4,5,6
  18,4025.78,4133.45,4666.83,5066.83,5666.85,6033.52
  17,3696.23,3966.79,4400.13,4666.83,5200.16,5513.51
  ```

3. `Meta.csv`: Speichert Metainformationen zu der Entgelttabelle.

  Feldbeschreibungen:
  - Die erste Spalte enthält den Namen des Feldes.
  - Die zweite Spalte steht für den entsprechenden Wert.
  - Wenn es mehrere Werte für ein Feld gibt, sollten sie durch ein Semikolon (`;`) getrennt werden.

  Beispiel:
  ```csv
  name,value
  pay_grad_name,E
  valid_from,2022.12.02
  link,
  name_de,Tarifvertrag Allgemeiner Teil
  name_en,Collective Agreement General Part
  allowances,tv-l-annual-bonus;tv-l-function-allowance;tv-l-foreman-allowance;tv-l-tier-allowance
  prv,vbl-west;vbl-east;vbl-west-n-atv;vbl-east-n-atv;kvbw
  ```

  Feldbeschreibungen:
   - `pay_grad_name`: Der Name der mit der Entgelttabelle verbundenen Entgeltgruppe. Er wird der Nummer der Entgeltgruppe der Entgelttabelle vorangestellt.
   - `valid_from`: Das Datum, ab dem die Entgelttabelle gültig ist.
   - `link`: Der Link zu dem Dokument, aus dem der Inhalt der Entgelttabelle entnommen wird.
   - `name_de`: Der Name der Entgelttabelle in deutscher Sprache.
   - `name_en`: Der Name der Entgelttabelle in englischer Sprache.
   - `allowances`: Eine durch Semikolon getrennte Liste der Namen der Zulagen, die mit dieser Entgelttabelle verbunden sind.
   - `prv`: Eine durch Semikolon getrennte Liste der mit dieser Entgelttabelle verknüpften Pensionsplantypen.


#### Zusatzrentenversicherung 

1. `Meta.csv`: Speichert Metainformationen über die Zusatzrentenversicherung.

  Spaltenbeschreibungen:
  - Die erste Spalte steht für den Namen des Feldes.
  - Die zweite Spalte steht für den entsprechenden Wert.
  - Die dritte Spalte enthält einen optionalen Kommentar zu dem Feld.

  Die Datei `Meta.csv` für jeden Rentenplan enthält die folgenden Felder:

   - `link`:: Die URL, die auf das Quelldokument für den Pensionsplan verweist.
   - `info`: Zusätzliche Informationen über den Pensionsplan.
   - `calc_fun`: Der Dateiname, der die Funktion `prv` enthält, die für die Berechnung der Sozialversicherungsbeiträge und des steuerpflichtigen Bruttogehalts zuständig ist. Sie sollte im Ordner `script/prv` gespeichert werden und muss der angegebenen Definition entsprechen.
   - `label_de`: Das für den Pensionsplan verwendete Label in deutscher Sprache.
   - `label_en`: Die Bezeichnung für den Pensionsplan in englischer Sprache.
   - `info_de`: Informationen über den Pensionsplan auf Deutsch.
   - `info_en`: Informationen über den Pensionsplan in englischer Sprache.
   - Benutzerdefinierte Felder: Diese Felder können je nach Rentenplan variieren und werden als Eingaben in der Funktion `prv` verwendet.

  Beispiel:
  ```csv
  name,value,comment
  link,,
  info,,
  calc_fun,vbl_west,
  label_de,VBL-West,
  label_en,VBL-West,
  info_de,,
  info_en,,
  arbeitnehmeranteil,1.81,,
  arbeitgeberanteil,5.49,,
  pauschal,92.03,"Pauschalversteuerung der Arbeitgeberumlage nach § 40b EStG i. V. m. § 37 Abs. 2 ATV"
  steuer_frei,219,"Steuerfreie Umlage des Arbeitgebers nach § 3 Nr. 56 EStG"
  grenzbetrag,100,"Zurechnungsbetrag 1: abzgl. Grenzbetrag"
  sozi_freibetrags,13.30,"Zurechnungsbetrag 2: abzgl. Abzüglich des Freibetrags"
  ```

#### Zulagen-Tabellen

1. `Table.csv`: Enthält die Zulage für jede Kombination aus Entgeltgruppe und Option.

  Feldbeschreibungen:
  - Die erste Spalte enthält die Namen der Entgeltgruppen.
  - Die erste Zeile enthält die Namen der Optionen.
  - Die Zellen enthalten die tatsächliche Zulage für jede Kombination aus Entgeltgruppe und Option.
  - Wenn für die Entgeltgruppe `-1` angegeben wird, dann wird diese Option für alle Entgeltgruppen verwendet.

  Beispiel:
  ```csv
  T,no,yes
  18,0,386.18
  ```

2. `Meta.csv`: Speichert Metainformationen über die Zulage.

  Spaltenbeschreibungen:
   - Die erste Spalte steht für den Namen des Feldes.
   - Die zweite Spalte steht für den entsprechenden Wert.
  
  Sie umfasst die folgenden Felder:

   - `info`: Zusätzliche Informationen über die Zulage.
   - `func_type`: Der zur Berechnung der Zulage verwendete Funktionstyp (z. B. fabsolute oder frelative).
   - `adding_type`: Soll dieser Betrag zum Monatsgehalt oder nur zum Jahresgehalt hinzugerechnet werden, wie ein Jahressonderzahlung (z. B. `monthly` oder `yearly`).
   - `label_de`: Das für die Zulage verwendete Label in deutscher Sprache.
   - `label_en`: Die Bezeichnung der Zulage in englischer Sprache.
   - `info_de`: Informationen über die Zulage in deutscher Sprache.
   - `info_en`: Informationen über die Zulage in englischer Sprache.
   - `options`: Die verfügbaren Optionen für die Zulage, getrennt durch `;`.
   - `default_option`: Die Standardoption für die Zulage.
   - `options_label_de`: Die Bezeichnungen für die Optionen in deutscher Sprache, getrennt durch `;`.
   - `options_label_en`: Die Bezeichnungen für die Optionen in englischer Sprache, getrennt durch `;`.


   Beispiel:
   ```csv
   name,value
   info,https://www.arbeitsagentur.de/bakarriere/ba-tarifvertrag
   func_type,fabsolute
   adding_type,monthly
   label_de,Funktionsstufe 2
   label_en,Function Level 2
   info_de,"Die Funktionsstufe ist ein zusätzliches Entgelt innerhalb des Entgeltsystems der Bundesagentur für Arbeit, das für zusätzliche Aufgaben oder Herausforderungen aufgrund der Komplexität und Verantwortung der Tätigkeit gewährt wird. Die Zusatzzahlung für Funktionsstufe 2 beträgt {{yes_value}}."
   info_en,"Funktionsstufe represents additional compensation within the Federal Employment Agency's pay system, awarded for extra tasks or challenges based on job complexity and responsibilities. The additional payment for Function Level 2 is {{yes_value}}."
   options,no;yes
   default_option,no
   options_label_de,Nein;Ja
   options_label_en,No;Yes
   ```
  

### Einrichten einer neuen Entgelttabelle

Um eine neue Entgelttabelle einzurichten, gehen Sie folgendermaßen vor:

1. Erstellen Sie einen neuen Ordner unter dem Ordner `tables` mit einem aussagekräftigen Namen für die Entgelttabelle (z.B. `TV-L`).
2. Erstellen Sie in dem neu angelegten Ordner die folgenden Dateien:
   - `Adv.csv`: Fügen Sie die Progression der Vergütung hinzu, wobei die Spalten die Tiers und die Zeilen die Entgeltgruppen darstellen. Die erste Spalte sollte den Namen/die Nummer der Entgeltgruppe (z. B. 1, 2a, 3 usw.) und die erste Zeile den Namen der Stufe enthalten. Die erste Zelle sollte `T` lauten. Geben Sie in die Zellen die Anzahl der Jahre ein, die in jeder Stufe verbracht werden müssen, um in die nächste Stufe aufzusteigen.
   - `Table.csv`: Erstellen Sie eine Tabelle mit der gleichen Struktur wie `Adv.csv`, aber geben Sie anstelle der Jahre das monatliche Bruttogehalt für jede Stufe und Entgeltgruppe ein.
   - `Meta.csv`: Fügen Sie Metainformationen zur Entgelttabelle hinzu, einschließlich der Bezeichnung der Entgeltgruppe, der Bezeichnungen in Deutsch und Englisch, der Art des Pensionsplans für den öffentlichen Sektor und der Zulagen. Die Feldnamen und -werte entnehmen Sie bitte dem obigen Beispiel.

### Einrichtung einer neuen Zusatzrentenversicherung

Gehen Sie wie folgt vor, um eine neue Zusatzrentenversicherung einzurichten:

1. Erstellen Sie einen neuen Ordner unter dem Ordner `prv` mit einem aussagekräftigen Namen für den Rentenplan (z. B. `vbl-west`).
2. Erstellen Sie innerhalb des neu erstellten Ordners eine Datei `Meta.csv` mit den erforderlichen Feldern zur Definition des Pensionsplans. Die Feldnamen und -werte entnehmen Sie bitte dem oben angeführten Beispiel.
3. Dieser Schritt kann entfallen, wenn das `script/prv` bereits ein Skript enthält, das zur Berechnung der Sozialversicherungsbeiträge und des steuerpflichtigen Bruttogehalts verwendet werden kann. Andernfalls implementieren Sie eine Python-Funktion zur Berechnung des Sozialversicherungsbeitrags und des steuerpflichtigen Bruttogehalts auf der Grundlage des in der Datei `Meta.csv` angegebenen Werts `calc_fun`. Speichern Sie diese Funktion im Ordner `script/prv`.

### Einrichten einer neuen Zulagentabelle

Führen Sie folgende Schritte aus, um eine neue Tabelle für Zulagen einzurichten:

1. Erstellen Sie einen neuen Ordner unter dem Ordner `allowances` mit einem aussagekräftigen Namen für die Zulage (z. B. `tv-l-function-allowance`).
2. Erstellen Sie innerhalb des neu erstellten Ordners die folgenden Dateien:
   - `Table.csv`: Erstellen Sie eine Tabelle mit den Zulagen für jede Kombination aus Entgeltgruppe und Option. Die Zeilen stehen für die Entgeltgruppen, die Spalten für die Optionen. Die Zellenwerte stellen die Zulagen dar. Verwenden Sie `-1` für die Entgeltgruppe, wenn die Option für alle Entgeltgruppen gilt.
   - `Meta.csv`: Fügen Sie Metainformationen zur Zulage hinzu. Die Feldnamen und -werte entnehmen Sie bitte dem obigen Beispiel.

### Verknüpfung der Entgelttabelle, der Zusatzrentenversicherung und der Zulagen

Um die Entgelttabelle, die Zusatzrentenversicherung und die Zulagen miteinander zu verknüpfen, müssen Sie Folgendes beachten:

1. Geben Sie in der Datei `Meta.csv` der Entgelttabelle die entsprechenden Zusatzrentenversicherungen und Zulagen an, indem Sie deren Ordnernamen in die Felder `prv` bzw. `allowances` aufnehmen.
2. In der Datei `Meta.csv` der prv geben Sie den Link zur Zusatzrentenversicherung und andere relevante Informationen an.
3. In der Datei `Meta.csv` für jede Zulage geben Sie die erforderlichen Metainformationen und den Link zu zusätzlichen Angaben an.

---

## :uk: English

### Introduction

Welcome to the Gross Net Salary Calculator repository! This open-source project was developed specifically for public sector employees in Germany to determine their net salary. The repository stores the necessary data and source code used by the website https://lohntastik.de/od-rechner/tv-gehaltsrechner, which calculates the gross salary based on the information stored in this repository. It contains an extensive collection of data including source codes, salary tables, progression tables, allowance options, private pension insurance details and more. We welcome contributions from the community to expand and improve this important tool. If you are interested in contributing, please read the description below to get started.

### Folder Structure

The folder structure for storing the remuneration information is as follows:

```
- tables Folder
  └── remuneration_name Folder
      ├── Adv.csv
      ├── Table.csv
      └── Meta.csv
- prv Folder
  └── prv_name Folder
      ├── Meta.csv
- allowances Folder
  └── allowance_name Folder
      ├── Table.csv
      └── Meta.csv
```

- The `tables` folder contains all the remuneration tables.
- Each remuneration table is stored in a separate folder under the `tables` folder.
- The folder name for each remuneration table should be specified and it is used later in the gross net salary calculator.
- The remuneration table folder includes three files: `Adv.csv`, `Table.csv`, and `Meta.csv`.
- The `prv` folder stores the information related to the Pension plans for the public sector.
- Each Pension plan should have its folder under the `prv` folder.
- The folder name for each Pension plan should be specified and used under the `prv` keyword in the remuneration tables `Meta.csv` file.
- The Pension plan folder includes a `Meta.csv` file with the relevant information.
- The `allowances` folder stores the information related to the allowances.
- Each allowance should have its folder under the `allowances` folder.
- The folder name for each allowance should be specified and used under the `allowances` keyword in the remuneration tables `Meta.csv` file.
- The allowance folder includes a `Table.csv` file and a `Meta.csv` file.

### Table Descriptions

#### Remuneration Tables

1. `Adv.csv`: Progression of the remuneration, specifying the number of years needed to advance to the next tier for each pay grade and tier combination.

  Field descriptions:
  - The first column represents the pay grade names.
  - The first row represents the tier names.
  - The other cells contain the number of years that need to be spent in a specific tier to advance to the next tier.

  Example:
  ```csv
  T,1,2,3,4,5,6
  18,1,3,4,4,5,
  17,1,3,4,4,5,
  ```

  For example, in the 18th pay grade, it takes 1 year to advance from tier 1 to tier 2, 3 years to advance from tier 2 to tier 3, and so on.

2. `Table.csv`: Contains the monthly gross salary for each pay grade and tier combination.

  Field descriptions:
  - The first column represents the pay grade names.
  - The first row represents the tier names.
  - The other cells contain the monthly gross salary for each pay grade and tier combination.

  Example:
  ```csv
  T,1,2,3,4,5,6
  18,4025.78,4133.45,4666.83,5066.83,5666.85,6033.52
  17,3696.23,3966.79,4400.13,4666.83,5200.16,5513.51
  ```

3. `Meta.csv`: Stores meta information related to the remuneration table.

  Field descriptions:
  - The first column represents the name of the field.
  - The second column represents the corresponding value.
  - If there are multiple values for a field, they should be separated by a semicolon (`;`).

  Example:
  ```csv
  name,value
  pay_grad_name,E
  valid_from,2022.12.02
  link,
  name_de,Tarifvertrag Allgemeiner Teil
  name_en,Collective Agreement General Part
  allowances,tv-l-annual-bonus;tv-l-function-allowance;tv-l-foreman-allowance;tv-l-tier-allowance
  prv,vbl-west;vbl-east;vbl-west-n-atv;vbl-east-n-atv;kvbw
  ```

  Field descriptions:
   - `pay_grad_name`: The name of the pay grade associated with the remuneration table. It will be prepended to the remuneration table pay grade number.
   - `valid_from`: The date from which the remuneration table is valid.
   - `link`: The link to the document from which the content of the remuneration table is extracted.
   - `name_de`: The name of the remuneration table in German.
   - `name_en`: The name of the remuneration table in English.
   - `allowances`: A semicolon-separated list of allowance names associated with this remuneration table.
   - `prv`: A semicolon-separated list of pension plan types associated with this remuneration table.


#### Supplementary Pension Insurance 

1. `Meta.csv`: Stores meta information related to the Supplementary Pension Insurance.

  Column descriptions:
  - The first column represents the name of the field.
  - The second column represents the corresponding value.
  - The third column represents an optional comment for the field.

  The `Meta.csv` file for each Pension plan contains the following fields:

   - `link`: The URL linking to the source document for the Pension plan.
   - `info`: Additional information about the Pension plan.
   - `calc_fun`: The file name that contains the `prv` function, which is responsible for calculating social security contribution and taxable gross salary, and it should be stored in the `script/prv` folder and must adhere to the specified definition.
   - `label_de`: The label used for the Pension plan in German.
   - `label_en`: The label used for the Pension plan in English.
   - `info_de`: Information about the Pension plan in German.
   - `info_en`: Information about the Pension plan in English.
   - Custom fields: These fields can vary based on the specific Pension plan and are used as inputs in the `prv` function.

  Example:
  ```csv
  name,value,comment
  link,,
  info,,
  calc_fun,vbl_west,
  label_de,VBL-West,
  label_en,VBL-West,
  info_de,,
  info_en,,
  arbeitnehmeranteil,1.81,,
  arbeitgeberanteil,5.49,,
  pauschal,92.03,"Pauschalversteuerung der Arbeitgeberumlage nach § 40b EStG i. V. m. § 37 Abs. 2 ATV"
  steuer_frei,219,"Steuerfreie Umlage des Arbeitgebers nach § 3 Nr. 56 EStG"
  grenzbetrag,100,"Zurechnungsbetrag 1: abzgl. Grenzbetrag"
  sozi_freibetrags,13.30,"Zurechnungsbetrag 2: abzgl. Abzüglich des Freibetrags"
  ```

#### Allowance Tables

1. `Table.csv`: Contains the allowance for each pay grade and option combination.

  Field descriptions:
  - The first column represents the pay grade names.
  - The first row represents the option names.
  - The cells contain the actual allowance for each pay grade and option combination.
  - If `-1` is specified for the pay grade, then that option will be used for all pay grades.

  Example:
  ```csv
  T,no,yes
  18,0,386.18
  ```

2. `Meta.csv`: Stores meta information related to the allowance.

   Column descriptions:
   - The first column represents the name of the field.
   - The second column represents the corresponding value.
  
  It includes the following fields:

   - `info`: Additional information about the allowance.
   - `func_type`: The function type used to calculate the allowance (e.g., `fabsolute` or `frelative`).
   - `adding_type`: Should this be added to the monthly salary or only to the yearly salary, such as an annual bonus (e.g., `monthly` or `yearly`).
   - `label_de`: The label used for the allowance in German.
   - `label_en`: The label used for the allowance in English.
   - `info_de`: Information about the allowance in German.
   - `info_en`: Information about the allowance in English.
   - `options`: The available options for the allowance, separated by ";".
   - `default_option`: The default option for the allowance.
   - `options_label_de`: The labels for the options in German, separated by ";".
   - `options_label_en`: The labels for the options in English, separated by ";".


   Example:
   ```csv
   name,value
   info,https://www.arbeitsagentur.de/bakarriere/ba-tarifvertrag
   func_type,fabsolute
   label_de,Funktionsstufe 2
   label_en,Function Level 2
   info_de,"Die Funktionsstufe ist ein zusätzliches Entgelt innerhalb des Entgeltsystems der Bundesagentur für Arbeit, das für zusätzliche Aufgaben oder Herausforderungen aufgrund der Komplexität und Verantwortung der Tätigkeit gewährt wird. Die Zusatzzahlung für Funktionsstufe 2 beträgt {{yes_value}}."
   info_en,"Funktionsstufe represents additional compensation within the Federal Employment Agency's pay system, awarded for extra tasks or challenges based on job complexity and responsibilities. The additional payment for Function Level 2 is {{yes_value}}."
   options,no;yes
   default_option,no
   options_label_de,Nein;Ja
   options_label_en,No;Yes
   ```
  

### Setting up a New Remuneration Table

To set up a new remuneration table, follow these steps:

1. Create a new folder under the `tables` folder with a meaningful name for the remuneration table (e.g., `TV-L`).
2. Inside the newly created folder, create the following files:
   - `Adv.csv`: Add the progression of the remuneration, where the columns represent the Tiers and the rows represent the pay grades. The first column should be the pay grade name/number (e.g. 1, 2a, 3 etc.), and the first row should be the tier name. The first cell should be `T`. Fill in the cells with the number of years that need to be spent in each tier to advance to the next tier.
   - `Table.csv`: Create a table with the same structure as `Adv.csv`, but instead of years, enter the monthly gross salary for each tier and pay grade.
   - `Meta.csv`: Add meta information related to the remuneration table, including the pay grade name, labels in German and English, pension plan type for the public sector, and allowances. Refer to the provided example above for field names and values.

### Setting up a New Supplementary Pension Insurance

To set up a new Supplementary Pension Insurance, follow these steps:

1. Create a new folder under the `prv` folder with a meaningful name for the Pension plan (e.g., `vbl-west`).
2. Inside the newly created folder, create a `Meta.csv` file with the necessary fields to define the Pension plan. Refer to the provided example above for field names and values.
3. This step can be excluded if the `script/prv` already includes a script that can be used to calculate the social security contribution and taxable gross salary. Otherwise, implement a Python function for the calculation of social security contribution and taxable gross salary based on the provided `calc_fun` value in the `Meta.csv` file. Store this function under the `script/prv` folder.

### Setting up a New Allowance Table

To set up a new allowance table, follow these steps:

1. Create a new folder under the `allowances` folder with a meaningful name for the allowance (e.g., `tv-l-function-allowance`).
2. Inside the newly created folder, create the following files:
   - `Table.csv`: Create a table with the allowance for each pay grade and option combination. The rows represent the pay grades, and the columns represent the options. The cell values represent the allowances. Use `-1` for the pay grade if the option applies to all pay grades.
   - `Meta.csv`: Add meta information related to the allowance. Refer to the provided example above for field names and values.

### Linking the Remunerations Table, Supplementary Pension Insurance, and Allowances

To link the remunerations table, supplementary pension insurance, and allowances together, ensure the following:

1. In the `Meta.csv` file of the remuneration table, specify the corresponding supplementary pension insurances and allowances by including their folder names under the `prv` and `allowances` fields, respectively.
2. In the `Meta.csv` file of the prv, specify the link to the Supplementary Pension Insurance and other relevant information.
3. In the `Meta.csv` file of each allowance, specify the necessary meta information and link to additional details.