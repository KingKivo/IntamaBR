from kivy.uix.scrollview import ScrollView
from kivy.uix.image import AsyncImage
from kivy.uix.boxlayout import BoxLayout
from api_helpers import fetch_chapter_pages

class MangaReaderPage(ScrollView):
    def __init__(self, chapter_id, **kwargs):
        super().__init__(**kwargs)

        # fetch pages for the chapter
        pages = fetch_chapter_pages(chapter_id)

        layout = BoxLayout(orientation='vertical', size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))

        # add each page as an image in a scrollable view
        for page_url in pages:
            image = AsyncImage(source=page_url, size_hint_y=None, height=800)
            layout.add_widget(image)

        self.add_widget(layout)
