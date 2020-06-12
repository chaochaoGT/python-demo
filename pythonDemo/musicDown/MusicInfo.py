class Musicinfo():

    def __init__(self, input, name, type, page):
        self.input = input
        self.name = name
        self.type = type
        self.page= page

    def __str__(self):
        return '''input=%s,name=%s,type=%s,page=%d'''(self.input,self.name,self.type,self.page)
