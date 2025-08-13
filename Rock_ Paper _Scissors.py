def rock_paper_scissors(first , second):
    first = first.lower()
    second = second.lower()

    valid_moves = ("rock" , "paper" , "scissor")
    if first not in valid_moves or second not in valid_moves:
        return "İnvalid move. Please us rock, paper, or scissor."

    if first == second:
        print(" Tie! ")

    if (first == "rock" and second == "scissor") or \
        (first == "paper" and second == "rock") or \
        (first == "scissor" and second == "paper"):
        return "First Player Wins"
    else:
        return "Second Player Wins"



def main():
    first = input("first : ").strip()
    second = input("second : ").strip()
    a  = rock_paper_scissors(first, second)
    print(a)

if __name__ == "__main__":
    main()
