# Nimiq miner monitor
Discord bot which helps users monitor their miners and wallet connected to SushiPool. 

## Getting Started


### Prerequisites

- Python 3.6. with IDLE (Bot written in PyCharm)
  - For required packages/libraries check Requirements.txt
- Nimiq wallet address
- Miners connected to the SushiPool
- Discord bot token 
- Own discord server
-Script:nimiq_miner_monitor.py


### Installing and running the bot
**Create own Discord server***
- For guidline--> https://support.discordapp.com/hc/en-us/articles/204849977-How-do-I-create-a-server-

**Discord bot set-up**
- Register and create application at Discord developer portal-> https://discordapp.com/developers/applications/
  - GENERAL INFORMATION: 
    - Choose name and profile picture for the bot 
    - Copy and store provided Client ID
  - BOT
    - Under Build-a-bot section select Add bot button and fill in required information
    - Copy and store provided TOKEN (Click to Reveal Token) into a folder where it is easilly accessible. You will need it to run the
      miner monitor set-up process.
  - Add a bot to a server
    - Replace in bellow provided link part 'YOUR_CLIENT_ID_HERE' with bot's Client ID. 
    https://discordapp.com/oauth2/authorize?&client_id=YOUR_CLIENT_ID_HERE&scope=bot&permissions=0
    - Select the server where you would like the bot to be addedd to and click button Authorize 
    
**Python (version above 3.6.)**
- Python IDLE
  - Download and install python from link(bot done in 3.6.5.): https://www.python.org/downloads/ 


**Running the script and installing Package requirements for script to run**
- Download zip of the project to your desktop
- Open Command Prompt (CMD) and navigate to the folder where you have download requirements.txt
  - Execute command:```pip install -r requirements.txt```
- Run nimiq_miner_monitor.py from IDLE.
  - For assistance watch the video from the link: http://www.pitt.edu/~naraehan/python3/getting_started_win_first_try.html

### Initial miner monitor set-up (Required everytime on restart)
- Once you run the nimiq_miner_monitor.py check the console for Initial set-up process. You will be asked to input following information:
  -  Please provide token for discord:  
  -  Please provide prefix you would like to have bot listening to:
  -  Provide channel ID:
    - On Discord, open your User Settings -> Appearance -> Enable Developer Mode. Right click on desired channel and select Copy ID
  -  Provide wallet address in format XXXX XXXX XXXX XXXX XXXX XXXX XXXX XXXXX
- Once everything is provided you will see bot online and ready on Discord. 

## Built With

* [Python 3.6.5](https://www.python.org/)
* [PyCharm](https://www.jetbrains.com/pycharm/) - Python IDLE

## Authors

**Animus** 
For additional questions or issues please contact me through SushiPool's Discord Community (@Animus#4608) or
on email:MissionMoon@rocketship.com

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


