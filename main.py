import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

from sentiment import generate_sentiment


def main():
    driver = webdriver.Chrome()

    driver.get('https://www.euronews.ro/verticals/travel')
    sleep(3)

    articles = []
    texts = driver.find_elements(By.CLASS_NAME, 'articlePreview_title__link__j1G6a')
    urls = []
    for text in texts:
        urls.append(text.get_attribute("href"))

    for url in urls:
        try:
            driver.get(url)
            sleep(2)
            content = driver.find_element(By.CLASS_NAME, 'body_content__mYvyx').text
            articleJson = {
                "text": content,
                "sentiment": "{sentiment}".format(sentiment=generate_sentiment(content))
            }
            articles.append(articleJson)
        except:
            # do nothing
            print("exception occurred, move on")
    export(articles)

    print("Subjective/Objective articles: {result}".format(result=calculate_subjectivity_on_objectivity(articles)))

    driver.quit()


def export(articles):
    with open("output.json", "w") as f:
        json.dump(articles, f)


def calculate_subjectivity_on_objectivity(articles):
    subjectiveArticles = 0
    objectiveArticles = 0
    for article in articles:
        if article['sentiment'] == 'Positive' or article['sentiment'] == 'Negative':
            subjectiveArticles = subjectiveArticles + 1
        else:
            objectiveArticles = objectiveArticles + 1
    return subjectiveArticles / objectiveArticles


if __name__ == "__main__":
    main()
