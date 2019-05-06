class Duck:
    def __int__(self, num_feathers, num_quacks, color, weight):
        self.num_feathers = num_feathers
        self.num_quacks = num_quacks
        self.color = color
        self.weight = weight

    def quack(self):
        for _ in range(self.num_quacks):
            print("Quacks!")

    def swims(self):
        print("The {} colored duck swims across the pond".format(self.color))

    def molting(self):
        if self.num_feathers > 0:
            self.num_feathers = self.num_feathers - 1
        else:
            print("The Duck is naked, stop trying to make a pillow!")

    def get_num_feathers(self):
        return self.num_feathers

    def get_weight(self):
        return self.weight


donald = Duck(80, 5, "blue", 2.0)
donald.quack()
donald.swims()

for i in range(100):
    donald.molting()
    print(donald.get_num_feathers())
