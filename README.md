# LEARN-IN

### Запуск проекта

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:shulga-alexey/learn-in.git
```

```
cd learn-in
```

Создать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

```
python3 -m pip install -U pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
cd learn_in
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

Проект будет доступен по адресу `http://127.0.0.1:8000/` .
