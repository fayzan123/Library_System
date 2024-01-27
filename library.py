
allBooks = [
                ['9780596007126',"The Earth Inside Out","Mike B",2,['Ali']],
                ['9780134494166',"The Human Body","Dave R",1,[]],
                ['9780321125217',"Human on Earth","Jordan P",1,['David','b1','user123']]
           ]
#initializes list for all books


borrowedISBNs = []
#initializes list for borrowed books by ISBN

def start(): #start function for program, runs all functions
    printMenu() #runs printmenu function
    makeSelection() #runs makeSelection function

def printMenu(): #prints out start menu for user
    print('\n######################')
    print('1: (A)dd a new book.')
    print('2: Bo(r)row books.')
    print('3: Re(t)urn a book.')
    print('4: (L)ist all books.')
    print('5: E(x)it.')
    print('######################\n')
def makeSelection(): #function that allows user to select option based on number or letter, runs corressponding function
    selection = input("Your selection> ") #asks user to input selection
    selection = selection.lower() #makes selection lower so input is case insensitive
    if selection == "1": #conditionals for if user selects first option (add a book)
        addNewBook()
    elif selection == "a":
        addNewBook()
    elif selection == "2": #conditionals if user selects second option (borrow a book)
        borrowBooks()
    elif selection == "r":
        borrowBooks()
    elif selection == "3": #conditionals if user selects third option (return a book)
        returnBooks()
    elif selection == "t":
        returnBooks()
    elif selection == "4": #conditionals if user selects fourth option (list all books)
        listAllBooks()
    elif selection == "l":
        listAllBooks()
    elif selection == "5": #conditionals if user selects fourth option (exit)
        exitLibrary()
    elif selection == "x":
        exitLibrary()
    else:
        print("Wrong selection! please select a valid option")
        start()
def addNewBook(): #define funciton for adding new book
    bookName = input("Book name> ") #asks user to input name of book
    global allBooks  # initalilzaes  global variable for list of all books
    while "*" in bookName or "%" in bookName: #next two while loops check if * or % in bookname, if so, notiofy user name is invalid and repeat till valid name given
        print("Invalid book name!")
        bookName = input("Book name> ")
    author = input("Author name> ") #ask user for authro name
    edition = input("Edition> ") #ask user for book edition
    while not edition.isnumeric(): #if user enters not a number, notify invalidity and repeatedly ask for number edition
        edition = input("Edition invalid. Please enter valid edition number> ")
    edition = int(edition) #convert edtion to interger
    ISBN = input("ISBN> ") #ask user to input isbn
    while len(ISBN) != 13: #checks if isbn is 13 characters, if not, user must re enter isbn until condition met
        print("Invalid ISBN!")
        ISBN = input("ISBN> ")
    while not ISBN.isnumeric(): #checks if isbn has letters in it, if so, repeatedly ask user for isbn till condition is met
        print("Invalid ISBN!")
        ISBN = input("ISBN> ")
    for isbnCheck in allBooks:
        curISBN = isbnCheck[0]
        if curISBN == ISBN:
            print("Duplicate ISBN is found! Cannot add the book")
            start()
    isbnList = [] #creates list for the given isbn in order to easily iterate through, and multiply
    for i in ISBN:
        isbnList.append(i) #appends all numebrs of isbn to list
    summationOne = 0 #initialises counter for all numbers multiplied by 1
    summationTwo = 0 #initialises counter for all numbers multiplied by 3
    for num in isbnList[0::2]: #interates throuhg every other number from first index, and adds it to sumOne
        num = int(num)
        summationOne += num
    for otherNum in isbnList[1::2]: #interates through all number from second index, multiplies them by 3, and adds them to sumtwo
        otherNum = int(otherNum)
        otherNum = otherNum * 3
        summationTwo += otherNum
    totalSum = summationOne + summationTwo #gets total sum of all numbers
    if totalSum % 10 == 0: #checks if sum of isbn is divisible by 10, if so isbn is valid, and book is added to allBooks
        oneNewBook = [ISBN, bookName, author, edition, []]
        print("A new book is added successfully")
        allBooks.append(oneNewBook)
        #print(allBooks)
        start() #returns to main menu
    elif totalSum % 10 != 0: #if isbn is not divisible by 10, return to main menu
        print("Invalid ISBN!")
        start()
def removeWhiteSpace(string): #function that removes whitespace by replacing whiteapces with empty string
    return string.replace(" ", "")
def borrowBooks(): #define function for borrowing books
    borrowerName = input("Enter the borrower name> ") #asks for borowwer name
    searchTerm = input("Search term> ") #asks for search temr ot find book
    global allBooks #calls list of all books into this function
    global borrowedISBNs #calls list of borrowed isbns in to this function
    matchingBooks = []
    for val in allBooks: #iterates through every list in the list of all books
        bookName = val[1] #indexes the second value in each list, as this is where the bookname is
        lowerNames = bookName.lower() #creates variable that makes all booknames lowercase
        formattedName = removeWhiteSpace(lowerNames) #calls function to remove white space in string to make searchTerm easier
        bookNameList = lowerNames.split() #creates list of each word in the book name to be able to match first word for "%" searchterm
        searchTerm = searchTerm.lower() #lowercases the searchterm to maek conditionals case insensitive
        if searchTerm[-1] == "*": #conditional to check if user wants to look for "contains"
            validTerm = searchTerm[:-1] #creates variable for searchterm without *
            if validTerm in formattedName:
                matchingBooks.append(bookName)
            #else:
                #print("fail")
        elif searchTerm[-1] == "%":
            validTerm = searchTerm[:-1]
            if validTerm == bookNameList[0]:
                matchingBooks.append(bookName)
            #else:
                #print("fail")
        else:
            if searchTerm == lowerNames:
                matchingBooks.append(bookName)
    if len(matchingBooks) == 0:
        print("no books found!")
        start()
    for term in allBooks:
        borrowerList = term[-1] #creates variable for list of borrowers
        origBook = term[1] #creates variable for books in allBooks
        ISBN = term[0] #creates varaible vor ISBNs is allBooks
        for book in matchingBooks: #for loop to iterate through books in search
            if book == origBook: #checks when book from search list matches book from allBooks
                if ISBN in borrowedISBNs: #if ISBN of book in search list is already borrowed, doenst allow borrowing
                    print('"' + str(origBook) + '"', "is  already borrowed!")
                else: #otherwise, allows user to borrow book
                    print("Sucessfully borrowed", '"' + str(origBook) + '"')
                    #print('-"' + str(origBook) + '"', "is borrowed!")
                    borrowerList.append(borrowerName) #adds name of borrower to list of borrower history
                    borrowedISBNs.append(ISBN) #adds isbn of borrowed book to list of borrowed isbns
    start() #returns to main menu
                    #print(borrowedISBNs)
    #print(allBooks)
        #print(borrowerList)
    #print(allBooks)
    #print(borrowedISBNs)
def returnBooks(): #define function for returning books
    global allBooks #calls lsit of all books
    global borrowedISBNs #callas lsit of borrowed ISBNs
    returnISBN = input("ISBN> ") #gets user unput fo ISBN they wish to return
    for book in allBooks: #iterate throuhg all lists in allBooks thoruhg variable "book"
        if returnISBN == book[0]: #check if the isbn exists in list of allbooks
            bookName = book[1] #creates variable for associated book name if given ISBN is in list of all books
    if returnISBN in borrowedISBNs: #conditional to check if book is already borrowed
        borrowedISBNs.remove(returnISBN) #if book is borrowed, remove returned ISBN from list of borrowed isbns
        print('"' + str(bookName) + '"', "is returned") #notify user that book is returned
        start() #return to main menu
    else: #if given isbn is not in list of books
        print("No book is found!") #notify user so
        start() #return to start menu



def listAllBooks():
    global allBooks
    global borrowedISBNs
    i = 0
    while i < len(allBooks):
        for val in allBooks:
            print("\n" + "-"*15, "\n")
            ISBN = val[0]
            if ISBN in borrowedISBNs:
                print("[Unavailable]")
            else:
                print("[Available]")
            print(val[1], "-", val[2])
            print("E:", val[3], "ISBN:", ISBN)
            print("Borrowed by:", val[-1])

            i += 1
    start()

def exitLibrary():
    print("$"*8, "FINAL LIST OF BOOKS", "$"*8)
    global allBooks
    global borrowedISBNs
    i = 0
    while i < len(allBooks):
        for val in allBooks:
            print("\n" + "-" * 15, "\n")
            ISBN = val[0]
            if ISBN in borrowedISBNs:
                print("[Unavailable]")
            else:
                print("[Available]")
            print(val[1], "-", val[2])
            print("E:", val[3], "ISBN:", ISBN)
            print("Borrowed by:", val[-1])

            i += 1
    exit()




start()






