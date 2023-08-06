from datetime import datetime

from diffcord import Client, VoteWebhookListener, UserBotVote, UserVoteInformation

import discord

intents = discord.Intents.default()

bot = discord.Bot(intents=intents)


