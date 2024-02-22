from sudachipy import Dictionary, Tokenizer

def katakana_to_hiragana(katakana_text):
    # Конвертируем каждый символ катаканы в соответствующий символ хираганы
    return ''.join(chr(ord(ch) - 0x60) if 'ァ' <= ch <= 'ヶ' else ch for ch in katakana_text)

def to_hiragana(text):
    tokenizer = Dictionary().create()
    words = tokenizer.tokenize(text, mode=Tokenizer.SplitMode.A)

    result = []
    for word in words:
        surface = word.surface()
        reading = katakana_to_hiragana(word.reading_form())
        # Если поверхностная форма и чтение совпадают или если это не кандзи, просто добавьте поверхностную форму
        if surface == reading or all(not ('㐀' <= ch <= '鿋') for ch in surface):
            result.append(surface)
        else:
            result.append(f"{surface}({reading})")

    return ''.join(result)

japanese_text = "常識的な申し合わせが行われていることには、私はいつも違和感を覚えている"
hiragana_text = to_hiragana(japanese_text)
print(hiragana_text)
