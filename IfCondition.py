if __name__ == "__main__":
        try:
                inp_score = float(input("Enter score: "))
                if inp_score > 1.0 or inp_score < 0.0:
                    print("Score is out of range")
                else:
                    if inp_score >= 0.9 :
                        print("A")
                    elif 0.8 <= inp_score < 0.9:
                        print("B")
                    elif 0.7 <= inp_score < 0.8:
                        print("C")
                    elif 0.6 <= inp_score < 0.7:
                        print("D")
                    elif inp_score < 0.6:
                        print("F")
        except:
            print("bad score")
