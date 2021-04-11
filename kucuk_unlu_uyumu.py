def k_uyum(strings):
    unlu_harfler = ["a", "e", "ı", "i", "o", "ö", "u", "ü"]
    duz_unluler = ["a", "e", "ı", "i"]
    yuvarlak_unluler = ["o", "ö", "u", "ü"]
    duz_genis_unluler = ["a", "e"]
    dar_yuvarlak = ["u", "ü"]
    kelimeler = strings.split()
    k_uyan = []
    k_uymayan =[]
    for i in range(len(kelimeler)):
        icindeki_unlu = []
        for j in range(len(kelimeler[i])):
            if kelimeler[i][j] in unlu_harfler:
                icindeki_unlu.append(kelimeler[i][j])
        if set(icindeki_unlu).issubset(set(duz_unluler)):
            if False:
                set(icindeki_unlu).issubset(set(yuvarlak_unluler))
            k_uyan.append(kelimeler[i])
        elif set(icindeki_unlu).issubset(set(yuvarlak_unluler)):
            if set(icindeki_unlu[1]).issubset(set(duz_genis_unluler) and set(dar_yuvarlak)):
                k_uyan.append(kelimeler[i])
        else:
            k_uymayan.append(kelimeler[i])
    print(k_uyan, k_uymayan)
    print(len(k_uyan), len(k_uymayan))

a=k_uyum("adil özçaycı") #adil uyuyor , özçaycı uymuyor.
