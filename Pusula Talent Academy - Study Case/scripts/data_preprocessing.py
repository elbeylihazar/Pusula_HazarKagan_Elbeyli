import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, StandardScaler

def clean_data(df):
    """Eksik verileri doldur ve kategorik verileri sayısallaştır."""
    # Sayısal sütunlar için imputer
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    imputer_num = SimpleImputer(strategy='mean')
    df[numerical_cols] = imputer_num.fit_transform(df[numerical_cols])

    # Kategorik sütunlar için imputer
    categorical_cols = df.select_dtypes(include=['object']).columns
    imputer_cat = SimpleImputer(strategy='most_frequent')
    df[categorical_cols] = imputer_cat.fit_transform(df[categorical_cols])

    return df


def encode_categorical(df, column_name):
    """Kategorik verileri sayısal verilere çevir."""
    label_encoder = LabelEncoder()
    df[column_name] = label_encoder.fit_transform(df[column_name])
    return df


def scale_data(df):
    """Veriyi standartlaştır."""
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    scaler = StandardScaler()
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])
    return df

def preprocess_data(df):
    df = clean_data(df)
    df = encode_categorical(df)
    df = scale_data(df)
    return df

def preprocess_dates(df):
    # Tarih sütunlarını datetime formatına çevir
    df['Dogum_Tarihi'] = pd.to_datetime(df['Dogum_Tarihi'], errors='coerce')
    df['Ilac_Baslangic_Tarihi'] = pd.to_datetime(df['Ilac_Baslangic_Tarihi'], errors='coerce')

    # Hatalı değerleri kontrol et
    print(df[df['Dogum_Tarihi'].isna()])
    print(df[df['Ilac_Baslangic_Tarihi'].isna()])
   
    # Yaş hesaplama (Ilac_Baslangic_Tarihi ve Dogum_Tarihi sütunları varsa)
    if 'Ilac_Baslangic_Tarihi' in df.columns and 'Dogum_Tarihi' in df.columns:
        df['Yas'] = (df['Ilac_Baslangic_Tarihi'] - df['Dogum_Tarihi']).dt.days / 365.25

    return df
