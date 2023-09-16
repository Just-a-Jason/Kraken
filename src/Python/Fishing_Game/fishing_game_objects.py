from enum import Enum


class Fish:
    def __init__(self, name: str, icon: str, value: float, rarity: float, bait: dict = None):
        self.name = name
        self.icon = icon
        self.value = value
        self.rarity = rarity
        self.bait = bait

    def __str__(self) -> str:
        return f'(ShopItem)({hex(id(self))}) name: {self.name}, icon: {self.icon}  value: {self.value}, rarity: {self.rarity}, bait: {self.bait}'

    def TryCatch(self):
        pass


class ItemType(Enum):
    bait = 0
    item = 1


class ShopItem:
    def __init__(self, name: str, icon: str, type: ItemType, cost: float, special: str = None, description: str = None, power: int = None):
        self.name = name
        self.icon = icon
        self.type = type,
        self.cost = cost
        self.power = power
        self.special = special
        self.description = description

    def __str__(self) -> str:
        return f'(ShopItem)({hex(id(self))}) name: {self.name}, icon: {self.icon}  type: {self.type}, cost: {self.cost}, special: {self.special}, description: {self.description}'
