import re
from bs4 import BeautifulSoup
from typing import Union, List, Tuple, Any
from .scrape_utils import load_html, get_html


def parse_sections(html: Union[bytes, str]) -> Tuple[Any, Any]:
    "Парсит секцию с переводом и секцию с примерами"
    soup = BeautifulSoup(html, "html.parser")
    main = soup.find("main", {"class": "TranslatePage"}).find(
                            "div", {"class": "TranslatePage-content"}).find(
                            "div", {"class": "TranslatePage-results"})
    translates = main.find_all("article", {"class": "Box--partOfSpeech"})
    translates = [translate.find("section") for translate in translates]
    try:
        examples = main.find("article", {"class": "Box--collapsable"}
                            ).find("section").find(
                            "div", {"class": "Box-content-words"})
    except AttributeError:
        examples = ""
    return translates, examples


def extract_text_in_translate(section: list):
    """Извлекает и форматирует текст из полученого перевода"""
    acronym_regex = r"\w{2,30}\."  # регулярка для поиска сокращений
    section_text = "".join([s.get_text(separator="|") for s in section])
    acronyms = re.findall(acronym_regex, section_text)
    translates_list = []
    if len(section) > 1:
        for elem in section:
            lis = []
            for n, li in enumerate(elem.find(re.compile('ol|ul')).find_all("li")):
                li_text = li.get_text(separator='|')
                for l in li_text.split("|"):
                    if l in acronyms:
                        li_text = li_text.replace(l, f"<i>({l})</i>")

                lilili_text = li_text.split("|", 1)
                if len(lilili_text) > 1:
                    rus, cz = lilili_text
                    cz = ' '.join(cz.split('|'))
                    nspaces = ("  ", "   ")
                    for nspace in nspaces:
                        cz = cz.replace(nspace, " ")
                    lis.append(f"{n}. <b>{rus.strip()}</b> {cz}")
                else:
                    l = lilili_text[0]
                    lis.append(f"{n}. <b>{l}</b>")
            translates_list.append(lis)
    else:
        tag = section[0]
        lis = []
        for n, li in enumerate(tag.find(re.compile('ol|ul')).find_all("li")):
            li_text = li.get_text(separator='|')
            for l in li_text.split("|"):
                if l in acronyms:
                    li_text = li_text.replace(l, f"<i>({l})</i>")

            lilili_text = li_text.split("|", 1)
            if len(lilili_text) > 1:
                rus, cz = lilili_text
                cz = ' '.join(cz.split('|'))
                nspaces = ("  ", "   ")
                for nspace in nspaces:
                    cz = cz.replace(nspace, " ")
                lis.append(f"{n}. <b>{rus.strip()}</b> {cz}")
            else:
                l = lilili_text[0]
                lis.append(f"{n}. <b>{l}</b>")
        translates_list.append(lis)

    return translates_list if len(translates_list) > 0 else ""
