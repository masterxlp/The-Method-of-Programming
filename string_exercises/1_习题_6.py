def CompressRepeatedStrings(string):

    # Store the compressed string
    comp_str_list = list()

    # Compress repeated strings
    i = 0
    while i < len(string):

        # Mark repeating element
        comp_chars = string[i]

        # Initialize the repeating element count to one
        count = 1

        # Count the number about chars
        j = i + 1

        while True:

            if j < len(string) and string[j] == comp_chars:
                count += 1
                j += 1
            else:
                break

        # Compress the repeat element and store it to new list
        if count != 1:
            comp_str_list.append((str(count) + comp_chars))
        else:
            comp_str_list.append(comp_chars)
        
        i = j

    return ''.join(comp_str_list)


if __name__ == "__main__":
    print(CompressRepeatedStrings('cccddecc'))