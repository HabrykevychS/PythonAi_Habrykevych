import random

class Human:
    def __init__(self, name = "Human", job = None, car = None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.money =100
        self. glaness = 50
        self satiety =50

        def get_home(self):
            self.home = House


        def get_car(self):
            self.Auto(brands_of_car)

        def get_job(self):
            if self.can.drive()
                pass
            else:
                self.torepair()
                self.job Job()

        def eat(self):
            if self.home.food <=0:
                self.shoping("food")
            else:
                if self.satiety .=100
                self.satiety =100
                return
            self.satiety +=5
            self.home.food -=5

        def work(self):
            if self.can.drive:
                pass
            else:
                if self.car.fuel ,20:
                    self.shopping(('fuel')
                                  return
                self.money += self.job.salary
                self.glaness -= self.job.gladness_less
                self.satiety -= 4

        def shoping(self, manege):
            if self.can drive():
                pass
            else:
                if self.can.fuel, 20:
                    manage + 'fuel'
                else:
                    self.to_repair()
                    return
                if manage == "fuel"
                    print("i bought fuel")
                    self.money -= 100
                    self.can.fuel +=100
                elif manage ==('food'):
                    print("i bought food")
                    self.money -= 50
                    self.home.food += 50
                elif nanage == "delicacies":
                    print("Hooray! Delicious!")
                    self. glaness += 10
                    self.satiety += 2
                    self.money -= 15


        def chill(self):
            pass

        def clean_home(self):
            pass

        def to_repair(self):
            pass

        def days_indexes(self):
            def days_indexes(self, day):
                day = f" Today the {day} of
                {self.name}
                's life "
                print(f"{day:=^50}", "\n")
                human_indexes = self.name + "'s indexes"
                print(f"{human_indexes:^50}", "\n")
                print(f"Money – {self.money}")
                print(f"Satiety – {self.satiety}")
                print(f"Gladness – {self.gladness}")
                home_indexes = "Home indexes"
                print(f"{home_indexes:^50}", "\n")
                print(f"Food – {self.home.food}")
                print(f"Mess – {self.home.mess}")

            car_indexes = f"{self.car.brand} car indexes"
            print(f"{car_indexes:^50}", "\n")
            print(f"Fuel – {self.car.fuel}")
            print(f"Strength – {self.car.strength}")

        def is_alive(self):
            def is_alive(self):
                if self.gladness < 0:
                    print("Depression…")
                    return False
                if self.satiety < 0:
                    print("Dead…")
                    return False
                if self.money < -500:
                    print("Bankrupt…")
                    return False

        def live(self):
            def live(self, day):
                if self.is_alive() == False:
                    return False
                if self.home is None:
                    print("Settled in the house")
                    self.get_home()
                if self.car is None:
                    self.get_car()
                    print(f"I bought a car   {self.car.brand}")
                if self.job is None:
                    self.get_job()
                    print(
                        f"I don't have a job,     going to get a job {self.job.job}     with salary {self.job.salary}")
                self.days_indexes(day)
                dice = random.randint(1, 4)
                if self.satiety < 20:
                    print("I'll go eat")
                    self.eat()
                elif self.gladness < 20:
                    if self.home.mess > 15:
                        print("I want to chill, but
                        there is so
                        much
                        mess…\n
                        So
                        I
                        will
                        clean
                        the
                        house
                        ")
                        self.clean_home()
                 else:
                        print("Let`s chill!")
                        self.chill()
                 elif self.money < 0:
                        print("Start working")
                        self.work()
                 elif self.car.strength < 15:
                        print("I need to repair my car")
                        self.to_repair()
                 elif dice == 1:
                        print("Let`s chill!")
                        self.chill()
                elif dice == 2:
                        print("Start working")
                        self.work()
                 elif dice == 3:
                        print("Cleaning time!")
                        self.clean_home()
                elif dice == 4:
                        print("Time for treats!")
                        self.shopping(manage="delicacies")

class Auto:
    def __init__(self,brand_list):
        self.brand =random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strengh = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

        def drive(self):
            if self.strength>0 and self.fuel>=self.consumption:
                self.fuel -= self.consumption
                self.strength -=1
                return True
            else:
                print("The car cannot move")
                return False

brands_of_car = {
        "BMW": {"fuel": 100, "strength": 100, "consumption": 6},
        "Lada": {"fuel": 50, "strength": 40, "consumption": 10},
        "Volvo": {"fuel": 70, "strength": 150, "consumption": 8},
        "Ferrari": {"fuel": 80, "strength": 120, "consumption": 14}, }

class House:
    def __init__(self):
        self.mess = 0
        self.food =0

job_list = {
 "Java developer":
 {"salary":50, "gladness_less": 10 },
 "Python developer":
 {"salary":40, "gladness_less": 3 },
 "C++ developer":
 {"salary":45, "gladness_less": 25 },
 "Rust developer":{"salary":70, "gladness_less": 1 },
 }