class ParentClass(object):

    def __init__(self):
        self.x = [1,2,3]

    def test(self):
        print 'Im in parent class'


class ChildClass(ParentClass):

    def test(self):
        super(ChildClass,self).test()
        print "Value of x = ". self.x


x = ChildClass()
x.test()
