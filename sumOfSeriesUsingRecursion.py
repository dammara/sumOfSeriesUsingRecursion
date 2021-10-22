# markhus Damamr
# 22 october 2021
# This program uses differneiques to compute series of a numbe


def sumOfSeriesUsingNonTailRecursion(myNumber: int): # non tail
    if myNumber == 0:
        return myNumber
    else:
        return myNumber + sumOfSeriesUsingNonTailRecursion(myNumber - 1)


def sumOfSeriesUsingTailRecursion(SumOfSeries, myNumber: int): # Tail
    if myNumber == 0:
        return SumOfSeries
    else:
        return sumOfSeriesUsingTailRecursion(SumOfSeries + myNumber, myNumber - 1)


def driver():
    user_number = int(input("Enter a number to find the sum of the series >>> "))
    choice = int(input("Non-Tail or Tail? (1 or 2) >>> "))
    if choice == 1:
        print(f"sum using non tail: " + str(sumOfSeriesUsingNonTailRecursion(user_number)))
    elif choice == 2:
        print(f"sum using tail: " + str(sumOfSeriesUsingTailRecursion(0, user_number)))
    else:
        print("Please enter 1 or 2")
        choice = int(input("Non-Tail or Tail? (1 or 2) >>> "))


driver()


