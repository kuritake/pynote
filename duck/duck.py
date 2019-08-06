#duck typing(proccess procedure of main routine.)
def say(kenousuihito):
    kenousuihito.confess()
    
#HageClass
class Hage:
    def __init__ (self):
        self.status = "hage"
    def confess(self):
        print("I'm a perfect hage.")
        print("-------------------")

#WakahageClass(inheritance:Hage)
class Wakahage(Hage):
    def confess(self):
        print("I'm a perfect young hage.")
        print("-------------------")

class Zura:
    def __init__ (self):
        self.status = "zura"        
    def confess(self):
        print("It's not my natural hair.")
        print("So I'm not a hage.")
        print("-------------------")

#Experiment "duck typing" .feat Hage
#class "Zura" act confess method in spite of not inheritting Hage class.
if __name__ == "__main__":
    pikkaOne = Hage()
    pikkaTwo = Wakahage()
    pikkaThree = Zura()

    say(pikkaOne)
    say(pikkaTwo)
    say(pikkaThree)


#Nomally activate Hages confess method.
"""
if __name__ == "__main__":
    pikkaOne = Hage()
    pikkaTwo = Wakahage()
    pikkaThree = Zura()

    pikkaOne.confess()
    pikkaTwo.confess()
    pikkaThree.confess()
"""
