# Домашнее задание к лекции «Python и БД. ORM»

## Задание 1
Составить модели классов SQLAlchemy по схеме.
Система хранит информацию об издателях (авторах), их книгах и фактах продажи. Книги могут продаваться в разных магазинах, поэтому требуется учитывать не только что за книга была продана, но и в каком магазине это было сделано, а также когда.
Интуитивно необходимо выбрать подходящие типы и связи полей.

## Задание 2

Используя SQLAlchemy, составить запрос выборки магазинов, продающих целевого издателя.

Написать Python-скрипт, который:

    - подключается к БД любого типа на выбор, например, к PostgreSQL;
    - импортирует необходимые модели данных;
    - принимает имя или идентификатор издателя (publisher), например, через input();
    - выводит построчно факты покупки книг этого издателя.

## Задание 3

Заполнить БД тестовыми данными. Например из JSON-файла.
Возможная реализация: прочитать JSON-файл или создать соотведствующие экземляры моделей и сохранить в БД.

## Рекомендации:

    - параметры подключения к БД следует выносить в отдельные переменные: 
      (логин, пароль, название БД и пр.);
    - загружать значения лучше из окружения ОС, например, через os.getenv();
    - заполнять данными можно вручную или выполнить задание 3.
