from kivy.uix.boxlayout import Boxlayout
from kivy.uix.button import Button
from api_helpers import fetch_chapters_for_manga

class ChapterListPage(BoxLayout):
    def __init__(self, manga_id, **kwargs):
        super().__init__(**kwargs)
        self.orientation ='vertical'

        chapters = fetch_chapters_for_manga(manga_id)

        for chapter in chapters:
            button = Button(text=f"Chapter {chapter['attributes']['chapter']}")
            button.bind(on_release=lambda instance, chapter_id=chapter['id']: self.open_manga_reader(chapter_id))
            self.add_widget(button)

    def open_manga_reader(self, chapter_id);
        # naviagate to manga reader page with selected chapter
        self.parent.switch_to_reader(chapter_id)
