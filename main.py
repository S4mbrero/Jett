import config
import stt
import tts
from fuzzywuzzy import fuzz
import datetime
from num2words import num2words
import webbrowser
import os
from pydub import AudioSegment
from pydub.playback import play




print(f"{config.VA_NAME} (v{config.VA_VER}) начала свою работу ...")
song = AudioSegment.from_mp3("реплики/привет.wav")
play(song)


def va_respond(voice: str):
    print(voice)
    if voice.startswith(config.VA_ALIAS):
        # обращаются к ассистенту
        cmd = recognize_cmd(filter_cmd(voice))

        if cmd['cmd'] not in config.VA_CMD_LIST.keys():
           song = AudioSegment.from_mp3("реплики/что.wav")
           play(song)
        else:
            execute_cmd(cmd['cmd'])


def filter_cmd(raw_voice: str):
    cmd = raw_voice

    for x in config.VA_ALIAS:
        cmd = cmd.replace(x, "").strip()

    for x in config.VA_TBR:
        cmd = cmd.replace(x, "").strip()

    return cmd


def recognize_cmd(cmd: str):
    rc = {'cmd': '', 'percent': 0}
    for c, v in config.VA_CMD_LIST.items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > rc['percent']:
                rc['cmd'] = c
                rc['percent'] = vrt

    return rc


def execute_cmd(cmd: str):
    if cmd == 'help':
        song = AudioSegment.from_mp3("реплики/help.wav")
        play(song)
        pass
    elif cmd == 'ctime':
        
        now = datetime.datetime.now()
        text = "Сейчас " + num2words(now.hour, lang='ru') + " " + num2words(now.minute, lang='ru')
        tts.va_speak(text)

    elif cmd == 'joke':
        song = AudioSegment.from_mp3("реплики/анекдот_2.wav")
        play(song)

    elif cmd == 'open_browser':

        song = AudioSegment.from_mp3("реплики/уже-открываю.wav")
        play(song)
        webbrowser.open('https://ya.ru/?utm_referrer=https%3A%2F%2Fwww.google.com%2F', new=2)
       

    elif cmd == 'open_vk':
            song = AudioSegment.from_mp3("реплики/выполняю.wav")
            play(song)
            webbrowser.open('https://vk.com', new=2)

    elif cmd == 'open_youtube':
        song = AudioSegment.from_mp3("реплики/ваша-просьба.wav")
        play(song)
        webbrowser.open('http://youtube.com', new=2)
        

    elif cmd == 'create_papka':
        song = AudioSegment.from_mp3("реплики/выполняю.wav")
        play(song)
        os.mkdir('Новая папка')

    elif cmd == 'name':
        song = AudioSegment.from_mp3("реплики/Джет.wav")
        play(song)
        
    

# начать прослушивание команд
stt.va_listen(va_respond)