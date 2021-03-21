import aiohttp
from typing import Union
from user_agent import generate_user_agent


async def get_html(
        translate: str, word: str, save: bool = False
    ) -> Union[bytes, str]:
    """Получаем html страницу с переводом для последующего парсинга.
    :param str translate: С какого на какой язык происходит перевод.
                          Может быть: cesky_rusky, rusky_cesky
    :param str word: Слово которое будет переводиться.
    :save bool: Сохранять страницу или нет. По умолчанию страница не 
                сохраняется а возвращается функцией.
    :rtype: bytes or str
    """
    if translate.lower() not in ("cesky_rusky", "rusky_cesky"):
        return f"Неправильный вариант перевода!" \
                "Допустимые варианты: cesky_rusky, rusky_cesky" 

    fname = "result.html"
    url = f"https://slovnik.seznam.cz/preklad/{translate}/{word}"
    params = {"strict": "true"}
    headers = {
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ru,en;q=0.5",
        "TE": "Trailers",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": generate_user_agent(),
    }
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url, params=params) as r:
            html = await r.read()
    if save:
        with open(fname, "wb") as f:
            f.write(html)
    return html if not save else f"Страница с переводом сохранена в {fname}"


def load_html(fname: str = "result.html") -> str:
    with open(fname) as f:
        return f.read()