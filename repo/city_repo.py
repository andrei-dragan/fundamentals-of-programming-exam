import random

from domain.city import City


class CityRepo:
    def __init__(self, people_starved, new_people, city_population, city_acres, harvest, rats, land_price,
                 grain_stocks):
        self.__city = City(people_starved, new_people, city_population, city_acres, harvest,
                           rats, land_price, grain_stocks)
        self.__game_state = True

    @property
    def city(self):
        return self.__city

    def set_lost_state(self):
        self.__game_state = False

    def get_game_state(self):
        return self.__game_state

    def check_game_final(self):
        if self.__city.city_population > 100 and self.__city.city_acres > 1000:
            return True
        return False

    def get_situation(self):
        """
        Get the current situation of the city
        :return: A tuple representing the information needed to be printed
        """
        return self.__city.people_starved, self.__city.new_people, self.__city.city_population, self.__city.city_acres, \
               self.__city.harvest, self.__city.rats, self.__city.land_price, self.__city.grain_stocks

    #####################################
    #           1st command             #
    #####################################
    def buy_sell_acres(self, new_acres):
        """
        Check if we can buy / sell this number of acres, while updating the city accordingly
        :param new_acres: The input given by the user for "acres to buy / sell"
        :return: None
        """
        # First, validate the input
        try:
            new_acres = int(new_acres)
        except ValueError:
            raise AcresError('The number of acres you buy or sell should be an integer number!')

        # Check if we can buy / sell that many acres of land
        if new_acres * self.__city.land_price > self.__city.grain_stocks:
            raise AcresError('You cannot buy more land than you have grain for!')

        if abs(new_acres) > self.__city.city_acres:
            raise AcresError('You cannot sell more land than you have!')

        # Update the grain stocks
        self.update_grain_based_on_land(new_acres)

        # Update the land price
        self.update_land_price()

    def update_grain_based_on_land(self, new_acres):
        """
        Update the grain stock and the land obtained based on the number of acres bought / sold
        :param new_acres: the number of acres bought / sold
        :return: None
        """
        self.__city.grain_stocks -= self.__city.land_price * new_acres
        self.__city.city_acres += new_acres

    def update_land_price(self):
        """
        Update the new land price
        :return: None
        """
        land_price = random.randrange(15, 26)
        self.__city.land_price = land_price

    #####################################
    #           2nd command             #
    #####################################
    def feed(self, units_to_feed):
        """
        Check if we can feed that many units to population, while updating the city accordingly
        :param units_to_feed: The input given by the user for "units to feed"
        :return:None
        """
        # First, validate the input
        try:
            units_to_feed = int(units_to_feed)
            if units_to_feed < 0:
                raise FeedError('The number of units to feed the population should be a positive integer number!')
        except ValueError:
            raise FeedError('The number of units to feed the population should be a positive integer number!')

        # Check if we can feed that many units
        if units_to_feed > self.__city.grain_stocks:
            raise FeedError('You cannot feed that many units!')

        # Update the grain stocks
        self.update_grain_based_on_feed(units_to_feed)

        # Update the population based on the units fed to them
        self.update_population_based_on_feed(units_to_feed)

    def update_grain_based_on_feed(self, units_to_feed):
        """
        Update the grain stock based on the number of units fed to people
        :param units_to_feed: The number of units fed
        :return: None
        """
        self.__city.grain_stocks -= units_to_feed

    def update_population_based_on_feed(self, units_to_feed):
        """
        Update the population according to the number of units fed
        :param units_to_feed: The number of units fed to the population
        :return: None
        """

        # There can only be fed units_to_feed // 20 people
        old_population = self.__city.city_population
        new_population = units_to_feed // 20

        if old_population <= new_population:
            # No one starved, new people come
            new_people = random.randrange(0, 11)
            self.__city.new_people = new_people
            self.__city.city_population = old_population + new_people
            self.__city.people_starved = 0
        else:
            if new_population > old_population // 2:
                # We are still good, but no new people come
                self.__city.new_people = 0
                self.__city.city_population = new_population
                self.__city.people_starved = old_population - new_population
            else:
                # We lost
                self.set_lost_state()

    #####################################
    #           3rd command             #
    #####################################
    def plant(self, acres_to_plant):
        """
        Check if we can plant that many acres, while updating the city accordingly
        :param acres_to_plant: The input given by the user for "acres to plant"
        :return: None
        """
        # First, validate the input
        try:
            acres_to_plant = int(acres_to_plant)
            if acres_to_plant < 0:
                raise PlantError('The number of acres to plant should be a positive integer number!')
        except ValueError:
            raise PlantError('The number of acres to plant should be a positive integer number!')

        # Check if we can plant that many acres
        if acres_to_plant > self.__city.city_acres:
            raise PlantError('There are not that many acres to plant!')

        if self.__city.grain_stocks < acres_to_plant:
            raise PlantError('There are not that many grains to plant!')

        # Update harvesting
        self.update_harvesting()

        # Update the grain stock based on harvesting
        self.harvest_planted_land(acres_to_plant)

    def harvest_planted_land(self, acres_to_plant):
        """
        Update the grain stock accordingly based on harvesting
        :param acres_to_plant: The number of acres of land planted
        :return: None
        """
        self.__city.grain_stocks -= acres_to_plant

        maximum_acres_harvested = self.__city.city_population * 10
        acres_harvested = min(maximum_acres_harvested, acres_to_plant)
        self.__city.grain_stocks += acres_harvested * self.__city.harvest

    def update_harvesting(self):
        """
        Assign randomly a new value to harvest the units
        :return: None
        """
        harvest = random.randrange(1, 7)
        self.__city.harvest = harvest

    #####################################
    #           Rat invasion            #
    #####################################
    def rat_infestation(self):
        """
        Check if we can have a rat infestation, while updating the damage it will produce to the city
        :return: None
        """
        chance_for_infestation = random.randrange(1, 101)
        if chance_for_infestation <= 20:
            # There is an infestation
            grain_eat = random.randrange(1, 11) * self.__city.grain_stocks // 100
            self.__city.rats = grain_eat
            self.__city.grain_stocks -= grain_eat
        else:
            # There is no infestation
            self.__city.rats = 0


class AcresError(Exception):
    pass


class FeedError(Exception):
    pass


class PlantError(Exception):
    pass
