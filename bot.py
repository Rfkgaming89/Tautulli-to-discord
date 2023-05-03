import requests
import json
import time
import discord

# Tautulli API endpoint and parameters
tautulli_url = 'http://localhost:8181/api/v2'
tautulli_apikey = 'YOUR_TAUTULLI_API_KEY'
tautulli_payload = {'apikey': tautulli_apikey, 'cmd': 'get_activity'}

# Discord bot token and channel IDs
discord_bot_token = 'YOUR_DISCORD_BOT_TOKEN'
bandwidth_channel_id = 'CHANNEL_ID_FOR_BANDWIDTH'
transcode_channel_id = 'CHANNEL_ID_FOR_TRANSCODE'
movies_channel_id = 'CHANNEL_ID_FOR_MOVIES'
tvshows_channel_id = 'CHANNEL_ID_FOR_TVSHOWS'

# Create a Discord client
client = discord.Client()

# Coroutine function to post a message to a Discord channel
async def post_to_discord(channel_id, message):
    channel = await client.fetch_channel(channel_id)
    await channel.send(message)

# Event handler for when the bot is ready
@client.event
async def on_ready():
    print('Logged in as', client.user.name)

    # Loop forever, updating every 5 minutes
    while True:
        # Retrieve activity data from Tautulli
        response = requests.get(tautulli_url, params=tautulli_payload)
        if response.status_code != 200:
            print('Error retrieving data from Tautulli:', response.text)
            continue
        data = response.json()['response']['data']

        # Extract relevant data
        bandwidth = round(data['stream_count'] * data['stream_bandwidth'], 2)
        transcode = data['stream_count_transcode']
        movies = data['library_media_count']['movie']
        tvshows = data['library_media_count']['episode']

        # Post messages to Discord channels
        await post_to_discord(bandwidth_channel_id, f'Bandwidth: {bandwidth} Mbps')
        await post_to_discord(transcode_channel_id, f'Transcode: {transcode}')
        await post_to_discord(movies_channel_id, f'Movies: {movies}')
        await post_to_discord(tvshows_channel_id, f'TV Shows: {tvshows}')

        # Wait 5 minutes before updating again
        time.sleep(300)

# Start the Discord client
client.run(discord_bot_token)
