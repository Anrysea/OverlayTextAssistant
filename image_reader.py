import io
import os

from google.cloud import vision

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\GK.json"




def recognize_japanese_text(image_data):
    client = vision.ImageAnnotatorClient()

    image = vision.Image(content=image_data)
    language_hint = ["ja"]
    image_context = vision.ImageContext(language_hints=language_hint)

    response = client.document_text_detection(image=image, image_context=image_context)
    document = response.full_text_annotation
    print(document.text.replace("\n", ""))

    return document.text