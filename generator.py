def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

def not_present(x,a):
    flag=0
    for b in a:
        if (b in x):
            flag=flag+1
    return flag
    
def present(x,a):
    flag=0
    for b in a:
        if (b not in x):
            flag=flag+1
    return flag

def wrong_position(x,a):
    flag=0
    for b in a:
        if(a[b]==x[b]):
            flag= flag+1
    return flag

def right_position(x,a):
    flag=0
    for b in a:
        if(a[b]!=x[b]):
            flag= flag+1
    return flag

if __name__ == '__main__':
    english_words = load_words()
    # demo print
    #print('fate' in english_words)
    wordle=set()
    for x in english_words:
        if len(x)==5:
            wordle.add(x)
    print(len(wordle))
    wordle1=set(wordle)
    for y in wordle:
             x=y
             x.lower()
             flag=0
             flag=flag+not_present(x, {})
             flag=flag+present(x, {'s','l','n','c'})
             #flag=flag+present(x, {'e','a','r','i','o'})
             flag=flag+wrong_position(x, {0:'',1:'',2:'',3:'',4:''})
             flag=flag+wrong_position(x, {0:'',1:'',2:'',3:'',4:''})
             flag=flag+right_position(x, {})
             if (flag>0):
                 wordle1.remove(x)
    print(len(wordle1))        
            