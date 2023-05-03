WORK IN PROGRESS MAY NOT WORK 


# Tautulli-Discord Bot

This is a simple bot that retrieves data from Tautulli and posts it to Discord. 

Please note that this code is a work in progress and may give errors that I've yet to fix.
## Prerequisites

Before you can use this bot, you need to have the following:

- Tautulli running on your media server
- A Tautulli API key
- Discord running and a bot token created
- Discord channel IDs where you want to post the updates

## Installation

1. Clone the repository to your local machine:

   ```sh
   git clone https://github.com/Rfkgaming89/Tautulli-to-discord.git
   ```

2. Install the required packages:

   ```sh
   pip install requests discord.py
   ```

3. Edit the `bot.py` file and replace the following values:

   - `TAUTULLI_API_KEY`: Your Tautulli API key
   - `DISCORD_BOT_TOKEN`: Your Discord bot token
   - `BANDWIDTH_CHANNEL_ID`: The channel ID where you want to post the bandwidth updates
   - `TRANSCODE_CHANNEL_ID`: The channel ID where you want to post the transcode updates
   - `MOVIES_CHANNEL_ID`: The channel ID where you want to post the movies updates
   - `TVSHOWS_CHANNEL_ID`: The channel ID where you want to post the TV shows updates

4. Run the bot:

   ```sh
   python bot.py
   ```

   The bot will start running and will post updates to the specified Discord channels every 5 minutes.

## Usage

Once the bot is running, it will automatically retrieve data from Tautulli and post updates

Contributing

Feel free to contribute to this project by submitting issues, feature requests, or pull requests.
