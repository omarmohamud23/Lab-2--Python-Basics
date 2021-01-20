#author is created as class
class Author:
    def __init__(self, name):
        self.name = name
        self.books = set()

    def publish(self, title):
   

        #no duplicate allowed
        if  title in self.books:
             print('No duplicate allowed')
        #books gets added after checking for no duplicate
        else:
              self.books.add(title)
                    

    def __str__(self):
        if self.books:
            titles = ', '.join(self.books)
        else:
            titles = 'No books published'
        return f'{self.name}. Books:{titles}' 


def main():
   
   #author and his books
    Orwell = Author('George Orwell')
    Orwell.publish('Animal Farm')
    Orwell.publish('Burmese Days')
    Orwell.publish('Nineteen Eighty Four')
    Orwell.publish('Nineteen Eighty Four')
    print(Orwell)

    Omar = Author('Omar')
    print(Omar)



main()
