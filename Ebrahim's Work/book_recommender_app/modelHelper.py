import pandas as pd
import time
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import linear_kernel
from sklearn.neighbors import NearestNeighbors

class ModelHelper():
    def __init__(self):
        pass

       
    def recommender(df, book_title, n_neighbors=11):
    
    df = pd.read_csv("static/data/knn_books_sentiment.csv")
    df_sub = df.drop(["bookTitle", "Genre", "Author"], axis=1)
    model_knn = NearestNeighbors(metric='cosine', n_neighbors=n_neighbors)
    model_knn.fit(df_sub)
    
    book = df.loc[df["bookTitle"] == book_title]
    book = book.drop(["bookTitle", "Genre", "Author"], axis=1)
    book = book.to_numpy()
    
    distances, indices = model_knn.kneighbors(book, n_neighbors = n_neighbors)
    
    result = df.iloc[indices.flatten()]
    result["Distance"] = distances.flatten()
    
    return result
        



