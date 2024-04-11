from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from tgbot.handlers.onboarding.manage_data import SECRET_LEVEL_BUTTON
from tgbot.handlers.onboarding.static_text import creator_tg, creator_insta, registration


def make_keyboard_for_start_command() -> InlineKeyboardMarkup:
    buttons = [[
        InlineKeyboardButton(creator_tg, url="https://t.me/AlisherPY"),
        InlineKeyboardButton(creator_insta, url="https://www.instagram.com/alisher_py"),
    ],
        [
            InlineKeyboardButton(registration, callback_data='register_me')

        ]
    ]

    return InlineKeyboardMarkup(buttons)
