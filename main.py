import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.network.urlrequest import UrlRequest

kivy.require('2.0.0')


class Menu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Button(text='Card of the day', on_press=self.open_cotd))
        layout.add_widget(Button(text='Open Green Screen', on_press=self.open_green))
        layout.add_widget(Button(text='Open Blue Screen', on_press=self.open_blue))
        layout.add_widget(Button(text='Exit', on_press=self.exit_app))
        self.add_widget(layout)

    def open_cotd(self, *args):
        screen_manager.current = 'cotd'

    def open_green(self, *args):
        screen_manager.current = 'green'

    def open_blue(self, *args):
        screen_manager.current = 'blue'

    def exit_app(self, *args):
        App.get_running_app().stop()


class Red(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Button(text='Back to Menu', on_press=self.back_to_menu))
        self.add_widget(layout)

    def back_to_menu(self, *args):
        screen_manager.current = 'menu'


class Green(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Button(text='Back to Menu', on_press=self.back_to_menu))
        self.add_widget(layout)

    def back_to_menu(self, *args):
        screen_manager.current = 'menu'


class Blue(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Button(text='Back to Menu', on_press=self.back_to_menu))
        self.add_widget(layout)

    def back_to_menu(self, *args):
        screen_manager.current = 'menu'



class COTDScreen(Screen):
    def on_enter(self):
        # Событие on_enter вызывается, когда экран становится активным
        # Создаем контейнер BoxLayout
        box = BoxLayout(orientation='vertical')

        # Создаем виджет для ввода числа
        self.numb_input = TextInput(text='', multiline=False)

        # Создаем кнопку
        btn = Button(text='Отправить запрос', size_hint=(.5, .5), pos_hint={'center_x': .5, 'center_y': .5})
        btn.bind(on_press=self.on_button_press)

        # Создаем виджет для вывода ответа
        self.result_label = Label(text='', size_hint_y=None, height=400, text_size=(400, None), valign='top')

        # Создаем прокручиваемую область для виджета Label
        scroll = ScrollView(size_hint=(1, None), size=(400, 400), pos_hint={'center_x': .5, 'center_y': .5})
        scroll.add_widget(self.result_label)

        # Создаем кнопку для возврата в меню
        return_btn = Button(text='Вернуться в меню', size_hint=(.5, .5), pos_hint={'center_x': .5, 'center_y': .5})
        return_btn.bind(on_press=self.back_to_menu)

        # Добавляем виджеты в контейнер
        box.add_widget(self.numb_input)
        box.add_widget(btn)
        box.add_widget(scroll)
        box.add_widget(return_btn)

        # Устанавливаем контейнер как корневой элемент экрана
        self.add_widget(box)

    def on_button_press(self, instance):
        # Получаем введенное число из виджета
        numb = self.numb_input.text

        # Формируем URL
        url = f"http://127.0.0.1:8000/cotd/{numb}"

        # Отправляем запрос на сервер
        UrlRequest(url=url, on_success=self.handle_success, on_error=self.handle_error)

    def handle_success(self, request, response):
        # Обновляем текст в виджете для вывода ответа
        self.result_label.text += response["your_result"] + '\n'

    def handle_error(self, request, error):
        # Выводим сообщение об ошибке в виджете
        self.result_label.text += str(error) + '\n'
    
    def back_to_menu(self, *args):
        screen_manager.current = 'menu'

screen_manager = ScreenManager()
screen_manager.add_widget(Menu(name='menu'))
screen_manager.add_widget(COTDScreen(name='cotd'))
screen_manager.add_widget(Green(name='green'))
screen_manager.add_widget(Blue(name='blue'))

class TestApp(App):
    def build(self):
        return screen_manager


if __name__ == '__main__':
    TestApp().run()
