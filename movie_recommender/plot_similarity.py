"""
    This module recommends movies based on how similar the plots are
"""

import random
from typing import List

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


class PlotSimilarity:
    """A class that returns movie recommendation based on plot similarity

    Parameters
    ----------
    metadata : pd.DataFrame
        The pandas dataframe containing the metadata

    Attributes
    ----------
    similarity : np.ndarray
        The cosine similarity between movies
    movies : List[str]
        The list of all movies in the database
    """

    def __init__(self, metadata: pd.DataFrame) -> None:
        self._metadata = metadata
        self.similarity = self.calculate_similarity(metadata)
        self._title_hash = dict(zip(metadata['title'], metadata.index))

    @staticmethod
    def calculate_similarity(metadata: pd.DataFrame) -> np.ndarray:
        """Get the pairwise plot similarity matrix between all movies

        Parameters
        ----------
        metadata : pd.DataFrame
            The pandas dataframe containing the metadata

        Returns
        -------
        np.ndarray
            The similarity between movie plots calculated using a linear kernel
        """
        overview = metadata['overview'].fillna('')
        tagline = metadata['tagline'].fillna('')
        description = overview + ' ' + tagline
        tf = TfidfVectorizer(analyzer="word", ngram_range=(1, 2), min_df=0, stop_words='english')
        tfid_matrix = tf.fit_transform(description)
        return linear_kernel(tfid_matrix, tfid_matrix)

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
        sorted_sim_scores = sim_scores.sort_values(ascending=False).iloc[:nhits]
        recommended_titles = self._metadata['title'].iloc[sorted_sim_scores.index]
        return list(recommended_titles)

    @property
    def movies(self) -> List[str]:
        """ Returns the list of all movies in the database """
        return list(self._metadata['title'])
