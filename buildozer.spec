[app]

# Имя вашего приложения
title = Ваше Приложение

# Пакет вашего приложения
package.name = ваше_приложение
package.domain = org.example

# Исходный код
source.dir = .

# Зависимости
requirements = kivy

# Используемый язык
osx.python_version = 3
android.python_version = 3

# Компиляция в архитектуру x86 (для симулятора)
# настройка таргета android сделана для симулятора, поэтому, если вы компилируете для устройства, измените ее
# на android_new_venv, но пользуйтесь только в случае ошибки
# target = android_x86

# Компиляция в архитектуру ARM (для реального устройства)
target = android_new_venv

# Версия приложения
version = 1.0

# Другие настройки...
