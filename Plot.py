import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pymongo import MongoClient

class DataVisualization:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["DataAirbnb"]
        self.collection = self.db["Data"]

    def load_data(self):
        data_to_find = {"neighbourhood group": 1, "price": 1}
        data = list(self.collection.find({}, data_to_find))
        
        return pd.DataFrame(data)
    
    def data_cleaning (self, df):
        #convertir a str
        df['price'] = df['price'].astype(str)

        #eliminar signo pesos y espacios
        df['price'] = df['price'].str.replace('$', '', regex=False)
        df['price'] = df['price'].str.replace(',', '', regex=False)
        
        #se pasa a numérico
        df['price'] = pd.to_numeric(df['price'], errors='coerce')

        #se eliminan los que no cumplieron
        df = df.dropna(subset=['price'])

        return df

    def plot_price_distribution(self, df):
        plt.figure(figsize=(10, 6))
        sns.barplot(x='neighbourhood group', y="price",data=df, hue="neighbourhood group", palette="viridis")
        plt.title('Price Distribution')
        plt.xlabel('Country')
        plt.ylabel('Price')
        plt.show()

if __name__ == "__main__":
    data_viz = DataVisualization()
    df = data_viz.load_data()
    df = data_viz.data_cleaning(df)
    data_viz.plot_price_distribution(df)