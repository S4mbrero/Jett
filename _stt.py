# import torch
# import sounddevice as sd
# import speech_recognition as sr
# import time
# from glob import glob

# device = torch.device('cpu')
# model, decoder, utils = torch.hub.load(repo_or_dir='snakers4/silero-models',
#                                        model='silero_stt',
#                                        language='en', # en, ru
#                                        device=device)
# (read_batch, split_into_batches,
#  read_audio, prepare_model_input) = utils

# def callback(_r, audio):
#     try:
        

#         print("Распознание ...")

#         # TODO: fix crutch, pass audio data directly as a model input of Silero STT
#         with open('speech.wav', 'wb') as f:
#             f.write(audio.get_wav_data())

#         test_files = glob('speech.wav')
#         batches = split_into_batches(test_files, batch_size=10)
#         input = prepare_model_input(read_batch(batches[0]),
#                                     device=device)

#         output = model(input)
#         for example in output:
#             print(decoder(example.cpu()))

      
#     except sr.UnknownValueError:
#         print("[log] Голос не распознан!")


# # запуск
# r = sr.Recognizer()
# r.pause_threshold = 0.5
# m = sr.Microphone(device_index=1)

# with m as source:
#     r.adjust_for_ambient_noise(source)

# stop_listening = r.listen_in_background(m, callback)
# while True: time.sleep(0.1)
