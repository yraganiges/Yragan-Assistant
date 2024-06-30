import pickle as pick, json
#===================================//////////

#JSON
with open('data\\app_data\\config.json', 'r') as file:
    j = json.load(file)

#APP-CONFIG
running_status = False
path_settings =  j['paths']['settings']
status_facts = j['status_facts']
show_background = True

try: NAME = pick.load(open(path_settings + 'nameAI.bin', 'rb'))
except: NAME = 'OpenChocolateHoleAI'

#window-config
win_title = f'{NAME} v.AI | v2.0 | by yraganiga...'
win_size = '500x500'
win_bg = 'gray12'
win_icon = 'assets\\icons\\YA_logo_2.ico'

#sounds
sound_click: str = 'audio\\sound_click.mp3'

#images
image = None

#components
default_bg = '#ffbdbf' 
pre_default_bg = '#ebdfa4'
default_font = 'Bahnschrift SemiBold'

#user-data
user_country = 'ru'
user_name = 'yraganiga'

#requests
try: max_limit_lenght_request = pick.load(open(path_settings + 'mllr.bin', 'rb'))
except: max_limit_lenght_request = 300 #letters

try: num_for_indentation = pick.load(open(path_settings + 'indendations.bin', 'rb'))
except: num_for_indentation = 7 #every <n> words 

try: max_time_wait_voice_request = pick.load(open(path_settings + 'time_wait_voice_request.bin', 'rb'))
except: max_time_wait_voice_request = 3

try: voiceActing_speed = pick.load(open(path_settings + 'VoiceActing_speed.bin', 'rb'))
except: voiceActing_speed = 220

path_music = None
#seconds
delay_write_text: float = 0.02
path_requests = 'data\\user_data\\requests'

status_response_to_the_offenses = True

#Errors
status_error_1 = 'ERROR:'
status_error_2 = '<Error>:'

#Voice / tts
voices = ['Bot', 'Artem', 'Daima']

try: VoiceActing_mode = pick.load(open(path_settings + 'VoiceActing_mode.bin', 'rb'))
except: VoiceActing_mode = voices[0]

save_requests = False
#AI
roles = ['joker', 'mentally-retarded', 'serious', 'old-man', 'scoundrel', 'normal']

try: role = pick.load(open(path_settings + 'roleAI.bin', 'rb'))
except: role = roles[0] #Recommend - 5

path_to_dictionary = 'dictionary.txt'
#'data\\app_data\\ai_data\\russian.txt'

conditions = ['funny', 'normal', 'sad']

class response:
    good_stage = 'хорошо отлично замечательно положительно'
    middle_stage = 'средне так-себе как-обычно по-баробану-как ни-как обычно нормально'
    bad_stage = 'плохо ужасно неудовлетворительно'

#<Binds>
class Key:
    send_text_request = 'Enter + Space'
    open_list_requests = 'Alt + L'
    copy_text = 'Ctrl + B'
    
tell_me_about = f'''Я "{NAME}", создатель обнулил моё описание...'''

#Facts
FACTS = ['Ураган любит пошалить', 'Ученые измерили iq Урагана и узнали, что оно составляет 128', 'Урагану всё равно, что он скажет', 'Не пытайтесь оскорбить урагана больше двух раз', 'Энштейн лично сотрудничал с Ураганом', 'Урагану захотелось пить - так он и создал воду', 'Ураган бухал с мегалодоном на дне марианской впадины', 'Причина вымерания динозавров - Ураган', 'Ураган - это не ураган!', 'Ураган в 90-ых держал половину всех районов под своим контролем', 'Всё, что скажет Ураган - это не то, или, сами думайте...']

#ваш голосовой помощник. 
# На данный момент я нахожусь в разработке, но
# уже умею выполнять некоторые функции.
# Также я надеюсь, что мне скоро добавят Искуственный Интелект
# и я смогу анализировать данные, внедрять свою фантазию и быть более умным.
# Но сейчас я всё ещё программа(. 
# Благодарю вас, что воспользовались моей помощью!