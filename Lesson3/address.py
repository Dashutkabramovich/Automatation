class Address:
    index = "000000"
    city = "name"
    street = "name"
    home_num = "00"
    flat_num = "00"

    def __init__(self, index, city, street, home_num, flat_num):
        self.i = index
        self.c = city
        self.s = street
        self.h = home_num
        self.an = flat_num

    def __init__(self, brend, model, num):
        self.brend = brend
        self.model = model
        self.number = num
