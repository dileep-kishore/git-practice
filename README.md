# git-practice

A repository with code to help you practice your git. Created for the workshop series organized by the Boston University Bioinformatics Programming Task Force (BUBPWTF).

This repository contains a movie recommender engine written in `Python`.


## Usage

### Installation

* Install [anaconda](https://conda.io/docs/user-guide/install/index.html)
* Clone the repository
* Set up the conda environment - `conda env create -f env.yml`
* Activate the conda environment - `source activate recommender`

### Command line
```sh
$ python cli.py --help
Usage: cli.py [OPTIONS] MOVIE

  Get great movie recommendations!

Options:
  -md, --metadata PATH  Metadata file
  -cr, --credits PATH   Credits file
  -kw, --keywords PATH  Keywords file
  -ra, --ratings PATH   Ratings file
  -ln, --links PATH     Links file
  -n, --nhits INTEGER   Number of recommendations to be returned
  -m, --method TEXT     The recommendation method to be used
  --help                Show this message and exit.
```

- The default metadata, credits, keywords, ratings and links files can be found in the `data` directory
- The supported methods are `PlotSimilarity` (default), `KeywordSimilarity` and `UserSimilarity`


### Python

There are three core classes that make up the package - `PlotSimilarity`, `KeywordSimilarity` and `UserSimilarity`

```python
# Importing
from movie_recommender import PlotSimilarity, KeywordSimilarity, UserSimilarity
```

`PlotSimilarity` usage
```
>>> ?PlotSimilarity
Init signature: PlotSimilarity(metadata:pandas.core.frame.DataFrame) -> None
Docstring:
A class that returns movie recommendation based on plot similarity

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
File:           ~/Documents/boston_university/collaborations/git-practice/movie_recommender/plot_similarity.py
Type:           type
```

`KeywordSimilarity` usage
```
>>> ?KeywordSimilarity
Init signature: KeywordSimilarity(metadata:pandas.core.frame.DataFrame, credits:pandas.core.frame.DataFrame, keywords:pandas.core.frame.DataFrame) -> None
Docstring:
A class that returns movie recommendations based on keyword similarity

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
File:           ~/Documents/boston_university/collaborations/git-practice/movie_recommender/keyword_similarity.py
Type:           type
```


The actual tasks for the workshop can be found [here](https://foundations-in-computational-skills.readthedocs.io/en/latest/content/workshops/07_version_control_with_git/07_version_control_with_git_workshop.html).

## Contributors

- Dileep Kishore


## Credits

The code for this repository has been adapted from https://www.kaggle.com/rounakbanik/movie-recommender-systems
