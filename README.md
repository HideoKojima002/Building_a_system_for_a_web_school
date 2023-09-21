

## Building_a_system_for_a_web_school
 Building a system using Django REST Framework with support for SQLite and MySQL for a platform in a web school. This is a technical task. All issues have been resolved, all tasks have been completed.

# Как запустить весь проект без проблем?

#### Прежде всего создайте виртуальное окружение VENV и включите его.
#### Установите все зависимости из requirements.txt написав:
```bash
pip install -r requirements.txt
```
## Выберите себе базу данных, которая больше нравится, в настройках есть задокументированная MySQL или пользуйтесь SQLite 
# ДЛЯ SQLITE ПЕРЕИМЕНОВАН ФОРМАТ В НАСТРОЙКАХ НА DBDB3 ИЗМЕНИТЕ ЕГО У СЕБЯ. 

#### Затем последовательно введите:
```bash
cd web_school
```
#### Проведите миграции.
```bash
python manage.py makemigrations
python manage.py migrate
```
#### Создайте админа, так как он нужен для полноценной работы.
```bash
python manage.py createsuperuser 
```


#### После регистрации запустите локальный сервер.
```bash
python manage.py runserver
```
#### Затем перейдите по ссылке "http://127.0.0.1:8000"
Далее настоятельно рекомендую добавить данные через админку (http://127.0.0.1:8000/admin), либо воспользуйтесь теми данными что уже есть в базе данных.

 --- 
 ---






## Building_a_system_for_a_web_school
  Building a system using Django REST Framework with support for SQLite and MySQL for a platform in a web school. This is a technical task. All issues have been resolved, all tasks have been completed.

# How to run the entire project without problems?

#### First of all, create the VENV virtual environment and enable it.
#### Install all dependencies from requirements.txt by writing:
```bash
pip install -r requirements.txt
```
## Choose the database you like best, there is a documented MySQL in the settings or use SQLite
# FOR SQLITE FORMAT RENAMED IN SETTINGS ON DBDB3 CHANGE IT FOR YOURSELF.

#### Then enter sequentially:
```bash
cd web_school
```
#### Perform migrations.
```bash
python manage.py makemigrations
python manage.py migrate
```
#### Create an administrator, as he is needed for full-fledged work.
```bash
python manage.py createsuperuser
```


#### After registration, start the local server.
```bash
python manage.py runserver
```
#### Then go to the link "http://127.0.0.1:8000"
Next, I strongly recommend adding data through the admin panel (http://127.0.0.1:8000/admin), or use the data that is already in the database.
