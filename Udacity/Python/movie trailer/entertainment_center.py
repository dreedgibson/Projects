# import media and fresh tomatoes to create the movie website
# media contains the Movie class, and fresh_tomatoes
# contains the open movies page method

import media
import fresh_tomatoes

# generate all of the movies for website
# Toy Story
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://vignette1.wikia.nocookie.net/toystory72/images/3/33/Toy_Story_3_Poster.jpg/revision/latest?cb=20100717205203",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        "G")

# Avatar
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://s3.foxmovies.com/foxmovies/production/films/18/images/posters/251-asset-page.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ",
                     "PG-13")

# The Shawshank Redemption
shawshank = media.Movie("Shawshank Redemption",
                        "An innocent man is sent to prison for a double murder "
                        "he did not commit",
                        "http://t0.gstatic.com/images?q=tbn:ANd9GcSkmMH-bEDUS2TmK8amBqgIMgrfzN1_mImChPuMrunA1XjNTSKm",
                        "https://www.youtube.com/watch?v=6hB3S9bIaco",
                        "R")

# The Recruit
the_recruit = media.Movie("The Recruit",
                          "Spy thriller",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/6/62/Recruitmovie.jpg/220px-Recruitmovie.jpg",
                          "https://www.youtube.com/watch?v=-aqecRSJo3o",
                          "R")

# Anchorman
anchorman = media.Movie("Anchorman",
                        "Hotshot television anchorman Ron Burgundy "
                        "(Will Ferrell) welcomes upstart reporter Veronica "
                        "Corningstone (Christina Applegate) into the male-"
                        "dominated world of 1970s broadcast news -- that is, "
                        "until the talented female journalist begins to outshine"
                        " Burgundy on air",
                        "http://www.gstatic.com/tv/thumb/dvdboxart/34589/p34589_d_v8_ai.jpg",
                        "https://www.youtube.com/watch?v=Ip6GolC7Mk0",
                        "R")

# Neighbors
neighbors = media.Movie ("Neighbors",
                         "New parents Mac (Seth Rogen) and Kelly (Rose Byrne) "
                         "move to the suburbs when they welcome an infant "
                         "daughter into their lives. All goes well with the "
                         "couple, until the Delta Psi Beta fraternity moves in "
                         "next door. ",
                         "http://t3.gstatic.com/images?q=tbn:ANd9GcQrjU294w8HS8ClO9GcLirMdkGTang4W2RRzU46VQhZ-oZv4UFk",
                         "https://www.youtube.com/watch?v=pzZgJZMXNEc",
                         "R")

# store the movies in a list for the fresh_tomatoes method
movies = [toy_story, avatar, shawshank, the_recruit, anchorman, neighbors]

# create the website
fresh_tomatoes.open_movies_page(movies)
