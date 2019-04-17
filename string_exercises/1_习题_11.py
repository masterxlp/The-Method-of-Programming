def initializeDict(pat_dict):

    # Initialize the value to 0 for each key
    for key in pat_dict.keys():
        pat_dict[key] = 0

    return pat_dict


def initializeList(lst):

    # Initialize the list to empty
    for i in range(len(lst)):
        lst.pop()

    return lst


def leastSubstring(pattern, article):

    # Use list to store each word of article
    # In python, can use split function :
    # art_list = article.split(' ')
    # Here don't use split function
    art_list = list()

    # Split words as spaces
    start_char_pos = 0
    for i in range(len(article)):

        if article[i] is ' ':
            end_char_pos = i
            art_list.append(article[start_char_pos:end_char_pos])
            start_char_pos = (i + 1)

        # In the article end, don't have spaces, only word
        elif i == len(article)-1:
            art_list.append(article[start_char_pos:len(article)])

    # Create a pattern dictionary and initialize it
    pat_dict = dict()
    for char in pattern:
        pat_dict[char] = 0

    # Start:
    # Create a list to record the start and end position for substring
    record = list()
    substr = dict()

    j = 0
    while j < len(art_list):

        # From the position j to article end start a new poll
        h = j
        while h < len(art_list):

            # Get the don't used word
            pat = [word for word in pat_dict.keys() if pat_dict[word] == 0]

            if len(record) == 3:
                substr[max(record) - min(record)] = (min(record), max(record))
                pat_dict = initializeDict(pat_dict)
                record = initializeList(record)
                break

            if art_list[h] in pat:
                pat_dict[art_list[h]] = 1
                record.append(h)

            h += 1

        j += 1

    # Get the least sub string
    start = substr[min(substr.keys())][0]
    end = substr[min(substr.keys())][1]

    return ' '.join(art_list[start:end+1])


if __name__ == "__main__":
    print(leastSubstring(['hello', 'world', 'good'], 'hello world I am a students hello you are good in the world'))