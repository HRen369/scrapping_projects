import bs4
import requests


def get_website():
    return requests.get("https://news.ycombinator.com/")


def convert_to_soup(r):
    return bs4.BeautifulSoup(r.content.decode('utf-8'), 'html.parser')


def convert_to_story_list(soup):
    stories = soup.find_all(attrs={"class": "athing"})
    story_list = []

    for story in stories:
        section = story.find(attrs={"class": "titlelink"})
        story_list.append({'title': section.text, "url": section['href']})

    return story_list


def print_story_list(li):
    for item in li:
        print(f"Title: {item['title']}")
        print(f"URL: {item['url']}")
        print()


def main():
    r = get_website()
    soup = convert_to_soup(r)
    story_list = convert_to_story_list(soup)
    print_story_list(story_list)


if __name__ == '__main__':
    main()
