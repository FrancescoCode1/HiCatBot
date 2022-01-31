import os
import hikari
import lightbulb
import dotenv

dotenv.load_dotenv()

bot = lightbulb.BotApp(
    os.environ["DISCORD_TOKEN"],
    default_enabled_guilds=int(os.environ["DISCORD_GUILD"]),
    help_slash_command=True,
    intents=hikari.Intents.ALL,
)


bot.load_extensions("ext.testplugin")
bot.load_extensions("ext.admin")

bot.run()

"""
@bot.command()
@lightbulb.option("text", "say something")
@lightbulb.command("say", "Say something description")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def cmd_say(ctx: lightbulb.SlashContext) -> None:
    await ctx.respond(ctx.options.text)
"""