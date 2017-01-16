# import webbroser to allow us to open new browser pages
import webbrowser

class Movie():
    """This class provides a way to store movie related information
    movie_title (str): title of the movie
    movie_storyline (str): description of the movie
    poster_image (str): url to an image of the movie poster
    trailer_youtube (str): url to the trailer of the movie
    rating (str): movie rating
    """
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube, rating):

        # ensure that the rating is a valid movie rating
        if rating not in Movie.VALID_RATINGS:
            raise ValueError('The movie rating can only be G, PG, PG-13, or R')

        # initiailize all instance variables
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = rating
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
