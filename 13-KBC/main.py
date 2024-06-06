
import requests # for reqesting data from third party API provider
import random

def main():
    print("Welcome to the KYA BANGE CODER")
    maxQuestion = int(input("Enter max question number")); # for max question 
    try:
        URL = f"https://opentdb.com/api.php?amount={maxQuestion}";
        # https://opentdb.com/api.php?amount=10;
    except:
        raise Exception("UNABLE TO LOAD DATA FROM API "); # if data not received
    
    res: list = requests.get(URL).json();
    quizData = res["results"];
    que_count: int = 1;
    marks: int = 0;
    question: int = 1;
    while que_count <= maxQuestion:
        for que in quizData:
            current_question_data = que;
            current_question:str = que["question"].replace("&quot;","'");
            correctAns = que["correct_answer"];
            all_ans = [];
            all_ans.append(correctAns);
            for wrong_ans in que["incorrect_answers"]:
                all_ans.append(wrong_ans);

            random.shuffle(all_ans);
            # print(correctAns, all_ans);

            print(f"{question} {current_question}");
            print("---options---");
            for ans in all_ans:
                print(ans);
            ans_option = int(input("\nEnter The answer index :"));

            if (ans_option - 1) == all_ans.index(correctAns):
                print("correct ans");
                marks += 1;
            else:
                print("Wrong ans");
                print(correctAns);

            question += 1;
            que_count += 1;

    print(f"Your Score is {marks}");
    print("THANK YOU FOR PARICIPATING IN KYA BANGE CODER");


if __name__ == "__main__":
    main()
