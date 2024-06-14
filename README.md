# Masterarbeit Julius Plots

Moin Julius, hier ist eine kleine Anleitung wie du das installierst.

Als erstes hast du hoffentlich Python installiert, du brauchst mindestens Version 3.11. Dann musst du poetry installieren:

    https://python-poetry.org/docs/#installing-with-the-official-installer

Siehe "Windows (Powershell)" Anleitung. Eigentlich musst du nur einen Befehl ausführen.

    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -

## Die Software runterladen

Wenn du das alles geschafft hast dann kannst du jetzt die Software runterladen.
Dafür klickst du auf das grüne Code Knöpfchen und sagst dann als "Zip Downloaden"

Jetzt entpackst du alles und gehst dann in den Ordner wo alles entpackt ist. Dort öffnest du jetzt eine Console und tippst:

    poetry install

Jetzt sollte der alles installieren. Er sagt dann am ende dass das nicht geklapt hat... dass ist aber egal.
Jetzt führst du den Spaß aus indem du eintippst:

    poetry run python create_plot.py
