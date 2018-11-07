"""
    Movie recommender recommends movies from a database of around 10,000 movies!
    There are three main kinds of recommendations that are offered:
    1. Based on similarity in the movie plot
    2. Based on similarity in the actors, directors and keywords
    3. Based on other user recommendations (not implemented yet)
"""

from typing import List

import pandas as pd

from .plot_similarity import PlotSimilarity
from .keyword_similarity import KeywordSimilarity
from .user_similarity import UserSimilarity


def movie_recommender(
        metadata_file: str,
        credits_file: str,
        keywords_file: str,
        ratings_file: str,
        links_file: str,
        movie: str,
        method: str = "PlotSimilarity",
        nhits: int = 10,
) -> List[str]:
    """
        Get movie recommendation using the chosen method

        Parameters
        ----------
        metadata_file : str
            The path to the file containing the movie metadata
        credits_file : str
            The path to the file containing the movie credits data
        keywords_file : str
            The path to the file containing the keywords data
        ratings_file : str
            The path to the file containing user ratings
        links_file : str
            The path to the file containing the movie id links
        movie : str
            The movie for which recommendations are to be made
        method : {'PlotSimilarity', 'KeywordSimilarity', 'UserSimilarity'}, optional
            The method to be used to make recommendations
            Default value is 'PlotSimilarity'
        nhits : int, optional
            The number of recommendations to be returned
            Default value is 10

        Returns
        -------
        List[str]
            The list of movie recommendations
    """
    print("Loading data")
    metadata = pd.read_csv(metadata_file)
    credits = pd.read_csv(credits_file)
    keywords = pd.read_csv(keywords_file)
    ratings = pd.read_csv(ratings_file)
    links = pd.read_csv(links_file)
    print(f"Using {method} for the recommendation engine...")
    if method == "PlotSimilarity":
        recommender = PlotSimilarity(metadata)
    elif method == "KeywordSimilarity":
        recommender = KeywordSimilarity(metadata, credits, keywords)
    elif method == "UserSimilarity":
        recommender = UserSimilarity(metadata, ratings, links)
    print("Returning recommendations")
    return recommender(movie, nhits=nhits)
