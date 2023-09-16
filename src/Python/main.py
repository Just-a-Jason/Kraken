from discord.ext.commands import Bot
from discord import Interaction, Embed
from config import PREFIX, TOKEN
from discord import Intents
from os import system

from Fishing_Game.fishing_game import FishingGame
from database_manager import DataBaseManager
from Fishing_Game.fishing_game_objects import Fish

system('cls')

manager: DataBaseManager = DataBaseManager('kraken')
fishingGame: FishingGame = FishingGame(manager)

KRAKEN_INSTANCE: Bot = Bot(command_prefix=PREFIX, intents=Intents.all())


@KRAKEN_INSTANCE.event
async def on_ready():
    print('KRAKEN IS READY!')
    await KRAKEN_INSTANCE.tree.sync()


@KRAKEN_INSTANCE.tree.command(name='fish', description='Use it to catch fish! 🦑')
async def fish(i: Interaction):
    fish: Fish = fishingGame.Fish()
    e: Embed = Embed(title='You caught')
    e.add_field(name='Fish', value=f'{fish.name} {fish.icon}')
    await i.response.send_message(embed=e)

KRAKEN_INSTANCE.run(token=TOKEN)
