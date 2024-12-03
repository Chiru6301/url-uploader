from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
import requests
import json
import subprocess
from pyrogram import Client, filters
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
from pyromod import listen
from pyrogram.types import Message
from pyrogram import Client, filters
from p_bar import progress_bar
from subprocess import getstatusoutput
from aiohttp import ClientSession
import helper
from logger import logging
import time
import asyncio
from pyrogram.types import User, Message
import sys
import re
import os

bot = Client("bot",
             bot_token= "7793991199:AAEjMEVABNjA6X2OMnULU5XVSZQ6BBaccZE",
             api_id= 27120862,
             api_hash= "53d8ec88810f7445732ea234121e6219")
ADMINS = [1226915008]

