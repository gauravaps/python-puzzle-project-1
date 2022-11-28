import random

def shuffleword(wrd):
    pw=random.sample(wrd,k=len(wrd))
    return '' .join(pw)

def printpuzzleqst(word,score):
    probword=shuffleword(word)
    print("\n arrange the to form a valid word")
    print(probword)
    userword=input()
    print()
    if userword.upper()==word:
        print("correct")
        score+=1
    else:
        print("wrong") 
        score-=1

    return score 

def main():
    score=0
    words=["FATHER","BREAK","COUNTRY"]
    words=random.sample(words,k=len(words))

    for word in words:
        score=printpuzzleqst(word,score)

    print("your score is",score)
main()


