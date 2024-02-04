import random
class Human:
    def __int__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.gladness =50
        self.satiety = 50
        self.money = 100

        self.job = job
        self.home = home
        self.csr = car

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(jobs)

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(cars)

    def eat(self):
        if self.home.food <=0:
            self.shopping("food")
        else:
            if self.satiety >=100:
                self.satiety = 100
                return
            self.satiety +=5
            self.home.food -=5

    def work(self):
        if self.car.fuel < 20:
            self.shopping("fuel")
            return
        else:
            self.to_repair()
            return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print("I bought fuel")
            self.money -= 100
            self.car.fuel +=100
        if manage == "food":
            print("I bought food")
            self.money -= 100
            self.home.food += 100
        if manage == "delicacies":
            print("Haarey! Delicious!")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 3

    def clean_home(self):
        self.gladness -= 3
        self.home.mess = 0
    def to_repair(self):
        self.car.strenght += 100
        self.money -= 50

    def days_indexes(self, day):
        day = f" Today the {day} of {self.name}' s life "
        print(f"{day:=^50}", "\n")

        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:=^50}","\n")
        print(f"Money - {self.money}")
        print(f"Satiety - {self.satiety}")
        print(f"Gladness - {self.gladness}")

        home_indexes = "Home indexes"
        print(f"{home_indexes:=^50}","\n")
        print(f"Food - {self.home.food}")
        print(f"Ness - {self.home.ness}")

        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:=^50}","\n")
        print(f"Fuel - {self.car.fuel}")
        print(f"Strength - {self.car.strenght}")

    def is_live(self):
        pass

    def live(self):
        pass

cars = {
    "BW": {"fluel":100, "strenght":100, "consution":8},
    "Opel": {"fluel":60, "strenght":40, "consution":6},
    "Volvo": {"fluel":70, "strenght":150, "consution":8},
    "Ferrari": {"fluel":80, "strenght":120, "consution":14}
}


class Auto:
    def __int__(self, cars):
        self.brand = random.choice(list(cars))
        self.fuel = cars[self.brand]["fuel"]
        self.strenght = cars[self.brand]["strenght"]
        self.consution = cars[self.brand]["consution"]

    def drive(self):
        if self.strenght > 0 and self.fuel > self.consution:
            self.fuel += self.consution
            self.strenght += 1
            return True
        else:
            print("The car cannot move")
            return False

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

jobs = {
    "Java Dev": {"salary":50, "gladness_less":10},
    "Python Dev": {"salary":40, "gladness_less":3},
    "C++ Dev": {"salary":45, "gladness_less":25},
    "Veb Dev": {"salary":37, "gladness_less":5}
}

class Job:
    def __int__(self, jobs):
        self.jobs = random.choice(list(jobs))
        self.salary = jobs[self.jobs]["salary"]
        self.gladness_less=jobs[self.jobs]["gladness_less"]

class Book:
   def __init__(self, title, author, year):
       self.title = title
       self.author = author
       self.year = year
       self.status = "available"


class Library:
   def __init__(self):
       self.books = []

   def add_book(self, book):
       self.books.append(book)

   def remove_book(self, book):
       self.books.remove(book)

   def lend_book(self, book):
       if book.status == "available":
           book.status = "lent"
           print(f"{book.title} by {book.author} has been lent out.")
       else:
           print("Sorry, this book is not available.")

   def return_book(self, book):
       if book.status == "lent":
           book.status = "available"
           print(f"{book.title} by {book.author} has been returned.")
       else:
           print("This book was not lent out.")

library = Library()
book1 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 1997)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book3 = Book("1984", "George Orwell", 1949)
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.lend_book(book1)

library.return_book(book1)

nick = Human("Nick")
kate = Human("Kate")
john = Human("John")

audi = Auto("Audi")
audi.add_passengers( nick, kate, john)

audi.print_passengers_name()
