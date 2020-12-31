from userbot import *
from userbot.utils import *

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ArceusUser"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

kraken = bot.uid

PM_IMG = "https://telegra.ph/file/00d83ccccfb983f76fa22.jpg"
pm_caption = "__**🔥🔥Arceus ɨs օռʟɨռɛ🔥🔥**__\n\n"

pm_caption += (
    f"               __↼🄼🄰🅂🅃🄴🅁⇀__\n**『[{DEFAULTUSER}](tg://user?id={kraken})』**\n\n"
)

pm_caption = "** ARCEUS BOT 𝙸𝚂 𝙾𝙽𝙻𝙸𝙽𝙴**\n\n"
pm_caption += "**Yes Surr, Am Alive And Systems Are Working Perfectly As It Should Be...**\n\n"
pm_caption += "✘ About My System ✘\n\n"
pm_caption += "➾ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ** ☞ 1.17.5\n"
pm_caption += "➾ **ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ** ☞ [ᴊᴏɪɴ](https://t.me/ArceususerBot)\n"
pm_caption += "🔥CREATOR🔥    : [Nub Here](https://t.me/Itz_Mr_Hillarious)\n\n"
pm_caption += "    [✨REPO✨](https://github.com/arceusbot/ArceusBot)🔹 [📜License📜](https://github.com/arceusbot/ArceusBot/blob/main/LICENSE)"


@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()
