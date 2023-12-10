from pyrogram.types import InlineKeyboardButton

import config
from AnonXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url="https://t.me/+MQn7rXz1LeViZmJl"),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text=_["S_B_5"], "user_id=1777270311"),
            InlineKeyboardButton(text=_["S_B_2"], url="https://t.me/+MQn7rXz1LeViZmJl"),
        ],
        [
            InlineKeyboardButton(text=_["S_B_6"], url="https://t.me/+PtOLQT04ocMzOTJl"),
            InlineKeyboardButton(text=_["S_B_7"], url="https://t.me/+m4oVCt2zFhYyMTdl"),
        ],
    ]
    return buttons
