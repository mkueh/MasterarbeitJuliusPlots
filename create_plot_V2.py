import pandas as pd
import matplotlib.pyplot as plt
from itertools import chain


# Wover kommen die Daten
onsite_data_file = './data/Zweier_Vergleich_onSite.xlsx'
lab_data_file = './data/Zweier_Vergleich_LabpXRF.xlsx'
icpoes_data_file = './data/Dreier_Vergleich_ICPOES.xlsx'

# Die Spalten welche geplottet werden sollen
elements = ['Cr', 'Ni', 'Cu', 'Zn', 'As', 'Cd', 'Sb', 'Hg', 'Pb']

# Hauptfunktion
def main():
    # Daten einlesen aus xlsx-Dateien
    onsite_data = pd.read_excel(onsite_data_file)
    lab_data = pd.read_excel(lab_data_file)
    icpoes_data = pd.read_excel(lab_data_file)
    
    # Gruppieren nach 'Point' und die einzelnen Dataframes in ein Dictionary speichern
    # ueber die Samplingpointnummer lassen sich jetzt alle zusammengehörige Daten aufrufen
    groups = onsite_data.groupby('Point')
    onsite_by_datapoints = {datapoint: group for datapoint, group in groups}

    lab_data = pd.read_excel(lab_data_file)
    groups = lab_data.groupby('Point')
    lab_data_by_datapoints = {datapoint: group for datapoint, group in groups}
    
    icpoes_data = pd.read_excel(icpoes_data_file)
    groups = icpoes_data.groupby('Point')
    icpoes_data_by_datapoints = {datapoint: group for datapoint, group in groups}
    
    #Suche für jedes Element den maximalen Wert in den Daten, um später die Y-Achsen zu skalieren
    max_value_by_elements = {}
    for element in elements:
        current_max_value = max(chain(onsite_data[element], lab_data[element], icpoes_data[element]))
        max_value_by_elements[element] = current_max_value

    # Iteriere über die Samplingpoints und erstelle für jeden einen 3x3 Plot
    for i, element in enumerate(elements):
        # Daten für den aktuellen Samplingpoint holen
        
    # Subplots erstellen
        # 3x3 Subplots erstellen mit einer Größe von 15x15 Zoll. Die Größe ist eigentlich egal da wir sie später als SVG gespeichert werden
        fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(15, 15))
        
        # Iteriere über die Elemente und erstelle die Subplots innerhalb des Plots
        for j, current_datapoint in enumerate(list(onsite_by_datapoints.keys())):
            selected_columns = ['Depth', 'Point', 'Lower', 'Upper' , element]
            lab_data_datapoint = lab_data_by_datapoints[current_datapoint][selected_columns]
            onsite_data_datapoint = onsite_by_datapoints[current_datapoint][selected_columns]
            icpoes_data_by_datapoint = icpoes_data_by_datapoints[current_datapoint][selected_columns]
            
            # welchen Plot bearbeite ich gerade
            ax = axes[j // 3, j % 3]
            
            #Welche Datenpunkte kommen in den Plot. Onsite Daten
            line1, = ax.plot(onsite_data_datapoint['Depth'], onsite_data_datapoint[element], color='blue', label='pXRF on-Site data' if j == 0 else "")
            
            # Labordaten in den Plot laden
            # Hier ist das etwas komplizierter da wir ja eine Linie zwischen den Werten ziehen wollen
            for _, row in lab_data_datapoint.iterrows():
                a, b, c = row['Lower'], row['Upper'], [row[element]] * 2
                line2, = ax.plot([row['Lower'], row['Upper']], [row[element]] * 2, color='orange', linestyle='-.', label='pXRF Lab data' if j == 0 else "")
        
            for _, row in icpoes_data_by_datapoint.iterrows():
                a, b, c = row['Lower'], row['Upper'], [row[element]] * 2
                line3, = ax.plot([row['Lower'], row['Upper']], [row[element]] * 2, color='green', linestyle='--', label='ICP-OES data' if j == 0 else "")
        
            # Achsenbeschriftungen und Titel hinzufügen
            ax.set_title(f'#{current_datapoint}', loc='left', fontweight='bold', fontsize=14)
            ax.set_ylabel('Conc. [mg/kg]')
            ax.set_xlabel('Depth [m]')
            ax.set_ylim(-10, max_value_by_elements[element]*1.01)  # Y-Achsenbereich festlegen

        # Gesamttitel hinzufügen
        plt.suptitle(f'{element} Concentration Comparison, ICP-OES vs pXRF (on-Site and Lab)', x=0.07, y=0.95, ha='left', fontweight='bold', fontsize=14)

        # Layout anpassen
        plt.tight_layout(rect=(0, 0.03, 1, 0.95))  # Platz für den Titel lassen
        
        # Letztes Plot-Feld für die Legende freihalten
        ax = axes[2, 2]
        ax.axis('off')
        handles, labels = [line1, line2, line3], ['On-Site data', 'Lab data', 'ICP-OES data']
        ax.legend(handles=handles, labels=labels, loc='center', frameon=False, fontsize=16)
        
        # Willst du dir den Plot anzeigen lassen dann nutze plt.show()
        #plt.show()
        
        #Als SVG speichern. Es gibt noch andere save Formate wie PNG, PDF, etc.
        plt.savefig(f'./output/element_{element}.svg', format='svg')
    
# Hauptfunktion aufrufen, nachdem alle Funktionen definiert und geladen wurden
if __name__ == '__main__':
    main()