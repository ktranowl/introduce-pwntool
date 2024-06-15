#!/usr/bin/env python3

import random
from time import time, sleep
import sys
import subprocess
import threading

def generate_problem():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return (num1, num2)

def check_answer(num1, num2, answer):
    return answer == num1 + num2

def game(calculations_count):
    start_time = time()
    for i in range(1, calculations_count+1):
        num1, num2 = generate_problem()
        print(f"Game {i}/{calculations_count}:")
        while True:
            try:
              user_answer = int(input(f"What is {num1} + {num2}? "))
              break  # Exit the loop if input is a valid number
            except ValueError:
              print("Invalid input. Please enter a number.")
        if check_answer(num1, num2, user_answer):
            print("Correct!")
        else:
            print(f"Incorrect. The answer is {num1 + num2}")
            print("Don't rush bruh!")
            quit()

    elapsed_time = time() - start_time

    print(f"Congratulations! You finished in {elapsed_time:.2f} seconds")
    print("Here's your gift:")
    sys.stdout.flush()
    process = subprocess.Popen(["bash"], shell=True)
    process.wait()

def timer_func():
    sleep(10)
    print("\nTime's up")
    print("Do faster next time.")

print("Welcome to our game FAST AND SMART!!")
calculations_count = 1000
print(f"You will do {calculations_count} calculations in 10 seconds.")
print("If you can do that, we'll have a gift for you ;) ")
is_ready = input("Are you ready? (y/n) > ")
if is_ready[0] == 'y':
    print("LET'S STARTTT")
    game_thread = threading.Thread(target=game, daemon=True, args=(calculations_count,)) 
    timer_thread = threading.Thread(target=timer_func)
    timer_thread.start()
    game_thread.start()
else:
    print("Take your time.")
