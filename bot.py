import os
import hikari
import lightbulb
import dotenv
from ext.modules import mongohandler

dotenv.load_dotenv()

#instantiate the bot
bot = lightbulb.BotApp(
    os.environ["DISCORD_TOKEN"],
    default_enabled_guilds=int(os.environ["DISCORD_GUILD"]),
    help_slash_command=True,
    intents=hikari.Intents.ALL,
)

#connect to the database
initializer = mongohandler.Mongo()
initializer.setup()

#load the extensions
bot.load_extensions("ext.testplugin")
bot.load_extensions("ext.admin")

bot.run()

