from libs import *

#Regex patterns
ID_PATTERN = re.compile("(?<=/)[\d]+(?=/)")

def format_tags(tag):
    '''
    Takes in a string of tags and filters them
    as desired.
    '''
    
    tags = tag.split(", ")

    tags_to_remove = ["Cars", "Dementia", "Demons", "Harem", "Josei",
                      "Martial Arts", "Parody", "Police", "Samurai",
                      "Seinen", "Shoujo", "Shoujo Ai", "Shounen Ai",
                      "Super Power", "Yaoi", "Yuri"]

    #Replace/remove genres that I don't want
    if "Slice of Life" in tags:
        tags = ["SoL" if x == "Slice of Life" else x for x in tags]

    for ele in tags_to_remove:
        if ele in tags:
            tags.remove(ele)

    #Reconstruct string
    string = ""
    for ele in tags:
        string += ele + ", "

    string = string[:-2]
    return string

def get_studio(browser, string):
    '''
    Adds the studio that animated the anime
    to the list of tags.
    '''

    #Get studios
    studios = browser.find_element_by_css_selector("span[class=\"information studio author\"")
    string += studios.text + ", "

    return string

def get_genres(browser, url):
    '''
    Obtains a formatted string of genres for the
    current anime in list.
    '''
    
    #Load tab
    time.sleep(3)
    browser.execute_script("window.open(\"{}\");".format(url))
    browser.switch_to_window(browser.window_handles[1])

    #Get genres
    genres = browser.find_elements_by_css_selector("a[href*=\"genre\"")
    string = ""
    for gen in genres:
        string += gen.text + ", "

    #Add studios
    string = get_studio(browser, string)

    string = string[:-2]

    #Close tab
    browser.close()
    browser.switch_to_window(browser.window_handles[0])

    string = format_tags(string)
    return string

def add_genres(browser, ID, string):
    '''
    Adds the genres for the current anime as a tag.
    '''

    #Add genres to current tag of anime
    browser.find_element_by_xpath("//a[@onclick=\"tag_showEdit({}, 1);\"]".format(ID)).click()
    tag = browser.find_element_by_id("tagInfo{}".format(ID))
    tag.send_keys(string)
    browser.find_element_by_xpath("//input[@onclick=\"tag_add({},1)\"]".format(ID)).click()

def fill_empty_tags(browser, urls, anime_list):
    '''
    Loops over every anime in the list and fills
    in any with empty tags.
    '''
    
    #Loop over all anime
    for i in range(len(anime_list)):
        #Get anime info
        name = anime_list[i].text
        url = urls[i].get_attribute("href")
        ID = re.search(ID_PATTERN, url).group()
        tags = browser.find_element_by_xpath("//*[@id=\"tagLinks{}\"]".format(ID)).text

        #Tags already exist
        if tags:
            print("Tags already exist for {}, skipping.".format(name))
            continue
        else:
            print("Adding tags for {}.".format(name))

        string = get_genres(browser, url)
        add_genres(browser, ID, string)

def remove_tags(browser, urls, anime_list):
    '''
    Removes all tags from anime in
    current tab.
    '''
    
    #Loop over all anime
    for i in range(len(anime_list)):
        #Get anime info
        name = anime_list[i].text
        url = urls[i].get_attribute("href")
        ID = re.search(ID_PATTERN, url).group()
        tags = browser.find_element_by_xpath("//*[@id=\"tagLinks{}\"]".format(ID)).text

        #Tags already exist
        if tags:
            print("Removing tags for {}.".format(name))
        else:
            print("No tags to remove for {}.".format(name))
            continue

        #Remove genres for current anime
        time.sleep(3)
        browser.find_element_by_xpath("//a[@onclick=\"tag_showEdit({}, 1);\"]".format(ID)).click()
        tag = browser.find_element_by_id("tagInfo{}".format(ID))
        tag.clear()
        browser.find_element_by_xpath("//input[@onclick=\"tag_add({},1)\"]".format(ID)).click()
