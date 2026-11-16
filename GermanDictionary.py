from time import sleep

def p(a, end='\n'):
    for letter in a:
        print(letter, end='')
        sleep(0.025)
    print('', end=end)

def ip(a):
    p(a, end=' ')
    return input('')

def record(german, english):
    n = 0
    while True:
        n += 1
        try:
            with open(f'german_fergus_python_program_{n}', 'r'):
                pass
        except:
            n -= 1
            break
    with open(f'german_fergus_python_program_{n}', 'a') as file:
        file.write(f'{german}\n') 
    with open(f'english_fergus_python_program_{n}', 'a') as file:
        file.write(f'{english}\n') 
    pass

def gfind(german):
    n = -1
    try:
        while True:
            n += 1
            with open(f'german_fergus_python_program_{n}', 'r') as file:
                lines = file.readlines()
            for i in range(100):
                if lines[i].strip() == german.strip():
                    with open(f'english_fergus_python_program_{n}', 'r') as file:
                        english_final = file.readlines()[i].strip()
                    return [n, i, english_final]
    except:
        return [-100000000,-10000000, 'SORRY, ENTRY NOT FOUND']

def Efind(english):
    n = -1
    try:
        while True:
            n += 1
            with open(f'english_fergus_python_program_{n}', 'r') as file:
                lines = file.readlines()
            for i in range(100):
                if lines[i].strip() == english.strip():
                    with open(f'german_fergus_python_program_{n}', 'r') as file:
                        german_final = file.readlines()[i].strip()
                    return [n, i, german_final]
    except:
        return [-100000000,-10000000, 'ENTSCHULDIGUNG, EINTRAG NICHT GEFUNDEN']


def efind(entry):
    text_num = int((entry-1)/100)
    num = entry - ((100 * text_num)+1)
    try:
        with open(f'german_fergus_python_program_{text_num}', 'r') as file:
            german = file.readlines()[num]
        with open(f'english_fergus_python_program_{text_num}', 'r') as file:
            english = file.readlines()[num]
        return [german, english]
    except:
        return ['ENTSCHULDIGUNG, EINTRAG NICHT GEFUNDEN', 'SORRY, ENTRY NOT FOUND']

def Gchangedef(german, english):
    g = gfind(german)
    if g == ['ENTSCHULDIGUNG, EINTRAG NICHT GEFUNDEN\n', 'SORRY, ENTRY NOT FOUND']:
        p('ERROR.')
        pass
    txtN = g[0]
    txtI = g[1]
    with open(f'english_fergus_python_program_{txtN}', 'r') as file:
        lines = file.readlines()
    lines[txtI] = english
    with open(f'english_fergus_python_program_{txtN}', 'w') as file:
        for thing in lines:
            file.write(thing)
    p('DONE!')

def Echangedef(german, english):
    g = efind(english)
    if g == ['ENTSCHULDIGUNG, EINTRAG NICHT GEFUNDEN\n', 'SORRY, ENTRY NOT FOUND']:
        p('ERROR.')
        pass
    txtN = g[0]
    txtI = g[1]
    with open(f'german_fergus_python_program_{txtN}', 'r') as file:
        lines = file.readlines()
    lines[txtI] = german
    with open(f'german_fergus_python_program_{txtN}', 'w') as file:
        for thing in lines:
            file.write(thing)
    p('DONE!')


p('WELCOME TO GERMAN DICTIONARY 3000')
p('© 2026 Fergus Yuile')
while True:
    ans = ip('What would you like to do?\n 1. Add a word\n 2. Find a word by German\n 3. Find a word by entry\n 4. Change the English of a word\n 5. Find a word by English\n 6. Change the German of a word\n Anything else: Returns an error and asks if you would like to quit.\nPlease input your choice as a number here >>>')
    if ans == '1':
        german = ip('Enter the word in German >>>').upper()
        english = ip('Enter the word in English >>>').upper()
        record(german, english)
    elif ans == '2':
        word = ip('Input the word you want to find in German >>>').upper()
        p(f'The word is {gfind(word)[2]}! It was found at Line {gfind(word)[1]+1}, in Document {gfind(word)[0]+1}.')
    elif ans == '3':
        ID = ip('Input the entry number (NO COMMAS ALLOWED) >>>')
        try:
            pureid = int(ID)
            p(f'English: {efind(pureid)[0]}German: {efind(pureid)[1]}')
        except:
            p('Sorry, there was an error.')
    elif ans == '4':
        german = ip('Type the word in German >>>').upper()
        english = ip('Type the new defenition >>>').upper()
        Gchangedef(german, english)
    elif ans == '5':
        english = ip('Input the word in English >>>').upper()
        p(f'The word is {Efind(word)[2]}! It was found at Line {Efind(word)[1]+1}, in Document {Efind(word)[0]+1}.')
    elif ans == '6':
        german = ip('Type the word in English >>>').upper()
        english = ip('Type the new German >>>').upper()
        Echangedef(german, english)
    else:
        if ip('Error. Would you like to stop the program?\ny/n >>>') == 'y':
            exit()