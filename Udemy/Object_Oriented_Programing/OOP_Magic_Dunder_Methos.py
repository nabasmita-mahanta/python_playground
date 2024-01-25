class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'{self.title} by {self.author}'

    def __len__(self):
        return self.pages


b = Book('Python Rocks', 'Jose', 200)

print(b)
print(len(b))

# NOTE : Use Del to Delete the book(referred object) from the memory ex del b


