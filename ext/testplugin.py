import lightbulb

plugin = lightbulb.Plugin("example")
botver = "Bot Version 0.0.1"


@plugin.command
@lightbulb.command("info", "Infos about the bot")
@lightbulb.implements(lightbulb.SlashCommand)
async def on_say(ctx: lightbulb.SlashContext) -> None:
    await ctx.respond(ctx.options.text)


def load(bot):
    bot.add_plugin(plugin)


def unload(bot):
    bot.remove_plugin(plugin)
