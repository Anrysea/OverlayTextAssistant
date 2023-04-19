import io
import os

from google.cloud import vision

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\GK.json"

def recognize_japanese_text(image_data):
    client = vision.ImageAnnotatorClient()

    image = vision.Image(content=image_data)

    language_hint = "ja"
    image_context = vision.ImageContext(language_hints=[language_hint])

    response = client.document_text_detection(image=image, image_context=image_context)
    document = response.full_text_annotation

    words = []
    for page in document.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                for word in paragraph.words:
                    word_text = ''.join([symbol.text for symbol in word.symbols])
                    word_box = word.bounding_box.vertices
                    avg_symbol_height = sum([symbol.bounding_box.vertices[3].y - symbol.bounding_box.vertices[0].y for symbol in word.symbols]) / len(word.symbols)
                    words.append((word_text, word_box, avg_symbol_height))

    return words
