from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
import api
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from cards import cards
from image_class import MirrorImage, image


class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        
        # Создаем макет
        layout = BoxLayout(orientation='vertical')
        
        # Добавляем заголовок
        layout.add_widget(Label(text='Меню', font_size=30))
        
        # Добавляем кнопку "Таро"
        taro_button = Button(text='Таро', size_hint=(1, 0.5),)
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

        self.tarot_image = image
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
                cardname = cardname.replace("The_", "")
                
                reverse = False
                if "Reversed_" in cardname:
                    cardname = cardname.replace("Reversed_", "")
                    reverse = True    

                cardname = cards[cardname]
                self.tarot_image.source = f'tarot_images/{cardname}.jpg'
                if reverse:
                    self.tarot_image.mirror = True
                else:
                    self.tarot_image.mirror = False
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
