class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def printpeople(self):
        print(self.nickname, 'is hero')

    def __mul__(self, other):
        print("Здоровье героя удвоено:")
        return int(self.health_points)*2

    def __len__(self):
        print("Длина коронной фразы:")
        return len(self.catchphrase)

    def __str__(self):
        return 'nickname='+self.nickname, 'superpower='+self.superpower, 'health points='+self.health_points


hero = SuperHero('subziro', 'sub', 'hz', '100', 'will be back')
hero.printpeople()
print(hero.__mul__(2))
print(hero.__len__())
print(hero.__str__())


class EarthHero(SuperHero):
    def damage(self):
        print(False)

    def fly(self):
        print(False)

    def run(self):
        print('Здоровье героя возведено в квадрат:', int(self.health_points)**2)


thanos = EarthHero('Thanos', 'Titan', 'immortality', '168909', 'will destroy this universe', )
# print(thanos.__mul__(2))
# print(thanos.__len__())
# print(thanos.__str__())
thanos.run()
