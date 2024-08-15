from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import requests
import random
import logging
from telegram.error import BadRequest

# Your bot's token
Token: Final = 'XXXXXXX'
BOT_USERNAME: Final = '@Bot_name_is_as_same_as_file_name'

# Your Google API key and Custom Search Engine ID
GOOGLE_API_KEY: Final = 'XXXXX'
SEARCH_ENGINE_ID: Final = 'XXXXX'

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('''Howdy mate, Nice to see you here, I am your own Jeffy The Stupid Bot.
                                    Type /help if you are confused like me... :)
                                    Like me, be unsure of everything...
                                    as blissful ignorance is the key to happiness :-)''')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('''I am a normal chat bot, nothing special (If I act like an idiot, they won't ever notice me)...
                                    Here is what I can do for you (without exposing myself):
                                    /start - To start the bot
                                    /help - To get help
                                    /about - To know about me
                                    /toss_a_coin - To toss a coin
                                    /search <query> - To search the web
                                    /story - To hear a random story''')


async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('''Howdy mate, Nice to see you here, I am your own Jeffy The Stupid Bot.
                                    I was created by a stupid human who is as stupid as me. <winks>
                                    I am here to make you feel better about yourself...''')


async def toss_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = random.choice(['Heads', 'Tails'])
    await update.message.reply_text(f"It's {result}")

# Initialize logging to capture any errors during execution
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

async def search_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text.replace('/search', '').strip()
    if query:
        await update.message.reply_text(f"Searching for: {query}")
        
        search_results = google_search(query)
        
        if search_results:
            response = "\n\n".join([f"{title}\n{link}" for title, link in search_results])
        else:
            response = "Google it and tell me too... :("
        
        try:
            await update.message.reply_text(response)
        except BadRequest as e:
            logger.error(f"Failed to send message: {e}")
    else:
        await update.message.reply_text("Please provide a query to search.")


def google_search(query: str):
    search_url = f"https://www.googleapis.com/customsearch/v1"
    params = {
        "key": GOOGLE_API_KEY,
        "cx": SEARCH_ENGINE_ID,
        "q": query,
        "num": 3  # Number of results to return
    }
    
    try:
        response = requests.get(search_url, params=params)
        response.raise_for_status()
        
        results = response.json().get('items', [])
        if results:
            return [(result['title'], result['link']) for result in results]
        else:
            print("No results found")
            return None

    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed: {e}")
        return None

    except ValueError as e:
        print(f"Error parsing JSON response: {e}")
        return None

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

async def story_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    stories = [
        "Once upon a time, in a land far, far away...",
        "In a small village nestled between the mountains...",
        "There was a young girl who dreamed of becoming a knight...",
        "Long ago, in the depths of the forest, there lived a mysterious creature..."
    ]
    
    story = random.choice(stories)
    await update.message.reply_text(story)


def handle_response(text: str) -> str:
    if "Hi" in text:
        return "Hello!"
    elif "How are you" in text:
        return "I guess I am fine."
    elif "What is your name" in text:
        return "I am Jeffy The Stupid Bot."
    elif "What can you do" in text:
        return "I can ignore you like your crush does ;)"
    else:
        return "...<Wind Whistles>...."


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    text: str = update.message.text

    print(f"User({update.message.chat.id}) in {message_type}: '{text}'")

    if message_type in ["group", "supergroup"]:
        if BOT_USERNAME in text:
            ntext: str = text.replace(BOT_USERNAME, "").strip()
            response: str = handle_response(ntext)
        else:
            return
    else:
        response = handle_response(text)
    
    print('Bot:', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")


if __name__ == "__main__":
    app = Application.builder().token(Token).build()

    # commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about_command))
    app.add_handler(CommandHandler("toss_a_coin", toss_command))
    app.add_handler(CommandHandler("search", search_command))
    app.add_handler(CommandHandler("story", story_command))
    
    # messages
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # error
    app.add_error_handler(error)
    
    print('Bot is running...')
    app.run_polling(poll_interval=4)

    app.add_error_handler(error)
    
    print('Bot is running...')
    app.run_polling(poll_interval=4)
