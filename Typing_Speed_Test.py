import time
import random

def typing_speed_test():
    # List of sentences to test typing speed
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "A journey of a thousand miles begins with a single step.",
        "To be or not to be, that is the question.",
        "All that glitters is not gold.",
        "Practice makes perfect."
    ]

    # Select a random sentence
    sentence = random.choice(sentences)
    print("\nTyping Speed Test")
    print("Type the following sentence as fast as you can:")
    print(f"\n\"{sentence}\"\n")

    # Record the start time
    input("Press Enter when you're ready to start...")
    start_time = time.time()

    # Get user input
    typed_sentence = input("\nStart typing: ")

    # Record the end time
    end_time = time.time()

    # Calculate time taken
    time_taken = end_time - start_time

    # Calculate typing speed in words per minute (WPM)
    word_count = len(sentence.split())
    typing_speed = (word_count / time_taken) * 60

    # Calculate accuracy
    correct_chars = sum(1 for a, b in zip(sentence, typed_sentence) if a == b)
    accuracy = (correct_chars / len(sentence)) * 100

    # Display results
    print("\nTyping Test Results:")
    print(f"Time Taken: {time_taken:.2f} seconds")
    print(f"Typing Speed: {typing_speed:.2f} WPM")
    print(f"Accuracy: {accuracy:.2f}%")

# Run the test
typing_speed_test()
