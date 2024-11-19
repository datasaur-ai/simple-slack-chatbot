# Datasaur Simple Slack Chatbot

Before getting started, make sure you have a development workspace where you have permissions to install apps. If you don’t have one setup, go ahead and [create one](https://slack.com/create).

## Installation

#### Create a Slack App
1. Open [https://api.slack.com/apps/new](https://api.slack.com/apps/new) and choose "From an app manifest".
2. Choose the workspace you want to install the application to.
3. Copy the contents of [manifest.json](./manifest.json) into the text box that says `*Paste your manifest code here*` (within the JSON tab) and click *Next*.
4. Review the configuration and click *Create*.
5. Click *Install to Workspace* and *Allow* on the screen that follows. You'll then be redirected to the App Configuration dashboard.

#### Setup Environment Variables
Before you can run the app, you'll need to store some environment variables.

1. Copy .env.example to .env and replace the placeholder values with your bot token and app token.
2. Click **OAuth & Permissions** in the left hand menu and follow the steps in the OAuth Tokens section to install the OAuth. Copy the Bot User OAuth Token and store it in your environment as `SLACK_BOT_TOKEN`.
3. Click **Basic Information** from the left hand menu and follow the steps in the App-Level Tokens section to create an app-level token with the `connections:write` scope. Copy this token and store it in your environment as `SLACK_APP_TOKEN`.


```zsh
# Replace with your app token and bot token
SLACK_BOT_TOKEN=<your-bot-token>
SLACK_APP_TOKEN=<your-app-token>
```

#### Setup Your Local Project

1. Install Python 3.9 or later (alternatively, you can install [Miniconda](https://docs.anaconda.com/miniconda/install/#quick-command-line-install) to manage your Python version).
  
2. Run the start script.

```zsh
bash start.sh
```

