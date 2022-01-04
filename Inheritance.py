class Animal:
    """Animal class"""
    def __init__(self, name, age, birthday):
        self.__name = name
        self.__age = age
        self.__birthday = birthday
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
        
    @property
    def age(self):
        return self.__age 
        
    @age.setter
    def age(self, age):
        self.__age = age
    
    @property
    def birthday(self):
        return self.__birthday
    
    @birthday.setter
    def birthday(self, birthday):
        self.__birthay = birthday
        
    def move(self):
        print('Moving....')
        
class Fish(Animal):
    """Fish class, inherits from Animal"""
    def __init__(self, name, age, birthday, freshwater):
        super().__init__(name, age, birthday)
        self.___freshwater = freshwater
        
    @property
    def freshwater(self):
        return self.___freshwater
       
    @freshwater.setter        
    def freshwater(self, freshwater):
        self.___freshwater = freshwater

class Snake(Animal):
    """Snake class, inherits from Animal"""
    def __init__(self, name, age, birthday, venomous):
        super().__init__(name, age, birthday)
        self.__venomous = venomous
    
    @property
    def venomous(self):
        return self.__venoumous
    
    @venomous.setter
    def venomous(self, venomous):
        self.__venomous = venomous
        
class Person(Animal):
    """Person class, inherits from Animal"""
    def __init__(self, name, age, birthday, job, married, address, phone):
        super().__init__(name, age, birthday)
        self.__job = job
        self.__married = married
        self.__address = address
        self.__phone = phone
        
    @property
    def job(self):
        return self.__job
    
    @job.setter
    def job(self, job):
        self.__job = job
    
    @property
    def married(self):
        return self.__married
    
    @married.setter
    def married(self, married):
        self.__married = married
    
    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

class Book:
    """Book class"""
    def __init__(self, title, author, length):
        self.__title = title
        self.__author = author
        self.__length = length
        
    def open_book():
        pass
    
    def close_book():
        pass
    
    def read_book():
        pass
    
class Textbook(Book):
    """Textbook class, inherits from Book class"""
    def __init__(self, title, author, length, subject):
        super().__init__(title, author, length)
        self.__subject = subject
    
    @property
    def subject(self):
        return self.__subject
    
    @subject.setter 
    def subject(self, subject):
        self.__subject = subject
        
class AddressBook(Book):
    """AddressBook class, inherits from Book class"""
    def __init__(self, title, author, length, contact):
        super().__init__(title, author, length)
        self.__contact = contact
        
    @property
    def contact(self):
        return self.__contact
    
    @contact.setter
    def contact(self, contact):
        self.__contact = contact
        
    def write():
        pass
    
class Vehicle:
    """Vehicle class"""
    def __init__(self, make, model, year, owner):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__owner = owner
        
    def move():
        print('Moving...')

class Car(Vehicle):
    """Car class, inherits from Vehicle class"""        
    def __init__(self, make, model, year, owner, electric):
        super().__init__(make, model, year, owner)
        self.__electric = electric
        
    @property
    def electric(self):
        return self.__electric
    
    @electric.setter
    def electric(self, electric):
        self.__electric = electric
        
class Bicycle(Vehicle):
    """Bicycle class, inherits from Vehicle class"""
    def __init__(self, make, model, year, owner, basket):
        super().__init__(make, model, year, owner)
        self.__basket = basket
        
    @property
    def basket(self):
        return self.__basket
    
    @basket.setter
    def basket(self, basket):
        self.__basket = basket
        
class Boat(Vehicle):
    """Boat class, inherits from Vehicle class"""
    def __init__(self, make, model, year, owner, sailboat):
        super().__init__(make, model, year, owner)
        self.__sailboat = sailboat
        
    @property
    def sailboat(self):
        return self.__sailboat
    
    @sailboat.setter
    def sailboat(self, sailboat):
        self.__sailboat = sailboat
        
class HotAirBalloon(Vehicle):
    """HotAirBalloon class, inherits from Vehicle class"""
    def __init__(self, make, model, year, owner, inflated):
        super().__init__(make, model, year, owner)
        self.__inflated = inflated
        
    @property
    def inflated(self):
        return self.__inflated 
    
    @inflated.setter
    def inflated(self, inflated):
        self.__inflated = inflated