from discord import Interaction, Embed, Game
from discord.ext.commands import Bot
from config import PREFIX, TOKEN
from discord import Intents
from os import system

from database_manager import DataBaseManager
from Fishing_Game.fishing_game import FishingGame
from Fishing_Game.fishing_game_objects import Fish

system('cls')

manager: DataBaseManager = DataBaseManager('kraken')
fishingGame: FishingGame = FishingGame(manager)

KRAKEN_INSTANCE: Bot = Bot(command_prefix=PREFIX, intents=Intents.all())


@KRAKEN_INSTANCE.event
async def on_ready():
    print('KRAKEN IS READY!')
    await KRAKEN_INSTANCE.tree.sync()
    await KRAKEN_INSTANCE.change_presence(activity=Game('/help'))


@KRAKEN_INSTANCE.tree.command(name='fish', description='Use it to catch fish! 🦑')
async def fish(i: Interaction):
    fish: Fish = fishingGame.Fish()
    from discord import Colour

    e: Embed = Embed(
        title=f'You caught... {fish.name.upper()}! {fish.icon}', colour=Colour.dark_magenta())

    await i.response.send_message(embed=e)

KRAKEN_INSTANCE.run(token=TOKEN)
