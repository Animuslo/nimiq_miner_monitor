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


### Installing
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
    
**Python (version above 3.6.) and Requirements**
- Python IDLE
  - Download and install python from link(bot done in 3.6.5.): https://www.python.org/downloads/ 
- Install packages
  - Download 
  - Open Command Prompt (CMD)


## Built With

* [Python 3.6.5](https://www.python.org/)
* [PyCharm](https://www.jetbrains.com/pycharm/) - Python IDLE

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Animus** 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

