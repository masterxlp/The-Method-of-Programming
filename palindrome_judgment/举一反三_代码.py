from palindrome_judgment.node import Node


def GenerateLink(lst):

    # Initialize the head node to None
    head = None
    # 最近插入的数据总是位于结构的开始处
    for count in lst:
        head = Node(count, head)

    return head


def IsPalindromeLink(link):

    link_cop = link

    # Step 1. Gets the length of link
    num = 0
    while link is not None:
        num += 1
        link = link.next

    # Step 2. Find the middle position of link
    mid = 0
    if num % 2 == 0:
        mid += int(num / 2)
    else:
        mid += int(num / 2) + 1

    head = link_cop

    # Step 3. Move the tail pointer to middle position
    i = 0
    while i < mid:
        link_cop = link_cop.next
        i += 1
    tail = link_cop

    # Step 4. Reverse the link from mid+1 to last
    lyst = list()
    while tail is not None:
        lyst.append(tail.data)
        tail = tail.next
    tail = GenerateLink(lyst)

    # In order to compare, update mid
    if mid % 2 == 0:
        mid = mid
    else:
        mid -= 1

    # Step 5. Compare the head data with tail
    for i in range(mid):
        if head.data != tail.data:
            return False
        head = head.next
        tail = tail.next

    return True


if __name__ == "__main__":

    link1 = GenerateLink(list('abba'))
    print(IsPalindromeLink(link1))