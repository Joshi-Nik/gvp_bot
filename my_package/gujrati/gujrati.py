import logging

from telegram import __version__ as TG_VER

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

# if __version_info__ < (20, 0, 0, "alpha", 1):
#     raise RuntimeError(
#         f"This example is not compatible with your current PTB version {TG_VER}. To view the "
#         f"{TG_VER} version of this example, "
#         f"visit https://github.com/python-telegram-bot/python-telegram-bot/tree/v{TG_VER}/examples"
#     )
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters


async def gujrati_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Prompt same text & keyboard as `start` does but not as new message"""
    # Get CallbackQuery from Update
    # query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    # await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("ગુજરાત વિદ્યાપીઠ વિશે", callback_data='2.1')
        ],
        [
            InlineKeyboardButton("શૈક્ષણિક કાર્યક્રમો", callback_data='2.2'),
            InlineKeyboardButton("વહીવટ", callback_data='2.3')
        ],
        [
            InlineKeyboardButton("પુસ્તકાલય", callback_data='2.4'),
            InlineKeyboardButton("રમતગમત", callback_data='2.5')
        ],
        [
            InlineKeyboardButton("આગામી કાર્યક્રમ", callback_data='2.6'),
            InlineKeyboardButton("ગ્રામીણ કેન્દ્ર", callback_data='2.7')
        ],
        [
            InlineKeyboardButton("KVK", callback_data='2.8'),
            InlineKeyboardButton("મ્યુઝિયમ", callback_data='2.9')
        ],
        [
            InlineKeyboardButton("હેરિટેજ વોક", callback_data='2.10')
        ],
        [
            InlineKeyboardButton("પાછળ", callback_data='0')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # await update.message.reply_text("Start handler, Choose a route", reply_markup=reply_markup)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="તમે ગુજરાતી ભાષા પસંદ કરી છે",reply_markup=reply_markup)

