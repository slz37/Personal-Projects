from pckg.src.login import *

def test():
    #Get anime in each tab
    animes = []

    tab = "Completed"

    #Load list
    urls, anime_list = goto_anime_list(tab)

    #Get anime info
    name = anime_list[0].text
    url = urls[0].get_attribute("href")
    ID = re.search(ID_PATTERN, url).group()

    #Instantiate class
    animes.append(anime(browser, name, url, ID, tab))

    tab = "Plan to Watch"
        
    #Load list
    urls, anime_list = goto_anime_list(tab)

    #Get anime info
    name = anime_list[0].text
    url = urls[0].get_attribute("href")
    ID = re.search(ID_PATTERN, url).group()

    #Instantiate class
    animes.append(anime(browser, name, url, ID, tab))

    #Get anime info
    name = anime_list[1].text
    url = urls[1].get_attribute("href")
    ID = re.search(ID_PATTERN, url).group()

    #Instantiate class
    animes.append(anime(browser, name, url, ID, tab))

    #Replace related anime with objects
    for anime in animes:
        anime.replace_related_anime(animes)

    #Get rankings
    rank(animes)

    '''
    #Get anime in each tab
    animes = []
    for tab in TABS:
        #Skip all anime tab
        if tab == "All Anime":
            continue
            
        #Loop over all anime
        for i in range(len(anime_list)):
            #Get anime info
            name = anime_list[i].text
            url = urls[i].get_attribute("href")
            ID = re.search(ID_PATTERN, url).group()

            #Instantiate class
            animes.append(anime(name, url, ID))
    '''