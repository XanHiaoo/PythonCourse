def issame(s1,s2):
    s1.replace(" ", "")
    s2.replace(" ", "")
    s1 = s1.upper()
    s2 = s2.upper()
    l1=list(s1)
    l2=list(s2)
    l1 = list(set(l1))
    l2 = list(set(l2))
    if len(l1)!=len(l2):
        return False
    else:
        for str in s2:
            if str not in s1:
                return False
        return True
if __name__ == '__main__':
    str1=input()
    str2=input()
    flag = issame(str1, str2)
    if flag:
        print("YES")
    else:
        print("NO")