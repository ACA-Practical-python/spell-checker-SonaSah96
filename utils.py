def lev_distance(str1, str2):
    table = [[0 for j in range(0, len(str2)+1)] for i in range(0, len(str1)+1)]
    table[0][0] = 0
    # i = 0
    for j in range(1, len(str2)+1):
        table[0][j] = table[0][j-1] + 1
    # j = 0
    for i in range(1, len(str1)+1):
        table[i][0] = table[i-1][0] + 1

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                table[i][j] = table[i-1][j-1]
            else:
                 chr_del = table[i][j-1]
                 chr_rep = table[i-1][j-1]
                 chr_ins = table[i-1][j]
                 table[i][j] = min(chr_del, chr_rep, chr_ins) + 1

    return table[len(str1)][len(str2)]


def soundex(st):
    alphabet_dict = {"0": "AEHIOUWY", "1": "BFPV", "2": "CGJKSXZQ", "3": "DT", "4": "L", "5": "MN", "6": "R"}
    st = st.upper()
    new_st = []
    new_st.append(st[0])
    for item in st[1:]:
        for key, value in alphabet_dict.items():
            if item in value:
                if key != new_st[-1]:
                    new_st.append(key)
                break
    new_st = [item for item in new_st if item != "0"]
    while len(new_st) != 4:
        if len(new_st) < 4:
            new_st.append("0")
        else:
            new_st.pop()
    return "".join(new_st)
