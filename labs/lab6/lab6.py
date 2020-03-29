import requests as req
from bs4 import BeautifulSoup as bS
from lxml import html
from collections import Counter


def main():
    try:
        url = "https://habr.com/en/all/"
        page = req.get(url)
        html_doc = page.text
        save_index_for_test(html_doc)
        soup = bS(html_doc, 'html.parser')

        count_img = len(soup.find_all("img"))  # Частота появления img
        print("Count of img - %d" % count_img)
        get_img_content((soup.find_all("img")))
        print("____________________________")

        count_link = len(soup.find_all("link"))  # Частота появления link
        print("Count of link - %d" % count_link)
        print(get_link_content(soup.find_all("link")))
        print("____________________________")

        get_all_tags_and_their_count(page)  # Частота появления всех тегов

    except req.ConnectionError:
        print("Your url is dead")


def get_all_tags_and_their_count(page):
    tree = html.fromstring(page.content)
    all_elms = tree.cssselect("*")
    all_tags = [x.tag for x in all_elms]
    c = Counter(all_tags)
    for e in c:
        print('{}: {}'.format(e, c[e]))


def get_img_content(list_elements):
    for img in list_elements:
        print(img.get("src"))


def get_link_content(list_elements):
    for link in list_elements:
        print(link.get("href"))


# I use it because had problem with encoding
def save_index_for_test(html_doc):
    with open('index.html', 'w', encoding="utf-8") as output_file:
        output_file.write(html_doc)


if __name__ == "__main__":
    main()
