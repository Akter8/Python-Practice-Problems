class cl:
    def __init__(self):
        n = int(input("Enter a number\n"))
        self.generator(n)

    def generator(self,n):
        ans = []
        for i in range(1,n+1):
            if i%7==0:
                ans.append(i)

        print(ans)

x = cl()
