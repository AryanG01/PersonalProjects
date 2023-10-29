print("What's the secret animal that has a long neck and brown spots.")
secret_word = "giraffe"
guess_word = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess_word != secret_word and not(out_of_guesses):
    if guess_count < guess_limit :
        guess_count += 1
        guess_word = input("Enter Guess: ")        
    else:
        out_of_guesses = True

if out_of_guesses:
    print('Out Of Guesses, YOU LOSE!')
else:
    print('YOU WIN!')


