from requests import get as requests_get, RequestException

class TranslationError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

ENDPOINT_URL = "https://iranianvacuums.com/translate"
SUPPORTED_LANGUAGES = ["en", "et", "fi", "fr", "gl", "de", "el", "zh-cn", "zh-tw", "he", "hu", "is", "id", "ga", "it", "ja", "ko", "lv", "lt", "mi", "nb", "fa", "pl", "pt", "ro", "ru", "gd", "sr", "sk", "sl", "es", "sv", "th", "tr", "uk", "vi", "cy", "zu"]

def translate(text: str, language: str = "en") -> str:
    if text is None:
        raise TranslationError("Text must be a string")
    elif text == "":
        raise TranslationError("Text must not be blank")
    if language is None:
        raise TranslationError("Language must be a string")
    elif language == "":
        raise TranslationError("Language must not be blank")
    if language not in SUPPORTED_LANGUAGES:
        raise TranslationError(f"Unsupported language: {language}\nSupported languages are: " + ",".join(SUPPORTED_LANGUAGES))
    
    try:
        response = requests_get(ENDPOINT_URL, params={"t": text, "l": language})
        if response.status_code == 200:
            return response.text
        else:
            raise TranslationError("Translation failed")
    except RequestException as e:
        raise TranslationError(f"Translation request failed with error: {e}")
