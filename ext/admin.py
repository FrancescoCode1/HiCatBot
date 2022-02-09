import time
import hikari
import lightbulb
import os
import dotenv

dotenv.load_dotenv()
plugin = lightbulb.Plugin("admin")
GUILD_ID = int(os.environ["DISCORD_GUILD"])

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
        await ctx.bot.rest.ban_user(guild=GUILD_ID, user=member, reason=reason)
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
        await ctx.bot.rest.kick_user(guild=GUILD_ID, user=member, reason=reason)
        await ctx.respond("Kicked " + member.mention + " Reason " + reason)
    except:
        await ctx.respond("something went wrong. Error_2")


@lightbulb.Check
def check_specific_channel(context: lightbulb.Context) -> bool:
    return context.channel_id == 937762815803011072


@plugin.command
@lightbulb.add_checks(check_specific_channel)
@lightbulb.option("user", "specify user to mute", type=hikari.User)
@lightbulb.option("duration", "Specify duration to mute", type=int)
@lightbulb.command("mute", "temporary mute a user")
@lightbulb.implements(lightbulb.SlashCommand)
async def on_mute(ctx: lightbulb.SlashContext) -> None:
    member = ctx.options.user
    rawtime = ctx.options.duration #time in seconds
    duration = int(rawtime) * 60 * 60 #time in hours
    await ctx.bot.rest.add_role_to_member(GUILD_ID, user=member, role=937724392824266814)
    await ctx.respond(f"User {member.mention} has been muted for {rawtime} hours")
    time.sleep(duration)
    await ctx.bot.rest.remove_role_from_member(GUILD_ID, user=member, role=937724392824266814)
    await ctx.respond(f"User {member.mention} has been unmuted")


@plugin.command
@lightbulb.command("fetch", "fetch users")
@lightbulb.implements(lightbulb.SlashCommand)
async def on_fetch(ctx: lightbulb.SlashContext) -> None:
    fetched_list = ctx.bot.rest.fetch_members(guild=GUILD_ID)
    new_string = "\n".join([str(x) async for x in fetched_list])
    embed = hikari.Embed(title="Server Info", description="Show users of this Server", color=[255, 255, 255])
    embed.add_field(name="Members", value="Members", inline=True)
    embed.add_field(name="ex", value="23", inline=True)
    await ctx.respond(embed)
    #await ctx.respond(new_string)


def load(bot):
    bot.add_plugin(plugin)
