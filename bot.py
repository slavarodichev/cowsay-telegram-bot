import random
import subprocess
import os

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    ContextTypes,
    filters,
)

# ВСТАВЬ СЮДА НОВЫЙ ТОКЕН ОТ BOTFATHER
TOKEN = os.getenv("TOKEN")


# временные цитаты (потом заменим на твои)
QUOTES = [
    "ты справляешься",
    "можно медленно",
    "ты не обязан быть идеальным",
    "твоя работа важна",
    "ценю то, что ты делаешь для других.",
    "горжусь твоими достижениями.",
    "доверяю твоим чувствам.",
    "счастье знать, что ты есть.",
    "проси, пожалуйста, о помощи.",
    "мне нравится, как ты действуешь.",
    "твоя безопасность – самое важное.",
    "доверяю твоему вкусу.",
    "ценю твое внимание.",
    "выбирай себя.",
    "уважаю твои принципы.",
    "поддерживаю твою интуицию.",
    "ты заслуживаешь безусловное принятие и любовь.",
    "ты имеешь право думать по-своему.",
    "не оставайся в одиночестве, когда тебе сложно.",
    "каждая ошибка помогает тебе и другим узнать больше.",
    "ты можешь жить в своем темпе.",
]


message_counter = 0


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    global message_counter
    message_counter += 1

    print("Сообщений:", message_counter)

    if message_counter % 30 == 0:

        quote = random.choice(QUOTES)

        cow = subprocess.run(
            ["cowsay", quote],
            capture_output=True,
            text=True
        ).stdout


        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=cow
        )


def main():

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )

    print("Бот запущен")

    app.run_polling()


if __name__ == "__main__":
    main()
