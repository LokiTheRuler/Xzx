from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

TOKEN = "8340967995:AAEKWqKZ-iE8ulzRbdHBJHoWcyeYi2MLgPI"  # Replace with your token
MAX_REACTIONS = 5  # Max reactions per post

# Track reactions (in-memory storage)
reaction_counts = {}

def auto_react(update: Update, context: CallbackContext):
    message = update.message
    chat_id = message.chat_id
    message_id = message.message_id

    # Unique key for each message
    key = f"{chat_id}_{message_id}"

    # Check if reaction limit reached
    if key in reaction_counts:
        if reaction_counts[key] >= MAX_REACTIONS:
            return  # Skip if limit reached
        reaction_counts[key] += 1
    else:
        reaction_counts[key] = 1

    # React with 👍 emoji
    context.bot.set_message_reaction(
        chat_id=chat_id,
        message_id=message_id,
        reaction=["👍","🔥", "❤️","🎉","🤣"],  # Change to any emoji (e.g., "🔥", "❤️")
        is_big=False
    )

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    # Auto-react to all non-command messages
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, auto_react))

    print("🤖 Bot is running...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
