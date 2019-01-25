from selenium import webdriver
import requests
import bs4
import os
import random

state = 1

def click():
    global state
    browser.find_element_by_css_selector('.sc-button-play.playButton.sc-button.m-stretch').click()

query_url = "https://soundcloud.com/search?q="

#Path for chromeDriver
browser = webdriver.Chrome("E:\chromedriver.exe")
browser.get("https://soundcloud.com")

while True:
    print("Tell your Mood !! ")
    print(">>> 1 - Sad")
    print(">>> 2 - Happy")
    print(">>> 3 - Excited")
    print(">>> 4 - Depressed")
    print(">>> 0 - Exit")
    print()
    choice = int(input(">>> Your choice: "))
    if choice == 0:
        browser.quit()
        break
    print()

    # search according to the mood
    if choice == 1:
        url = query_url + "sad"
        request = requests.get(url)
        soup = bs4.BeautifulSoup(request.text, "lxml")

        tracks = soup.select("h2")[3:]
        track_links = []
        track_names = []
    
        for index, track in enumerate(tracks):
            track_links.append(track.a.get("href"))
            track_names.append(track.text)
            print()
        st="next"
        while True:
            if st=="next":
                choice = random.randint(0,5)
                print("Now playing: " + track_names[choice])
                browser.get("http://soundcloud.com" + track_links[choice])
                browser.find_element_by_css_selector('.sc-button-play.playButton.sc-button.m-stretch').click()
                state=1

            st = input()
            if st=="play" and state==0:
                state=1
                click()
            elif st=="pause" and state==1:
                state=0
                click()
            elif st=="close":
                state=0
                break

        continue

print()
print("Goodbye!")
print()
