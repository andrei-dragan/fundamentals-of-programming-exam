class City:
    def __init__(self, people_starved, new_people, city_population, city_acres, harvest, rats, land_price, grain_stocks):
        self.__people_starved = people_starved
        self.__new_people = new_people
        self.__city_population = city_population
        self.__city_acres = city_acres
        self.__harvest = harvest
        self.__rats = rats
        self.__land_price = land_price
        self.__grain_stocks = grain_stocks

    @property
    def people_starved(self):
        return self.__people_starved

    @property
    def new_people(self):
        return self.__new_people

    @property
    def city_population(self):
        return self.__city_population

    @property
    def city_acres(self):
        return self.__city_acres

    @property
    def harvest(self):
        return self.__harvest

    @property
    def rats(self):
        return self.__rats

    @property
    def land_price(self):
        return self.__land_price

    @property
    def grain_stocks(self):
        return self.__grain_stocks

    @grain_stocks.setter
    def grain_stocks(self, new_grain_stocks):
        self.__grain_stocks = new_grain_stocks

    @city_population.setter
    def city_population(self, new_city_population):
        self.__city_population = new_city_population

    @new_people.setter
    def new_people(self, new_new_people):
        self.__new_people = new_new_people

    @land_price.setter
    def land_price(self, new_land_price):
        self.__land_price = new_land_price

    @harvest.setter
    def harvest(self, new_harvest):
        self.__harvest = new_harvest

    @rats.setter
    def rats(self, new_rats):
        self.__rats = new_rats

    @city_acres.setter
    def city_acres(self, new_city_acres):
        self.__city_acres = new_city_acres

    @people_starved.setter
    def people_starved(self, new_people_starved):
        self.__people_starved = new_people_starved