from libs import *

def rank(animes):
    '''
    Ranks anime on the plan to watch
    list of a user to aid in choosing
    a user's next anime they should
    watch.
    '''

    '''
    Things to include when ranking:
    -Rating of related anime if on list
    -Number of related anime on list
    -Status of related anime(completed, dropped, etc.)
    -Average rating of genres
    -For a specific anime, if a recommendation is in the user's list, weight by
     number of users recommending
    '''

    #Setup and calculate genre avgs
    genres, avgs, nums = setup_genres()
    genre_avgs = genre_avg(animes, genres, avgs, nums)

    #Now sort by final rankings and output
    rankings = sorted(animes, key = lambda x: x.ranking, reverse = True)

    for anime in rankings:
        print("{} {}".format(anime.ranking, anime.name))

    return rankings

def update_rankings(animes, metric):
    '''
    Takes in the current rankings and
    a metric by which to weight them
    and updates the rankings based
    on that metric.
    '''

    return rankings

def setup_genres():
    '''
    Sets up the necessary lists for
    calculating genre averages.
    '''
    
    genres = ["Action", "Adventure", "Cars", "Comedy", "Dementia", "Demons",
          "Drama", "Ecchi", "Fantasy", "Game", "Harem", "Hentai", "Historical",
          "Horror", "Josei", "Kids", "Magic", "Martial Arts", "Mecha", "Military",
          "Music", "Mystery", "Parody", "Police", "Psychological", "Romance",
          "Samurai", "School", "Sci-Fi", "Seinen", "Shoujo", "Shoujo Ai", "Shounen",
          "Shounen Ai", "Slice of Life", "Space", "Sports", "Super Power",
          "Supernatural", "Thriller", "Vampire", "Yaoi", "Yuri"]
    avgs = [5.0]*len(genres) #Initialize at 5 to start at neutral value
    nums = [1]*len(genres)   #Pretend there's already an anime rated at 5

    return genres, avgs, nums    

def genre_avg(animes, genres, avgs, nums):
    '''
    Calculates the average score of each
    genre to weight by the genres of each
    anime.
    '''

    #Check if each anime has rating and update avg for all genres
    for anime in animes:
        if anime.user_rating != "-":
            for genre in anime.genres:
                index = genres.index(genre)

                avgs[index] = (nums[index] * avgs[index] + int(anime.user_rating)) / (nums[index] + 1)
                nums[index] += 1

    #Create dictionary of averages
    genre_avgs = dict(zip(genres, avgs))
    
    return genre_avgs
        

def num_related_anime(animes):
    '''
    Calculates the number of related anime
    on the user's list.
    '''
