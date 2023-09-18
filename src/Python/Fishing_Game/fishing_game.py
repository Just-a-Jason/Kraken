from Fishing_Game.fishing_game_objects import Fish, ShopItem, FishList
from utils import KeyHelper
from typing import List
from json import loads


class FishingGame():
    shopData: dict[int, ShopItem] = None
    fishData: dict[int, Fish] = None

    from database_manager import DataBaseManager

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

    def GetAllFishWithBait(self, bait: str = 'none') -> FishList:

        fishFound: List[Fish] = [
            fish for fish in FishingGame.fishData.values()
            if (fish.bait and bait in fish.bait) or fish.bait == None]

        maxChance: int = 0

        for fish in fishFound:
            maxChance += fish.rarity

        return FishList(maxChance=maxChance, fishList=fishFound)

    def Fish(self, bait='none') -> Fish:
        fishes: FishList = self.GetAllFishWithBait(bait=bait)
        from random import randrange

        chance: int = randrange(0, fishes.maxChance)
        caught: Fish

        for fish in fishes.fishList:
            if chance <= fish.rarity:
                caught = fish
                break
            else:
                chance -= fish.rarity

        return caught
