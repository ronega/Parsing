def CurrentPageSplit(list):
    import pandas as pd
    try:
        j = 1
        list_now = []
        list_final = []
        while j != 0:
            for i in range(0, 11):
                elem = str(list[0:1]).strip('[]')
                list.pop(0)
                elem = elem.replace('\'', '')
                elem = elem.replace('\n', '')
                list_now.append(elem)
                i += 1
            list_final.append(list_now[1:])
            list_now = []
            i = 1
    except IndexError:
        key_pd = pd.DataFrame(list_final)
        key_pd.to_csv('parse.csv', index=False, header=False, sep='!', mode='a', encoding='utf-16')
