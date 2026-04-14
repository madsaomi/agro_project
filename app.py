"""
Agro 5 Lang Hub — Flask Translation Website
Всё на сервере, без JavaScript. Jinja2 + Flask sessions.
"""

from flask import Flask, render_template, request, session, redirect, url_for
from flask_cors import CORS
import requests as http_requests
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
CORS(app)

# ══════════════════════════════════════════════════════════════════════════
# TRANSLATIONS DICTIONARY (Interface i18n)
# ══════════════════════════════════════════════════════════════════════════

TRANSLATIONS = {
    "ru": {
        "site_title": "Agro 5 Lang Hub — Онлайн Переводчик",
        "hero_title": "Переводите мгновенно",
        "hero_subtitle": "Бесплатный перевод текстов на 5 языков — быстро и точно",
        "from_label": "Откуда",
        "to_label": "Куда",
        "input_placeholder": "Введите текст для перевода...",
        "result_placeholder": "Перевод появится здесь...",
        "translate_btn": "Перевести",
        "swap_btn": "Поменять местами",
        "copy_hint": "Выделите текст для копирования",
        "clear_btn": "Очистить",
        "feature1_title": "Быстро",
        "feature1_desc": "Мгновенный перевод текстов любой длины",
        "feature2_title": "5 языков",
        "feature2_desc": "Русский, узбекский, английский, японский и каракалпакский",
        "feature3_title": "Бесплатно",
        "feature3_desc": "Без регистрации и ограничений",
        "footer_text": "© 2026 Agro 5 Lang Hub. Бесплатный переводчик.",
        "error_empty": "Введите текст для перевода",
        "error_same_lang": "Выберите разные языки",
        "error_api": "Ошибка перевода. Попробуйте снова.",
        "error_too_long": "Текст слишком длинный (максимум 5000 символов)",
    },
    "uz": {
        "site_title": "Agro 5 Lang Hub — Onlayn Tarjimon",
        "hero_title": "Darhol tarjima qiling",
        "hero_subtitle": "5 tilga bepul matn tarjimasi — tez va aniq",
        "from_label": "Qayerdan",
        "to_label": "Qayerga",
        "input_placeholder": "Tarjima qilish uchun matn kiriting...",
        "result_placeholder": "Tarjima shu yerda paydo bo'ladi...",
        "translate_btn": "Tarjima qilish",
        "swap_btn": "Almashtirib qo'yish",
        "copy_hint": "Matnni nusxalash uchun tanlang",
        "clear_btn": "Tozalash",
        "feature1_title": "Tez",
        "feature1_desc": "Har qanday uzunlikdagi matnlarni bir zumda tarjima qilish",
        "feature2_title": "5 til",
        "feature2_desc": "Rus, o'zbek, ingliz, yapon va qoraqalpoq tillari",
        "feature3_title": "Bepul",
        "feature3_desc": "Ro'yxatdan o'tmasdan va cheklovlarsiz",
        "footer_text": "© 2026 Agro 5 Lang Hub. Bepul tarjimon.",
        "error_empty": "Tarjima uchun matn kiriting",
        "error_same_lang": "Turli tillarni tanlang",
        "error_api": "Tarjima xatosi. Qayta urinib ko'ring.",
        "error_too_long": "Matn juda uzun (maksimum 5000 belgi)",
    },
    "en": {
        "site_title": "Agro 5 Lang Hub — Online Translator",
        "hero_title": "Translate Instantly",
        "hero_subtitle": "Free text translation in 5 languages — fast and accurate",
        "from_label": "From",
        "to_label": "To",
        "input_placeholder": "Enter text to translate...",
        "result_placeholder": "Translation will appear here...",
        "translate_btn": "Translate",
        "swap_btn": "Swap languages",
        "copy_hint": "Select text to copy",
        "clear_btn": "Clear",
        "feature1_title": "Fast",
        "feature1_desc": "Instant translation of texts of any length",
        "feature2_title": "5 Languages",
        "feature2_desc": "Russian, Uzbek, English, Japanese, and Karakalpak",
        "feature3_title": "Free",
        "feature3_desc": "No registration or restrictions",
        "footer_text": "© 2026 Agro 5 Lang Hub. Free translator.",
        "error_empty": "Enter text to translate",
        "error_same_lang": "Please select different languages",
        "error_api": "Translation error. Please try again.",
        "error_too_long": "Text too long (max 5000 characters)",
    },
    "ja": {
        "site_title": "Agro 5 Lang Hub — オンライン翻訳",
        "hero_title": "瞬時に翻訳",
        "hero_subtitle": "5つの言語への無料テキスト翻訳 — 迅速で正確",
        "from_label": "翻訳元",
        "to_label": "翻訳先",
        "input_placeholder": "翻訳するテキストを入力...",
        "result_placeholder": "翻訳がここに表示されます...",
        "translate_btn": "翻訳する",
        "swap_btn": "言語を入れ替える",
        "copy_hint": "テキストを選択してコピー",
        "clear_btn": "クリア",
        "feature1_title": "高速",
        "feature1_desc": "あらゆる長さのテキストを即座に翻訳",
        "feature2_title": "5言語",
        "feature2_desc": "ロシア語、ウズベク語、英語、日本語、カラカルパク語",
        "feature3_title": "無料",
        "feature3_desc": "登録不要・制限なし",
        "footer_text": "© 2026 Agro 5 Lang Hub. 無料翻訳サービス。",
        "error_empty": "翻訳するテキストを入力してください",
        "error_same_lang": "異なる言語を選択してください",
        "error_api": "翻訳エラー。もう一度お試しください。",
        "error_too_long": "テキストが長すぎます（最大5000文字）",
    },
    "kaa": {
        "site_title": "Agro 5 Lang Hub — Onlayn Awdarmashı",
        "hero_title": "Derrew awdarıń",
        "hero_subtitle": "5 tilge tegin tekst awdarması — tez hám anıq",
        "from_label": "Qayerden",
        "to_label": "Qayerge",
        "input_placeholder": "Awdarıw ushın tekst kiritiń...",
        "result_placeholder": "Awdarma usı jerde payda boladı...",
        "translate_btn": "Awdarıw",
        "swap_btn": "Tillerdi almastırıw",
        "copy_hint": "Tekstti nusxalaw ushın tańlań",
        "clear_btn": "Tazalaw",
        "feature1_title": "Tez",
        "feature1_desc": "Qanday uzınlıqtaǵı tekstlerdi bir zumda awdarıw",
        "feature2_title": "5 til",
        "feature2_desc": "Rus, ózbeksha, ingliz, yapon hám qaraqalpaq tilleri",
        "feature3_title": "Tegin",
        "feature3_desc": "Dizimnen ótpesten hám sheklawlarsız",
        "footer_text": "© 2026 Agro 5 Lang Hub. Tegin awdarmashı.",
        "error_empty": "Awdarıw ushın tekst kiritiń",
        "error_same_lang": "Basqa tillerdi tańlań",
        "error_api": "Awdarma qátesi. Qayta urınıp kóriń.",
        "error_too_long": "Tekst juda uzın (maksimum 5000 belgi)",
    },
}

# Available translation languages
LANGUAGES = {
    "ru": "🇷🇺 Русский",
    "uz": "🇺🇿 Ўзбекча",
    "en": "🇬🇧 English",
    "ja": "🇯🇵 日本語",
    "kaa": "🇰🇷 Қарақалпақ",
}

# UI language labels (short)
UI_LANGS = {
    "ru": "RU",
    "uz": "UZ",
    "en": "EN",
    "ja": "JP",
    "kaa": "QQ",
}

# ══════════════════════════════════════════════════════════════════════════
# TRANSLATION API
# ══════════════════════════════════════════════════════════════════════════

MYMEMORY_URL = "https://api.mymemory.translated.net/get"
LIBRETRANSLATE_URL = "https://libretranslate.com/translate"


def translate_mymemory(text: str, source: str, target: str) -> dict:
    """Translate using MyMemory API (primary, free, no key)."""
    langpair = f"{source}|{target}"
    try:
        resp = http_requests.get(
            MYMEMORY_URL,
            params={"q": text, "langpair": langpair},
            timeout=15,
        )
        resp.raise_for_status()
        data = resp.json()
        if data.get("responseStatus") == 200:
            return {"success": True, "text": data["responseData"]["translatedText"]}
    except Exception:
        pass
    return {"success": False, "text": ""}


def translate_libretranslate(text: str, source: str, target: str) -> dict:
    """Translate using LibreTranslate API (fallback)."""
    try:
        resp = http_requests.post(
            LIBRETRANSLATE_URL,
            json={"q": text, "source": source, "target": target, "format": "text"},
            timeout=15,
        )
        resp.raise_for_status()
        data = resp.json()
        return {"success": True, "text": data.get("translatedText", "")}
    except Exception:
        pass
    return {"success": False, "text": ""}


def do_translate(text: str, source: str, target: str) -> dict:
    """Try MyMemory first, then LibreTranslate as fallback."""
    result = translate_mymemory(text, source, target)
    if not result["success"]:
        result = translate_libretranslate(text, source, target)
    return result


# ══════════════════════════════════════════════════════════════════════════
# HELPER — get current UI language strings
# ══════════════════════════════════════════════════════════════════════════

def get_ui_lang():
    """Get current interface language from session, default 'ru'."""
    lang = session.get("ui_lang", "ru")
    if lang not in TRANSLATIONS:
        lang = "ru"
    return lang


def t(key: str) -> str:
    """Get translation string for current UI language."""
    lang = get_ui_lang()
    return TRANSLATIONS[lang].get(key, key)


# ══════════════════════════════════════════════════════════════════════════
# ROUTES
# ══════════════════════════════════════════════════════════════════════════

@app.route("/", methods=["GET", "POST"])
def index():
    """Main page — handles translation form and displays results."""
    ui_lang = get_ui_lang()
    strings = TRANSLATIONS[ui_lang]

    # Default form state
    source_lang = session.get("source_lang", "en")
    target_lang = session.get("target_lang", "ru")
    source_text = ""
    result_text = ""
    error_msg = ""

    if request.method == "POST":
        action = request.form.get("action", "translate")

        # ── Language swap ──
        if action == "swap":
            source_lang = request.form.get("source_lang", "en")
            target_lang = request.form.get("target_lang", "ru")
            source_text = request.form.get("source_text", "")
            result_text = request.form.get("result_text", "")

            # Swap languages
            source_lang, target_lang = target_lang, source_lang
            # Swap texts
            source_text, result_text = result_text, source_text

        # ── Clear ──
        elif action == "clear":
            source_text = ""
            result_text = ""
            source_lang = request.form.get("source_lang", "en")
            target_lang = request.form.get("target_lang", "ru")

        # ── Translate ──
        else:
            source_lang = request.form.get("source_lang", "en")
            target_lang = request.form.get("target_lang", "ru")
            source_text = request.form.get("source_text", "").strip()

            if not source_text:
                error_msg = strings["error_empty"]
            elif len(source_text) > 5000:
                error_msg = strings["error_too_long"]
            elif source_lang == target_lang:
                error_msg = strings["error_same_lang"]
            else:
                result = do_translate(source_text, source_lang, target_lang)
                if result["success"]:
                    result_text = result["text"]
                else:
                    error_msg = strings["error_api"]

        # Save preferences to session
        session["source_lang"] = source_lang
        session["target_lang"] = target_lang

    return render_template(
        "index.html",
        s=strings,
        ui_lang=ui_lang,
        ui_langs=UI_LANGS,
        languages=LANGUAGES,
        source_lang=source_lang,
        target_lang=target_lang,
        source_text=source_text,
        result_text=result_text,
        error_msg=error_msg,
    )


@app.route("/lang/<lang_code>")
def set_language(lang_code):
    """Switch interface language."""
    if lang_code in TRANSLATIONS:
        session["ui_lang"] = lang_code
    return redirect(url_for("index"))


# ══════════════════════════════════════════════════════════════════════════
# RUN
# ══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
