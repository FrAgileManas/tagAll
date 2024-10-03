# Group Tagging Bot for WhatsApp Web

## Description

The **TagAll** is a Python-based automation tool designed to make tagging members in a WhatsApp Web group quick and easy. It automatically tags all members in the group, regardless of their position, helping you save time during group mentions.

## Features

- Automatically tags all members in a WhatsApp group using the "@" mention symbol.
- Easy to use with a simple setup process.
- A brief 5-second delay allows you to position the cursor in the WhatsApp input box before the bot starts tagging.
  
## How It Works

1. **Input Group Size:** The bot prompts you to enter the total number of members in the group (including yourself).
2. **5-Second Delay:** After starting the script, you'll have 5 seconds to place your cursor in the input field of the WhatsApp Web chat window.
3. **Automated Tagging:** The bot will automatically type the "@" symbol and tag each member one by one.
4. **Completion:** The tagging stops after reaching the specified number of members.

## Installation

### Prerequisites

Before running the bot, ensure the following are installed:

- **Python 3.6+**
- **Required Modules:**
  - `keyboard` (can be installed via pip)

### Installation Steps

1. **Clone the Repository** or **Download the Script**:

   ```bash
   git clone https://github.com/FrAgileManas/tagAll.git
