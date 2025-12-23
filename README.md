# BewerbungsGenerator

## Kurzbeschreibung

Ein automatisiertes Python-Tool zur Erstellung und zum Versand personalisierter Bewerbungsunterlagen. Das Programm liest Schuldaten aus einer CSV-Datei, generiert individuell angepasste Bewerbungs-PDFs mithilfe von LaTeX-Templates, fügt Zeugnisse hinzu und versendet die fertigen Dokumente automatisch per E-Mail an die jeweiligen Schulen.

## Inhaltsverzeichnis

- [Funktionsweise](#funktionsweise)
- [Voraussetzungen](#voraussetzungen)
- [Installation](#installation)
- [Konfiguration](#konfiguration)
- [Verwendung](#verwendung)
- [Dateistruktur](#dateistruktur)
- [CSV-Format](#csv-format)
- [LaTeX-Template](#latex-template)
- [Lizenz](#lizenz)

## Funktionsweise

Der BewerbungsGenerator automatisiert den gesamten Prozess der Bewerbungserstellung und -versendung:

1. **Datenimport**: Liest Schulinformationen (Name, Adresse, E-Mail) aus einer CSV-Datei
2. **Personalisierung**: Passt ein LaTeX-Template für jede Schule individuell an
3. **PDF-Generierung**: Kompiliert die personalisierten LaTeX-Dokumente zu PDF-Dateien
4. **Dokumentenzusammenführung**: Fügt Zeugnisse und andere Anhänge zur Bewerbung hinzu
5. **Komprimierung**: Reduziert die PDF-Dateigröße mittels Ghostscript für E-Mail-Versand
6. **Automatischer Versand**: Sendet die fertige Bewerbung per E-Mail an die jeweilige Schule

Das Tool ist besonders nützlich für Lehrkräfte, die sich bei mehreren Schulen bewerben möchten, da es den manuellen Aufwand erheblich reduziert und gleichzeitig eine professionelle, einheitliche Präsentation gewährleistet.

## Voraussetzungen

### Software

- **Python 3.x** mit folgenden Paketen:
  - `pandas` - für CSV-Verarbeitung
  - `pypdf` - für PDF-Manipulation
  
- **LaTeX-Distribution** (z.B. MiKTeX oder TeX Live)
  - `pdflatex` muss im System-PATH verfügbar sein
  
- **Ghostscript** für PDF-Komprimierung
  - Download: [https://www.ghostscript.com/](https://www.ghostscript.com/)
  - Standard-Installationspfad: `C:\Program Files\gs\gs10.05.1\bin\gswin64c.exe`

### E-Mail-Konto

- Ein GMX-E-Mail-Konto (oder anpassbar für andere SMTP-Server)
- SMTP-Zugriff aktiviert
- Anwendungsspezifisches Passwort (empfohlen)

## Installation

1. **Repository klonen:**
```bash
git clone https://github.com/Haasrobertgmxnet/BewerbungsGenerator.git
cd BewerbungsGenerator
```

2. **Python-Abhängigkeiten installieren:**
```bash
pip install pandas pypdf
```

3. **LaTeX-Distribution installieren:**
   - Windows: [MiKTeX](https://miktex.org/download)
   - Linux: `sudo apt-get install texlive-full`
   - macOS: [MacTeX](https://www.tug.org/mactex/)

4. **Ghostscript installieren:**
   - Windows: Download von [ghostscript.com](https://www.ghostscript.com/)
   - Linux: `sudo apt-get install ghostscript`
   - macOS: `brew install ghostscript`

## Konfiguration

### 1. E-Mail-Zugangsdaten

Öffnen Sie die Hauptdatei und tragen Sie Ihre E-Mail-Zugangsdaten ein:

```python
sender_email = "ihre-email@gmx.net"
sender_pass = "ihr-passwort"  # Verwenden Sie ein anwendungsspezifisches Passwort!
```

**⚠️ Sicherheitshinweis:** Speichern Sie keine Passwörter im Code! Verwenden Sie Umgebungsvariablen oder eine separate Konfigurationsdatei.

### 2. Pfade anpassen

Falls erforderlich, passen Sie folgende Pfade an:

```python
csv_path = '../../Schulen.csv'          # Pfad zur CSV-Datei
tex_file = '../../../Template/ACV.tex'  # Pfad zum LaTeX-Template
gs_path = r"C:\Program Files\gs\gs10.05.1\bin\gswin64c.exe"  # Ghostscript-Pfad
```

### 3. Zeugnisse vorbereiten

Platzieren Sie Ihre Zeugnisse als `Zeugnisse.pdf` im gleichen Verzeichnis wie das Hauptskript.

## Verwendung

1. **CSV-Datei vorbereiten** mit den Schuldaten (siehe [CSV-Format](#csv-format))
2. **LaTeX-Template anpassen** mit Ihren persönlichen Daten
3. **Programm ausführen:**

```bash
python BewerbungsGenerator.py
```

Das Programm durchläuft dann automatisch alle Einträge in der CSV-Datei und:
- Erstellt für jede Schule ein personalisiertes PDF
- Versendet die Bewerbung per E-Mail
- Gibt den Fortschritt in der Konsole aus

## Dateistruktur

```
BewerbungsGenerator/
├── BewerbungsGenerator/
│   └── BewerbungsGenerator.py    # Hauptprogramm
├── Schulen.csv                    # Schuldaten
├── Template/
│   └── ACV.tex                    # LaTeX-Vorlage
├── Zeugnisse.pdf                  # Ihre Zeugnisse
├── BewerbungsGenerator.sln        # Visual Studio Solution
├── .gitignore
├── .gitattributes
└── README.md
```

## CSV-Format

Die CSV-Datei `Schulen.csv` muss folgende Spalten enthalten (Trennzeichen: Semikolon):

| Spalte | Beschreibung | Beispiel |
|--------|--------------|----------|
| ID | Eindeutige Kennung | `001` |
| Name | Schulname | `Gymnasium Musterstadt` |
| Straße | Straße und Hausnummer | `Hauptstraße 123` |
| PLZ | Postleitzahl | `12345` |
| Stadt | Stadtname | `Musterstadt` |
| E-Mail | E-Mail-Adresse | `sekretariat@gymnasium-musterstadt.de` |

**Beispiel:**
```csv
ID;Name;Straße;PLZ;Stadt;E-Mail
001;Gymnasium Musterstadt;Hauptstraße 123;12345;Musterstadt;sekretariat@gymnasium-musterstadt.de
002;Realschule Beispielort;Schulweg 45;67890;Beispielort;info@realschule-beispielort.de
```

## LaTeX-Template

Das LaTeX-Template (`ACV.tex`) muss folgende Markierungen enthalten:

```latex
%%% Adressat 1 Begin
% Hier wird die vollständige Adresse eingefügt
%%% Adressat 1 End

%%% Adressat 2 Begin
% Hier wird nur der Schulname eingefügt
%%% Adressat 2 End
```

Diese Markierungen werden vom Programm automatisch durch die entsprechenden Daten aus der CSV-Datei ersetzt.

## Technische Details

### Verwendete Technologien

- **Python 3.x**: Hauptprogrammiersprache
- **pandas**: CSV-Verarbeitung und Datenmanipulation
- **pypdf (PdfReader, PdfWriter)**: PDF-Zusammenführung
- **subprocess**: Ausführung externer Programme (pdflatex, Ghostscript)
- **smtplib & email**: E-Mail-Versand
- **re (Regular Expressions)**: Template-Manipulation

### Workflow-Diagramm

```
CSV-Datei → pandas → Für jede Zeile:
                     ├→ LaTeX-Template personalisieren
                     ├→ pdflatex ausführen
                     ├→ Mit Zeugnissen zusammenführen
                     ├→ PDF komprimieren (Ghostscript)
                     └→ E-Mail versenden
```

## Bekannte Einschränkungen

- Passwörter sind im Code gespeichert (Sicherheitsrisiko)
- Keine Fehlerbehandlung bei fehlgeschlagenen E-Mail-Versendungen
- Temporäre Dateien werden nicht automatisch gelöscht
- Hardcodierte Pfade müssen manuell angepasst werden
- Nur für GMX-E-Mail-Konten vorkonfiguriert

## Zukünftige Verbesserungen

- [ ] Externe Konfigurationsdatei für Einstellungen
- [ ] Umgebungsvariablen für sensible Daten
- [ ] Umfassende Fehlerbehandlung und Logging
- [ ] Automatisches Aufräumen temporärer Dateien
- [ ] GUI für einfachere Bedienung
- [ ] Unterstützung weiterer E-Mail-Provider
- [ ] Testabdeckung
- [ ] Fortschrittsanzeige und Zusammenfassung

## Lizenz

Dieses Projekt ist Open Source. Bitte beachten Sie, dass Sie für die Verwendung selbst verantwortlich sind.

## Autor

Robert Haas

## Haftungsausschluss

Dieses Tool dient der Automatisierung des Bewerbungsprozesses. Der Benutzer ist selbst dafür verantwortlich, die Richtigkeit und Angemessenheit der versendeten Bewerbungen zu überprüfen. Der Autor übernimmt keine Haftung für Fehler oder Probleme, die durch die Verwendung dieses Tools entstehen.
