#encoding:utf-8
class father():
    fatherName=None
    fatherAge=None
    def getFatherInfo(self):
        print "father's name %s and father's age %s "%(self.fatherName ,self.fatherName)
class son(father):
    def __init__(self,name,age):
        self.fname=name
        self.fage=age
        print self.fname
        print self.fage
    @classmethod
    def class_son(cls):
        print 'I am son'
    def father_name(self):
        print ("my fatehr's name is %s" %self.fname)
    @property
    def info(self):
        info="my fatehr's name is %s , my father's age is %s"%(self.fname ,self.fage)
        print info
son1=son('yanzhenxing','18')
son1.father_name()
son.class_son()
son1.info
son1.getFatherInfo()
father1=father()
father1.getFatherInfo()
