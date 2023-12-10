from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def queue_markup(
    _,
    DURATION,
    CPLAY,
    videoid,
    played: Union[bool, int] = None,
    dur: Union[bool, int] = None,
):
    not_dur = [
        [
            InlineKeyboardButton(
                text=_["QU_B_1"],
                callback_data=f"GetQueued {CPLAY}|{videoid}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
            ),
        ]
    ]
    dur = [
        [
            InlineKeyboardButton(
                text=_["QU_B_2"].format(played, dur),
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="☆", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="˹ᴘʟᴀʏʟɪsᴛ˼", callback_data=f"add_playlist {videoid}",
                ),
            InlineKeyboardButton(
                text="˹ᴏᴡɴᴇʀ˼", user_id="1777270311",
            ),
        ],
        [
            InlineKeyboardButton(
                text="˹sᴜᴘᴘᴏʀᴛ˼", url="https://t.me/+PtOLQT04ocMzOTJl",
                ),
            InlineKeyboardButton(
                text="˹ᴄʜᴀɴɴᴇʟ˼", url="https://t.me/+m4oVCt2zFhYyMTdl",
             ),
            InlineKeyboardButton(
                text="˹ʏᴏᴜᴛᴜʙᴇ˼", url="https://www.youtube.com/channel/UCoOmopJ8YVYz9Lm8iHhNYMw",       
            ),
            InlineKeyboardButton(
                text="˹ᴛғ ᴡᴏʀʟᴅ˼", url="https://t.me/+MQn7rXz1LeViZmJl",
            )
        ],
    ]
    upl = InlineKeyboardMarkup(not_dur if DURATION == "Unknown" else dur)
    return upl


def queue_back_markup(_, CPLAY):
    upl = [
         [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="☆", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="˹ᴘʟᴀʏʟɪsᴛ˼", callback_data=f"add_playlist {videoid}",
                ),
            InlineKeyboardButton(
                text="˹ᴏᴡɴᴇʀ˼", user_id="1777270311",
            ),
        ],
        [
            InlineKeyboardButton(
                text="˹sᴜᴘᴘᴏʀᴛ˼", url="https://t.me/+PtOLQT04ocMzOTJl",
                ),
            InlineKeyboardButton(
                text="˹ᴄʜᴀɴɴᴇʟ˼", url="https://t.me/+m4oVCt2zFhYyMTdl",
             ),
            InlineKeyboardButton(
                text="˹ʏᴏᴜᴛᴜʙᴇ˼", url="https://www.youtube.com/channel/UCoOmopJ8YVYz9Lm8iHhNYMw",       
            ),
            InlineKeyboardButton(
                text="˹ᴛғ ᴡᴏʀʟᴅ˼", url="https://t.me/+MQn7rXz1LeViZmJl",
            )
        ],
    ]
    return upl


def aq_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
    ]
    return buttons
