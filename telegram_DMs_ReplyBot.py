import os
import logging
import time
from dotenv import load_dotenv
from telethon import TelegramClient, events
from telethon.errors import FloodWaitError, RPCError
from asyncio import sleep
from datetime import datetime, timedelta


load_dotenv()


api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")

# enable/disable logging
LOGGING_ENABLED = False


if LOGGING_ENABLED:
    logging.basicConfig(
        filename="telegram_bot.log",
        level=logging.ERROR,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

# Create a client session
client = TelegramClient('session_name', api_id, api_hash)

# Dictionary to keep track of when we last replied to each user
last_replied = {}

# Define the time window (7 minutes) for ignoring repeated replies
REPLY_TIMEOUT = timedelta(minutes=7)

# Function to handle logging and retry logic
async def run_client():
    while True:
        try:
            # Start the client and log in (this will prompt for the code only once)
            await client.start()

            # Event handler for new messages (DMs)
            @client.on(events.NewMessage(incoming=True))
            async def handler(event):
                try:
                    # Check if the message is a DM (private chat)
                    if event.is_private:
                        sender_id = event.sender_id
                        current_time = datetime.now()

                        # Check if we replied to this user in the last 7 minutes
                        if sender_id in last_replied:
                            last_reply_time = last_replied[sender_id]
                            if current_time - last_reply_time < REPLY_TIMEOUT:
                                # Skip replying if we have replied in the last 7 minutes
                                return

                        # Update the last reply time for this user
                        last_replied[sender_id] = current_time

                        # The message to reply with
                        reply_message = "Hello! I am no longer active on Telegram."

                        # Send an automatic reply
                        await event.reply(reply_message)

                except Exception as e:
                    if LOGGING_ENABLED:
                        logging.error(f"Error while handling the message: {e}")

            # Keep the client running
            await client.run_until_disconnected()

        except FloodWaitError as e:
            if LOGGING_ENABLED:
                logging.error(f"Flood wait error. Sleeping for {e.seconds} seconds.")
            await sleep(e.seconds)
        except RPCError as e:
            if LOGGING_ENABLED:
                logging.error(f"RPC error occurred: {e}. Retrying in 10 seconds.")
            await sleep(10)
        except ConnectionError:
            if LOGGING_ENABLED:
                logging.error("Network connection lost. Retrying in 10 seconds.")
            await sleep(10)
        except Exception as e:
            if LOGGING_ENABLED:
                logging.error(f"Unexpected error occurred: {e}. Retrying in 10 seconds.")
            await sleep(10)

        # Short delay before retrying the connection
        time.sleep(5)

# Entry point: Start the client with retry logic
if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(run_client())
