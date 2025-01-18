import sqlalchemy
from sqlalchemy.orm import sessionmaker

import json
import os

from models import Publisher, Book, Shop, Stock, Sale, create_tables

file_name = 'tests_data.json'
path = os.getcwd()
file_path = path + '\\' + file_name
system = 'postgresql'
login = 'postgres'
password = 'postgres'
host = 'localhost'
port = 5432
db_name = "book_shop"

DSN = f'{system}://{login}:{password}@{host}:{port}/{db_name}'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()


if __name__ == '__main__':
    
    # Импорт данных в БД из внешнего источника (json-файл)
    # Мой вариант
    with open(file_path, 'r') as json_db:
        data = json.load(json_db)

        for iter in data:
            if iter['model'] == 'publisher':
                session.add(Publisher(id=iter["pk"], name=iter["fields"]["name"]))
            elif iter['model'] == 'book':
                session.add(Book(id=iter["pk"], title=iter["fields"]["title"], id_publisher=iter["fields"]["id_publisher"]))
            elif iter['model'] == 'shop':
                session.add(Shop(id=iter["pk"], name=iter["fields"]["name"]))
            elif iter['model'] == 'stock':
                session.add(Stock(id=iter["pk"], id_book=iter["fields"]["id_book"], id_shop=iter["fields"]["id_shop"], count=iter["fields"]["count"]))    
            elif iter['model'] == 'sale':
                session.add(Sale(id=iter["pk"], price=iter["fields"]["price"], date_sale=iter["fields"]["date_sale"], id_stock=iter["fields"]["id_stock"], count=iter["fields"]["count"]))
        
        session.commit()
        
    # Импорт данных в БД из внешнего источника (json-файл)
    # Вариант Netology ----------------------------------*
    # with open('fixtures/tests_data.json', 'r') as fd:
    #     data = json.load(fd)
    #     for record in data:
    #         model = {
    #             'publisher': Publisher,
    #             'shop': Shop,
    #             'book': Book,
    #             'stock': Stock,
    #             'sale': Sale,
    #         }[record.get('model')]
    #         session.add(model(id=record.get('pk'), **record.get('fields')))
    #     session.commit()
            
print()
#  Получение имени или идентификатора издателя (publisher).
#  Вывод построчно покупок книг этого издателя:
#     -Книга-Магазин-Стоимость-Дата продажи.        
publisher_name = input('Ведите имя или идентификатор издателя: ') 
# 1 - O’Reilly
# 2 - Pearson
# 3 - Microsoft Press
# 4 - No starch press
print()

if publisher_name.isnumeric():
    for iter in session.query(Book.title,
                              Shop.name,
                              Sale.price,
                              Sale.date_sale,
                              Publisher.name
                        ).join(Publisher).join(Stock).join(Shop).join(Sale).filter(
                              Publisher.id == int(publisher_name)    
                              ).all():
        print(f'({iter[4]}) -> Книга: "{iter[0]}", Магазин: "{iter[1]}", Стоимость: {iter[2]}, Дата продажи: {iter[3]}.')
        print()
else:
    for iter in session.query(Book.title,
                              Shop.name,
                              Sale.price,
                              Sale.date_sale,
                              Publisher.name
                        ).join(Publisher).join(Stock).join(Shop).join(Sale).filter(
                              Publisher.name.like(f'%{publisher_name}%')    
                              ).all():
        print(f'({iter[4]}) -> Книга: "{iter[0]}", Магазин: "{iter[1]}", Стоимость: {iter[2]}, Дата продажи: {iter[3]}.')
        print()


    session.close()
    