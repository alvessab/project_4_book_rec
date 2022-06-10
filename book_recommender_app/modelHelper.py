import pandas as pd
import time
import numpy as np
import s3fs 

#read in the data
df = pd.read_csv("static/data/goodreads_final_bagowords.csv")

s3 = s3fs.S3FileSystem(anon=True)
arr1= np.load(s3.open("book-rec-nlp/goodreads_cos_data.npy"))

class ModelHelper1():
    def __init__(self):
        pass

    def recommendation_df(self, bookTitle):
       
        #variable reliant code
        indices = pd.Series(df['bookTitle'])

        recommended_book = []
        recommended_book_url = []
        recommended_book_image= []
        recommended_book_author = []
        recommended_book_rating =[]
        recommended_book_descrip =[]
        recommended_book_genre =[]
        recommended_book_score =[]

        idx = indices[indices == bookTitle].index[0]

        score_series = pd.Series(arr1[idx]).sort_values(ascending = False)

        top_10_indices = list(score_series.iloc[1:11].index)

        for i in top_10_indices:
            recommended_book.append(list(df['bookTitle'])[i])
            recommended_book_url.append(list(df['url'])[i])
            recommended_book_image.append(list(df['bookImage'])[i])
            recommended_book_author.append(list(df['Author'])[i])
            recommended_book_rating.append(list(df['bookRating'])[i])
            recommended_book_descrip.append(list(df['bookDesc'])[i])
            recommended_book_genre.append(list(df['Genre'])[i])
            recommended_book_score.append(score_series[i])

        data = {'Title': recommended_book,
            'Author': recommended_book_author,
                'Genre': recommended_book_genre,
                'Description' : recommended_book_descrip,
                'Rating':recommended_book_rating,
                'URL': recommended_book_url,
                'Image': recommended_book_image,
                'Score': recommended_book_score
            }
        rec_df = pd.DataFrame(data)
        
        return rec_df



