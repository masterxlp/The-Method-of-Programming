def GenerateDictSequence():

    # Code range a ~ y
    code_range = list('abcdefghijklmnopqrstuvwxy')

    # Generate code
    code = list()

    for char in code_range:

        # Generate 1 ~ 3 coding
        code.append(char)
        code.append(char + 'a')
        code.append(char + 'aa')

        # Generate template
        template = list(char + 'aaa')

        # Generate 4 coding
        for char1 in code_range:
            template[1] = char1
            for char2 in code_range:
                template[2] = char2
                for char3 in code_range:
                    template[3] = char3
                    code.append(''.join(template))

    return code



def GetPosition(string):

    # Illegal input
    if len(string) > 4:
        print('The input string length is illegal!')
    else:
        code = GenerateDictSequence()
        position = code.index(string)
        print(position)


def GetString(position):

    code = GenerateDictSequence()
    print(code[position])


if __name__ == "__main__":
    GetString(12345)
    GetPosition('baca')