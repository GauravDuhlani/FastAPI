from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]


@app.get("/books")
async def read_all_books():
    return {'books': BOOKS}


@app.get("/get-book/{book_author}")
async def get_books_by_author_path_variable(book_author: str):
    books_to_return = []
    for book in BOOKS:
        if book['author'].casefold() == book_author.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/get-book")
async def get_book_by_category_query_parameter(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/get-book/{book_title}")
async def get_book_by_title_path_variable_and_category_query_parameter(book_title: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book['title'].casefold() == book_title.casefold() and \
                book['category'].casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.post("/books/add-book")
async def add_book(new_book=Body()):
    BOOKS.append(new_book)


@app.put("/books/update-book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book


@app.delete("/books/delete-book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break
