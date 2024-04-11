import datetime

from django.utils import timezone
from telegram import ParseMode, Update
from telegram.ext import CallbackContext, ConversationHandler
import re

from tgbot.handlers.onboarding import static_text
from tgbot.handlers.utils.info import extract_user_data_from_update
from tgbot.states import GET_numer, GET_Full_name
from users.models import User
from xitoy_cargo.models import Client
from tgbot.handlers.onboarding.keyboards import make_keyboard_for_start_command


def command_start(update: Update, context: CallbackContext) -> None:
    u, created = User.get_user_and_created(update, context)

    if created:
        text = static_text.start_created.format(first_name=u.first_name)
    else:
        text = static_text.start_not_created.format(first_name=u.first_name)

    update.message.reply_text(text=text,
                              reply_markup=make_keyboard_for_start_command())


def secret_level(update: Update, context: CallbackContext) -> None:
    # callback_data: SECRET_LEVEL_BUTTON variable from manage_data.py
    """ Pressed 'secret_level_button_text' after /start command"""
    user_id = extract_user_data_from_update(update)['user_id']
    text = static_text.unlock_secret_room.format(
        user_count=User.objects.count(),
        active_24=User.objects.filter(updated_at__gte=timezone.now() - datetime.timedelta(hours=24)).count()
    )

    context.bot.edit_message_text(
        text=text,
        chat_id=user_id,
        message_id=update.callback_query.message.message_id,
        parse_mode=ParseMode.HTML
    )


def Name_Handler(update, context):
    full_name = update.message.text.strip()
    name_parts = full_name.split()
    if len(name_parts) == 2:
        context.user_data['Full_name'] = full_name
        update.message.reply_text(
            text=f"{full_name} Saqlandi !\n📞Bog'lanish uchun telefon raqamingizni yozing..\n(namuna: +998903332211)")
        return GET_numer
    else:
        update.message.reply_text("Xato! Ism va familiyangizni to'liq kiriting (namuna: Alisher Axmadov).")
        return GET_Full_name


def Phone_number_handler(update, context):
    message_text = update.message.text
    if re.match(r"^\d{12}$", message_text):
        context.user_data["NUMBER"] = message_text


        if not Client.objects.filter(telegram_id=update.message.from_user.id).exists():
            Client.objects.create(telegram_id=update.message.from_user.id,
                                  fullname=context.user_data["Full_name"],
                                  phone_number=context.user_data["NUMBER"] ,
                                  )
            update.message.reply_text(
                f"☎️ +{message_text} Saqlandi !\n✔️Ro'yxatdan o'tish yakunlandi.\nSiz bosh menyudasiz!")
        else:
            client=Client.objects.get(telegram_id=update.message.from_user.id)
            client.full_name=context.user_data["Full_name"]
            client.phone_number=context.user_data["NUMBER"]
            client.save()
            update.message.reply_text(
                f"☎️ +{message_text} Malumotlar yangilandi rahmat !")
        return ConversationHandler.END
    else:
        update.message.reply_text(
            "Xato!\nQaytadan uruning,Telefon raqamni to'g'ri kiriting \n(12 ta raqam,masalan: +998903332211).")
        return GET_numer

def got_register(update: Update, context: CallbackContext) -> None:

    context.bot.send_message(
        chat_id=update.callback_query.message.chat_id,
        text="Ism familiyanggizni to'liq kiriting...",
    )
    return GET_Full_name
