# FlexBot
FlexBot is a python script that runs a Discord bot. The general purpose of the bot is to retrieve and display OSRS character data. Its inspiration is from the really stale meme [detailed here.][stale]

[stale]:http://knowyourmeme.com/memes/u-ever-flex-on-niggas
## Commands:
### $stats
Format: `$stats [OSRS Username]`

If the `[OSRS Username]` is left blank and your account is registered, then the command will use your registered username

Gets and displays the statistics for the OSRS username that was provided, if the username's statistics cannot be found then the bot will notify the user of this.

![stats](https://i.imgur.com/WxwJOrx.png)
### $pie
Format: `$pie [OSRS Username]`

If the `[OSRS Username]` is left blank and your account is registered, then the command will use your registered username

Gets and displays the statistics for an OSRS username in pie chart form. It seperates the pie based on XP. If the username's statistics cannot be found then the bot will notify the user of this.

![pie](https://i.imgur.com/pUfDwct.png)
### $flex
Format: `$flex [OSRS Username]`

This command is only available to those who have a registered account.

To use this command, put the account you would like to compare your account to in the OSRS Username field. The bot will then direct message you and ask what skill you would like to compare. After you have provided a proper skill, it will submit the amount of difference between your account and the account provided with a bar graph.

![flex](https://i.imgur.com/dJxtczj.png)
### $combat
Format: `$combat [OSRS Username]`

If the `[OSRS Username]` is left blank and your account is registered, then the command will use your registered username

Gets and displays the combat statistics for is OSRS username that was provided. If the username's statistics cannot be found then the bot will notify the user of this. The bot also displays the breakdown of how their combat lvl is calculated.

![combat](https://i.imgur.com/gaHxJIG.png)
### $register
Format: `$register [OSRS Username]`

Registers a Runescape username to a Discord account. If done properly, it should enable the ability to use the $flex command as well as using defaults on the $stats, $pie and $combat commands.

![register](https://i.imgur.com/BTjCDFJ.png)
### $LB
Format: `$LB [skill name]`

Gets and displays the leaderboard for the skill provided, if the skill cannot be found then the user will be notified with a DM that that skill could not be found.

![LB](https://i.imgur.com/HaCKXvI.png)
### $users
Format: `$users`

Gets and displays the OSRS usernames that have been registered to the server so far.

![users](https://i.imgur.com/6sFOjtl.png)
## Sources:
### discord.py
https://github.com/Rapptz/discord.py

This is a wonderful tool that was made by "Danny" Rapptz. It allows for the communication between a bot and Discord.
### Plotly
https://plot.ly/python/

Plotly is a python library that allows the bot to make visually pleasing graph images
### Beautiful Soup
https://www.crummy.com/software/BeautifulSoup/

Beautiful Soup is a python library that allows the bot to get information off of the OSRS hiscore website.

## Future Plans:
- Grand exchange search function
- Daily gain leaderboard automation on Monday - Saturday, Weekly gain leaderboard Sunday
- Website for the bot