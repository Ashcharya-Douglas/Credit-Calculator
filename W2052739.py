# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: W2052739
# Date: 02/12/2023

from graphics import *
import time


# Part 1 (B)
def get_credits(prompt):  # Getting a function to call in the future in main() and validate the data type
    while True:
        try:
            received_credits = int(input(prompt))
            return received_credits
        except ValueError:
            print("Integer Required.")


# ---------------------------------------------------------#

# Part 1 (A)
def predicted_outcome(pass_credits, defer_credits, fail_credits):  # Starting the comparison of the entered values and the given combinations
    total_credits = pass_credits + defer_credits + fail_credits

    if total_credits != 120:
        return "Total Incorrect."

    if pass_credits == 120:
        return "Progress."
    elif (pass_credits == 100 and defer_credits == 20 and fail_credits == 0) or (
            pass_credits == 100 and defer_credits == 0 and fail_credits == 20):
        return "Progress(Module trailer)."
    elif (pass_credits == 80 and defer_credits == 40 and fail_credits == 0) or (
            pass_credits == 80 and defer_credits == 20 and fail_credits == 20) or (
            pass_credits == 80 and defer_credits == 0 and fail_credits == 40):
        return "Do Not Progress - Module Retriever."
    elif (pass_credits == 60 and defer_credits == 60 and fail_credits == 0) or (
            pass_credits == 60 and defer_credits == 40 and fail_credits == 20) or (
            pass_credits == 60 and defer_credits == 20 and fail_credits == 40) or (
            pass_credits == 60 and defer_credits == 0 and fail_credits == 60):
        return "Do Not Progress - Module Retriever."
    elif (pass_credits == 40 and defer_credits == 80 and fail_credits == 0) or (
            pass_credits == 40 and defer_credits == 60 and fail_credits == 20) or (
            pass_credits == 40 and defer_credits == 40 and fail_credits == 40) or (
            pass_credits == 40 and defer_credits == 20 and fail_credits == 60):
        return "Do Not Progress - Module Retriever."
    elif (pass_credits == 20 and defer_credits == 100 and fail_credits == 0) or (
            pass_credits == 20 and defer_credits == 80 and fail_credits == 20) or (
            pass_credits == 20 and defer_credits == 60 and fail_credits == 40) or (
            pass_credits == 20 and defer_credits == 40 and fail_credits == 60):
        return "Do Not Progress - Module Retriever."
    elif (pass_credits == 0 and defer_credits == 120 and fail_credits == 0) or (
            pass_credits == 0 and defer_credits == 100 and fail_credits == 20) or (
            pass_credits == 0 and defer_credits == 80 and fail_credits == 40) or (
            pass_credits == 0 and defer_credits == 60 and fail_credits == 60):
        return "Do Not Progress - Module Retriever."
    elif pass_credits == 100 and defer_credits == 20 and fail_credits == 0:
        return "Exclude."
    elif (pass_credits == 20 and defer_credits == 20 and fail_credits == 80) or (
            pass_credits == 20 and defer_credits == 0 and fail_credits == 100):
        return "Exclude."
    elif (pass_credits == 0 and defer_credits == 40 and fail_credits == 80) or (
            pass_credits == 0 and defer_credits == 20 and fail_credits == 100) or (
            pass_credits == 0 and defer_credits == 0 and fail_credits == 120):
        return "Exclude."


# ---------------------------------------------------------#

# Part 1 (D)
def graph(progress_count, trailer_count, retriever_count, excluded_count, total):  # Learned the graphics.py module through YouTube - https://www.youtube.com/watch?v=R39vTAj1u_8&list=PLmzkEJ1Zz_uZ5nvTOLaGHfinCzEVEVBlz&index=1
    height_index = 10  # The increment amount of pixels per tallied outcomes
    progress_rect = (progress_count * height_index)  # ending with "_rect" means the total amount of pixels which the histogram is tall per each outcome
    trailer_rect = (trailer_count * height_index)
    retriever_rect = (retriever_count * height_index)
    excluded_rect = (excluded_count * height_index)


    column_start = 535  # The starting point of the histogram per each outcome
    progress_height = (column_start - progress_rect)
    trailer_height = (column_start - trailer_rect)
    retriever_height = (column_start - retriever_rect)
    excluded_height = (column_start - excluded_rect)


    counter_start = 522  # The starting point of the Text above the histogram rectangle indicating how many outcomes of that specific outcome
    progress_counter = (counter_start - progress_rect)  # ending with "_counter" means the total amount of pixels which the tallied amount should be displayed
    trailer_counter = (counter_start - trailer_rect)
    retriever_counter = (counter_start - retriever_rect)
    excluded_counter = (counter_start - excluded_rect)


    total_outcomes = (f"{total} outcomes in total")


    win = GraphWin("histogram", 1080, 720)  # The histogram being created
    win.setBackground(color_rgb(255, 255, 204))


    progress_position_1 = Text(Point(380, 550), "Progress")  # The positions the outcomes in text below the histogram
    progress_position_1.draw(win)
    trailer_position_1 = Text(Point(472, 550), "Trailer")
    trailer_position_1.draw(win)
    retriever_position_1 = Text(Point(572, 550), "Retriever")
    retriever_position_1.draw(win)
    excluded_position_1 = Text(Point(680, 550), "Excluded")
    excluded_position_1.draw(win)
    total_position_1 = Text(Point(380, 600), total_outcomes)
    total_position_1.draw(win)


    progress_position_3 = Rectangle(Point(340, progress_height), Point(420, 535))  # Rectangle being created of Progress
    progress_position_3.setOutline(color_rgb(0, 0, 0))
    progress_position_3.setFill(color_rgb(144, 238, 144))
    progress_position_3.draw(win)


    progress_position_2 = Text(Point(380, progress_counter), progress_count)  # Text below progress being created
    progress_position_2.draw(win)


    trailer_position_3 = Rectangle(Point(432, trailer_height), Point(512, 535))  # Rectangle being created of Trailer
    trailer_position_3.setOutline(color_rgb(0, 0, 0))
    trailer_position_3.setFill(color_rgb(255, 100, 50))
    trailer_position_3.draw(win)


    trailer_position_2 = Text(Point(472, trailer_counter), trailer_count)  # Text below trailer being created
    trailer_position_2.draw(win)


    retriever_position_3 = Rectangle(Point(532, retriever_height),Point(612, 535))  # Rectangle being created of Retriever
    retriever_position_3.setOutline(color_rgb(0, 0, 0))
    retriever_position_3.setFill(color_rgb(0, 110, 51))
    retriever_position_3.draw(win)


    retriever_position_2 = Text(Point(572, retriever_counter), retriever_count)  # Text below Retriever being created
    retriever_position_2.draw(win)


    excluded_position_3 = Rectangle(Point(640, excluded_height), Point(720, 535))  # Rectangle being created of Excluded
    excluded_position_3.setOutline(color_rgb(0, 0, 0))
    excluded_position_3.setFill(color_rgb(255, 0, 0))
    excluded_position_3.draw(win)


    excluded_position_2 = Text(Point(680, excluded_counter), excluded_count)  # Text below excluded being created
    excluded_position_2.draw(win)


    line_1 = Line(Point(310, 535), Point(760, 535))  # Line dividing histogram and text below being created
    line_1.setOutline(color_rgb(0, 0, 0))
    line_1.setWidth(4)
    line_1.draw(win)

    win.getMouse()
    win.close()


# ---------------------------------------------------------#

# Part 2 (A)
def create_list(data_list, pass_credits, defer_credits, fail_credits, outcome):  # Saving the outcomes to a list
    data_list.append([pass_credits, defer_credits, fail_credits, outcome])


# ---------------------------------------------------------#

# Part 2 (B)
def print_list(data_list):  # Printing the saved List
    print("part 2 (B)")
    print("Stored Data List:")
    for data in data_list:
        print(f"{data[3]} - Pass: {data[0]}, Defer: {data[1]}, Fail: {data[2]}")


# ---------------------------------------------------------#

# Part 3 (A)
def create_and_print_text_file(data_list, file_name="outcome_data.txt"):  # Saving the outcomes to a text file
    with open(file_name, 'w') as file:
        for data in data_list:
            pass_credits, defer_credits, fail_credits, outcome = data
            file.write(f"{outcome.capitalize()} - {pass_credits}, {defer_credits}, {fail_credits}\n")
    file1 = open("outcome_data.txt", "r+") # Learned printing from a text file through GeeksForGeeks - https://www.geeksforgeeks.org/reading-writing-text-files-python/
    print("Part 3 (A)")
    print("Stored Data Text File:")
    print(file1.read())


# ---------------------------------------------------------#

def main():  # Main process of the program being made
    progress_count = 0  # getting the tally of all types of outcomes
    trailer_count = 0
    retriever_count = 0
    excluded_count = 0
    outcome_data = []  # List being created for all outcomes

    # Part (B)
    while True:  # The credits being requested
        pass_credits = get_credits("Please Enter Your Credits at Pass : ")
        if pass_credits not in [0, 20, 40, 60, 80, 100, 120]:
            print("Out of Range.")
            continue

        defer_credits = get_credits("Please Enter your Credits at Defer : ")
        if defer_credits not in [0, 20, 40, 60, 80, 100, 120]:
            print("Out of Range.")
            continue

        fail_credits = get_credits("Please Enter Your Credits at Fail : ")
        if fail_credits not in [0, 20, 40, 60, 80, 100, 120]:
            print("Out of Range.")
            continue

        outcome = predicted_outcome(pass_credits, defer_credits, fail_credits)  # Outcome is being calculated
        print(outcome)

        create_list(outcome_data, pass_credits, defer_credits, fail_credits, outcome)  # Being saved to list

        if outcome == "Progress.":  # Counter being calculated
            progress_count = progress_count + 1
        elif outcome == "Progress(Module trailer).":
            trailer_count = trailer_count + 1
        elif outcome == "Do Not Progress - Module Retriever.":
            retriever_count = retriever_count + 1
        elif outcome == "Exclude.":
            excluded_count = excluded_count + 1

        total = (progress_count + trailer_count + retriever_count + excluded_count)  # Total being calculated

        # Part 1 (C)
        continue_program = input("Do you want to predict another student's outcome? (y/q):")  # Asking whether more predictions to be included or not
        if continue_program.lower() == "y":
            continue
        elif continue_program.lower() == "q":
            graph(progress_count, trailer_count, retriever_count, excluded_count, total)  # Final calling of functions to create & display Histogram and List and Text
            print_list(outcome_data)
            create_and_print_text_file(outcome_data)
            time.sleep(2)
            break
        else:
            continue_program = input("Do you want to predict another student's outcome? (y/q):")


main()  # Whole main program being run
