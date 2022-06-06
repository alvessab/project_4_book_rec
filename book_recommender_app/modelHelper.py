import pandas as pd
import time
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import linear_kernel

class ModelHelper():
    def __init__(self):
        pass

    def recommendation_df(rating_min, bookTitle):
       
        df = pd.read_csv("../static/data/goodreads_final_bagowords.csv")

        df_fil = df.loc[df['bookRating'] >= rating_min]

        tfidf = TfidfVectorizer(stop_words='english',smooth_idf=True)

        # numbers to calculate similarities
        tfidf_matrix = tfidf.fit_transform(df_fil['bag_of_words']).todense()

        #calculate cosine matrix
        cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)


        indices = pd.Series(df_fil['bookTitle'])

    
        recommended_book = []
        recommended_book_url = []
        recommended_book_image= []
        recommended_book_author = []
        recommended_book_rating =[]
        recommended_book_descrip =[]
        recommended_book_genre =[]
        
        idx = indices[indices == bookTitle].index[0]
        
        score_series = pd.Series(cosine_similarities[idx]).sort_values(ascending = False)
        
        top_10_indices = list(score_series.iloc[1:11].index)
        
        for i in top_10_indices:
            recommended_book.append(list(df_fil['bookTitle'])[i])
            recommended_book_url.append(list(df_fil['url'])[i])
            recommended_book_image.append(list(df_fil['bookImage'])[i])
            recommended_book_author.append(list(df_fil['Author'])[i])
            recommended_book_rating.append(list(df_fil['bookRating'])[i])
            recommended_book_descrip.append(list(df_fil['bookDesc'])[i])
            recommended_book_genre.append(list(df_fil['Genre'])[i])
        
        data = {'Titles': recommended_book,
            'Author': recommended_book_author,
                'Genre': recommended_book_genre,
                'Description' : recommended_book_descrip,
                'Rating':recommended_book_rating,
                'URL': recommended_book_url,
                'image': recommended_book_image
            }
        rec_df = pd.DataFrame(data)
        
        return data



