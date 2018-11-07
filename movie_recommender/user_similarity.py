"""
    This module recommends movies based on ratings of other users
"""

import pandas as pd


class UserSimilarity:
    """A class that returns movie  recommendations based on user similarity

    Parameters
    ----------
    metadata : pd.DataFrame
        The pandas dataframe containing the metadata
    ratings : pd.DataFrame
        The pandas dataframe containing the ratings
    links : pd.DataFrame
        The pandas dataframe containing the links
    """

    def __init__(self, metadata: pd.DataFrame, ratings: pd.DataFrame, links: pd.DataFrame) -> None:
        raise NotImplementedError("This class has not been implemented yet")
