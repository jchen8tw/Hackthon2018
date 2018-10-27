import vlc
from googletrans.gtoken import TokenAcquirer
import sys
from time import sleep
def get_len(string):
    a = string.split(' ')
    return len(a)
def get_token(string):
    acquirer = TokenAcquirer()
    tk = acquirer.do(string)
    return tk

def string_to_google(string):
    
    i = vlc.Instance('--verbose 2'.split())
    p = i.media_player_new()
    url = 'http://translate.google.com.tw/translate_tts?ie=UTF-8&q=' + string.replace(' ','%20')+'&tl=en&total=1&idx=0'+'&textlen='+str(get_len(string)) +'&tk=' + str(get_token(string)) +'&client=webapp&prev=input'
    '''
    url = 'https://translate.google.com.tw/translate_tts?ie=UTF-8&q=%E8%B6%95%E7%BE%9A%E7%BE%8A&tl=zh-CN&total=1&idx=0&textlen=3&tk=353679.254520&client=t&prev=input&ttsspeed=0.24'
    '''
    #print('the url is: ',url)
    p.set_mrl(url)
    p.play()
    sleep(2)
    return 

if(__name__ == '__main__'):
    string_to_google(sys.argv[1])



