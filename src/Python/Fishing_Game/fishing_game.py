from Fishing_Game.fishing_game_objects import Fish, ShopItem
from database_manager import DataBaseManager
from utils import KeyHelper
from typing import List
from json import loads


class FishingGame():
    shopData: dict[int, ShopItem] = None
    fishData: dict[int, Fish] = None

    def __init__(self, dataBaseManager: DataBaseManager):
        self.manager = dataBaseManager
        self.LoadGameData()

    def LoadGameData(self):
        if not FishingGame.shopData:
            with open('src/Json/Bot/Fishing Game/shop.json') as shop:
                FishingGame.shopData = dict()
                jsonData: dict = loads(shop.read())

                for item in jsonData:
                    id: int = item['id']

                    shopItem: ShopItem = ShopItem(
                        name=item['name'],
                        icon=item['icon'],
                        type=item['type'],
                        cost=item['cost'],
                        special=KeyHelper.GetKey('special', item),
                        description=KeyHelper.GetKey('description', item),
                        power=KeyHelper.GetKey('power', item)
                    )

                    FishingGame.shopData[id] = shopItem

        if not FishingGame.fishData:
            with open('src/Json/Bot/Fishing Game/fish.json') as fish:
                FishingGame.fishData = dict()
                jsonData: dict = loads(fish.read())

                for item in jsonData:
                    id: int = item['id']

                    fish: Fish = Fish(
                        name=item['name'],
                        icon=item['icon'],
                        value=item['value'],
                        rarity=item['rarity'],
                        bait=item['bait']
                    )

                    FishingGame.fishData[id] = fish

    def Fish(self) -> Fish:
        from random import choice
        # self.manager.AddItemToInventory(478514930958598174, 0, 5)
        self.manager.GetItem(owner_id=478514930958598174, itemID=0)
        return choice(FishingGame.fishData)
