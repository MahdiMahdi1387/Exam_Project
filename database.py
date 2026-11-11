from sqlalchemy import create_engine, Column, INTEGER, String
from sqlalchemy.orm import declarative_base, sessionmaker
import requests as rq
from bs4 import BeautifulSoup as bs

engine = create_engine('sqlite:///Bookdata.db')
engine.connect()

Base = declarative_base()

class Book(Base):
    __tablename__ = 'booksinfo'

    id = Column(INTEGER, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    price = Column(String, nullable=False)
    image = Column(String, nullable=False, unique=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session_local = Session()


def info_print(mode: int) -> None:
    '''this function print a information for the items in the database in three modes.'''

    if mode is None:
        raise ValueError('mode of info_print can\'t be None')

    if mode == 1:
        print('=' * 30)
        first_book = session_local.query(Book).filter_by(id=1).first()

        if first_book:
            print(f'id = {first_book.id}')
            print(f'name = {first_book.name}')
            print(f'price = {first_book.price}')

        print('=' * 30)
    if mode == 2:
        print('=' * 30)
        two_first_books = session_local.query(Book).filter(Book.id < 3).all()

        i = 1
        if two_first_books:
            for item in two_first_books:
                print(f'id = {item.id}')
                print(f'name = {item.name}')
                print(f'price = {item.price}')
                if i != 2:
                    print('-' * 30)
                i += 1

        print('=' * 30)
    if mode == 5:
        print('=' * 30)
        all_books = session_local.query(Book).all()

        i = 1
        if all_books:
            for item in all_books:
                print(f'id = {item.id}')
                print(f'name = {item.name}')
                print(f'price = {item.price}')
                if i != len(all_books):
                    print('-' * 30)
                i += 1

        print('=' * 30)


if __name__ == '__main__':
    #################################################################

    url = 'https://books.toscrape.com/'
    response = rq.get(url)
    soup = bs(response.text, 'html.parser')

    cards = soup.select('li.col-xs-6.col-sm-4.col-md-3.col-lg-3')
    print('part 1 done.', cards, sep='\n')
    #################################################################

    for card in cards:
        name: str = card.select_one('h3').get_text()
        if name is None:
            continue
        price: str = card.select_one('p.price_color').get_text()
        if price is None:
            continue
        image = 'https://books.toscrape.com/' + card.select_one('img.thumbnail').get('src')
        if image is None:
            continue

        book = Book(name=name, price=price, image=image)
        session_local.add(book)
        print('Done!')
    session_local.commit()
    