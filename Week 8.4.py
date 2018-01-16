page = int(input("Enter page number:"))

def main():
           if isOdd(page):
               print(page)
           else:
               print("%60s%d" % (" ", page))

def isOdd(page):
           return page%2 ==0
main()
