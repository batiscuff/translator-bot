from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from app.misc import bot, dp


@dp.message_handler(commands="start", state="*")
async def cmd_start(message: types.Message, state: FSMContext):
    await message.reply(
        "Что бы использовать переводчик введите команду (/translate)",
        reply_markup=types.ReplyKeyboardRemove(),
    )


@dp.message_handler(commands="cancel", state="*")
@dp.message_handler(Text(equals="отмена", ignore_case=True), state="*")
async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        "Действие отменено", reply_markup=types.ReplyKeyboardRemove()
    )


@dp.message_handler(commands="set_commands", state="*")
async def cmd_set_commands(message: types.Message):
    if message.from_user.id == 448086107:
        command = types.BotCommand(
            command="/translate", description="Перевести слово"
        )
    await bot.set_my_commands(command)
    await message.answer("Команды установлены")
