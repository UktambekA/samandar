import asyncio
import asyncpg
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, Location
from aiogram.filters import CommandStart
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.types.input_file import FSInputFile
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from openpyxl import Workbook
from datetime import datetime
from openpyxl.styles import Font, Alignment
from aiogram.types import BufferedInputFile
from openpyxl.utils import get_column_letter
import logging
import json
import os
import io


# Ma'lumotlarni kiritish so'rovi
insert_query = """
    INSERT INTO dorixonalar (inn, dorixona_nomi, manzil, kontrakt, dorixona_egasi, mfo, rs, dagovor)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""



import pandas as pd

# df = pd.read_excel("dorixonalar.xlsx")  
df =  pd.read_csv("apteka.csv", dtype={"mfo": str})

data = df.values.tolist()



# Bir nechta yozuvlarni kiritish
cursor.executemany(insert_query, data)



conn.commit()
