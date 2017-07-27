#databases
#Structured Query Language-SQL
#essential in lots of job situations
#object oriented programming
class PartyAnimal: #moment of construction
    x = 0 #each PartyAniaml object has a bit of data

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)
an = PartyAnimal() #construt a partyanimal object and store in an variable
an.party() #this is equal to PartyAniaml.party(an)
an.party()
an.party()

#how object are built and thrown away
#object are created, used and discarded
#construtor and destructor
#the construtor and destructor are optional, The constructor is typically used
#to set up variables and the destructor is seldom used.
class PartyAniaml:
    x = 0
    name = ""
    def __init__(self, z):
        self.name = z
        print(self.name, "constructed")
    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)
s = PartyAniaml("Sally")
s.party()

j = PartyAniaml("Jim")
j.party()
s.party()

#Object inheritance
#When we make a new class- We can reuse an existing class and inherit all
#thed capabilities of an existing class and then add our own little bit to make
#our new class
#subclasses


class FootballFan(PartyAniaml):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)

j = FootballFan("Jim")
j.party()
j.touchdown()
