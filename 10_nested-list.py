if __name__ == '__main__':
    pythonlist = []
    scoreList = []
    nameList = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scoreList.append(score)
        pythonlist.append([name,score])
    for i in range(len(pythonlist)):
        if pythonlist[i][1]==sorted(list(set(scoreList)))[1]:
                nameList.append(pythonlist[i][0])
    for i in sorted(nameList):
        print(i) 
