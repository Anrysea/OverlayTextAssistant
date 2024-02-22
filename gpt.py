import re
import openai
import csv
import os

history = []


openai.api_key = ""

start_string = "This is a question from a test, the data may have been copied slightly incorrectly, but try to give an answer. SEND ONLY THE ANSWER -- \"\n"
#start_responce = "Понял вас. Пришлите мне кандзи, и я предоставлю примеры в указанном вами формате, я обязательно буду следовать установленным правилам"

def get_part_after_dash(s):
    parts = s.split('-')
    return parts[-1].strip() if len(parts) > 1 else s
def get_words_after_dash(input_string):
    words = input_string.split('\n')
    words1 = [get_part_after_dash(s) for s in words]
    return '\ '.join(word.strip() for word in words1)

#history.append({"role": "assistant", "content": start_responce})

def generate_response(string):
        history = []
        request_string = start_string + string + "\"\n"
        print(request_string)
        history.append({"role": "user", "content": request_string})
        completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages=history
        )
        print(completion.choices[0].message.content.strip())
        return completion.choices[0].message.content.strip()





