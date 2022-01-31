import hikari
import lightbulb
import os
import dotenv

dotenv.load_dotenv()
plugin = lightbulb.Plugin("admin")


@plugin.command
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.permissions.Permissions.KICK_MEMBERS))
@lightbulb.option("user", "Specify user to ban", type=hikari.User)
@lightbulb.option("reason", "specify reason")
@lightbulb.command("tempban", "temporary ban a user")
@lightbulb.implements(lightbulb.SlashCommand)
async def on_tempban(ctx: lightbulb.SlashContext) -> None:
    try:
        member = ctx.options.user
        reason = ctx.options.reason
        await ctx.bot.rest.ban_user(guild=int(os.environ["DISCORD_GUILD"]), user=member, reason=reason)
        await ctx.respond("Banned " + member.mention + " Reason " + reason)
    except:
        await ctx.respond("Something went wrong. Error_1")


@plugin.command
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.permissions.Permissions.KICK_MEMBERS))
@lightbulb.option("user", "Specify user to ban", type=hikari.User)
@lightbulb.option("reason", "specify reason")
@lightbulb.command("kick", "temporary ban a user")
@lightbulb.implements(lightbulb.SlashCommand)
async def on_kick(ctx: lightbulb.SlashContext) -> None:
    try:
        member = ctx.options.user
        reason = ctx.options.reason
        await ctx.bot.rest.kick_user(guild=int(os.environ["DISCORD_GUILD"]), user=member, reason=reason)
        await ctx.respond("Kicked " + member.mention + " Reason " + reason)
    except:
        await ctx.respond("something went wrong. Error_2")


def load(bot):
    bot.add_plugin(plugin)
