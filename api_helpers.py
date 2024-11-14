import requests

BASE_URL ="https://api.mangadex.org/"

def fetch_manga_list():
    url = f"{BASE_URL}manga"
    response = requests.get(url)
    if repsonse.status_code ==200:
        manga_data = response.json()
        return manga_data['data']
    else:
        return []

def fetch_chapters_for_manga(manga_id):
    url = f"{BASE_URL}manga/{manga_id}/feed"
    response = requests.get(url)
    if response.status_code ==200:
        chapter_data = response.json()
        return chapter_data['data']
    else:
        return []
def fetch_chapter_pages(chapter_id):
    url = f"{BASE_URL}at-home/server/{chapter_id}"
    response = requests.get(url)
    if response.status_code ==200:
        base_url = response.json()['baseUrl']
        pages = response.json()['chapter']['data']
        return [f"{base_url}/{page}" for page in pages]
    else:
        return []
