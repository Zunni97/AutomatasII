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
    user = update.message.from_user
    print(f"Usuario: {user.id} ha iniciado la conversación.")
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
        await update.message.reply_text(mensaje)
        await context.bot.send_message(
            chat_id=update.message.chat_id, text="", reply_markup=mensaje)
        
async def salir(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /salir is issued."""

# Send the message with menu
    await context.bot.send_message(
    chat_id=update.message.chat_id, text="Gracias por contactarnos, que tengas excelente dia.")

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /menu is issued."""

    keyboard = [[InlineKeyboardButton('Agendar Cita', callback_data='Agendar Cita')],
                    [InlineKeyboardButton('Contacto', callback_data='Contacto')],
                    [InlineKeyboardButton('Sobre Nosotros', callback_data='Sobre Nosotros')],
                    [InlineKeyboardButton('Salir', callback_data='Salir')]]
    menu_choices = InlineKeyboardMarkup(keyboard)
# Send the message with menu
    await context.bot.send_message(
    chat_id=update.message.chat_id, text="Bienvenido a SmileWorks, estamos aqui para ayudarte con cualquier pregunta o inquietud que tengas sobre tus dientes. Por favor selecciona una de nuestras opciones:", reply_markup=menu_choices)

async def contacto(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /contacto is issued."""

    keyboard = [[InlineKeyboardButton('Regresar', callback_data='Regresar')]]
    menu_choices = InlineKeyboardMarkup(keyboard)

    # Enviar la imagen desde un archivo local
    photo_file_path = "smileworks.jpg"
    await context.bot.send_photo(
        chat_id=update.message.chat_id,
        photo=open(photo_file_path, 'rb')
    )

    # Send the message with menu
    await context.bot.send_message(
    chat_id=update.message.chat_id, 
    text="Estamos ubicados en calle sexta #1447-7 (a un costado de la catedral). Telefono: (646)4877812 y (646)4877812. Buscanos en Facebook e Instagram como: Smileworks ens. Horario: Lunes - Viernes 9:00 a 19:00, Sabado - 9:00 a 15:00, Domingo: Previa Cita", 
    reply_markup=menu_choices)

async def nosotros(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /nosotros is issued."""

    keyboard = [[InlineKeyboardButton('Regresar', callback_data='Regresar')]]
    menu_choices = InlineKeyboardMarkup(keyboard)

    # Enviar la imagen desde un archivo local
    photo_file_path = "maiky.jpg"
    await context.bot.send_photo(
        chat_id=update.message.chat_id,
        photo=open(photo_file_path, 'rb')
    )

    # Send the message with menu
    await context.bot.send_message(
    chat_id=update.message.chat_id, 
    text="Nuestra mision es brindar atencion dental personalizada y de alta calidad a nuestros pacientes, con el fin de mejorar su salud bucal. Nos esforzamos por crear un ambiente seguro, confiable y amigable, donde nuestros pacientes se sientan comodos y valorados.", 
    reply_markup=menu_choices)

async def cita(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /cita is issued."""

    keyboard = [[InlineKeyboardButton('Eliminacion de Caries', callback_data='Eliminacion de Caries')],
                [InlineKeyboardButton('Extracciones', callback_data='Extracciones')],
                [InlineKeyboardButton('Limpieza', callback_data='Limpieza')],
                [InlineKeyboardButton('Valoracion', callback_data='Valoracion')],
                [InlineKeyboardButton('Regresar', callback_data='Regresar')],
                [InlineKeyboardButton('Salir', callback_data='Salir')]]
    menu_choices = InlineKeyboardMarkup(keyboard)
# Send the message with menu
    await context.bot.send_message(
    chat_id=update.message.chat_id, text="¿Que tipo de Cita necesitas?", reply_markup=menu_choices)

async def mes(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /mes is issued."""
    
    keyboard = [[InlineKeyboardButton('Julio', callback_data='Julio'),
                InlineKeyboardButton('Agosto', callback_data='Agosto')],
                [InlineKeyboardButton('Septiembre', callback_data='Septiembre'),
                InlineKeyboardButton('Mas', callback_data='Mas')],
                [InlineKeyboardButton('Regresar', callback_data='Regresar'),
                InlineKeyboardButton('Salir', callback_data='Salir')]]
    menu_choices = InlineKeyboardMarkup(keyboard)
# Send the message with menu
    await context.bot.send_message(
    chat_id=update.message.chat_id, text="Seleccione el mes para agendar su cita", reply_markup=menu_choices)

async def dia(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /dia is issued."""

    keyboard = [
    [InlineKeyboardButton('1', callback_data='1'),
     InlineKeyboardButton('2', callback_data='2'),
     InlineKeyboardButton('3', callback_data='3'),
     InlineKeyboardButton('4', callback_data='4'),
     InlineKeyboardButton('5', callback_data='5'),
     InlineKeyboardButton('6', callback_data='6'),
     InlineKeyboardButton('7', callback_data='7')],
         [InlineKeyboardButton('8', callback_data='1'),
     InlineKeyboardButton('9', callback_data='2'),
     InlineKeyboardButton('10', callback_data='3'),
     InlineKeyboardButton('11', callback_data='4'),
     InlineKeyboardButton('12', callback_data='5'),
     InlineKeyboardButton('13', callback_data='6'),
     InlineKeyboardButton('14', callback_data='7')],
         [InlineKeyboardButton('15', callback_data='1'),
     InlineKeyboardButton('16', callback_data='2'),
     InlineKeyboardButton('17', callback_data='3'),
     InlineKeyboardButton('18', callback_data='4'),
     InlineKeyboardButton('19', callback_data='5'),
     InlineKeyboardButton('20', callback_data='6'),
     InlineKeyboardButton('21', callback_data='7')],
         [InlineKeyboardButton('22', callback_data='1'),
     InlineKeyboardButton('23', callback_data='2'),
     InlineKeyboardButton('24', callback_data='3'),
     InlineKeyboardButton('25', callback_data='4'),
     InlineKeyboardButton('26', callback_data='5'),
     InlineKeyboardButton('27', callback_data='6'),
     InlineKeyboardButton('28', callback_data='7')],    
        [InlineKeyboardButton('29', callback_data='1'),
     InlineKeyboardButton('30', callback_data='2'),
     InlineKeyboardButton('31', callback_data='3')],
     [InlineKeyboardButton('Regresar', callback_data='1'),
     InlineKeyboardButton('Salir', callback_data='2')]
 ]
    menu_choices = InlineKeyboardMarkup(keyboard)
# Send the message with menu
    await context.bot.send_message(
    chat_id=update.message.chat_id, text="Selecciona el dia de tu cita", reply_markup=menu_choices)

async def horario(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /horario is issued."""
    
    keyboard = [[InlineKeyboardButton('9:00', callback_data='1'),
                InlineKeyboardButton('10:00', callback_data='2'),
                InlineKeyboardButton('11:00', callback_data='3'),
                InlineKeyboardButton('12:00', callback_data='4')],
                [InlineKeyboardButton('13:00', callback_data='1'),
                InlineKeyboardButton('14:00', callback_data='2'),
                InlineKeyboardButton('15:00', callback_data='3'),
                InlineKeyboardButton('16:00', callback_data='4')],
                [InlineKeyboardButton('17:00', callback_data='1'),
                InlineKeyboardButton('16:00', callback_data='2')],
                [InlineKeyboardButton('Regresar', callback_data='Regresar'),
                InlineKeyboardButton('Salir', callback_data='Salir')]]
    menu_choices = InlineKeyboardMarkup(keyboard)
# Send the message with menu
    await context.bot.send_message(
    chat_id=update.message.chat_id, text="Seleccione la hora de su cita:", reply_markup=menu_choices)

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("7441348706:AAGa0AfzOPJzQNye0kj_s6VqBqS66s0bClk").build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("menu", menu))
    application.add_handler(CommandHandler("contacto", contacto))
    application.add_handler(CommandHandler("nosotros", nosotros))
    application.add_handler(CommandHandler("cita", cita))
    application.add_handler(CommandHandler("mes", mes))
    application.add_handler(CommandHandler("dia", dia))
    application.add_handler(CommandHandler("horario", horario))
    application.add_handler(CommandHandler("salir", salir))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()