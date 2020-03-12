def commonCharacterCount(s1, s2):
    dem = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                dem +=1
                s2 = s2.replace(s2[j],"",1)
                break
    print(dem)
commonCharacterCount(s1 = "zzzz" ,s2 = "zzzzzzzb" )