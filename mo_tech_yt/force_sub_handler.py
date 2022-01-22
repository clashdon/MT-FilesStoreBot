# (c) @MRK_YT

from configs import Config
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def handle_force_sub(bot, cmd):
    invite_link = await bot.create_chat_invite_link(int(Config.UPDATES_CHANNEL))
    try:
        user = await bot.get_chat_member(int(Config.UPDATES_CHANNEL), cmd.from_user.id)
        if user.status == "kicked":
            await bot.send_message(
                chat_id=cmd.from_user.id,
                text="**Sorry Sir😔**, **You are Banned to use me. Contact my** [Support Group] (https://t.me/Berlinsupportg).",
                parse_mode="markdown",
                disable_web_page_preview=True
            )
            return 400
    except UserNotParticipant:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="**Please Join My Updates Channel to use this Bot!**\n\n**Files വേണക്കിൽ ആദ്യം ഞങ്ങളുടെ Update Channelil ജോയിൻ ചെയ്യണം...!**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔊 𝐉𝐨𝐢𝐧 𝐔𝐩𝐝𝐚𝐭𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 🔊", url=invite_link.invite_link)
                    ],
                    [
                        InlineKeyboardButton("🎉 𝐉𝐨𝐢𝐧 𝕄𝕆𝕍𝕀𝔼𝕊 ℝ𝕖𝕘. 𝔾𝕣𝕠𝕦𝕡 💕🎉", url="https://t.me/likemoviesearch")
                    ],
                    [
                        InlineKeyboardButton("🔄 𝐑𝐞𝐟𝐫𝐞𝐬𝐡 🔄", callback_data="refreshmeh")
                    ]
                ]
            ),
            parse_mode="markdown"
        )
        return 400
    except Exception:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="Something went Wrong. Contact my [Support Group] (https://t.me/Berlinsupportg).",
            parse_mode="markdown",
            disable_web_page_preview=True
        )
        return 400
