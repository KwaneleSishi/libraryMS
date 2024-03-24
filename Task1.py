""" Task 1: Data Structures Implementation (lists and data frames for managing books and 
members).	 
Initialize two data structures to keep track of books and members  both represented as lists. The system features two functions (You must create these functions): add_book and add_member. The add_book function takes three parameters (book_id, title, author, status) and appends a new book dictionary to the books list. The add_member function, on the other hand, requires two parameters (member_id, name) and appends a new member dictionary to the members list. Each member dictionary includes an empty list for borrowed_books to track the IDs of books each member has borrowed. 
Sequence hint: initialize two variables as lists, then create two functions as per the above requires. An example of the appending part of the question is as follows: 
books.append({ 
        "book_id": book_id, 
        "title": title, 
        "author": author     }) 
You must use the same procedure for all appends! 
  """
# Initializing empty lists for books and members
books = []
members = []

#The add_book function takes three parameters (book_id, title, author, status) and appends a new book dictionary to the books list
def add_book(book_id, title, author, status):

    books.append({
        "book_id": book_id,
        "title": title,
        "author": author,
        "status": status
    })

#The add_member function, on the other hand, requires two parameters (member_id, name) and appends a new member dictionary to the members list
def add_member(member_id, name):

    members.append({
        "member_id": member_id,
        "name": name,
        "borrowed_books": []  # Empty list to track borrowed books
    })

#TASK 1A 
"""Suppose you use the system to add a book titled "Python Programming" written by Jacob Zuma with a book_id of 2024001, and a member named Anelisa Maleka with a member_id of 1. How would these additions reflect in the books and members lists, and what would the output look like if you printed both lists immediately after these additions? 
Hint: call the functions and write a print statement for them 
"""
#Calling the Functions
add_book(2024001,"Python Programming","Jacob Zuma", "Available")
add_member(1,"Anelisa Maleka")

#Print Statements
print("Task 1A Output:")
print("Books:")
print(books)
print("\nMembers:")
print(members)


#Task 1B: 
#Rewrite the entire task 1 and task 1B without using parameters and arguments in your functions
books = []
members = []
def add_book():
    books.append({
        "book_id": 2024001,
        "title": "Python Programming",
        "author": "Jacob Zuma",
        "status": "available"
    })

def add_member():
    members.append({
        "member_id": 1,
        "name": "Anelisa Maleka",
        "borrowed_books": []
    })

add_book()
add_member()

print("\nTask 1B Output:")
print("Books:")
print(books)
print("\nMembers:")
print(members)


#Task 1 C: 
#Rewrite the entire task 1B without using functions 
books = [{
    "book_id": 2024001,
    "title": "Python Programming",
    "author": "Jacob Zuma",
    "status": "available"
}]

members = [{
    "member_id": 1,
    "name": "Anelisa Maleka",
    "borrowed_books": []
}]

print("\nTask 1C Output:")
print("Books:")
print(books)
print("\nMembers:")
print(members)

#Task 1 D: 
#Rewrite the entire Task 1 C using Data frames instead of lists. 
import pandas as pd
books_data={
        'book_id':[2024001],
        'title':["Python Programming"],
        'author':["Jacob Zuma"],
        'status':["Available"]
}
books_df=pd.DataFrame(books_data)

members_data={
          'member_id':[1],
          'name':["Anelisa Maleka"],
          'borrowed_books':[[]] ## Explicitly specifying an empty list
}
members_df=pd.DataFrame(members_data)

print("\nTask 1D Output:")
print("Books:")
print(books_df)
print("\nMembers:")
print(members_df)










