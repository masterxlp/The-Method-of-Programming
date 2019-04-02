def StringMatch(string, article):

    # Letter list
    letter1 = list('abcdefghijklmnopqrstuvwxyz')
    letter2 = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    letter = letter1[:] + letter2[:]

    # Store result in list
    match_result = list()

    # Identify wildcard
    i, j = 0, 0

    while i < len(string) and j < len(article):

        if string[i] is '*':
            char = string[i+1]

            while article[j] is not char:

                if article[j] not in letter:
                    j += 1
                    match_result = list()
                    break
                else:
                    match_result.append(article[j])
                    j += 1

            if len(match_result) != 0:
                i += 1
            else:
                i = 0
        elif string[i] is '?':
            if article[j] not in letter:
                i = 0
                match_result = list()
            else:
                match_result.append(article[j])
                i += 1
            j += 1

        else:
            if string[i] != article[j]:
                j += 1
            else:
                match_result.append(string[i])
                i += 1
                j += 1

        if i == len(string):
            i = 0
            match_result.append(';')

    print(''.join(match_result))


StringMatch('J* Smi??', 'I am John Smith, and are you Jon Smitj?')