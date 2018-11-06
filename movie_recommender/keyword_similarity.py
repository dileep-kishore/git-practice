"""
    This module recommends movies based on:
    1. genres
    2. director
    3. main actors
    4. keywords
"""

from ast import literal_eval
from functools import partial
import random
from typing import List

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import linear_kernel


class KeywordSimilarity:
    """A class that returns movie recommendations based on keyword similarity

    Parameters
    ----------
    metadata : pd.DataFrame
        The pandas dataframe containing the metadata
    credits : pd.DataFrame
        The pandas dataframe containing the credits data (cast, crew)
    keywords : pd.DataFrame
        The pandas dataframe containing the keywords data

    Attributes
    ----------
    similarity : np.ndarray
        The cosine similarity between movies
    movies : List[str]
        The list of all movies in the database
    """

    def __init__(self, metadata: pd.DataFrame, credits: pd.DataFrame, keywords: pd.DataFrame) -> None:
        self._metadata = self._update_metadata(metadata, credits, keywords)
        if self._metadata.shape[0] != metadata.shape[0]:
            raise ValueError("Some data was lost")
        self.similarity = self.calculate_similarity(self._metadata)
        self._title_hash = dict(zip(self._metadata['title'], self._metadata.index))

    def _update_metadata(
            self,
            metadata: pd.DataFrame,
            credits: pd.DataFrame,
            keywords: pd.DataFrame
    ) -> pd.DataFrame:
        """ Merge and update metadata """

        def get_director(crew):
            for member in crew:
                if member['job'] == 'Director':
                    return [member['name'].replace(" ", "")] * 3
            return ['']

        def get_names(x, num):
            if not isinstance(x, list):
                return []
            names = []
            for member in x[:num]:
                names.append(member['name'].replace(" ", "").lower())
            return names

        md = metadata.merge(credits, on="id").merge(keywords, on="id")
        md['cast'] = md['cast'].apply(literal_eval)
        md['crew'] = md['crew'].apply(literal_eval)
        md['keywords'] = md['keywords'].apply(literal_eval)
        md['cast_size'] = md['cast'].apply(len)
        md['crew_size'] = md['crew'].apply(len)
        md['director'] = md['crew'].apply(get_director)
        get_cast = partial(get_names, num=3)
        get_kwrds = partial(get_names, num=100)
        md['cast'] = md['cast'].apply(get_cast)
        md['keywords'] = md['keywords'].apply(get_kwrds)
        md['genres'] = md['genres'].apply(get_kwrds)
        return md

    @staticmethod
    def calculate_similarity(merged_metadata: pd.DataFrame) -> np.ndarray:
        """Get the pairwise keyword similarity matrix between all movies

        Parameters
        ----------
        merged_metadata : pd.DataFrame
            The pandas dataframe containing the metadata, credits and keywords data

        Returns
        -------
        np.ndarray
            The similarity between movie keywords calculated using a linear kernel
        """
        soup = (
            merged_metadata['keywords'] +
            merged_metadata['cast'] +
            merged_metadata['director'] +
            merged_metadata['genres']
        ).apply(' '.join)
        count = CountVectorizer(analyzer='word', ngram_range=(1, 2), min_df=0, stop_words='english')
        count_matrix = count.fit_transform(soup)
        return linear_kernel(count_matrix, count_matrix)

    def __call__(self, title: str, nhits: int = 10) -> List[str]:
        """Return the list of recommended movies based on plot similarity

        Parameters
        ----------
        title : str
            The title of the movie for which recommendations are to be made
        nhits : int, optional
            The number of recommendations to be returned
            Default value is 10

        Returns
        -------
        List[str]
            The list of movie recommendations
        """
        try:
            ind = self._title_hash[title]
        except KeyError:
            movies = random.choices(self.movies, k=nhits)
            raise KeyError(f"{title} is not in the database. Try: {movies}")
        sim_scores = pd.Series(self.similarity[ind])
        sorted_sim_scores = sim_scores.sort_values(ascending=False).iloc[:nhits + 1]
        recommended_titles = self._metadata['title'].iloc[sorted_sim_scores.index]
        return list(recommended_titles[1:])

    @property
    def movies(self) -> List[str]:
        """ Returns the list of all movies in the database """
        return list(self._metadata['title'])
