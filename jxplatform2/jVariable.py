class jVariable:

    def __init__(self,variable):
        self.modifier = variable.split("#")[0]
        self.name = (variable.split("#")[1]).split("@")[0]
        self.type = (variable.split("#")[1]).split("@")[1]

    def __repr__(self):
        return f"{self.modifier}#{self.type}@{self.name}"

    def getModifier(self):
        return self.modifier
    def getName(self):
        return self.name
    def getType(self):
        return self.type