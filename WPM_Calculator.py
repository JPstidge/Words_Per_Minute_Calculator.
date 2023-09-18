import time


def calc_wpm(text, type_time):
    words = len(text.split())
    minutes = type_time / 60.0
    wpm = words / minutes
    return wpm


def calculate_accuracy(sample_text, user_input):
    sample_text = sample_text.lower()
    user_input = user_input.lower()

    correct_chars = 0
    total_chars = len(sample_text)

    for i in range(total_chars):
        if i < len(user_input) and sample_text[i] == user_input[i]:
            correct_chars += 1

    accuracy = (correct_chars / total_chars) * 100.0
    return accuracy


def main():
    print("\nAre you ready to calculate your typing speed and accuracy?\n\n")

    sample_text = "Hello! This is a word per minute calculator!"
    print(f"Type the following: {sample_text}")

    # Wait for the user to press ENTER to start the timer
    input("Press ENTER to start.\nDon't forget to press ENTER when finished!")

    start_time = time.time()

    user_input = input("")

    end_time = time.time()

    type_time = end_time - start_time

    wpm = calc_wpm(user_input, type_time)
    accuracy = calculate_accuracy(sample_text, user_input)

    print(f"\nTIME = {type_time:.2f} seconds.")
    print(f"WPM = {wpm:.2f}")
    print(f"Accuracy = {accuracy:.2f}%")


main()

