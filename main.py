from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
import api
from kivy.uix.textinput import TextInput

from kivy.lang import Builder
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout

import random
from kivy.graphics.transformation import Matrix
from kivy.uix.scatter import Scatter

class MyBox(BoxLayout):



    def later_(self, dt=None):
        self.t.apply_transform(Matrix().scale(-1, 1.0, 1.0),
                             post_multiply=True,
                             anchor=self.to_local(*self.center))
        Clock.schedule_once(self.later_, 1.0)

class TestApp(App):
    def build(self):


        Builder.load_string("""\
<MyBox>:
    t: s
    orientation: 'vertical'
    Scatter:
        id: s
        do_scale: 0
        do_rotate: 0
        do_translation: 0,0 
        Label:

            pos: s.pos
            size: s.size
            text: "The text below will keep changing using a delayed function..."

        """
        )
        mybox = MyBox()
        Clock.schedule_once(mybox.later_, 1.0)

        return mybox


cards = {
  "Fool": "Fool",
  "Magician": "Magician",
  "High_Priestess": "High Priestess",
  "Empress": "Empress",
  "Emperor": "Emperor",
  "Hierophant": "Hierophant",
  "Lovers": "Lovers",
  "Chariot": "Chariot",
  "Strength": "Strength",
  "Hermit": "Hermit",
  "Wheel_Of_Fortune": "Wheel of Fortune",
  "Justice": "Justice",
  "Hanged_Man": "Hanged Man",
  "Death": "Death",
  "Temperance": "Temperance",
  "Devil": "Devil",
  "Tower": "Tower",
  "Star": "Star",
  "Moon": "Moon",
  "Sun": "Sun",
  "Judgement": "Judgement",
  "World": "World",
  "Ace_Of_Cups": "1",
  "Two_Of_Cups": "2",
  "Three_Of_Cups": "3",
  "Four_Of_Cups": "4",
  "Five_Of_Cups": "5",
  "Six_Of_Cups": "6",
  "Seven_Of_Cups": "7",
  "Eight_Of_Cups": "8",
  "Nine_Of_Cups": "9",
  "Ten_Of_Cups": "10",
  "Page_Of_Cups": "11",
  "Knight_Of_Cups": "12",
  "Queen_Of_Cups": "13",
  "King_Of_Cups": "14",
  "Ace_Of_Wands": "15",
  "Two_Of_Wands": "16",
  "Three_Of_Wands": "17",
  "Four_Of_Wands": "18",
  "Five_Of_Wands": "19",
  "Six_Of_Wands": "20",
  "Seven_Of_Wands": "21",
  "Eight_Of_Wands": "22",
  "Nine_Of_Wands": "23",
  "Ten_Of_Wands": "24",
  "Page_Of_Wands": "25",
  "Knight_Of_Wands": "26",
  "Queen_Of_Wands": "27",
  "King_Of_Wands": "28",
  "Ace_Of_Swords": "29",
  "Two_Of_Swords": "30",
  "Three_Of_Swords": "31",
  "Four_Of_Swords": "32",
  "Five_Of_Swords": "33",
  "Six_Of_Swords": "34",
  "Seven_Of_Swords": "35",
  "Eight_Of_Swords": "36",
  "Nine_Of_Swords": "37",
  "Ten_Of_Swords": "38",
  "Page_Of_Swords": "39",
  "Knight_Of_Swords": "40",
  "Queen_Of_Swords": "41",
  "King_Of_Swords": "42",
  "Ace_Of_Pentacles": "43",
  "Two_Of_Pentacles": "44",
  "Three_Of_Pentacles": "45",
  "Four_Of_Pentacles": "46",
  "Five_Of_Pentacles": "47",
  "Six_Of_Pentacles": "48",
  "Seven_Of_Pentacles": "49",
  "Eight_Of_Pentacles": "50",
  "Nine_Of_Pentacles": "51",
  "Ten_Of_Pentacles": "52",
  "Page_Of_Pentacles": "53",
  "Knight_Of_Pentacles": "54",
  "Queen_Of_Pentacles": "55",
  "King_Of_Pentacles": "56",
}


class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        
        # Создаем макет
        layout = BoxLayout(orientation='vertical')
        
        # Добавляем заголовок
        layout.add_widget(Label(text='Меню', font_size=30))
        
        # Добавляем кнопку "Таро"
        taro_button = Button(text='Таро', size_hint=(1, 0.5))
        taro_button.bind(on_press=self.taro_button_pressed)
        layout.add_widget(taro_button)
        
        # Добавляем кнопку "Выход"
        exit_button = Button(text='Выход', size_hint=(1, 0.5))
        exit_button.bind(on_press=self.exit_button_pressed)
        layout.add_widget(exit_button)
    
        self.add_widget(layout)

    def taro_button_pressed(self, instance):
        self.manager.current = 'tarot_screen'

    def exit_button_pressed(self, instance):
        App.get_running_app().stop()


class TarotScreen(Screen):
    def __init__(self, **kwargs):
        super(TarotScreen, self).__init__(**kwargs)
        self.connection = api.Connection()
        self.cotd = self.connection.get_cotd_random()
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Your card of the day:', font_size=30, size_hint=(1, 0.2)))

        self.tarot_image = Image(source='back_image.png')
        self.tarot_image.bind(on_touch_down=self.flip_card)
        layout.add_widget(self.tarot_image)
        
        self.scrollview = ScrollView(
            size_hint=(0.8, 0.4),
            do_scroll_y=True,
            do_scroll_x=False,
            pos_hint={'center_x': 0.5},
        )
        text = ('Нажмите на карту')
        self.textinput = TextInput(text=text, size_hint_y=None, font_size='20sp', readonly=True, halign = 'center')

        self.textinput.bind(minimum_height=self.textinput.setter('height'))
        self.textinput.background_color = (0, 0, 0, 0)
        self.textinput.foreground_color = (1, 1, 1, 1)
        self.scrollview.add_widget(self.textinput)
        layout.add_widget(self.scrollview)

        self.add_widget(layout)

    def flip_card(self, instance, touch):
        if self.tarot_image.collide_point(*touch.pos):
            if self.tarot_image.source == 'back_image.png':
                cardname:str = self.cotd["Card"]
                cardname = cardname.replace(' ', "_")
                cardname = cardname.replace("The", "")
                
                if "Reversed_" in cardname:
                    cardname = cardname.replace("Reversed_", "")

                cardname = cards[cardname]
                self.tarot_image.source = f'tarot_images/{cardname}.jpg'
                self.textinput.halign  = 'left'
                self.textinput.text = self.cotd["your_result"]
            else:
                self.tarot_image.source = 'back_image.png'
                self.textinput.text = 'Нажмите на карту'
                self.textinput.halign  = 'center'


class MyApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(MenuScreen(name='menu_screen'))
        sm.add_widget(TarotScreen(name='tarot_screen'))

        return sm

if __name__ == '__main__':
    MyApp().run()
