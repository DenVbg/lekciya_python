text  = ['dfds', 'sdfsdf', 'sdfsdfs','dsfs', 'sdf']
search='df'

for i in range(len(text)):
    #print(i)
    if search in text[i]:
        print(f"В элементе с индексом {i} - Да")