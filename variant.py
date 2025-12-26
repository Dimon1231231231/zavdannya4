import random

class Character:
    def __init__(self, name, health, max_attack, max_defense):
        self.name = name
        self.health = health
        self.max_attack = max_attack
        self.max_defense = max_defense

    def generate_attack(self):
        return random.randint(1, self.max_attack)

    def generate_defense(self):
        return random.randint(1, self.max_defense)

    def take_damage(self, damage):
        if damage > 0:
            self.health -= damage
            if self.health < 0:
                self.health = 0

    def is_alive(self):
        return self.health > 0

class Hero(Character):
    def __init__(self, name, hero_type):
        if hero_type == "sword":
            super().__init__(name, 100, 20, 25)  # Гарний захист
        elif hero_type == "bow":
            super().__init__(name, 100, 30, 15)  # Ефективне ураження
        else:
            raise ValueError("Невірний тип героя")

class Dragon(Character):
    def __init__(self):
        super().__init__("Fire Dragon", 150, 25, 20)

def get_hero_action():
    while True:
        action = input("Оберіть дію (attack/defend): ").lower()
        if action in ["attack", "defend"]:
            return action
        print("Невірний вибір. Спробуйте знову.")

def battle():
    hero_name = input("Введіть ім'я героя: ")
    hero_type = input("Оберіть тип (sword/bow): ").lower()
    hero = Hero(hero_name, hero_type)
    dragon = Dragon()

    round_num = 1

    while hero.is_alive() and dragon.is_alive():
        print(f"\nРаунд {round_num}")
        print(f"{hero.name} HP: {hero.health}")
        print(f"{dragon.name} HP: {dragon.health}")

        hero_action = get_hero_action()
        dragon_action = random.choice(["attack", "defend"])

        print(f"{hero.name} обирає {hero_action}")
        print(f"{dragon.name} обирає {dragon_action}")

        if hero_action == "attack":
            hero_value = hero.generate_attack()
        else:
            hero_value = hero.generate_defense()

        if dragon_action == "attack":
            dragon_value = dragon.generate_attack()
        else:
            dragon_value = dragon.generate_defense()

        if hero_action == "attack" and dragon_action == "attack":
            print(f"Атака героя: {hero_value}, Атака дракона: {dragon_value}")
            if hero_value == dragon_value:
                damage = hero_value // 2
                hero.take_damage(damage)
                dragon.take_damage(damage)
                print("Співпадіння атак! Кожен втрачає половину атаки противника.")
            elif hero_value > dragon_value:
                dragon.take_damage(hero_value)
                print("Атака героя більша! Дракон втрачає здоров'я.")
            else:
                hero.take_damage(dragon_value)
                print("Атака дракона більша! Герой втрачає здоров'я.")
        elif hero_action == "attack" and dragon_action == "defend":
            print(f"Атака героя: {hero_value}, Захист дракона: {dragon_value}")
            if hero_value > dragon_value:
                damage = hero_value - dragon_value
                dragon.take_damage(damage)
                print(f"Атака успішна! Дракон втрачає {damage} HP.")
            else:
                print("Атака відбита!")
        elif hero_action == "defend" and dragon_action == "attack":
            print(f"Захист героя: {hero_value}, Атака дракона: {dragon_value}")
            if dragon_value > hero_value:
                damage = dragon_value - hero_value
                hero.take_damage(damage)
                print(f"Атака успішна! Герой втрачає {damage} HP.")
            else:
                print("Атака відбита!")
        else:  # Обидва захищаються
            print("Обидва захищаються. Нічия!")

        round_num += 1

    if hero.is_alive():
        print(f"\n{hero.name} переміг!")
    else:
        print(f"\n{dragon.name} переміг!")

if __name__ == "__main__":
    battle()
