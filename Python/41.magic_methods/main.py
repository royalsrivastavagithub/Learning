# double undersroce methods are also called magic methods

class Book:
    def __init__(self,title,author,num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        # this method is called when we want to get a string representation of the object
        return f"{self.title} by {self.author}"

    def __len__(self):
        # this method is called when we want to get the length of the object
        return self.num_pages

    def __eq__(self,other):
        # this method is called when we want to check if two objects are equal
        return self.title == other.title and self.author == other.author
    
    def __gt__(self,other):
        # this method is called when we want to check if an object is greater than another one
        return self.num_pages > other.num_pages
    
    def __lt__(self,other):
        # this method is called when we want to check if an object is less than another one
        return self.num_pages < other.num_pages
    
    def __add__(self,other):
        # this method is called when we want to add two objects
        return self.num_pages + other.num_pages
    
    def __contains__(self,word):
        # this method is called when we want to check if an object contains a specific value
        return word in self.title

book1 = Book("The Alchemist","Paulo Coelho",208)
book2 = Book("Harry Potter","J.K Rowling",223)
book3 = Book("The Great Gatsby","F. Scott Fitzgerald",180)
book4 = Book("The Great Gatsby","F. Scott Fitzgerald",180)

# print the string representation of book1
print(book1)

# print the string representation of book2
print(book2)

# check if book3 is equal to book4
print(book3 == book4)

# check if book1 is greater than book2
print(book1 > book2)

# check if book1 is less than book2
print(book1 < book2)

# add the number of pages of book1 and book2
print(book1 + book2)

# check if the word "The" is in the title of book1
print("The" in book1)







