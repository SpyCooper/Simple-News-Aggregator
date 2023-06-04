from bs4 import BeautifulSoup
from textwrap import wrap
import requests

# ---------------------------------- News website functions ----------------------------------


# ---------------------------------- Beginning of CNN function ----------------------------------
def cnn():
    # gets the latest homepage of CNN News
    homepage = requests.get('https://www.cnn.com/').text
    soup = BeautifulSoup(homepage, 'lxml')

    # finds the trending articles list
    trending_list = soup.find('div', class_='container_ribbon__cards-wrapper')
    trending_articles = trending_list.find_all('div', class_='card')

    # for each article in the trending articles list
    for index, article in enumerate(trending_articles):
        # gets the title of the article
        title = article.a.text.strip()

        # the first article in the list has 'trending now:' in the front, so that part is ignored
        if index == 0:
            title = title[10:]

        # makes filters out the articles that have a category to them (ex: 'Podcast:', or 'Video:')
        if title.find(':') == -1:
            # resets the file when it opens it
            file_name = 'trending_article_' + str(index+1)
            with open(f'News/CNN/{file_name}.txt', 'w', encoding="utf-8") as f:
                f.write('')
            f = open(f'News/CNN/{file_name}.txt', 'r+', encoding="utf-8")

            # gets the link to the article
            link = article.a['href']

            # writes the title of the article at the top of the file
            f.write(f'----- {title} -----\n')
            f.write(f'\n')

            # gets each articles HTML
            page_HTML = requests.get(link).text
            pageSoup = BeautifulSoup(page_HTML, 'lxml')

            # writes each article's text to the file
            body_HTML = pageSoup.find('div', class_='article__content')
            body_text = body_HTML.find_all('p')
            for paragraph in body_text:
                text = paragraph.text.replace('  ', '')
                text = wrap(text)
                for line in text:
                    if line[0] == ' ':
                        f.write(f'{line[1:]}\n')
                    else:
                        f.write(f'{line}\n')
                f.write(f'\n')

            # writes the link to the original article at the end
            f.write(f'\nLink to the original article: {link}')

# ---------------------------------- End of CNN function ----------------------------------




# ---------------------------------- Beginning of BBC function ----------------------------------
def bbc():
    # gets the latest homepage of BBC News
    homepage = requests.get('https://www.bbc.com/news').text
    soup = BeautifulSoup(homepage, 'lxml')

    # finds the trending articles list
    trending_list = soup.find('div', class_='nw-c-most-read__items gel-layout gel-layout--no-flex')
    trending_articles = trending_list.find_all('li')

    # for each article in the recent articles list
    for index, article in enumerate(trending_articles):
        # resets the file when it opens it
        file_name = 'trending_article_' + str(index+1)
        with open(f'News/BBC/{file_name}.txt', 'w', encoding="utf-8") as f:
            f.write('')
        f = open(f'News/BBC/{file_name}.txt', 'r+', encoding="utf-8")

        # finds the data for the recent articles and writes the title first
        title = article.find('span', class_='gs-c-promo-heading__title gel-pica-bold').text
        link = 'https://www.bbc.com/' + article.a['href']
        f.write(f'----- {title} -----\n')
        f.write(f'\n')

        # gets each articles HTML
        page_HTML = requests.get(link).text
        pageSoup = BeautifulSoup(page_HTML, 'lxml')

        # writes each article's text to the file
        body_HTML = pageSoup.find('article')
        body_text = body_HTML.find_all('p')
        for paragraph in body_text:
            text = paragraph.text.replace('  ', '')
            text = wrap(text)
            for line in text:
                if line[0] == ' ':
                    f.write(f'{line[1:]}\n')
                else:
                    f.write(f'{line}\n')
            f.write(f'\n')

        # writes the link to the original article at the end
        f.write(f'\nLink to the original article: {link}')

# ---------------------------------- End of BBC function ----------------------------------




# ---------------------------------- Beginning of PC Gamer function ----------------------------------
def pcGamer():
    # gets the latest homepage of PC Gamer
    homepage = requests.get('https://www.pcgamer.com/').text
    soup = BeautifulSoup(homepage, 'lxml')
    
    # finds the most recent articles list
    recent_articles_list = soup.find('div', class_='list-text-links list-text-links-trending-panel')
    recent_articles = recent_articles_list.find_all('div', class_='listingResult')

    # for each article in the recent articles list
    for index, article in enumerate(recent_articles):
        # resets the file when it opens it
        file_name = 'trending_article_' + str(index+1)
        with open(f'Gaming/PC Gamer/{file_name}.txt', 'w', encoding="utf-8") as f:
            f.write('')
        f = open(f'Gaming/PC Gamer/{file_name}.txt', 'r+', encoding="utf-8")

        # finds the data for the recent articles and writes the title first
        title = article.a['aria-label']
        link = article.a['href']
        f.write(f'----- {title} -----\n')
        f.write(f'\n')

        # gets each articles HTML
        page_HTML = requests.get(link).text
        pageSoup = BeautifulSoup(page_HTML, 'lxml')

        # writes each article's text to the file
        body_HTML = pageSoup.find('div', id='article-body')
        body_text = body_HTML.find_all('p')
        for paragraph in body_text:
            text = wrap(paragraph.text)
            for line in text:
                f.write(f'{line} \n')
            f.write(f'\n')
        
        # writes the link to the original article at the end
        f.write(f'\nLink to the original article: {link}')

# ---------------------------------- End of PC Gamer function ----------------------------------




# ---------------------------------- Beginning of GamesRadar function ----------------------------------
def gamesRadar():
    # gets the latest homepage of gamesradar
    homepage = requests.get('https://www.gamesradar.com/').text
    soup = BeautifulSoup(homepage, 'lxml')

    #  ----------------- beginning of finding recent articles -----------------

    # finds the most recent articles list
    recent_articles_list = soup.find('div', class_='list-text-links list-text-links-trending-panel')
    recent_articles = recent_articles_list.find_all('div', class_='listingResult')
    
    # for each article in the recent articles list
    for index, article in enumerate(recent_articles):
        # resets the file when it opens it
        file_name = 'recent_article_' + str(index+1)
        with open(f'Gaming/Games Radar/{file_name}.txt', 'w', encoding="utf-8") as f:
            f.write('')
        f = open(f'Gaming/Games Radar/{file_name}.txt', 'r+', encoding="utf-8")

        # finds the data for the recent articles and writes the title first
        title = article.a['aria-label']
        link = article.a['href']
        f.write(f'----- {title} -----\n')
        f.write(f'\n')

        # gets each articles HTML
        page_HTML = requests.get(link).text
        pageSoup = BeautifulSoup(page_HTML, 'lxml')

        # writes each article's text to the file
        body_HTML = pageSoup.find('div', id='article-body')
        body_text = body_HTML.find_all('p')
        for paragraph in body_text:
            text = wrap(paragraph.text)
            for line in text:
                f.write(f'{line} \n')
            f.write(f'\n')
        
        # writes the link to the original article at the end
        f.write(f'\nLink to the original article: {link}')

    # ----------------- beginning of finding hot articles -----------------

    # gets the html for the hot articles section
    hot_articles_section = soup.find('div', class_='listingResults curated')
    hot_articles_list = hot_articles_section.find_all('div', class_='listingResult')

    # for each article in the section
    for index, article in enumerate(hot_articles_list):
        # resets the file when it opens it
        file_name = 'hot_article_' + str(index+1)
        with open(f'Gaming/Games Radar/{file_name}.txt', 'w', encoding="utf-8") as f:
            f.write('')
        f = open(f'Gaming/Games Radar/{file_name}.txt', 'r+', encoding="utf-8")

        # finds the data for the hot articles and writes the title first
        title = article.a['aria-label']
        link = article.a['href']
        f.write(f'----- {title} -----\n')
        f.write(f'\n')

        # gets each article's HTML
        page_HTML = requests.get(link).text
        pageSoup = BeautifulSoup(page_HTML, 'lxml')

        # writes each article's text to the file
        body_HTML = pageSoup.find('div', id='article-body')
        body_text = body_HTML.find_all('p')
        for paragraph in body_text:
            text = wrap(paragraph.text)
            for line in text:
                f.write(f'{line} \n')
            f.write(f'\n')
        
        # writes the link to the original article at the end
        f.write(f'\nLink to the original article: {link}')

# ---------------------------------- End of GamesRadar function ----------------------------------




# ---------------------------------- Main function ----------------------------------
print('Beginning news aggregation...')

print('Starting CNN articles...')
cnn()
print('Starting BBC articles...')
bbc()
print('Starting PC Gamer articles...')
pcGamer()
print('Starting GamesRadar articles...')
gamesRadar()

print('Completed news aggregation.')
print('Program ended.')
