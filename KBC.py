print("Welcome To Kon Banega Corepati")

print("Rules Of the Game! \
      1 question = amount 1000 \
      2 question = amount 2000  \
      3 question = amount 2000  \
      4 question = amount 2000  \
      5 question = amount 2000")

question1 = ["1, What is The PH value of human Body", '9.2', '7.0', '6.1', '5.4']
print("Question Number 1\
      What is the Ph value of human body\
      a, 9.2\
      b, 7.0\
      c, 6.1\
     d, 5.4 ")

answer = input("Enter You answer Here\n")


if '7.0' == answer:
    print("Correct Answer")
    print("You Win 1000 Rs")
else:
     print("Wrong Answer")
     print("You Lose 1000 Rs")


question2 = ["Which of the following are called Key Industrial animals?", "Producers", " Tertiary consumers", "Primary consumers", "None of these"]

print("Question Number 2\
      Which of the following are called Key Industrial animals?\
      Producers\
      Tertiary consumers\
      Primary consumers\
      None of these")

answer = input("Enter You answer Here\n")

if 'primary consumer' == answer:
    print("Correct Answer")
    print("You Win 2000 Rs")
else:
     print("Wrong Answer")
     print("You Lose 2000 RS")

        