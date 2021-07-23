## Library Management::
import sys
class Lib_Project:

    def __init__(self):
        self.book = {}

    def screen(self):
        print('1:Add Book')
        print('2:display all books')
        print('3:Search a book')
        print('4:Edit')
        print('5:delete')
        
        print('6:Exit')

        m = int(input('enter choice:'))
        return m

    def add_book(self):
        while True:
            bid = int(input('enter book id:'))
            if bid not in self.book:
                break
            print('plz enter unique id')
        bname = input('enter book name:')
        pages = int(input('enter pages:'))

        self.book[bid] = {'name':bname,'pages':pages}

    def display(self):

        print('\t{}\t{}\t{}'.format('ID','Name','Pages'))

        for i in self.book:
            print('\t{}\t{}\t{}'.format(i,self.book[i]['name'],self.book[i]['pages']))

    def search(self):
        bid = int(input('enter book id:'))
        print('\t{}\t{}\t{}'.format('ID','Name','Pages'))
        if bid in self.book:
            print('\t{}\t{}\t{}'.format(bid,self.book[bid]['name'],self.book[bid]['pages']))
        else:
            print('bid not found')

    def edit(self):
        bid = int(input('enter book id:'))

        if bid in self.book:
            print('1:Book name')
            print('2:Pages')

            ch = int(input('enter choice:'))

            if ch==1:
                new_name = input('enter new name:')
                self.book[bid]['name'] = new_name

            elif ch==2:
                new_pages = int(input('enter pages:'))
                self.book[bid]['pages'] = new_pages

            else:
                print('plz enter a valid choice')

        else:
            print('not found')


    def delete(self):
        bid = int(input('enter book id:'))

        if bid in self.book:
            del self.book[bid]
            print('book record deleted')

        else:
            print('not found')
        
        
        
        
        
lib = Lib_Project()

while True:
    k = lib.screen()
    if k==1:
        lib.add_book()

    elif k==2:
        lib.display()

    elif k==3:
        lib.search()

    elif k==4:
        lib.edit()

    elif k==5:
        lib.delete()

    else:
        sys.exit()






        
