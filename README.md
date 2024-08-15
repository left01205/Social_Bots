# Jeffy The Stupid Bot

This repository contains Jeffy The Stupid Bot, a Telegram bot built using Python. Jeffy is designed to perform various tasks and interact with users on the Telegram platform with a fun, quirky personality.

## Features

- **Start Command**: Initiates interaction with the bot.
- **Help Command**: Provides users with a list of available commands and their descriptions.
- **About Command**: Shares details about Jeffy and his purpose.
- **Toss a Coin Command**: Flips a coin and returns either "Heads" or "Tails".
- **Search Command**: Searches the web for a given query and returns the top results using the Google Custom Search API.
- **Random Story Command**: Generates and sends a random story to the user.
- **Text Response Handling**: Replies to user messages based on predefined responses.

## Installation

To set up and run Jeffy The Stupid Bot, follow these steps:

1. Clone the repository: 
    ```sh
    git clone https://github.com/your-username/jeffy-the-stupid-bot.git
    ```

2. Navigate to the project directory:
    ```sh
    cd jeffy-the-stupid-bot
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Obtain a Telegram Bot API token from the BotFather on Telegram.

5. Obtain a Google Custom Search API key and Search Engine ID by creating a project on the Google Cloud Console.

6. Update the bot's configuration:
   - Replace `Token` in the code with your Telegram Bot API token.
   - Replace `GOOGLE_API_KEY` and `SEARCH_ENGINE_ID` with your Google API key and Custom Search Engine ID, respectively.

7. Run the bot:
    ```sh
    python bot.py
    ```

## Usage

Once the bot is up and running, you can interact with it on Telegram. Here are some commands you can use:

- `/start` - Initiates interaction with Jeffy The Stupid Bot.
- `/help` - Provides a list of available commands and their descriptions.
- `/about` - Tells you more about Jeffy.
- `/toss_a_coin` - Flips a coin and returns either "Heads" or "Tails".
- `/search <query>` - Searches the web for the given query and returns the top 3 results.
- `/story` - Generates and sends a random short story.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or improvements for Jeffy The Stupid Bot, feel free to open an issue or submit a pull request.

---

**Note:** Ensure that your bot's API key and other sensitive information are kept secure and not shared publicly.
