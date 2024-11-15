import os
import requests
from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget

# MangaDex API to fetch manga chapters
MANGANDEX_API = "https://api.mangadex.org/v2/manga/{manga_id}/chapters"

def download_image(image_url, save_path):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded: {save_path}")
    else:
        print(f"Failed to download image: {image_url}")

def download_manga_chapter(manga_id, save_dir):
    url = MANGANDEX_API.format(manga_id=manga_id)
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch manga data")
        return

    chapters = response.json()['data']
    for chapter in chapters:
        chapter_title = chapter['attributes']['title']
        print(f"Downloading chapter: {chapter_title}")
        chapter_folder = os.path.join(save_dir, chapter_title)
        os.makedirs(chapter_folder, exist_ok=True)

        for page_num, page in enumerate(chapter['relationships'], start=1):
            page_url = page['attributes']['url']
            image_url = page_url  # Adjust this based on MangaDex API response format
            save_path = os.path.join(chapter_folder, f"page_{page_num}.jpg")
            download_image(image_url, save_path)

# Kivy App to display manga images
class MangaReaderApp(App):
    def build(self):
        self.title = "IntamaBR - Manga Reader"
        self.is_manga = True  # Set to True for manga
        self.manga_id = "manga-id-here"  # Replace with MangaDex manga ID
        self.save_dir = "manga_download"  # Define the download directory

        layout = BoxLayout(orientation='vertical')

        # Create a button to start downloading manga
        self.download_button = Button(text="Download Manga", size_hint=(1, 0.1))
        self.download_button.bind(on_press=self.download_manga)
        layout.add_widget(self.download_button)

        # Create a label to show the manga name or other info
        self.info_label = Label(text="Select a manga to read", size_hint=(1, 0.1))
        layout.add_widget(self.info_label)

        # Create a button to start reading manga
        self.read_button = Button(text="Read Manga", size_hint=(1, 0.1))
        self.read_button.bind(on_press=self.read_manga)
        layout.add_widget(self.read_button)

        # Create the scrollview to display manga images
        self.scrollview = ScrollView()
        layout.add_widget(self.scrollview)

        return layout

    def download_manga(self, instance):
        print("Downloading manga from MangaDex...")
        download_manga_chapter(self.manga_id, self.save_dir)
        print("Manga downloaded successfully!")

    def read_manga(self, instance):
        print("Displaying manga...")
        manga_folder = os.path.join(self.save_dir, "chapter1")  # Modify to the appropriate chapter path

        # Load all the images into the app
        image_files = os.listdir(manga_folder)
        self.image_list = [Image(source=os.path.join(manga_folder, img)) for img in image_files if img.endswith(".jpg")]
        self.show_image(0)

    def show_image(self, index):
        if index < len(self.image_list):
            self.scrollview.clear_widgets()
            self.scrollview.add_widget(self.image_list[index])

    def next_image(self):
        # Show next image
        pass

    def prev_image(self):
        # Show previous image
        pass

if __name__ == '__main__':
    app = MangaReaderApp()
    app.run()
