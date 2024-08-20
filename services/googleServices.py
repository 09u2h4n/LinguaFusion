from googletrans import Translator
import gtts

import requests
from urllib import parse
from bs4 import BeautifulSoup

from typing import Generator

class googleServices:
    def __init__(self) -> None:
        pass

class googleTranslator(googleServices):
    def __init__(self) -> None:
        super().__init__()
        self.translator = Translator()

    def __ajax_method_text_translate(self, text: str, source_lang="auto", dest_lang="en") -> str:
        translated_text = self.translator.translate(text, dest=dest_lang, src=source_lang)
        return translated_text

    def __fetch_method_text_translate(self, text: str, source_lang="auto", dest_lang="en") -> str:
        parsed_text = parse.quote(text)
        url = f"https://translate.google.com/m?sl={source_lang}&tl={dest_lang}&q={parsed_text}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        translated_text = soup.find_all("div", class_="result-container")[0].text
        return translated_text

    def text_translate(self, text: str, source_lang="auto", dest_lang="en", method="ajax") -> str:
        method = method.lower()
        if method == "ajax":
            return self.__ajax_method_text_translate(text, source_lang, dest_lang)
        elif method == "fetch":
            return self.__fetch_method_text_translate(text, source_lang, dest_lang)
        else: 
            return "Unvalid method. Valid methods: ['ajax', 'fetch']"

    def detect_lang(self, text: str) -> dict["<detected_lang>":"<confidence>"]:
        data = self.translator.detect(text)
        detected_lang = data.lang
        confidence = data.confidence
        return {"detected_lang": detected_lang, "confidence": confidence}
    
    def get_languages(self) -> dict[str:str]:
        SPECIAL_CASES = {
            'ee': 'et',
        }

        LANGUAGES = {
            'af': 'afrikaans',
            'sq': 'albanian',
            'am': 'amharic',
            'ar': 'arabic',
            'hy': 'armenian',
            'az': 'azerbaijani',
            'eu': 'basque',
            'be': 'belarusian',
            'bn': 'bengali',
            'bs': 'bosnian',
            'bg': 'bulgarian',
            'ca': 'catalan',
            'ceb': 'cebuano',
            'ny': 'chichewa',
            'zh-cn': 'chinese (simplified)',
            'zh-tw': 'chinese (traditional)',
            'co': 'corsican',
            'hr': 'croatian',
            'cs': 'czech',
            'da': 'danish',
            'nl': 'dutch',
            'en': 'english',
            'eo': 'esperanto',
            'et': 'estonian',
            'tl': 'filipino',
            'fi': 'finnish',
            'fr': 'french',
            'fy': 'frisian',
            'gl': 'galician',
            'ka': 'georgian',
            'de': 'german',
            'el': 'greek',
            'gu': 'gujarati',
            'ht': 'haitian creole',
            'ha': 'hausa',
            'haw': 'hawaiian',
            'iw': 'hebrew',
            'he': 'hebrew',
            'hi': 'hindi',
            'hmn': 'hmong',
            'hu': 'hungarian',
            'is': 'icelandic',
            'ig': 'igbo',
            'id': 'indonesian',
            'ga': 'irish',
            'it': 'italian',
            'ja': 'japanese',
            'jw': 'javanese',
            'kn': 'kannada',
            'kk': 'kazakh',
            'km': 'khmer',
            'ko': 'korean',
            'ku': 'kurdish (kurmanji)',
            'ky': 'kyrgyz',
            'lo': 'lao',
            'la': 'latin',
            'lv': 'latvian',
            'lt': 'lithuanian',
            'lb': 'luxembourgish',
            'mk': 'macedonian',
            'mg': 'malagasy',
            'ms': 'malay',
            'ml': 'malayalam',
            'mt': 'maltese',
            'mi': 'maori',
            'mr': 'marathi',
            'mn': 'mongolian',
            'my': 'myanmar (burmese)',
            'ne': 'nepali',
            'no': 'norwegian',
            'or': 'odia',
            'ps': 'pashto',
            'fa': 'persian',
            'pl': 'polish',
            'pt': 'portuguese',
            'pa': 'punjabi',
            'ro': 'romanian',
            'ru': 'russian',
            'sm': 'samoan',
            'gd': 'scots gaelic',
            'sr': 'serbian',
            'st': 'sesotho',
            'sn': 'shona',
            'sd': 'sindhi',
            'si': 'sinhala',
            'sk': 'slovak',
            'sl': 'slovenian',
            'so': 'somali',
            'es': 'spanish',
            'su': 'sundanese',
            'sw': 'swahili',
            'sv': 'swedish',
            'tg': 'tajik',
            'ta': 'tamil',
            'te': 'telugu',
            'th': 'thai',
            'tr': 'turkish',
            'uk': 'ukrainian',
            'ur': 'urdu',
            'ug': 'uyghur',
            'uz': 'uzbek',
            'vi': 'vietnamese',
            'cy': 'welsh',
            'xh': 'xhosa',
            'yi': 'yiddish',
            'yo': 'yoruba',
            'zu': 'zulu'}

        return {"languages": LANGUAGES, "special_cases": SPECIAL_CASES}

class googleText2Speech(googleServices):
    def __init__(self) -> None:
        super().__init__()

    def text2speech(self, text: str, accent="auto") -> Generator[bytes, any, None] | any:
        tts = gtts.gTTS(text) if accent == "auto" else gtts.gTTS(text, lang=accent)
        return tts.stream()

    def get_languages(self) ->  dict["<lang>": "<name>"] :
        return gtts.lang.tts_langs()

if __name__ == "__main__":
    # t = googleTranslator().translate(text="merhaba", method="fetch")
    # print(t)
    # tts = googleText2Speech().text2speech("Hello")
    # with open("audio.mp3", "wb") as f:
    #     for i in tts:
    #         f.write(i)
    pass