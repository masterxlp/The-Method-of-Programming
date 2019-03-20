# CalcAllCombination算法之过程分析 #

## Code ##

In[1]:
```
    if len(lst) != 0:
        print(''.join(lst))
    
    for i in range(num, len(str_list)):
        lst.append(str_list[i])
        CalcAllCombination(str_list, lst, i+1)
        lst.pop()
```

## 过程分析 ##

总结：
- 由于组合的性质，有当列表不为空，即列表中只要有元素无论几个都会输出；
- 显然地，这与字符串的全排列以及允许重复下的全排列不同，前者隐性的要求了输出字符串的
长度，而组合则没有（除了不能为空）；

过程：

Action|i|lst|out  
|:---:|:---:|:---:|:---:|
append|0|a|a
