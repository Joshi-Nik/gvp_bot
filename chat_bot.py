import time
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CallbackContext, CommandHandler
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from telegram import ForceReply, Update
from datetime import datetime
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
)
from telegram import InlineKeyboardButton,InlineKeyboardMarkup
from my_package.English.english import english_button
from my_package.gujrati.gujrati import gujrati_button
from my_package.English.about import about_us
from my_package.English.academic import academic
from my_package.English.administration import administration
from my_package.English.library import library
from my_package.English.pg import pg
from my_package.English.ug import ug
from my_package.English.certificate import certificate
from my_package.English.diploma import diploma
from my_package.English.mca import mca
from my_package.English.admission import admission
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
    rf"Available Languages",
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


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
   
    query = update.callback_query

    await query.answer()

    # await query.edit_message_text(text=f"Selected option: {query.data}")
    button_choice=query.data
    print(type(button_choice))
    if button_choice=='1':
        await english_button(update, context)
    if button_choice=='2':
        await gujrati_button(update, context)


    if button_choice=='1.1':
        await about_us(update,context)
    if button_choice=='1.2':
        await academic(update,context)
    if button_choice=="1.3":
        await administration(update, context)
    if button_choice=='1.4':
        await library(update,context)
    if button_choice=='1.2.1':
        await ug(update,context)
    if button_choice=='1.2.2':
        await pg(update,context)
    if button_choice=='1.2.3':
        await certificate(update,context)
    if button_choice=='1.2.4':
        await diploma(update,context)
    if button_choice=='1.2.2.1':
        await mca(update,context)
    if button_choice=='1.2.2.1.1':
        await admission(update,context)
    
    # About us
    if button_choice=='1.1.1':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="Click The Following Link. https://www.gujaratvidyapith.org/overview.htm")
    if button_choice=='1.1.2':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="Click The Following Link. https://www.gujaratvidyapith.org/history.htm")
    if button_choice=='1.1.3':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="Click The Following Link. https://www.gujaratvidyapith.org/roadmap.htm")
    if button_choice=='1.1.4':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="Click The Following Link. https://www.gujaratvidyapith.org/values.htm")
    if button_choice=='1.1.5':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="Click The Following Link. https://www.gujaratvidyapith.org/emblem.htm")
    if button_choice=='1.1.6':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="Click The Following Link. https://www.gujaratvidyapith.org/annualreportsaccounts.htm")
    if button_choice=='1.1.7':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="Activities : Gram Jivan Padyatra For More Information Click On Heritage Walk ")
    if button_choice=='1.1.8':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="Click The Following Link. https://gujaratvidyapith.org/newsandevents/IIQA%20Undertaking.pdf")

    if button_choice=='1.2.2.1.2':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="To Check Syllabus Click The Following Link. https://gujaratvidyapith.org/dcs/syllabus.php")
    if button_choice=='1.2.2.1.3':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="For Faculty Details Click The Following Link. https://gujaratvidyapith.org/computerscience.htm")
    if button_choice=='1.2.2.1.4':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="FACILITIES PROVIDED BY DEPARTMENT OF COMPUTER SCIENCE")
         await context.bot.send_message(chat_id=update.effective_chat.id, text="Software Development : https://gujaratvidyapith.org/dcs/swlab.php")
         await context.bot.send_message(chat_id=update.effective_chat.id, text="Internet of Things : https://gujaratvidyapith.org/dcs/iotlab.php")
         await context.bot.send_message(chat_id=update.effective_chat.id, text="Machine Learning : https://gujaratvidyapith.org/dcs/mllab.php")
         await context.bot.send_message(chat_id=update.effective_chat.id, text="Cyber Security : https://gujaratvidyapith.org/dcs/cslab.php")
         await context.bot.send_message(chat_id=update.effective_chat.id, text="Library : https://gujaratvidyapith.org/dcs/library.php")

    if button_choice=="1.2.2.1.5":
        await context.bot.send_message(chat_id=update.effective_chat.id, text="For Placement Details Click on this link : https://gujaratvidyapith.org/dcs/placement.php")
    
    if button_choice=='1.2.2.1.1.3':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="INTAKE : 60 Students")
    if button_choice=='1.2.2.1.1.4':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="DURATION : 2 Years (Four Semester)")
    if button_choice=='1.2.2.1.1.1':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="FEES : Approx 10,000 /- Per Year..")
    if button_choice=='1.2.2.1.1.2':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="ELIGIBILITY : BCA / Bachelor Degree in Computer Science, Engineering or Equivalent Degree. OR B.Sc. / B.Com. / B.A. with mathematics at 10+2 level or at Graduation level (With additional bridge courses as per the norms of the concerned university). Obtained at least 50% marks (45% marks in case of candidates belonging to reserved category) in the qualifying examination.")

    #Administration
    if button_choice=='1.3.1':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="For Information of Governing Council Click on this link: https://gujaratvidyapith.org/admin.htm")
    if button_choice=='1.3.2':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="For Information about Chancellors Click on this link: https://gujaratvidyapith.org/chancellor.htm")
    if button_choice=='1.3.3':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="For Information about Vice-Chancellors Click on this link: https://gujaratvidyapith.org/vice-chancellors.htm")
    if button_choice=='1.3.4':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="For Information about Registrars Click on this link: https://gujaratvidyapith.org/registrars.htm")

    #Library

    if button_choice=='1.4.1':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="Central Library Information : https://gujaratvidyapith.org/centrallibrary.htm")
    if button_choice=='1.4.2':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="Online Library Access  : http://192.168.205.201/webopac/")
    if button_choice=='1.4.3':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="Book Catalogue Searching : http://library.gujaratvidyapith.org/LibrarySystem/")
    if button_choice=='1.4.4':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="Membership Registration Form : http://links.gujaratvidyapith.org/LibrarySystem/MembershipRegistrationform.pdf")
    if button_choice=='1.4.5':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="Book Purchase Request Form : http://links.gujaratvidyapith.org/LibrarySystem/BookPurchaseRequestForm.pdf")
    
    #sports
    
    if button_choice=='1.5':
         await context.bot.send_message(chat_id=update.effective_chat.id, text="Ahmedabad and two other campuses have running track of 400 mtr. There are different grounds for outdoor sports such as Volleyball, Basketball, Handball, Kabaddi, Kho-Kho, Badminton, and Netball. In addition, Vidyapith also has Gymnasium and Swimming pool. All these facilities are being utilised by students, staff and also by citizens.\n\nSadra campus has well known, well developed physical education college where B.PEd and M.PEd courses are offered. There are separate grounds for Cricket, Volleyball, Basketball and Football. A big Gymnasium hall of national standard prepares the students to compete at higher level. A big open stadium is also available at Sadra campus. A well facilitated indoor stadium for Tennis, Carom, and Weight lifting is also available. The impressive facilities of the physical education department including a large variety of sports and necessary equipment for students under the able guidance and supervision of highly qualified teachers acts as a positive incentive for the students.\n\nGujarat Vidyapith have 4 Multipurpose Play Ground, 1 Tennis, 7 Volley Ball, 2 Basket Ball, 2 Hand Bal, 4 Kabaddi, 2 Kho-Kho, 3 Badminton and 1 Net Ball Courts for Indoor and Outdoor games. 2 400 meters Tracks and Fields, 2 Gymnasium and 2 Outdoor Stadium.")

    #up coming program

    if button_choice=='1.6':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="UPCOMING PROGRAM : ")

    #Rural center
    if button_choice=='1.7':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="UPCOMING PROGRAM : ")

    #KVK
    if button_choice=='1.8':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="UPCOMING PROGRAM : ")

    #Meseum
    if button_choice=='1.9':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="UPCOMING PROGRAM : ")

    #heritage walk
    if button_choice=='1.10':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="UPCOMING PROGRAM : ")

    if button_choice=='0':
        await back(update,context)
        

async def reply(update: Update, context: CallbackContext):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Click . /start")


async def back(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton("English", callback_data="1"),
            InlineKeyboardButton("ગુજરાતી", callback_data="2"),
        ],
        [InlineKeyboardButton("हिन्दी", callback_data="3")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_message(chat_id=update.effective_chat.id,text="Please Choose Language:", reply_markup=reply_markup)

if __name__ == '__main__':
    application = ApplicationBuilder().token('5329459226:AAFmA9lwqHDhb1kdmvM97sBTwVEhJm0ca7Q').build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    application.add_handler(CallbackQueryHandler(button))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,reply))
    
    application.run_polling()