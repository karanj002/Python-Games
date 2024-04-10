#rock paper scissor with AI

import random

def main():

    r="""
                  _ _ _ _
                /        _ _\

    _ _ _ _/        _ _ _|
                           _ _ _|
    _ _ _ _         _ _ _|
                 \ _ _ _ _|
    """

    p="""
                  __
                 /   |
                /    |
               /     | _ _ _ _
    _ _ _ _/     _ _ _ _ _|
                    |_ _ _ _ _ _
                     _ _ _ _ _ _|
                    |_ _ _ _ _
    _ _ _         _ _ _ _ _|
              \     |_ _ _ _ 
                \ _ _ _ _ _|
    """

    s="""                   __
                /     \

    _ _ _ _ /   /\   \ 
                     \ _\_ _ _ _ _ _
                      _ _ _ _ _ _ _ |
                      |_ _ _ _ _ _ _
                      _ _ _ _ _ _ _ |
    _ _ _          |_ _ _
             \        _ _ _|
               \ _ _ _ _ _|
    """

    intro="""
    This is the rock paper scissors game created by stharanzn.
    Enter r for Rock
    p for Paper
    and s for Scissor
    """
    print(intro)
    while True:
        user_choice=input("Enter your choice ")
        machine_choice=random.choice([r,p,s])
        print(machine_choice)
        if machine_choice==r and user_choice=="r" or machine_choice==s and user_choice=="s" or machine_choice==p and user_choice=="p":
            print("Draw")
        if machine_choice==r and user_choice=="s" or machine_choice==s and user_choice=="p" or machine_choice==p and user_choice=="r":
            print("You lose")
        if machine_choice==r and user_choice=="p" or machine_choice==s and user_choice=="r" or machine_choice==p and user_choice=="s":
            print("You win")
