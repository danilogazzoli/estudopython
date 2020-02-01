from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys


def print_same_line(text):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(text)
    sys.stdout.flush()


class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(10)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
        passworword_elem.clear()
        passworword_elem.send_keys(self.password)
        passworword_elem.send_keys(Keys.RETURN)
        time.sleep(10)

    def get_heart_icon_xpath(self, post_num):
        """
        Return heart icon xpath corresponding to n-post.
        """
        if post_num == 1:
            return 'xpath=//button/span'
        else:
            return f'xpath=//article[{post_num}]/div[2]/section/span/button/span'

    def like_pic(self): 
        time.sleep(4) 
        like = self.driver.find_element_by_xpath('/html/body/div/section[1]/main/div/div/article/div[2]/section[1]/span[1]/button') 
        #like = self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button/span') 

        # you can find the like button using class name too 
        time.sleep(2) 
        like.click() # clicking the like button 

    def like_photo(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(15)

        # gathering photos
        pic_hrefs = []
        for i in range(1, 7):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                # get tags
                hrefs_in_view = driver.find_elements_by_tag_name('a')
                # finding relevant hrefs
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                 if '.com/p/' in elem.get_attribute('href')]
                # building list of unique photos
                [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
                # print("Check: pic href length " + str(len(pic_hrefs)))
            except Exception:
                continue

        # Liking photos
        unique_photos = len(pic_hrefs)
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                time.sleep(random.randint(2, 4))
                ##my_xpath = self.get_heart_icon_xpath(1)
                ##heart_icon = driver.find_element_by_xpath(my_xpath)
                ##heart_icon.click()
                ##like_button = lambda: driver.find_element_by_xpath('//span[@aria-label="Curtir"]').click()
                ##like_button().click()
                self.like_pic()
                ##if heart_icon == None:
                #     print('botão like nao encontrado')
                #else:    
                for second in reversed(range(0, random.randint(18, 28))):
                    print_same_line("#" + hashtag + ': unique photos left: ' + str(unique_photos)
                                        + " | Sleeping " + str(second))
                    time.sleep(2)
            except Exception as e:
                print("outra exceção:" + e.__class__.__name__ )    
                print("Mensagem:" + str(e))                
                time.sleep(20)

            unique_photos -= 1

if __name__ == "__main__":

    username = "fiona.tasso"
    password = "123fiona"

    ig = InstagramBot(username, password)
    ig.login()

    hashtags = ['catlovers', 'redcat', 'catsofinstagram', 'instacats', 'instapets',
                'petlovers', 'gataruiva', 'redcats', 'amogatos', 'bosscats', 'topcat', 'topcats',
                'bichanosbr', 'cwbcats', 'gatoscwb', 'cats' , 'catsofinstagram' , 'catlovers' , 'gingercats' , 'redcats' , 'rescuedcats' , 'catstorys' ,
                'sleepingcats' , 'cats', 'catsofinstagram' , 'catlovers' , 'catlover' , 'gingercats', 'redcats', 'orangecats', 'cats_of_instagram' , 
                'catstagram' , 'catlove' , 'catpage' , 'catsagram' , 'catinstagram' , 'catlady' , 'gatto', 'gato', 'gatti',
                'katze', 'pet', 'pets', 'petsofinstagram' , 'petstagram' , 'petslover' , 'picoftheday' , 'photography' , 'photooftheday' , 
                'instagood' , 'instamood' , 'instalike' , 'exoticcats' , 'exoticshorthair' , 'catsofinstagram' , 'cat' , 
                'sweet' , 'handsome' , 'wednesday' , 'redcats' , 'bigeyes' , 'catlovers' , 'instacat' , 'crazycatmen' , 'love' , 'bellyrubs' , 
                'scratch', 'catsofinstagram' , 'catgrams' , 'redcats' , 'bkhkatze' , 'britishkurzhaar' , 'ilovemycat' , 'roterkater' , 
                'catlovers ' , 'schlafen' , 'bettwäsche' , 'mittwoch' , 'liebe' , 'kuschelnmitpuschel' , 'aufregend' , 'siberiancatofinstagram' , 
                'siberian_cat_lovers' , 'siberiancat' , 'siberiancatsofinstagram' , 'siberian' , 'siberiancats' , 'siberian_cats_lovers' ,
                'siberiancatworld' , 'redcats' , 'bosscat' , 'instacat' , 'catsofinstagram' , 'catphotography' , 'catsiberian' , 'catworldwide' , 'catsoftheworld' , 
                'cats_of_instagram' , 'catstagram' , 'animals' , 'colbythecat' , 'fluffycat' , 'mainecoon' , 'redcats' , 'bestfriendsanimalsociety' , 'bestfriendsofutah' ,
                'purrfect' , 'catsofinstagram' , 'ithinkhelovesustoo' , 'snuggles' , 'ifoundmypeople' , 'kitten' , 'purrfect', 'purrpurrpurr', 'happykitty', 'kittenoftheday', 'catcuddles',
                'gingercatsrule', 'igcats', 'gingerkitty', 'catlover', 'pets', 'meow', 'gatitos', 'gatosfotos',
                'kittenlife' , 'katzenkinder' , 'katzenliebe' , 'catlovers' , 'catsoninstagram' , 'redcats' , 'redcatsoninstagram' , 'brüder', 'geschwisterliebe' , 'catsoftheday' ,
                'catsoﬁnstagram' , 'catspam' , 'redcats' , 'sleepycat' , 'lazycat' , 'catsatnight' , 'blackcats' , 
                'animallovers' , 'animallove' ,  'catlovers' , 'catsofinsta' , 'topcat' ]


    while True:
        try:
            # Choose a random tag from the list of tags
            tag = random.choice(hashtags)
            ig.like_photo(tag)
        except Exception:
            ig.closeBrowser()
            time.sleep(60)
            ig = InstagramBot(username, password)
            ig.login()