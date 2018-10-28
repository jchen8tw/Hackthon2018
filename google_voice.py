from googletrans.gtoken import TokenAcquirer
import vlc
import sys
from time import sleep
def get_len(string):
    a = string.split(' ')
    return len(a)
def get_token(string):
    acquirer = TokenAcquirer()
    tk = acquirer.do(string)
    return tk
def is_chinese(string):
    if(string[0] >= u'\u4e00' and string[0]<=u'\u9fa5'):
        return 'zh_CN'
    else:
        return 'en'
    

def string_to_google(string):
    
    i = vlc.Instance()
    p = i.media_player_new()
    url = 'http://translate.google.com.tw/translate_tts?ie=UTF-8&q=' + string.replace(' ','%20')+'&tl='+is_chinese(string)+ '&total=1&idx=0'+'&textlen='+str(get_len(string)) +'&tk=' + str(get_token(string)) +'&client=webapp&prev=input'
    '''
    url = 'https://translate.google.com.tw/translate_tts?ie=UTF-8&q=%E8%B6%95%E7%BE%9A%E7%BE%8A&tl=zh-CN&total=1&idx=0&textlen=3&tk=353679.254520&client=t&prev=input&ttsspeed=0.24'
    '''
    #print('the url is: ',url)
    p.set_mrl(url)
    p.play()
    sleep(1)
    return 

# if(__name__ == '__main__'):
    # string_to_google(sys.argv[1])

