import unittest
from project.hero import Hero

class Hero_Test(unittest.TestCase):
    def setUp(self):
        self.my_hero = Hero("Michael", 1, 100, 100)
        self.enemy_hero = Hero("John", 1, 50, 50)

    def test_init(self):
        result = [self.my_hero.username, self.my_hero.level, self.my_hero.health, self.my_hero.damage]
        expected_result = ["Michael", 1, 100, 100]
        self.assertEqual(result, expected_result)

    def test_battle_exception_own_and_enemy_hero_username(self):
        with self.assertRaises(Exception) as exc_msg:
            self.enemy_hero.username = self.my_hero.username
            self.my_hero.battle(self.enemy_hero)
        self.assertEqual("You cannot fight yourself", str(exc_msg.exception))

    def test_battle_exception_low_health_own_hero(self):
        with self.assertRaises(Exception) as exc_msg:
            self.my_hero.health = 0
            self.my_hero.battle(self.enemy_hero)
        self.assertEqual(f"Your health is lower than or equal to 0. You need to rest", str(exc_msg.exception))

    def test_battle_exception_low_health_enemy_hero(self):
        with self.assertRaises(Exception) as exc_msg:
            self.enemy_hero.health = 0
            self.my_hero.battle(self.enemy_hero)
        self.assertEqual(f"You cannot fight John. He needs to rest", str(exc_msg.exception))

    def test_health_and_damage_taken_and_removed_when_result_after_fight_is_draw(self):
        self.my_hero.health = self.enemy_hero.health  # Arrange
        self.my_hero.damage = self.enemy_hero.damage

    def test_battle_outcome_draw(self):
        self.enemy_hero.health, self.enemy_hero.damage = self.my_hero.health, self.my_hero.damage
        result = self.my_hero.battle(self.enemy_hero)
        expected_result = "Draw"
        self.assertEqual(result, expected_result)

    def test_battle_outcome_draw_calculation(self):
        self.my_hero.battle(self.enemy_hero)
        result = [self.my_hero.health, self.enemy_hero.health]
        expected_result = [55, -50]
        self.assertEqual(result, expected_result)

    def test_battle_outcome_win(self):
        self.enemy_hero.health, self.enemy_hero.damage = 80, 80
        result = self.my_hero.battle(self.enemy_hero)
        expected_result = "You win"
        self.assertEqual(result, expected_result)

    def test_battle_outcome_win_calculation(self):
        # self.enemy_hero.health, self.enemy_hero.damage = 80, 80
        self.my_hero.battle(self.enemy_hero)
        result = [self.my_hero.level, self.my_hero.health, self.my_hero.damage]
        expected_result = [2, 55, 105]
        self.assertEqual(result, expected_result)

    def test_battle_outcome_lose(self):
        self.enemy_hero.health, self.enemy_hero.damage = 150, 10
        result = self.my_hero.battle(self.enemy_hero)
        expected_result = "You lose"
        self.assertEqual(result, expected_result)

    def test_battle_outcome_lose_calculation(self):
        self.enemy_hero.health, self.enemy_hero.damage = 150, 10
        self.my_hero.battle(self.enemy_hero)
        result = [self.enemy_hero.level, self.enemy_hero.health, self.enemy_hero.damage]
        expected_result = [2, 55, 15]
        self.assertEqual(result, expected_result)

    def test_str(self):
        result = self.my_hero.__str__()
        expected_result = f"Hero Michael: 1 lvl\n" \
               f"Health: 100\n" \
               f"Damage: 100\n"
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
