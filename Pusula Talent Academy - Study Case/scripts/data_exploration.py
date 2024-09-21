import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def explore_data(df):
    """Veriyi keşfetmek ve temel bilgileri göstermek için fonksiyonlar."""
    print(df.info())
    print(df.describe())
    print("Eksik veriler:")
    print(df.isnull().sum())
    print("Eksik verilerin yüzdesi:")
    print(df.isnull().mean() * 100)

    # Eksik verileri görselleştirme (Isı haritası)
    plt.figure(figsize=(12, 8))
    sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
    plt.title('Eksik Veri Isı Haritası')
    plt.show()

    # Tarih sütunlarını dönüştürme
    date_columns = ['Dogum_Tarihi', 'Ilac_Baslangic_Tarihi', 'Ilac_Bitis_Tarihi', 'Yan_Etki_Bildirim_Tarihi']
    for column in date_columns:
        if column in df.columns:
            df[column] = pd.to_datetime(df[column], errors='coerce')  # Hatalı tarihleri NaT yapar
            print(f"{column} sütunu dönüştürüldü. Hatalı değerler NaT olarak ayarlandı.")
            print(f"Hatalı değerler:\n{df[df[column].isna()]}")  # Hatalı değerleri göster

    # Sayısal değişkenlerin kontrolü
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    print("Sayısal sütunlar:", numeric_columns)

def visualize_data(df):
    """Veriyi görselleştirmek için fonksiyonlar."""
    # Histogram
    df.hist(figsize=(12, 10), bins=20)
    plt.tight_layout()
    plt.xticks(rotation=45)  # X eksenindeki etiketleri 45 derece döndür
    plt.show()

    # Sayısal sütunları seç ve heatmap ile görselleştir
    numeric_df = df.select_dtypes(include=['float64', 'int64'])  # Sadece sayısal sütunları seç
    if not numeric_df.empty:  # Sayısal sütunlar varsa
        plt.figure(figsize=(10, 8))
        sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', vmin=-1, vmax=1)
        plt.title('Sayısal Sütunlar Korelasyon Haritası')
        plt.show()
    else:
        print("Veri çerçevesinde sayısal sütun yok, heatmap gösterilemiyor.")

    # Kategorik değişkenlerin dağılımı (Cinsiyet)
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='Cinsiyet')  # Örnek olarak cinsiyet dağılımı
    plt.title('Cinsiyet Dağılımı')
    plt.show()

    # Kategorik değişkenlerin dağılımı (Uyruk)
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='Uyruk')  # Örnek olarak Uyruk dağılımı
    plt.title('Uyruk Dağılımı')
    plt.show()

def visualize_categorical_data(df):
    """Kategorik değişkenlerin dağılımını görselleştirme."""
    categorical_columns = df.select_dtypes(include=['object']).columns
    for column in categorical_columns:
        plt.figure(figsize=(10, 6))
        sns.countplot(data=df, x=column)
        plt.title(f'{column} Dağılımı')
        plt.show()

def plot_age_vs_weight(df):
    if 'Yas' in df.columns and 'Kilo' in df.columns:
        df_filtered = df.dropna(subset=['Yas', 'Kilo'])
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=df_filtered, x='Yas', y='Kilo')
        plt.title('Yaş ve Kilo Arasındaki İlişki')
        plt.xlabel('Yaş')
        plt.ylabel('Kilo')
        plt.show()
    else:
        print("Scatter plot için uygun sütunlar bulunamadı.")
