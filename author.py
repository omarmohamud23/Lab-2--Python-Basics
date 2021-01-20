class Author:
    def __init__(self, name):
        self.name = name
        self.books = set()

    def publish(self, title):
         self.books.add(title)

    def __str__(self):
        if self.books:
            titles = ', '.join(self.books)
        else:
            titles = 'No books published'
        return f'{self.name}. Books:{titles}' 

def main():

    #authors getting added with their books
    Shakespeare = Author('William Shakespeare')
    Shakespeare.publish('Hamlet')
    Shakespeare.publish('Macbeth')
    Shakespeare.publish('Othello')
    print(Shakespeare)

    Angelou = Author('Maya Angelou')
    Angelou.publish('And still i rise')
    Angelou.publish('I shall not be moved')
    Angelou.publish('Letter to my daughter')
    print(Angelou)
    
    Omar = Author('Omar')
    print(Omar)

main() 
