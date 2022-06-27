from repo.city_repo import AcresError, FeedError, PlantError


class UI:
    def __init__(self, city_repo):
        self.__city_repo = city_repo

    def __print_situation(self, year):
        city_info = self.__city_repo.get_situation()
        print('')
        print("In Year " + str(year) + ", " + str(city_info[0]) + " people starved.")
        print(str(city_info[1]) + " people came to the city.")
        print("City population is " + str(city_info[2]))
        print("City owns " + str(city_info[3]) + " acres of land.")
        print("Harvest was " + str(city_info[4]) + " units per acre.")
        print("Rats ate " + str(city_info[5]) + " units.")
        print("Land price is " + str(city_info[6]) + " units per acre.")
        print('')
        print("Grain stocks are " + str(city_info[7]) + " units.")

    def start(self):
        for year in range(1, 5):
            self.__print_situation(year)

            # Get the input
            print('')
            print("Now it's your turn to choose!")
            print("=============================")
            print('')

            # Buy / sell
            acres_input = False
            while not acres_input:
                new_acres = input("Acres to buy/sell(+/-)-> ")
                try:
                    self.__city_repo.buy_sell_acres(new_acres)
                    acres_input = True
                except AcresError as ae:
                    print(ae)

            # Feed
            units_to_feed_input = False
            while not units_to_feed_input:
                units_to_feed = input("Units to feed the population-> ")
                try:
                    self.__city_repo.feed(units_to_feed)
                    units_to_feed_input = True
                except FeedError as fe:
                    print(fe)

            # Plant
            acres_to_plant_input = False
            while not acres_to_plant_input:
                acres_to_plant = input("Acres to plant-> ")
                try:
                    self.__city_repo.plant(acres_to_plant)
                    acres_to_plant_input = True
                except PlantError as pe:
                    print(pe)

            # Rat invasion
            self.__city_repo.rat_infestation()

            # Check win_condition
            if self.__city_repo.get_game_state() is False:
                print("GAME OVER. You did not do well. Half of your population starved!")
                return

        self.__print_situation(5)

        if self.__city_repo.check_game_final() is True:
            print("Congratulations! You won!")
        else:
            print("GAME OVER. You did not do well.")
