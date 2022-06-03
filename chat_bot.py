import time
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CallbackContext, CommandHandler
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from telegram import ForceReply, Update
from datetime import datetime
from telegram import InlineKeyboardButton,InlineKeyboardMarkup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: CallbackContext):
    user = update.effective_user
    currentTime = time.strftime('%H:%M')
    hour = datetime.now().hour
    if hour < 12 :
        await update.message.reply_html(
            rf"Hi.. {user.mention_html()}, Good Morning ",
            reply_markup=ForceReply(selective=True),
        )
    
    if hour > 12 :
            await update.message.reply_html(
            rf"Hi.. {user.mention_html()}, Good Afternoon",
            reply_markup=ForceReply(selective=True),
        )
    if hour > 18 :
            await update.message.reply_html(
            rf"Hi.. {user.mention_html()}, Good Evening",
            reply_markup=ForceReply(selective=True),
        )

    await update.message.reply_html(
    rf"I'm Gujarat Vidyapith Student Assistent. I Will Help You With Every Information About Gujarat Vidyapith. https://www.gujaratvidyapith.org",
    reply_markup=ForceReply(selective=True),
    )

    await update.message.reply_html(
    rf"How May I Help You Today ?",
    reply_markup=ForceReply(selective=True),
    )

    await update.message.reply_html(
    rf"Select Your Language : ",
    reply_markup=ForceReply(selective=True),
    )

    
    keyboard = [
        [
            InlineKeyboardButton("English", callback_data="1"),
            InlineKeyboardButton("ગુજરાતી", callback_data="2"),
        ],
        [InlineKeyboardButton("हिन्दी", callback_data="3")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Please choose:", reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
   
    query = update.callback_query

    await query.answer()

    await query.edit_message_text(text=f"Selected option: {query.data}")

    

async def reply(update: Update, context: CallbackContext):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm Akhil!")

if __name__ == '__main__':
    application = ApplicationBuilder().token('5329459226:AAFmA9lwqHDhb1kdmvM97sBTwVEhJm0ca7Q').build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,reply))

    
    application.run_polling()