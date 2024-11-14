from kivy.uix.screenmanager import ScreenManager

class IntamaScreenManager(ScreenManager):
    def switch_to_chapter_page(self, manga_id):
        self.current= 'chapter_list'
        self.get_screen('chapter_list').load_chapters(manga_id)

    def switch_to_reader(self, chapter_id):
        self.current = 'reader'
        self.get_screen('reader').load_chapter(chapter_id)
