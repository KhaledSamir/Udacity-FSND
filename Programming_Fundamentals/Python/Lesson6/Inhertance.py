class Parent():

    """ Parent Class """

    def __init__(self, firstname, lastname):
        print 'Parent constructor called'
        self.firstname = firstname
        self.lastname = lastname

    def showname(self):
        print self.firstname + ' ' + self.lastname


class Child(Parent):

    def __init__(self, firstname, lastname, grade):
        print 'Child constructor called'
        Parent.__init__(self, firstname, lastname)
        self.grade = grade

    def showname(self):
        print str(self.grade)
        print self.firstname
        print self.lastname


kid = Child('Mohammed', 'Ahmed', 5)

print kid.showname()