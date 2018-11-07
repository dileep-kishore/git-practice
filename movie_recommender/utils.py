"""
    This module contains general utilities for this package
"""

from typing import List

from fuzzywuzzy import process


def search(targets: List[str], query: str, nhits: int = 3) -> List[str]:
    """Perform a fuzzy search on the targets using the query

    Parameters
    ----------
    targets : List[str]
        The targets on which the search is to be performed
    query : str
        The search query

    Returns
    -------
    List[str]
        The list of `nhits` best matches
    """
    if nhits > len(targets):
        raise ValueError("You cannot request more hits than the number of targets")
    results = process.extract(query, targets, limit=nhits)
    return [r[0] for r in results]
