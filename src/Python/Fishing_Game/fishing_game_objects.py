from enum import Enum
from typing import List


class Fish:
    def __init__(self, name: str, icon: str, value: float, rarity: float, bait: dict = None):
        self.name: str = name
        self.icon: str = icon
        self.value: float = value
        self.rarity: float = rarity
        self.bait: dict = bait

    def __str__(self) -> str:
        return f'(Fish)({hex(id(self))}) name: {self.name}, icon: {self.icon}  value: {self.value}, rarity: {self.rarity}, bait: {self.bait}'

    def TryCatch(self):
        pass


class ItemType(Enum):
    bait = 0
    item = 1


class ShopItem:
    def __init__(self, name: str, icon: str, type: ItemType, cost: float, special: str = None, description: str = None, power: int = None):
        self.name: str = name
        self.icon: str = icon
        self.type: ItemType = type,
        self.cost: float = cost
        self.power: int = power
        self.special: str = special
        self.description: str = description

    def __str__(self) -> str:
        return f'(ShopItem)({hex(id(self))}) name: {self.name}, icon: {self.icon}  type: {self.type}, cost: {self.cost}, special: {self.special}, description: {self.description}'


class FishList:
    def __init__(self, maxChance: int, fishList: List[Fish]):
        self.maxChance: int = maxChance
        self.fishList: List[Fish] = fishList
