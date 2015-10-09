class Shoe:
    size = 9.5
    color = "red"

    def put_on(self):
        print("You put on your {} shoes.".format(self.color))

    @classmethod
    def create(cls, description):
        shoe = cls()
        size, color = description.split()
        shoe.size = float(size)
        shoe.color = color
        return shoe

    @staticmethod
    def shoe_rack(shoes):
        for shoe in shoes:
            yield Shoe.create(shoe)



my_shoes = Shoe()
my_shoes.color = "blue"
my_shoes.put_on()

your_shoes = Shoe()
print(your_shoes.color)

Shoe.color = "black"
print(your_shoes.color)

new_shoes = Shoe.create("10.5 orange")
print(new_shoes.size)
new_shoes.put_on()

closet = Shoe.shoe_rack(["10.5 green", "8 brown", "13 yellow"])
for shoe in closet:
    shoe.put_on()
