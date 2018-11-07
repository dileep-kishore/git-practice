# git-practice

A repository with code to help you practice your git. Created for the workshop series organized by the Boston University Bioinformatics Programming Task Force (BUBPWTF).

This repository contains a movie recommender engine written in `Python`.


## Usage

* Install [anaconda](https://conda.io/docs/user-guide/install/index.html)
* Clone the repository
* Set up the conda environment - `conda env create -f env.yml`
* Activate the conda environment - `source activate recommender`

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

The actual tasks for the workshop can be found [here](https://foundations-in-computational-skills.readthedocs.io/en/latest/content/workshops/07_version_control_with_git/07_version_control_with_git_workshop.html).

## Contributors

- Dileep Kishore


## Credits

The code for this repository has been adapted from https://www.kaggle.com/rounakbanik/movie-recommender-systems
