from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os
from download import *
from database import *
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from download.youtube import youtube
load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = Bot(token = TOKEN, parse_mode = types.ParseMode.HTML)

channels=['@masteruzdev']

dp = Dispatcher(bot)

@dp.message_handler(commands = ['start'])
async def start_bot(message: types.Message):
    await message.answer(f'''
                        🇺🇿 Salom {message.chat.full_name}! - botga hush kelibsiz bot haqida malumot olish uchun /help buyrug'ini kiriting 😊\n
🇬🇧 Hello {message.chat.full_name}! - Welcome to the bot To enter information about the bot, enter the / help command 😊\n
🇷🇺 Здравствуйте, {message.chat.full_name}! - Добро пожаловать в бот Для ввода информации о боте введите команду /help 😊\n
                        ''')
    
@dp.message_handler(commands = ['help'])
async def help_bot(message: types.Message):
    inline_btn_1 = InlineKeyboardButton('Instagram', callback_data='instagram')
    inline_btn_2 = InlineKeyboardButton('YouTube', callback_data='youtube')
    inline_btn_3 = InlineKeyboardButton('TikTok', callback_data='tiktok')
    
    inline_kb1 = InlineKeyboardMarkup()
    inline_kb1.add(inline_btn_3,inline_btn_2)
    inline_kb1.row(inline_btn_1)
    
    
    await message.answer('🇺🇿 Platformani tanlang!\n🇬🇧 Select a platform!\n🇷🇺 Выберите платформу!',reply_markup=inline_kb1)
@dp.callback_query_handler()
async def process_callback(callback_query: types.CallbackQuery):
    media_group=types.MediaGroup()
    if callback_query.data=='instagram':
        media_group.attach_photo(types.InputFile('images/photo_instagram1.jpg'))
        media_group.attach_photo(types.InputFile('images/photo_instagram2.jpg'))
        media_group.attach_photo(types.InputFile('images/photo_instagram3.jpg'),"<b>🇺🇿 Bizga Instagram havolasini yuboring \
            \n🇬🇧 Send us an Instagram link\n🇷🇺 Отправьте нам ссылку в инстаграмм</b>")
        await bot.send_media_group(callback_query.from_user.id,media=media_group)
    elif callback_query.data=='youtube':
        media_group.attach_photo(types.InputFile('images/photo_youtube1.jpg'))
        media_group.attach_photo(types.InputFile('images/photo_youtube2.jpg'))
        media_group.attach_photo(types.InputFile('images/photo_youtube3.jpg'),"<b>⚠️BU XUSUSIYAT HOZIRDA ISHLAMAYDI!\n\n🇺🇿 Bizga YouTube havolasini yuboring \
            \n🇬🇧 Send us an YouTube link\n🇷🇺 Отправьте нам ссылку в YouTube</b>")
        await bot.send_media_group(callback_query.from_user.id,media=media_group)
    elif callback_query.data=='tiktok':
        media_group.attach_photo(types.InputFile('images/photo_tiktok1.jpg'))
        media_group.attach_photo(types.InputFile('images/photo_tiktok2.jpg'))
        media_group.attach_photo(types.InputFile('images/photo_tiktok3.jpg'),"<b>🇺🇿 Bizga TikTok havolasini yuboring \
            \n🇬🇧 Send us an TikTok link\n🇷🇺 Отправьте нам ссылку в TikTok</b>")
        await bot.send_media_group(callback_query.from_user.id,media=media_group)
        
@dp.message_handler(content_types = ['text'])
async def on_text_message(message: types.Message):
    
    
    if message.text.lower() == 'ассалом алейкум'\
        or message.text.lower() =='salom alaykum' or message.text.lower() == 'salom'\
        or message.text.lower() == 'салом' or message.text.lower() == 'assalom alaykum':
            await message.reply('Salom <b>{}</b>!'.format(message.from_user.full_name))
    elif message.text.lower() == 'привет' or message.text.lower() == 'здравствуй' or message.text.lower() == 'здравствуйте':
            await message.reply('привет <b>{}</b>!'.format(message.from_user.full_name))
            
    
        
    # TikTok Video Download 
    else:
        for entity in message.entities:
            if entity.type in ["url", "text_link"]:
                
                try:
                    for channel in channels:
                        global status
                        status = await bot.get_chat_member(channel, message.chat.id)
                    # channel 
                    
                    if status['status'] == 'member' or status['status'] == 'creator' or status['status'] == 'administrator':
                        # TEKTOK
                        if message.text.lower().startswith('https://www.tiktok.com/') or message.text.lower().startswith('https://vt.tiktok.com/') or message.text.lower().startswith('https://tiktok.com/') \
                            or message.text.lower().startswith('https://vm.tiktok.com/'):
                            await tiktok(message,os.getenv('THOST'),os.getenv('KEY'),os.getenv('TURL'))
                            break
                        # INSTAGRAM
                        if message.text.lower().startswith('https://www.instagram.com/') or message.text.lower().startswith('https://instagram.com/'):
                            await instagram(message,os.getenv('IHOST'),os.getenv('KEY'),os.getenv('IURL'))
                            break
                        # if message.text.lower().startswith('https://www.youtube.com/') or message.text.lower().startswith('https://youtube.com/'):
                        #     await youtube(message)
                        #     break
                        else:
                            await message.reply('<b>{}</b> - tiktok va instagram video yuklanmadi qaytib link ni tug\'riligini tekshirib ko\'ring'.format(message.text))
                            break
                    else:
                        
                        button = types.InlineKeyboardButton(text = '🔗 Kanalga O\'ting 🔗', url = 'https://t.me/masteruzdev')
                        markup = types.InlineKeyboardMarkup()
                        markup.add(button)
                        await message.reply('<b>{}</b> - Kanalga obuna buling va qaytib linkni tashlang.'.format(message.text), reply_markup = markup)
                except Exception as error:
                    logging.error(f'Bot File: {error}')
                    
                    await message.reply('<b>{}</b> - Botda Xato! '.format(message.text))
                    
            
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)