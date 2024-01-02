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
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = False

    def double_health_points(self):
        return int(self.health_points) ** 2
        self.fly = True

    def true_in_true_phrase(self, true_phrase):
        return true_phrase in str(self.fly)


class AirHero(SuperHero):

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = False

    def double_health_points(self):
        return int(self.health_points) ** 2
        self.fly = True

    def true_in_true_phrase(self, true_phrase):
        return true_phrase in str(self.fly)


class CosmicHero(SuperHero):

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = False

    def double_health_points(self):
        return int(self.health_points) ** 2
        self.fly = True

    def true_in_true_phrase(self, true_phrase):
        return true_phrase in str(self.fly)


class Villain(CosmicHero):
     people = 'monster'

     def gen_x(self):
         pass

     def crit(self, other_hero):
         other_hero.health_points **= self.damage


earth_hero = EarthHero('Thanos', 'Titan', 'immortality', '168909', 'will destroy this universe', '80089')
air_hero = AirHero('Sky Hero', 'Твой герой', 'непобедимый', '1029384', 'Воздушный защитник', '76567')
cosmic_hero = CosmicHero('Super Star', 'звездун', 'самый быстрый', '298709', 'Галактические герой', '5678')
villain = Villain('Dark hero', 'Владыка Тьмы', 'РАзрушение всего живого', '142536475', 'Ваш конец близок', '456787')

print(f"Никнейм:", earth_hero.nickname)
print(f"Здоровье возведено в квдрат:", earth_hero.double_health_points())
print(f"Ваш урон:", earth_hero.damage)

print(f"Никнейм:", air_hero.nickname)
print(f"Здоровье возведено в квдрат:", air_hero.double_health_points())
print(f"Ваш урон:", air_hero.damage)
print(air_hero.true_in_true_phrase(True))

print(f"Никнейм:", cosmic_hero.nickname)
print(f"Здоровье возведено в квдрат:", cosmic_hero.double_health_points())
print(f"Ваш урон:", cosmic_hero.damage)

villain.crit(air_hero)
print(f"Здоровье {air_hero.name} после атаки врага: {air_hero.health_points}")
