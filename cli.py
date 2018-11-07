#!/usr/bin/env python

import click

from movie_recommender import movie_recommender


@click.command()
@click.option('--metadata', '-md', default="data/metadata.csv", type=click.Path(exists=True), help="Metadata file")
@click.option('--credits', '-cr', default="data/credits.csv", type=click.Path(exists=True), help="Credits file")
@click.option('--keywords', '-kw', default="data/keywords.csv", type=click.Path(exists=True), help="Keywords file")
@click.option('--ratings', '-ra', default="data/ratings.csv", type=click.Path(exists=True), help="Ratings file")
@click.option('--links', '-ln', default="data/links.csv", type=click.Path(exists=True), help="Links file")
@click.option('--nhits', '-n', default=10, type=click.INT, help="Number of recommendations to be returned")
@click.option('--method', '-m', default="PlotSimilarity", help="The recommendation method to be used")
@click.argument('movie')
def recommender(metadata, credits, keywords, ratings, links, nhits, method, movie):
    """ Get great movie recommendations! """
    recommendations = movie_recommender(
        metadata,
        credits,
        keywords,
        ratings,
        links,
        movie,
        method,
        nhits
    )
    click.secho('\n' + '=' * 36 + "[RECOMMENDATIONS]" + '=' * 36, fg="green", bold=True)
    for recommendation in recommendations:
        click.secho(recommendation, fg="green", bold=True)


if __name__ == "__main__":
    recommender()
