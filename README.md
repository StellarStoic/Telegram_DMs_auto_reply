# Telegram DMs Auto-Reply Bot

This repository contains a Python script that uses the **Telethon** library to create a Telegram auto-reply bot for handling direct messages (DMs). The bot automatically replies to incoming DMs with a custom predefined message. This solution is ideal if you're not so active on Telegram and want to inform others in a friendly, automated way.

## Why Not Use BotFather?

**BotFather** is the official way to create Telegram bots, but it has certain limitations:
- **BotFather Bots can’t access personal chats (DMs)**: Telegram bots created via BotFather cannot read or reply to messages from normal user accounts. They can only function in groups, channels, or as standalone bots where people send commands directly to them.

**Telethon**, on the other hand, allows us to log in with a **user account** and monitor incoming personal messages (DMs). It provides the flexibility to auto-reply to users as if it were from your personal Telegram account.

## What This Script Does

- Automatically replies to personal messages (DMs) sent to your Telegram account with a predefined message.
- You can set a timer in minutes how long the scrypt will ignore received messages so it won't reply to every message. 
- After the first login (where you enter your phone number and receive a verification code via Telegram or SMS), it saves the session file, so you don’t need to re-authenticate on each script run.
- Handles reconnections, so the bot can run continuously even after a network outage or server reboot.

## Prerequisites

- **Python 3.7 or later**
- **Linux Server or Raspberry Pi** (can also run locally on any machine with Python installed)

## Step-by-Step Setup

### Get Your Telegram API ID and API Hash
To interact with the Telegram API as a user, you need to create an application and obtain your API ID and API Hash from the Telegram API page:

Go to https://my.telegram.org/auth.
Log in with your Telegram account. (Phone number)
Under "API Development Tools", create a new application.
Note down your API ID and API Hash.

### Install Required Libraries

You’ll need the following Python libraries:
- **Telethon** (to interact with the Telegram API)
- **python-dotenv** (to manage environment variables for API credentials)

To install these libraries, run the following commands:

```pip install -r requirements.txt```


#### Set Up Your Environment Variables
Create a .env file in the same directory as your script. This file will securely store your API ID, API Hash.

Example .env file:

API_ID=your_api_id_here
API_HASH=your_api_hash_here

### First-Time Script Setup

Now, you’re ready to run the script for the first time.

```python ./telegram_DMsReplyBot.py```

What Happens During the First Run:
Enter Your Phone Number: When you run the script, it will prompt you to enter your phone number (including country code).
Enter the Verification Code: After entering the phone number, you will receive a verification code via the Telegram app or SMS. Enter this code.
Session File Creation: Once authenticated, Telethon will create a session_name.session file. This file securely stores your session information so you don’t need to re-enter your phone number or verification code again in future runs.

### What Is the Session File?
The session_name.session file stores your login credentials and session state with Telegram. This allows the script to:

Automatically re-authenticate without needing your phone number and code again in cases like server reboots, power outages, or script restarts.


Feel free to fork the repository and contribute improvements!