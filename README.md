# ClearPostBot: Telegram Bot for Managing Text-Only Posts

## Project Description

ClearPostBot is a Telegram bot developed for a client on the **Kwork** platform. The bot's main purpose is to monitor real-time posts in Telegram channels and automatically delete messages containing only text (without images, videos, or other attachments). The bot offers the following features:

- Monitors published posts in Telegram channels where it has administrator rights.
- Automatically deletes text-only posts with no multimedia content.
- Operates exclusively in channels where it is assigned as an administrator.
- Simple to set up and use, leveraging modern libraries like `aiogram 3` and `envirosn`.

## Features

### Real-Time Monitoring
- The bot processes `channel_post` updates in real time to identify new posts.

### Automatic Deletion of Text-Only Messages
- If a post contains only text without attachments (images, videos, documents), the bot deletes it automatically.

### Administrator Rights Validation
- The bot only performs its tasks in channels where it has the necessary administrator rights.

### Ease of Deployment
- Utilizes a virtual environment (`.venv`) and systemd service for seamless automatic startup.

## Technologies Used

- **Python 3.9+**
- **aiogram 3**: A modern, asynchronous library for building Telegram bots.
- **envirosn**: A convenient tool for managing environment variables.
- **Systemd**: For running the bot as a system service.

## Kwork Case Study

This project was completed for a client on the **Kwork** platform. The task involved developing a Telegram bot with the above-mentioned functionality and setting up a system service for automatic deployment. All client requirements were successfully met, the bot was thoroughly tested, and the final solution was delivered.
