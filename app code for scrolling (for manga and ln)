from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
import os
import json

class ReaderApp(App):
    def build(self):
        self.root = BoxLayout(orientation='vertical')

        #Decide whether its a manga or novel based on the module
        self.is_manga = True  # Change this flag to toggle between manga and novel

        if self.is_manga:
            #Load manga images from folder
            self.module_path = 'modules/manga1/chapter1'
            self.pages = sorted([os.path.join(self.module_path, f) for f in os.listdir(self.module_path) if f.endswith('.png')])
            self.current_page = 0
            self.display_image_page()
        else:
            #Load novel text files from folder
            self.module_path = 'modules/novel1'
            self.chapters = sorted([os.path.join(self.module_path, f) for f in os.listdir(self.module_path) if f.endswith('.txt')])
            self.current_chapter = 0
            self.display_text_chapter()

        return self.root

    def display_image_page(self):
        #Use ScrollView for smooth scrolling of manga pages
        scroll_view = ScrollView()
        image_widget = Image(source=self.pages[self.current_page])  # Load current page image
        scroll_view.add_widget(image_widget)
        self.root.clear_widgets()  #Clear previous content
        self.root.add_widget(scroll_view)  #Add the new image page

    def display_text_chapter(self):
        #Use ScrollView for smooth scrolling of text (novels)
        with open(self.chapters[self.current_chapter], 'r') as file:
            text = file.read()
        
        text_label = Label(text=text, size_hint_y=None, height=len(text) * 1.5)  #Dynamically size the text
        scroll_view = ScrollView()
        scroll_view.add_widget(text_label)
        
        self.root.clear_widgets()  #Clear previous content
        self.root.add_widget(scroll_view)  #Add the new text chapter

    def on_touch_move(self, touch):
        #This will allow swiping gesture for smooth navigation (manga or novels)
        if touch.dy > 50:  #Detect swipe down to go to the previous page/chapter
            self.prev_page()
        elif touch.dy < -50:  #Detect swipe up to go to the next page/chapter
            self.next_page()

    def prev_page(self):
        #Navigate to the previous page or chapter
        if self.is_manga:
            if self.current_page > 0:
                self.current_page -= 1
                self.display_image_page()
        else:
            if self.current_chapter > 0:
                self.current_chapter -= 1
                self.display_text_chapter()

    def next_page(self):
        #Navigate to the next page or chapter
        if self.is_manga:
            if self.current_page < len(self.pages) - 1:
                self.current_page += 1
                self.display_image_page()
        else:
            if self.current_chapter < len(self.chapters) - 1:
                self.current_chapter += 1
                self.display_text_chapter()

if __name__ == '__main__':
    ReaderApp().run()
