# 2 字符串包含 #

## 2.1 问题描述 ##

Q：给定一个长字符串a和一个短字符串b。请问，如何最快地判断出字符串b中的所有字符是否
都在长字符串a中？请编写函数bool StringContain(string &a, string &b)实现此功
能。

注：为简单起见，假设输入的字符串只包含大写英文字母。如：
- 字符串a为"ABCD"，字符串b为"BAD"，答案为True；
- 字符串a为"ABCD"，字符串b为"BCE"，答案为False；
- 字符串a为"ABCD"，字符串b为"AA"，答案为True；