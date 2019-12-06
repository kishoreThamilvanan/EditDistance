def editDistance(str1, str2):
    l1 = len(str1)
    l2 = len(str2)

    distanceList = []

    for i in range(l1 + 1):
        distanceList.append([])
        for j in range(l2 + 1):
            distanceList[i].append(0)

    for i in range(l1 + 1):
        for j in range(l2 + 1):

            # if STR1 is empty, then copy all elements from STR2 to STR1
            if i == 0:
                distanceList[i][j] = j

            # if STR2 is empty, then remove all elements from STR2
            elif j == 0:
                distanceList[i][j] = i

            elif str1[i - 1] == str2[j - 1]:
                distanceList[i][j] = distanceList[i - 1][j - 1]

            else:
                distanceList[i][j] = 1 + min(distanceList[i - 1][j], distanceList[i][j - 1], distanceList[i - 1][j - 1])

    return distanceList[l1][l2]


if __name__ == "__main__":

    str1 = "watch the movie raising arizona?" #"leonard skiena" # "watch the movie raising arizona?"
    str2 = "watch da mets raze arizona?" #"lynard skynard" # "watch da mets raze arizona?"

    result = editDistance(str1, str2)

    print(result)
