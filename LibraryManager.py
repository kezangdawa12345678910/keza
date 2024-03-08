 # Initialize empty lists,set, and dictionary 
books_list =[]
authors_set = set()
books_dict ={}

#add books

books_list.append("python progamming")
authors_set.add ("jhon smith")
books_dict["python progamming"]="jhon smith"

books_list.append("data structures and algorithms")
authors_set.add("jane doe")
books_dict["data and structures and algorithms"]="jane doe"

books_list.append("machine learning bascis")
authors_set.add("alice jhonson")
books_dict["machine learning bascis "]="alice jhonson"

#search for a book

search_title=input("enter the title of the book to search:")
if search_title in books_list:
    print(f"book found! author:{books_dict[search_title]}")
else:
    print("sorry! book not found!")

#display all books
print("list of books:")
for book in books_list:
    print(book)

# remove a book
remove_title=input("enter the title of the book to remove or else enter skip:")
if remove_title in books_list:
    remove_author=books_dict[remove_title]
    books_list.remove(remove_title)
    authors_set.remove(remove_author)
    del books_dict[remove_title]
    print("book removed successfully!")
    print("books avaiable:",books_list)
else:
    print("book not found!")