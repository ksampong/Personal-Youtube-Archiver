# Personal Youtube Archiver

This project is a Telegram bot designed for personal media preservation. The bot allows users to download YouTube videos by sending a YouTube URL to the bot. The video is then downloaded and saved locally on the machine running the bot.

## Features

- **Download YouTube Videos**: Send a YouTube URL to the bot, and it will download the video to a specified directory.
- **Telegram Bot Integration**: Easily interact with the bot via Telegram.
- **Local Storage**: Videos are saved locally on the machine where the bot is running.

## Prerequisites

- **Python 3.6+**: Ensure Python is installed on your machine.
- **Virtual Environment (optional but recommended)**: Use a virtual environment to manage dependencies.
- **Telegram Bot Token**: Create a bot using [BotFather](https://core.telegram.org/bots#botfather) on Telegram and obtain your bot token.

## Setup and Installation

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/youtube-downloader-bot.git
cd youtube-downloader-bot
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```
### 4. Run the Bot
Start the bot by running:

```bash
python tgbot.py
```
### 5. Interact with the Bot
Open Telegram and search for your bot.
Send a /start command to initiate the conversation.
Send a YouTube URL, and the bot will download the video 

## File Structure
```bash
.
├── downloader.py          # Contains the video downloading logic
├── tgbot.py               # Contains the Telegram bot logic
├── requirements.txt       # List of required Python packages
└── README.md              # Project documentation
```
## Using the Downloader Script Independently
The downloader.py script can also be used independently to download videos by running it directly:

```bash
python downloader.py
```
## Steps:
Input YouTube URL: Enter the YouTube URL when prompted.
Select Save Directory: Choose a directory where the video will be saved using a GUI file dialog.

## Deployment on Linux KVM Machine
If you are running this bot on a virtual machine (VM) on your Linux KVM setup, follow these additional steps:

### 1. Set Up the VM
Ensure your VM is configured and running with an appropriate Linux distribution.

### 2. Install Required Software on the VM
```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip
```
### 3. Clone the Repository and Set Up the Environment
```bash
git clone https://github.com/yourusername/youtube-downloader-bot.git
cd youtube-downloader-bot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### 4. Run the Bot on the VM
Start the bot by running:

```bash
python tgbot.py
```
## Contributing
This project is intended for personal use. Contributions are not expected, but feel free to fork the repository and modify it for your needs.

## License
This project is licensed under the  License.

