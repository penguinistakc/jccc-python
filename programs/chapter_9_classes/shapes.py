#!/usr/bin/env python3


class Shape:
    idnumber = 100

    def __init__(self, name):
        self.name = name
        self.id = Shape.idnumber
        Shape.idnumber += 1

    def shapeID(self):
        return self.id

    def myname(self):
        return self.name

    def area(self):
        pass
