from pyrogram import filters, Client

from .ai import *
from .data import *
from .func import *
from .inline import *
from .lgs import *
from .what import *
from .filter import *
from .constants import *

async def ajg(client):
    try:
        await ayra_bot.join_chat("@kynansupport")
        await ayra_bot.join_chat("@kontenfilm")
        await ayra_bot.join_chat("@Mengzsad")
        await ayra_bot.join_chat("@abtnaaa")
    except BaseException:
        pass