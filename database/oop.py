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
