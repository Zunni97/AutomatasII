#!/usr/bin/env python
# pylint: disable=unused-argument
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages

First, a few handler functions are defined. Then, those functions are passed to
the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram import ForceReply, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    mensaje = update.message.text
    if update.message.text == 'hola':
        mensaje = "Hola como estas?"
    if update.message.text == 'menu':
        keyboard = [[InlineKeyboardButton('Agendar Cita', callback_data='Agendar Cita')],
                    [InlineKeyboardButton('Contacto', callback_data='Contacto')],
                    [InlineKeyboardButton('Sobre Nosotros', callback_data='Sobre Nosotros')],
                    [InlineKeyboardButton('Salir', callback_data='Salir')]]
        menu_choices = InlineKeyboardMarkup(keyboard)
        await context.bot.send_message(
            chat_id=update.message.chat_id, text="Bienvenido a SmileWorks, estamos aqui para ayudarte con cualquier pregunta o inquietud que tengas sobre tus dientes. Por favor selecciona una de nuestras opciones:", reply_markup=menu_choices)
        
    if update.message.text == 'cita':
        keyboard_cita = [[InlineKeyboardButton('Eliminacion de Caries', callback_data='Eliminacion de Caries')],
                    [InlineKeyboardButton('Extracciones', callback_data='Extracciones')],
                    [InlineKeyboardButton('Limpieza', callback_data='Limpieza')],
                    [InlineKeyboardButton('Valoracion', callback_data='Valoracion')]]
        cita_choices = InlineKeyboardMarkup(keyboard_cita)
        await context.bot.send_message(
            chat_id=update.message.chat_id, text="¿Que tipo de Cita necesitas?", reply_markup=cita_choices)
        await update.message.reply_text(mensaje)
        return
        


# async def agendar_cita(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     """Echo the user message."""
#     mensaje = update.message.text
#     if update.message.text == 'hola':
#         mensaje = "Hola como estas?"
#     if update.message.text == 'cita':
#         keyboard = [[InlineKeyboardButton('Eliminacion de Caries', callback_data='Eliminacion de Caries')],
#                     [InlineKeyboardButton('Extracciones', callback_data='Extracciones')],
#                     [InlineKeyboardButton('Limpieza', callback_data='Limpieza')],
#                     [InlineKeyboardButton('Valoracion', callback_data='Valoracion')]]
#         cita_choices = InlineKeyboardMarkup(keyboard)
#         await context.bot.send_message(
#             chat_id=update.message.chat_id, text="¿Que tipo de Cita necesitas?", reply_markup=cita_choices)
#         return
#     await update.message.reply_text(mensaje)

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("7441348706:AAGa0AfzOPJzQNye0kj_s6VqBqS66s0bClk").build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    #application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, agendar_cita))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()