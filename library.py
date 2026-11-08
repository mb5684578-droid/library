print("hello in our library")
books = []
print("1 to add books")
print("2 to view all books")
print("3 to searck book ")
print("4 to borrow book ")
print("5 to return book")
print("6 to delete book ")
print('7 to exit ')
while True :
   
    process=int(input("what is ur process :"))
    if process==1 :
        title=input("enter ur title :")
        author=input("enter ur author :")
        copies=int(input("enter ur copies"))
        book={             

        "title" :title ,
        "author" :author ,
        "copies" : copies
        }
        books.append(book)

    elif process==2 :
       if len(books) == 0 :
           print("no avaliable books")
       else :
           for book in books :
               print("title :" , book["title"])
               print("author :" ,book ["author"])
               print("copies :" ,book ["copies"])
    elif process==3 :
        search=input("enter ur book title")
        found = False
        for book in books :
          if book["title"].lower() ==search.lower() :
            print("book found")
            print('title:' , book["title"])
            print("author" , book["author"])
            print("copies" , book["copies"])
            found = True
    elif process==4 :
        book_name=input("book ur to borrow it: ")
        for book in books :
            if book["title"] == book_name :
                print("title:" , book["title"])
                print("author:" , book ["author"])
                print("copies" , book["copies"])  
        if found == False :
                print("book not found")
    elif process==5 :
        search_borrow= input("enter ur book : ")
        for book in books :
          if book["title"] == book_name :
              print("title:" , book["title"])
              print("author:" , book ["author"])
              print("copies" , book["copies"]) 
              book["copies"]-=1 
    elif process ==6 :
        return_book=input("enter ur book :")
        for book in books :
               if book["title"] == book_name :
                      print("title:" , book["title"])
                      print("author:" , book ["author"])
                      print("copies" , book["copies"]) 
                      book["copies"]+=1
    elif process == 7 :
        break
    else :
        print("invalid c")
