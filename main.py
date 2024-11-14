from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from manga_list_page import MangaListPage
from chapter_list_page import ChapterListPage
from manga_reader_page import MangaReaderPage

class IntamaBRApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MangaListPage(name='manga_list'))
        sm.add_widget(ChapterListPage(name='chapter_list'))
        sm.add_widget(MangaReaderPage(name='reader'))
        return sm

if __name__ == "__main__":
    IntamaBRApp().run()
    
