import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors

class ModelHelper():
    def __init__(self):
        pass

       
    def recommender(df, bookTitle='', n_neighbors=11):
    
        df = pd.read_csv('static/data/knn_books_sentiment.csv')
        df_rec = df.drop(["bookTitle", "Genre", "Author"], axis=1)
        
        if bookTitle != '':
            model_knn = NearestNeighbors(metric='cosine', n_neighbors=n_neighbors)
            model_knn.fit(df_rec)
            
            book = df.loc[df["bookTitle"] == bookTitle]
            book = book.drop(["bookTitle", "Genre", "Author"], axis=1)
            book = book.to_numpy()
            
            distances, indices = model_knn.kneighbors(book, n_neighbors = n_neighbors)
            
            result = df.iloc[indices.flatten()]
            result["Distance"] = distances.flatten()
        
            plt.plot(result["bookTitle"], result["Distance"])
            plt.title("Distance Between Neighbors", fontsize=16, fontweight="bold")
            plt.xlabel("Book Title", fontsize=14)
            plt.xticks(rotation = 90)
            plt.ylabel("Distance", fontsize=14)

            result = result[["bookTitle", "bookRating", "Genre", 'Author']].to_json(orient='records')
            
            return result



        



