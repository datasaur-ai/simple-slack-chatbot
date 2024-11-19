# Datasaur Simple Slack Chatbot

Before getting started, make sure you have a development workspace where you have permissions to install apps. If you don’t have one setup, go ahead and [create one](https://slack.com/create).

## Installation

### Create a Slack App
1. Open [https://api.slack.com/apps/new](https://api.slack.com/apps/new) and choose "From an app manifest".
2. Choose the workspace you want to install the application to.
3. Copy the contents of [manifest.json](./manifest.json) into the text box that says `*Paste your manifest code here*` (within the JSON tab) and click *Next*.
4. Review the configuration and click *Create*.
5. Click *Install to Workspace* and *Allow* on the screen that follows. You'll then be redirected to the App Configuration dashboard.

### Setting Up Environment Variables
Before running the app, follow these steps to configure the necessary environment variables:

1. Prepare the `.env` file
   - Duplicate the `.env.example` file and rename it to `.env`.  
   - Open the `.env` file and replace the placeholder values with your actual **bot token** and **app token**.
2. Get the Bot User OAuth Token
   - In the Slack web app, go to **OAuth & Permissions** from the left-hand menu.  
   - Follow the instructions in the **OAuth Tokens** section to install the OAuth.  
   - Copy the **Bot User OAuth Token** and save it in your `.env` file as:  
     ```zsh
     SLACK_BOT_TOKEN=<your-bot-token>
     ```
3. Create and Store the App-Level Token
   - Navigate to **Basic Information** in the left-hand menu.  
   - Under the **App-Level Tokens** section, create a new token with the `connections:write` scope.  
   - Copy this token and save it in your `.env` file as:  
     ```zsh
     SLACK_APP_TOKEN=<your-app-token>
     ```

### Setup Your Local Project
1. Install Python 3.9 or later (alternatively, you can install [Miniconda](https://docs.anaconda.com/miniconda/install/#quick-command-line-install) to manage your Python version).
2. Run the start script.
    ```zsh
    ./start.sh
    ```

