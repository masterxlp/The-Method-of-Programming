def mergeStringSet(set_list, merge_set_list):

    used_set = list()
    set_1 = set_list[0]
    used_set.append(0)

    j = 1
    while j < len(set_list):

        count = 0
        for char in set_list[j]:
            if char in set_1:
                count += 1

        if count > 0:
            for char in set_list[j]:
                if char not in set_1:
                    set_1.append(char)
            used_set.append(j)

        j += 1

    merge_set_list.append(set_1)

    set_list = updateSetList(set_list, used_set)

    return merge_set_list, set_list


def updateSetList(set_list, used_set):

    used_set = sorted(used_set, reverse=True)

    for i in used_set:
        set_list.pop(i)

    return set_list


def main(str_set):

    # Transfer set to list
    set_list = list()
    for i in range(len(str_set)):
        set_list.append(list(str_set[i]))

    set_list2 = set_list[:]
    merge_set_list = list()


    while len(set_list) != 0:

        merge_set_list, set_list = mergeStringSet(set_list2, merge_set_list)

    print(merge_set_list)

main([{'aaa', 'bbb', 'ccc'}, {'bbb', 'ddd'}, {'eee', 'fff'}, {'ggg'}, {'ddd', 'hhh'}])