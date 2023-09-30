from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight: int = 0
    started: bool = False
    fuel: int = 0
    fuel_consumption: int = 0

    def __init__(self, weight: int, fuel: int, fuel_consumption: int):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started:
            return

        if self.fuel > 0:
            self.started = True
        else:
            raise LowFuelError

    def move(self, distance: int):
        fuel_left = distance * self.fuel_consumption

        if fuel_left > self.fuel:
            raise NotEnoughFuel

        self.fuel = self.fuel - fuel_left
