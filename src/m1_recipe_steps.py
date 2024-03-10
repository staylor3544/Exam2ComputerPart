# collect recipe steps (accumulate steps and step numbers to display)
# print back steps at the end

###############################################################################
# DONE: 1. (5 pts)
#
#   In this module, we will be making a tool that allows a user to input the
#   steps to a recipe. Once the user has entered all the steps, it will print
#   out each step for the user.
#
#   First we need a function that will simply gather a step from the user.
#
#   For this _TODO_ write a function called get_step() that takes one
#   parameter:
#       - num       <-- int
#
#   If given the number 1 for its parameter, this function should prompt the
#   user like so:
#
#       "Please enter the details for step 1: "
#
#   The function should return a re-formatted step. So, if the user typed
#   "Combine dry ingredients.", the function would return
#
#       "1) Combine dry ingredients."
#
#   based on the number that the function was given and the text that the user
#   typed.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def get_step(num):
    details = (input("Please enter the details for step 1: "))
    print(f"{num}: {details}")



###############################################################################
# DONE: 2. (7 pts)
#
#   For this _TODO_, write a function called main() that will start everything
#   off.
#
#   This function should continually as the user for steps in a recipe using a
#   while loop.
#
#   For each iteration of the loop, the function should:
#
#       1. Prompt the user to enter a step for the recipe.
#       2. You should increment the step number so that it starts at 1 and goes
#          up as the user puts in each step.
#       3. You should add each step to a list of steps as you go so you can use
#          the list later.
#       4. If the user types "end" instead of a step, the program should stop
#          asking for new steps.
#       5. Once it is done asking for steps, the program should loop through
#          each re-formatted step that the user typed and print it individually.
#          So you would end up with something like this at the end:
#
#           1) Combine dry ingredients
#           2) Combine wet ingredients
#           3) Combine all ingredients
#           4) Pour batter into pan
#           5) Bake at 350 for 20 min
#           6) Let cool
#
#   Make sure you call your main function to start things off.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def main():
    steps = []
    step_number = 1

    while True:
        user_input = get_step(step_number)

        if user_input.lower() == 'end':
            break

        steps.append(user_input)
        step_number += 1

main()

