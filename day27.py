import random
import timer


CHARS =" abcdefghijklmnopqrstuvwxyz"
NUM_CHARS = int(input("how many characters would you like?\n" ))

def generate_string(num_chars):
    string = ""
    for _ in range(num_chars):
        string += random.choice(CHARS)
    return string

def user_input():
    return input("copy the given string\n")

def check_string(generated, user):
    if generated == user:
        print("well done")
    else:
        print("try again")

def time_taken(start_time, end_time):
    return timer.elapsed(start_time, end_time)


if __name__ == "__main__":
    generated_string = generate_string(NUM_CHARS)
    print(generated_string)

    start_time = timer.start()
    user_string = user_input()
    end_time = timer.stop()

    check_string(generated_string, user_string)
    print(f"Time taken: {time_taken(start_time, end_time):.2f} seconds")

