import unittest
from hero.project.hero import Hero


class HeroTest(unittest.TestCase):
    def setUp(self) -> None:
        self.hero = Hero("Emil", 7, 10, 5)
        self.enemy_hero = Hero("Mage", 5, 10, 2)

    def test_initialization_if_correctly(self):
        self.assertEqual("Emil", self.hero.username)
        self.assertEqual(7, self.hero.level)
        self.assertEqual(10, self.hero.health)
        self.assertEqual(5, self.hero.damage)

    def test_battle_if_usernames_are_same_raise_exception(self):
        enemy_hero1 = Hero('Emil', 2, 12, 54)

        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy_hero1)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_if_hero_health_is_negative_or_zero(self):

        for i in range(0, -3, -1):
            self.hero.health = i
            with self.assertRaises(ValueError) as ex:
                self.hero.battle(self.enemy_hero)

            self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_if_enemy_hero_health_is_negative_or_zero(self):

        for i in range(0, -3, -1):
            self.enemy_hero.health = i
            with self.assertRaises(ValueError) as ex:
                self.hero.battle(self.enemy_hero)

            self.assertEqual(f"You cannot fight Mage. He needs to rest", str(ex.exception))

    def test_battle_health_decrease_each_player_after_damaged(self):
        self.hero.battle(self.enemy_hero)
        self.assertEqual(0, self.hero.health)
        self.assertEqual(-25, self.enemy_hero.health)

    def test_battle_if_draw(self):

        result = self.hero.battle(self.enemy_hero)
        self.assertEqual("Draw", result)
        self.enemy_hero.health = 30
        self.hero.health = 5
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual("Draw", result)

        self.enemy_hero.health = 30
        self.hero.health = 15
        result = self.hero.battle(self.enemy_hero)
        self.assertNotEqual(result, "Draw")

    def test_battle_if_win(self):
        self.assertEqual(7, self.hero.level)
        self.assertEqual(10, self.hero.health)
        self.assertEqual(5, self.hero.damage)

        self.hero.health = 11
        result = self.hero.battle(self.enemy_hero)

        self.assertEqual("You win", result)
        self.assertEqual(8, self.hero.level)
        self.assertEqual(6, self.hero.health)
        self.assertEqual(10, self.hero.damage)

    def test_battle_if_lose(self):
        self.assertEqual(5, self.enemy_hero.level)
        self.assertEqual(10, self.enemy_hero.health)
        self.assertEqual(2, self.enemy_hero.damage)
        self.enemy_hero.health = 36

        result = self.hero.battle(self.enemy_hero)
        self.assertEqual("You lose", result)
        self.assertEqual(6, self.enemy_hero.level)
        self.assertEqual(6, self.enemy_hero.health)
        self.assertEqual(7, self.enemy_hero.damage)

    def test_str_method(self):
        expected_result = f"Hero Emil: 7 lvl\n" \
               f"Health: 10\n" \
               f"Damage: 5\n"

        result = str(self.hero)

        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()