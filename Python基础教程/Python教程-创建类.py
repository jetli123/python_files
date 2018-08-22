_metaclass_ = type
class Person:

    def setName(self, name):
        self.name = name
        print self.name

    def getName(self):
        return self.name

    def greet(self):
        print "Hello, world! I'm %s." % self.name

foo = Person()
bar = Person()
foo.setName('Luke Skywalker')
bar.setName('Anakin in Skywalker')
foo.greet()
