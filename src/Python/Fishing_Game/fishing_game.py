from Fishing_Game.fishing_game_objects import Fish, ShopItem
from database_manager import DataBaseManager
from typing import List
from json import loads


class KeyHelper:
    def GetKey(key: str, dict: dict):
        return None if not key in dict else dict[key]


class FishingGame():
    shopData: List[ShopItem] = None
    fishData: List[Fish] = None

    def __init__(self, dataBaseManager: DataBaseManager):
        self.manager = dataBaseManager
        self.LoadGameData()

    def LoadGameData(self):
        if not FishingGame.shopData:
            with open('src/Json/Bot/Fishing Game/shop.json') as shop:
                FishingGame.shopData = list()
                jsonData: dict = loads(shop.read())

                for item in jsonData:
                    shopItem: ShopItem = ShopItem(
                        item['name'],
                        item['icon'],
                        item['type'],
                        item['cost'],
                        KeyHelper.GetKey('special', item),
                        KeyHelper.GetKey('description', item),
                        KeyHelper.GetKey('power', item)
                    )

                    FishingGame.shopData.append(shopItem)

        if not FishingGame.fishData:
            with open('src/Json/Bot/Fishing Game/fish.json') as fish:
                FishingGame.fishData = list()
                jsonData: dict = loads(fish.read())

                for item in jsonData:
                    fish: Fish = Fish(
                        item['name'],
                        item['icon'],
                        item['value'],
                        item['rarity'],
                        item['bait']
                    )
                    FishingGame.fishData.append(fish)

    def Fish(self) -> Fish:
        from random import choice
        return choice(FishingGame.fishData)
