
def score_pin():
    score=[]
    frames=10

    #Frame start
    for i in range(frames):
        no_frame=i + 1
        print(f"\nFrame {no_frame}")

        first_shot=0
        sec_shot=0
        third_shot=0

        #to separate frame 1-9 and 10
        if i< 9:
            while condition:
                first_shot=input("Enter the number of pins down for the First Throw :")
                if int(first_shot)>10:
                    break
                elif int(first_shot)==10:
                    score_list.append(int(first_shot))
                    break
                else:
                    score_list.append(int(first_shot))
                    sec_shot=input("Enter the number of pins down for the Second Throw :")
                    score_list.append(int(sec_shot))
                    break
        else:
             while condition:
                first_shot=input("Enter the number of pins down for the First Throw :")
                if int(first_shot)>10:
                   break

                elif int(first_shot)==10:
                    score_list.append(int(first_shot))
                    sec_shot=input("Enter the number of pins down for the Second Throw :")
                    score_list.append(int(sec_shot))
                    third_shot=input("Enter the number of pins down for the Third Throw :")
                    score_list.append(int(third_shot))
                    break

                else:
                     score_list.append(int(first_shot))
                     sec_shot=input("Enter the number of pins down for the Second Throw :")
                     score_list.append(int(sec_shot))

                     if int(first_shot) + int(sec_shot) == 10:
                        third_shot=input("Enter the number of pins down for the Third Throw :")
                        score_list.append(int(third_shot))
                        break
                     break
                
                


countbowler=int(input("Enter number of players: "))
print("\nLETS START THE GAME!!")

score_list=[]
condition=True

for i in range(0,countbowler):
     name=input(f"\nEnter Player {i + 1} Name : ")
     score=score_pin()
     print(score_list)



