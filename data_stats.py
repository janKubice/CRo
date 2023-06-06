import os
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Nastavení cesty k adresáři se zdrojovými soubory
source_directory = "./source/"

def load_files_from_directory(directory):
    """Funkce pro načtení souborů ze zadaného adresáře
    """
    files = os.listdir(directory)
    data = []
    for file in files:
        with open(os.path.join(directory, file), 'r') as f:
            file_data = json.load(f)
            data.append(file_data)
    return data

if __name__ == "__main__":
    # Načtení dat ze zdrojového adresáře
    data = load_files_from_directory(source_directory)
    df = pd.DataFrame(data)

    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['year week'] = df['date'].dt.strftime('%Y-W%U')

    yearly_counts = df['year week'].value_counts().sort_index()
    yearly_counts.plot(kind='bar', figsize=(18, 6))
    plt.title('Porovnání počtu příspěvků v jednotlivých týdnech roků')
    plt.xlabel('Rok')
    plt.ylabel('Počet příspěvků')
    plt.show()

    yearly_counts = df['year'].value_counts().sort_index()
    yearly_counts.plot(kind='bar', figsize=(10, 6))
    plt.title('Porovnání počtu příspěvků v jednotlivých letech')
    plt.xlabel('Rok')
    plt.ylabel('Počet příspěvků')
    plt.show()
    
    yearly_avg_length = df.groupby('year')['text'].apply(lambda x: np.mean(x.str.len()))
    yearly_avg_length.plot(kind='bar', figsize=(10, 6))
    plt.title('Porovnání průměrné délky textu příspěvků v jednotlivých letech')
    plt.xlabel('Rok')
    plt.ylabel('Průměrná délka textu')
    plt.show()

    yearly_avg_length = df.groupby('year week')['text'].apply(lambda x: np.mean(x.str.len()))
    yearly_avg_length.plot(kind='bar', figsize=(18, 6))
    plt.title('Porovnání průměrné délky textu příspěvků v jednotlivých týdnech roků')
    plt.xlabel('Rok')
    plt.ylabel('Průměrná délka textu')
    plt.show()