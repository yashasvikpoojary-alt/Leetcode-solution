import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    #check author id and viewer id same
    view_own_article = views[
        views['author_id']==views['viewer_id']
    ]
    #Remove the duplicates
    unique_author = view_own_article[['author_id']].drop_duplicates()
    #Rename author id -> id
    unique_author.columns = ['id']
    #After sorting return the id
    return unique_author.sort_values('id')