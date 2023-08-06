import requests

def get_json(prompt):
    return requests.get('https://zephyrus-chatbot.tjwllms52.repl.co/api/response?prompt=%s' % prompt).json()

def get_response(prompt):
    return get_json(prompt)['message']['CHATBOT']
