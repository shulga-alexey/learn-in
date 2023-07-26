# LEARN-IN

## Алгоритм командной работы в GitHub

### Начало работы
1. Клонируем проект по ссылке с репозитория тимлида.
   ```bash
   git clone git@github.com:shulga-alexey/learn-in.git
   ```
2. Забываем о ветке `main` до релиза проекта.
3. Разработку ведем на ветке `develop`, создавать ее самостоятельно не надо,
   если ветка отсутствует - обратиться к тимлиду.
   * Проверяем, что такая ветка есть:
        ```bash
        git branch
        ```
     ```
     > develop
     > * master
     ``` 
     Если ветки нет, забираем данные в локальный репозиторий и
     снова проверяем наличие `develop`:
        ```bash
        git fetch
        git branch
        ```
   * Переходим на ветку:
        ```bash
        git checkout develop
        ```
4. Код текущей задачи пишем в отдельной ветке, и уже с нее делаем `pull request` в `develop`.
   В ветку `develop` код попадает только через `pull request`.
   > МЕРЖИТЬ `pull request` НЕ НАДО. Это должен делать кто-то один, в данном случае - тимлид.

### Решение текущей задачи
1. Подготовка
    1. Обновляем локальную ветку `develop`.
        ```bash
        git pull origin develop:develop
        ```
    2. Устанавливаем зависимости и применяем миграции, которые могли прилететь с обновлениями.
        ```bash
        pip install -r requirements.txt
        cd learn_in
        python manage.py migrate
        ```
        > Если не удается применить миграции, сносим файл базы данных, и накатываем миграции с нуля.
    3. Создаем ветку под текущую задачу, имена веток рекомендую группировать по модулям.
        ```bash
        git checkout -b api/views-urls-serializers
        ```
2. Решение
    1. Решаем задачу и проверяем работоспособность - локально проект должен запускаться.
    2. Проверяем `flake8` (`pip install flake8` - в requirements.txt добавлять не надо).
        ```bash
        cd learn_in
        pip install flake8
        flake8
        ```
    3. Проверяем, что находимся на ветке задачи, индексируем и коммитим изменения.
        ```bash
        git checkout <ветка-текущей-задачи>
        git add .
        git commit -m 'commit_message'
        ```
    4. Перед тем как пушить в удаленный репозиторий проверяем изменения ветки `develop`,
       повторяя действия п. 1.1 - 1.2 данной инструкции.
       Делаем мерж с локальной веткой текущей задачи:
        ```bash
        git checkout <ветка-текущей-задачи>
        git merge develop
        ```
        Если есть конфликты, решаем их и повторяем действия п. 2.2 - 2.3 данной инструкции.
    5. Пушим в удаленный репозиторий
        ```bash
        git push origin <ветка-текущей-задачи>
        ```
3. Pull request
    1. В удаленном репозитории создаем `pull request`, указываем ревьюера.
       > Примечание: переименование ветки влечет закрытие `pull request`.
    2. В телеге оповещаем - "создал `pull request`" и ссылку на него.
    3. * Если `pull request` одобрен коллегами и слит в ветку `develop` тимлидом,
         то переходим к п. 1.1 данной инструкции.
       * Если `pull request` вернули на доработку - дорабатываем задачу в той же ветке,
         то повторяем все действия, начиная с п. 2.1 данной инструкции.
         > Примечание: чтобы внести доработки, не нужно создавать новый `pull request`, достаточно
           запушить изменения (см. п. 2.5) в ветку, от которой `pull request` был создан.