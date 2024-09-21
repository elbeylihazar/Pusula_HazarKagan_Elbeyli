import pandas as pd 


file_path = ('/Users/hazarelbeyli/Desktop/Pusula Talent Academy - Study Case/data/side_effect_data 1.xlsx')

# Load the data
def load_data(file_path):
    """Excel dosyasını yükleyip bir DataFrame olarak döndür."""
    return pd.read_excel(file_path)

print(load_data(file_path).head())
