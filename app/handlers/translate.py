from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery, ContentTypes, ParseMode
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from deep_translator import GoogleTranslator
from app.misc import dp
from app.services.scrape_slovnik import parse_sections, extract_text_in_translate as etit
from app.services.scrape_utils import get_html


modes = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton("Чешско-Украинский", callback_data="cesky_rusky"),
    InlineKeyboardButton("Украинско-Чешский", callback_data="rusky_cesky")
)


class TranslateStates(StatesGroup):
    waiting_mode = State()
    waiting_word = State()
   

@dp.message_handler(commands="translate", state="*")
async def translate_step_1(message: Message):
    await message.answer("Выберите вариант вариант перевода",
                        reply_markup=modes)
    await TranslateStates.waiting_mode.set()


@dp.callback_query_handler(state=TranslateStates.waiting_mode)
async def translate_step_2(c: CallbackQuery, state: FSMContext):
    if c.data in ("cesky_rusky", "rusky_cesky"):
        await c.message.answer("Введите слово которое хотите перевести")
        await state.update_data(mode=c.data)
        await TranslateStates.next()
    else:
        await c.message.reply("Выберите действие используя клавиатуру ниже")
        return
    await c.answer()


@dp.message_handler(
    state=TranslateStates.waiting_word,
    content_types=ContentTypes.TEXT,
)
async def translate_step_3(message: Message, state: FSMContext):
    translate_mode = await state.get_data("mode")
    translate_mode = translate_mode.get("mode")
    if translate_mode == "rusky_cesky":
        ukr_word = message.text.lower()
        word = GoogleTranslator(source='auto', target="ru").translate(ukr_word)
    else:
        word = message.text.lower()
    html = await get_html(translate_mode, word)
    sections = parse_sections(html)
    translates, _ = sections
    translates_list = etit(translates)

    for tl in translates_list:
        await message.answer("\n".join(tl), parse_mode=ParseMode.HTML)
    await state.finish()