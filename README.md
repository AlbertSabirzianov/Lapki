# Lapki
Api для интернет магазина украшений, позволяет сохранять, удалять и изменять товары украшений (описание и картинки).
При заказе украшения отправляется письмо на электронную почту мастера.
# Стэк
Написан с помощью djangorestframework
# Установка
Скачайте репозиторий на свой компьютер
```commandline
git clone https://github.com/AlbertSabirzianov/Lapki.git
```
Создайте файл .env, где напишите почту и пароль от ящика мастера (необходимо для отправки сообщения о заказе на почту).
```.env
Mail_User=<email>
Password=<password>
```
Запустите миграции
```commandline
python manage.py migrate
```
Запустите сервер
```commandline
python manage.py runserver
```
# Оцените приложение онлайн!
Заходите в онлайн магазин [Lapkistore](https://lapkistore.ru) и совершайте покупки!
