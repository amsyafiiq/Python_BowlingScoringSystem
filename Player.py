class Player:
    def __init__(self, name, points):
        self.name = name
        self.points = points
    
    def printPoints(self):
        output = "_"
        for i in range(len(self.points)):
            rows = self.points[i]
            if len(rows) == 3:
                output += "____________"
            else:
                output += "________"
        
        output += "\n|"
        
        for i in range(len(self.points)):
            rows = self.points[i]
            if len(rows) == 3:
                output += "    {0}     |".format(i + 1)
            else:
                output += "   {0}   |".format(i + 1)
        
        output += "\n|"

        for i in range(len(self.points)):
                rows = self.points[i]
                if len(rows) == 3:
                    output += "-----------|"
                else:
                    output += "-------|"
                    
        output += "\n|"

        for i in range(len(self.points)):
            rows = self.points[i]
            if len(rows) == 1:
                output +=  " {} | {} |".format("X", " ")
            elif (len(rows) == 2):
                if rows[0] + rows[1] == 10:
                     output += " {} | {} |".format(rows[0], "/")
                else:
                    value = [-1] * 2
                    for j in range(len(rows)):
                        if rows[j] == 0:
                            value[j] = "-"
                        else:
                            value[j] = rows[j]
                    output += " {} | {} |".format(value[0], value[1])
            else:
                value = [-1] * 3
                for j in range(len(rows)):
                    if rows[j] == 10:
                        value[j] = "X"
                    elif rows[j] == 0:
                        value[j] = "-"
                    else:
                        value[j] = ""

                if value[0] == "":
                    value[0] = rows[0]
                
                if value[1] == "":
                    if rows[1] + rows[1] == 10:
                        value[1] = "/"
                    else:
                        value[1] = rows[1]
                
                if value[2] == "":
                    if rows[1] + rows[2] == 10:
                        value[2] = "/"
                    else:
                        value[2] = rows[2]
                
                output += " {} | {} | {} |".format(value[0], value[1], value[2])
            
            
        output += "\n-"
        for i in range(len(self.points)):
                rows = self.points[i]
                if len(rows) == 3:
                    output += "------------"
                else:
                    output += "--------"


        return output

        

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