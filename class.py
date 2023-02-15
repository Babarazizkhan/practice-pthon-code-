class Human:
    def __init__(self, n, o):   # this is the properties of the class in function
        self.name = n
        self.occupation = o

    def do_work(self):
        if self.occupation == "tenis star":
           print(self.name,"playr of the tenis")   # this is the method of class which we define
        elif self.occupation == "actor ":
          print(self.name, "shot a  film ")

    def speaks(self):
       print(self.name,"says how are you")

tom = Human("tom crouse","actor")
tom.do_work()
tom.speaks()

maria = Human("maria sharapora","tenis star")
maria.do_work()
maria.speaks()