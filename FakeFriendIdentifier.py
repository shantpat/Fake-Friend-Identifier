from selenium import webdriver
import time
import instaloader

L = instaloader.Instaloader()

# Login or load session
L.login('fake_friend_identifier', 'asdfghjkl123@')
input_username = input()

# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, str(input_username))

# Print list of followees

follow_list = []
following_list = []

for followee in profile.get_followers():
    follow_list.append(followee.username)
    #print("on going")

count1 = 0
for following in profile.get_followees():
    following_list.append(following.username)

ans = []
for i in following_list:
    if i not in follow_list:
        ans.append(i)


class InstaBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.instagram.com/direct/inbox/')
        time.sleep(2)
        self.driver.find_element_by_name('username').send_keys(username)
        time.sleep(2)
        self.driver.find_element_by_name('password').send_keys(password)
        time.sleep(2)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()

        time.sleep(6)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
        time.sleep(3)
        self.driver.find_elements_by_xpath("//button[contains(text(), 'Not Now')]")[0].click()
        time.sleep(3)
        self.driver.find_elements_by_xpath("//button[contains(text(), 'Send Message')]")[0].click()
        time.sleep(5)
        self.driver.find_elements_by_name('queryBox')[0].send_keys(str(input_username))
        time.sleep(4)
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[2]/div[1]/div').click()
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/div/button").click()
        time.sleep(4)

        global ans

        for unfollower in ans:
            self.driver.find_element_by_xpath(
                '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys('@'+str(unfollower))
            self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()

        time.sleep(4)


InstaBot('fake_friend_identifier', 'asdfghjkl123@')
