from typing import Final


from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os
from downloader import download_video

#telegram bot details
TOKEN: Final= "7399519009:AAFpSSS7BBpF_PRxAQkHd75HcouWytJq0_U"
BOT_USERNAME: Final = "@KOS_YT_ARCHbot"

#Bot functions
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello there! Send me a YouTube URL and I'll download the video for you.")

async def download_video_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    url = update.message.text
    await update.message.reply_text('Downloading the video...')


    download_path = os.path.join(os.getcwd(), 'downloads')
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    result_message = download_video(url, download_path)
    await update.message.reply_text(result_message)






def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download_video_command))

    application.run_polling()

if __name__ == '__main__':
    main()
