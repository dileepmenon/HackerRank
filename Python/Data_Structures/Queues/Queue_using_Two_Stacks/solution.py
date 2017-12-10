#!bin/python3


class Queue:
    def __init__(self):
        self.st1 = []
        self.st2 = []

    def enqueue(self, x):
        if not self.st1:
            self.st1.append(x)
            self.front = x
        else:
            self.st1.append(x)

    def transfer_from_st1_to_st2(self):
        while self.st1:
            e = self.st1.pop()
            self.st2.append(e)

    def dequeue(self):
        if not self.st2:
            self.transfer_from_st1_to_st2()
        return self.st2.pop()

    def peek(self):
        if self.st2:
            return self.st2[-1]
        return self.front


num_queries = int(input())
q = Queue()
for i in range(num_queries):
    query = list(map(int, (input().split(' '))))
    if query[0] == 1:
        q.enqueue(query[1])
    elif query[0] == 2:
        q.dequeue()
    else:
        print(q.peek())
