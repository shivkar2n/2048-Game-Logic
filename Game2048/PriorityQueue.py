class PriorityQueue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def isEmpty(self):
        return len(self.queue) == 0

    def insert(self, data):
        self.queue.append(data)

    def delete(self):
        try:
            max_val = 0
            for i in range(len(self.queue)):
                if self.queue[i][1] > self.queue[max_val][1]:
                    max_val = i
            item = self.queue[max_val][0]
            del self.queue[max_val]
            return item
        except IndexError:
            print()
            exit()

    def (self):
        return [i[0] for i in self.queue]
