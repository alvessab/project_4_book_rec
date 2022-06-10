import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors

class ModelHelper():
    def __init__(self):
        pass

       
    def knn_recommender(self, bookTitle):
    
        df = pd.read_csv('static/data/knn_books_sentiment.csv')
        df_rec = df.drop(["bookImage", "bookDesc","bookTitle", "Genre", "Author"], axis=1)
        
        if bookTitle != '':
            model_knn = NearestNeighbors(metric='cosine', n_neighbors=11)
            model_knn.fit(df_rec)
            
            book = df.loc[df["bookTitle"] == bookTitle]
            book = book.drop(["bookImage", "bookDesc","bookTitle", "Genre", "Author"], axis=1)
            book = book.to_numpy()
            
            distances, indices = model_knn.kneighbors(book, n_neighbors = 11)
            
            result = df.iloc[indices.flatten()]
            result["Distance"] = distances.flatten()

            result = result[["bookImage", "bookTitle", 'Author',"bookDesc", "Genre", "bookRating"]].to_json(orient='records')
            
            return result



        



