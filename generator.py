from joblib import Parallel, delayed
from wordfreq import word_frequency

def load_words():
    with open('allowed_words.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

def not_present(x,a):
    flag=0
    for b in a:
        if (b in x):
            flag=flag+1
            return flag
    return flag
    
def present(x,a):
    flag=0
    for b in a:
        if (b not in x):
            flag=flag+1
            return flag
    return flag

def wrong_position(x,a):
    flag=0
    for b in a:
        if(x[b] in a[b]):
            flag= flag+1
            return flag
    return flag

def right_position(x,a):
    flag=0
    for b in a:
        if(a[b]!=x[b]):
            flag= flag+1
            return flag
    return flag

def simulator(word,x,p,np,rp,wp):
    i=0
    for y in x:
        if (y in word):
            p.add(y)
            if (y==word[i]):
                rp.update({i:y})
            else:
                wp.update({i:y})
        else:
            np.add(y)
        i=i+1
    
            
        

def generator(x):
    
    x.lower()
    count=0
    for y1 in wordle1:
        y=y1.lower()
        np=set()
        p=set()
        wp={}
        rp={}
        simulator(y,x,p,np,rp,wp)
        #print(x1,y1,p,np,rp,wp)
        #print(x)
        for z1 in wordle1:
            flag=0
            #print(len(wordle1))
            z=z1.lower()
            flag=flag+not_present(z,np)
            if (flag>0):
                count=count+freq_word[z]
                continue
            flag=flag+present(z,p )
            if (flag>0):
                count=count+freq_word[z]
                continue
            flag=flag+wrong_position(z, wp )
            if (flag>0):
                count=count+freq_word[z]
                continue
            flag=flag+right_position(z, rp)
            if (flag>0):
                count=count+freq_word[z]
                continue
    #print(x)
    return x,count       

    

english_words = load_words()
wordle=set()
for x in english_words:
    if len(x)==5:
        wordle.add(x)
print(len(wordle))
freq_word={}
for x in wordle:
    freq_word.update({x:word_frequency(x,'en',wordlist='best')})
    #freq_word.update({x:1})
np=set()
p=set()
wp={}
rp={}
word='salet'
while True:
    wordle1=set(wordle)
    color=input("Enter the colors:")
    if (len(color)<5):
        break
    for i in range(5):
        if (color[i]=='g'):
            rp.update({i:word[i]})
            p.add(word[i])
        elif (color[i]=='o'):
            wp.update({i:word[i]})
            p.add(word[i])
        else:
            np.add(word[i])
 
    for y in wordle:
             x=y
             x.lower()
             flag=0
             flag=flag+not_present(x, np)
             flag=flag+present(x, p)
             flag=flag+wrong_position(x,wp)
             flag=flag+right_position(x, rp)
             if (flag>0):
                 wordle1.remove(x)
    print(len(wordle1))  
    if (len(wordle1)>400):
        result=Parallel(n_jobs=8)(delayed(generator)(x) for x in wordle1)
    else:
        result=Parallel(n_jobs=8)(delayed(generator)(x) for x in wordle)
    Result={}
    for x in result:
        Result.update({x[0]:x[1]})
    Keymax = max(zip(Result.values(), Result.keys()))[1]
    if (len(wordle1)<50):
        print(wordle1)
    if(len(wordle1)>1):
        print(Keymax)
    
    word=Keymax

