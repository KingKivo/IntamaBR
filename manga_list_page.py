from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from api_helpers import fetch_manga_list

class MangaListPage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # add a search bar
        search_bar = TextInput(hint_text="Search Manga",multiline=False)
        search_bar.bind(text=self.on_search_text)
        self.add_widget(search_bar)

        # add a refresh button
        refresh_button = Button(text="Refresh")
        refresh_button.bind(on_release=lambda x: self.refresh_manga_list())
        self.add_widget(refresh_button)

        # load initial manga list
        self.manga_list_layout = BoxLayout(orientation='vertical', size_hint_y=None)
        self.add_widget(self.manga_list_layout)
        self.refresh_manga_list()

    def on_search_text(self, instance, value):
        self.display_manga_list(value)

    def refresh_manga_list(self):
        self.manga_date = fetch_manga_list() # fetch fresh data
        self.display_manga_list() # display updated data

    def display_manga_list(self, query=""):
        # clear previous widgets
        self.manga_list_layout.clear_widgets()

        # display manga that match the search query
        for manga  in self.manga_data:
            title = manga['attributes']['title']['en']
            if query.lower() in title.lower():
                button = Button(text=title)
                button.bind(on_release=lambda instance, manga_id=manga['id']: self.open_chapter_list(manga_id))
                self.manga_list_layout.add_widget(button)


    def open_chapter_list(self, manga_id):
        # switch to chapter list page when manga is selected
        self.parent.switch_to_chapter_page(manga_id)
        
