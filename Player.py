class Player:
    def __init__(self, name, points):
        self.name = name
        self.points = points
        
    def calc_totalPoint(self):
        total = 0

        for i in range(len(self.points)):
            rows = self.points[i]
            for j in range(len(rows)):
                if i != len(self.points) - 1:
                    if rows[j] == 10:
                        if len(self.points[i + 1]) == 1:
                            row = self.points[i + 2]
                            total += (20 + row[0])
                        elif len(self.points[i + 1]) == 2:
                            total += (10 + sum(self.points[i + 1]))
                        else:
                            next_row = self.points[i + 1]
                            total += (10 + next_row[0] + next_row[1])
                    elif (rows[j] + rows[j + 1]) == 10:
                        total += (10 + self.points[i + 1][0])
                        break
                    else:
                        total += rows[j] + rows[j + 1]
                        break
                else:
                    total += sum(rows)
                    break
    
        return total