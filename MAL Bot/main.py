from libs import *

#User info
MAL_PAYLOAD = {
    "user_name": input("MAL Username: "),
    "password": input("MAL Password: "),
    }

#Regex patterns
ID_PATTERN = re.compile("(?<=/)[\d]+(?=/)")

#MAL Anime List Tabs
TABS = {
        "Currently Watching": 1,
        "Completed": 2,
        "On Hold": 3,
        "Dropped": 4,
        "Plan to Watch": 6,
        "All Anime": 7
        } 

#Urls
LOGIN_URL = u"https://myanimelist.net/login.php"
LIST_URL = u"https://myanimelist.net/animelist/{}".format(MAL_PAYLOAD["user_name"])

#Driver Options - Hide Window
CHROMEDRIVER_PATH = "chromedriver"
WINDOW_SIZE = "1920, 1080"
chrome_options = Options()  
#chrome_options.add_argument("--headless")  
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)

#Initiate driver and load page
browser = webdriver.Chrome(
    executable_path = CHROMEDRIVER_PATH,
    chrome_options = chrome_options
    )
browser.get(LOGIN_URL)

def verify_login():
    '''
    Checks the html after attempting to
    login to confirm whether login
    was successful.
    '''
    
    #Check for logout form
    forms = browser.find_elements_by_xpath("//form[@action=\"https://myanimelist.net/logout.php\"]")
    if forms:
        print("Login successful")
        return
    else:
        print("Login failed")
        sys.exit()

def login():
    '''
    Sets up global variables and selenium driver
    and logs in to MAL. Then verifies login.
    '''

    #Skip privacy policy
    try:
        browser.find_element_by_xpath("//html//body//div[7]//div//div[2]//div//button").click()
    except:
        pass

    #Login
    username = browser.find_element_by_id("loginUserName")
    password = browser.find_element_by_id("login-password")
    username.send_keys(MAL_PAYLOAD["user_name"])
    password.send_keys(MAL_PAYLOAD["password"])
    time.sleep(3)
    browser.find_element_by_xpath("//input[@value=\"Login\"]").click()

    verify_login()

def goto_anime_list(tab = ""):
    '''
    Moves to anime list and gathers the urls and
    names of all anime in list. If list default
    is not all anime, this will only grab the
    ones from the current tab.
    '''
    time.sleep(3)

    #Go to specified tab, otherwise default
    if tab:
        browser.get(LIST_URL + "?status={}&tag=".format(TABS[tab]))
    else:
        browser.get(LIST_URL)

    #Get anime and urls
    anime_list = browser.find_elements_by_class_name("animetitle")
    urls = browser.find_elements_by_xpath("//*[@class=\"animetitle\"]")

    return urls, anime_list

if __name__ == "__main__":
    login()
    funct = "rank"

    if funct == "tag":
        #Clear tags and then add new ones
        urls, anime_list = goto_anime_list()

        for i in range(0, len(anime_list)):
            #Remove tags
            #remove_tag(browser, urls[i], anime_list[i])

            #Fill any empty slots
            #fill_empty_tag(browser, urls[i], anime_list[i])

            #Or replace all tags
            #replace_tag(browser, urls[i], anime_list[i])

            #Or update tags
            #update_tag(browser, urls[i], anime_list[i])
    elif funct == "rank":
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
    else:
        print("{} not suppored.".format(funct))
        sys.exit()

    #browser.close()