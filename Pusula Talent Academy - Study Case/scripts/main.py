import os
import pandas as pd

from data_loader import load_data
from data_exploration import explore_data, visualize_data, plot_age_vs_weight
from data_preprocessing import clean_data, encode_categorical, scale_data, preprocess_dates

# Veriyi yükleme
try:
    df = load_data('data/side_effect_data 1.xlsx')
except Exception as e:
    print(f"Veri yükleme hatası: {e}")
    exit()

# Veri keşfi
explore_data(df)
visualize_data(df)  

# Veri keşfi (Yaş ve kilo arasındaki ilişkiyi görselleştir)
plot_age_vs_weight(df)

# Tarih sütunlarını işleme
df = preprocess_dates(df)

# Veri temizleme ve ön işleme
df_cleaned = clean_data(df)

# Kategorik sütunları otomatik olarak tespit etme
categorical_columns = df_cleaned.select_dtypes(include=['object']).columns
print(f"Kategorik sütunlar: {categorical_columns}")

# Kategorik sütunları kodlama
for column in categorical_columns:
    df_cleaned = encode_categorical(df_cleaned, column)

# Veriyi ölçekleme
df_scaled = scale_data(df_cleaned)

# İşlenmiş veriyi göster
print("İşlenmiş veri:", df_scaled.head())
