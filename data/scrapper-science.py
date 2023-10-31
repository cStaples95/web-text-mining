from bs4 import BeautifulSoup
import requests

# Credit to RJ

# setup
base = 'https://cnn.com/'
links = []
headlines = []

# set target genre
url = 'https://www.cnn.com/us/space-science'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'lxml')
counter = 1

# scrape for links
for link in soup.find_all('a', {"class": "container__link container_grid-4__link"})[:32]:
    # cnn uses link format twice (for headline hyperlink and thumbnail hyperlink), so to avoid scraping same uri twice
    if "videos" not in link.get('href'):
        if not (counter % 2 == 0):
            links.append(base[:-1]+link.get('href'))
        counter += 1

counter = 1
# scrape for headlines
for link in links:
    # setup soup
    url = link
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'lxml')
    if "videos" not in link:
        for headline in soup.find_all('h1', {"class": "headline__text inline-placeholder"}):
            headlines.append("{}".format(headline.text))


counter = 1
# scrape 12 science links for info
for link in links[:12]:
    # setup soup
    url = link
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'lxml')

    # visual separator
    if "videos" not in link:
        if counter < 10:
            file = open("science_040"+str(counter) +
                        ".txt", 'w', encoding='utf-8')
        else:
            file = open("science_04"+str(counter) +
                        ".txt", 'w', encoding='utf-8')
        file.write(
            "\n**********************************************************\n")
        file.write(link + '\n')
        file.write('\n'+str(counter) + ") " + headlines[counter-1])
        file.write('\n')

        # print scraped info
        for location in soup.find_all('div', {"class": "byline__names"}):
            # CNN is based in Atlanta, Georgia. All articles are published by CNN
            file.write(location.text.strip() + " Atlanta, Georgia")
        for date in soup.find_all('div', {"class": "timestamp"}):
            file.write("\n" + date.text.strip() + '\n')
        for content in soup.find_all('p', {"class": "paragraph"}):
            file.write(content.text.strip())
        file.close()
        counter += 1
