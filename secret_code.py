st = input("Enter the message\n")
words = st.split(" ")

coding = True
if(coding):
    nwords = []
    for word in words:
        if(len(word)>=3):
            r1 = "dsf"
            r2 = "jkr"
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        print(" ".join(nwords))

else:
    pass