import unittest

from repo.city_repo import CityRepo, AcresError, FeedError, PlantError


class FullTests(unittest.TestCase):
    def setUp(self):
        self.city_repo = CityRepo(0, 0, 100, 1000, 3, 200, 20, 2800)

    def test_buy_sell(self):
        with self.assertRaises(AcresError):
            self.city_repo.buy_sell_acres("one hundred")

        with self.assertRaises(AcresError):
            self.city_repo.buy_sell_acres("2.4")

        with self.assertRaises(AcresError):
            self.city_repo.buy_sell_acres(200)

        with self.assertRaises(AcresError):
            self.city_repo.buy_sell_acres(-1500)

    def test_update_grain_based_on_land(self):
        self.city_repo.update_grain_based_on_land(0)
        self.assertEqual(self.city_repo.city.city_acres, 1000)
        self.assertEqual(self.city_repo.city.grain_stocks, 2800)

        self.city_repo.update_grain_based_on_land(100)
        self.assertEqual(self.city_repo.city.city_acres, 1100)
        self.assertEqual(self.city_repo.city.grain_stocks, 800)

        self.city_repo.update_grain_based_on_land(-100)
        self.assertEqual(self.city_repo.city.city_acres, 1000)
        self.assertEqual(self.city_repo.city.grain_stocks, 2800)

    def test_update_land_price(self):
        self.city_repo.update_land_price()
        self.assertEqual(15 <= self.city_repo.city.land_price <= 25, True)

    def test_feed(self):
        with self.assertRaises(FeedError):
            self.city_repo.feed("one hundred")

        with self.assertRaises(FeedError):
            self.city_repo.feed("2.4")

        with self.assertRaises(FeedError):
            self.city_repo.feed(3000)

    def test_update_grain_based_on_feed(self):
        self.city_repo.update_grain_based_on_feed(2000)
        self.assertEqual(self.city_repo.city.grain_stocks, 800)

    def test_update_population_based_on_feed(self):
        self.city_repo.update_population_based_on_feed(2000)
        self.assertEqual(0 <= self.city_repo.city.new_people <= 10, True)
        self.assertEqual(100 <= self.city_repo.city.city_population <= 110, True)

        self.city_repo.update_population_based_on_feed(1500)
        self.assertEqual(self.city_repo.city.new_people, 0)
        self.assertEqual(self.city_repo.city.city_population, 75)

        self.city_repo.update_population_based_on_feed(500)
        self.assertEqual(self.city_repo.get_game_state(), False)

    def test_plant(self):
        with self.assertRaises(PlantError):
            self.city_repo.plant("one hundred")

        with self.assertRaises(PlantError):
            self.city_repo.plant("2.4")

        with self.assertRaises(PlantError):
            self.city_repo.plant("-32")

        with self.assertRaises(PlantError):
            self.city_repo.plant(1001)

        self.city_repo.update_grain_based_on_feed(2000)
        with self.assertRaises(PlantError):
            self.city_repo.plant(900)

    def test_harvest_planted_land(self):
        old_grain_stocks = self.city_repo.city.grain_stocks
        self.city_repo.harvest_planted_land(800)
        self.assertEqual(self.city_repo.city.grain_stocks, old_grain_stocks + self.city_repo.city.harvest * 800 - 800)

    def test_update_harvesting(self):
        self.city_repo.update_harvesting()
        self.assertEqual(1 <= self.city_repo.city.harvest <= 6, True)

    def test_rat_infestation(self):
        old_grain_stocks = self.city_repo.city.grain_stocks
        self.city_repo.rat_infestation()
        self.assertEqual(old_grain_stocks - self.city_repo.city.rats, self.city_repo.city.grain_stocks)