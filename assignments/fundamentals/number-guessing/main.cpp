/*
    Guess the Number Assignment
    Updated By: Austin Saylor
    CSCI 111
    Date: 10/24/2022
    
    This program generates a random number, and gives the player 6 chances to guess it before it's game over. Then, regardless of if
    the player "wins" or not, they will have the option to play another game. When the player decides to quit, the program
    will calculate and display statistics like the player's win and loss rate, and the amount of times they played.

    Here are the steps of the program:

        1. Define the necessary variables.
        2. Ask the player for their name, and greet them.
        3. Generate a random number, using the randomNumber() function.
        4. Prompt the player for their guess, check if it is between 1 and 20, and compare it to the random number.
        5. Repeat Step 4 six times, or until the player guesses correctly.
        6. Print a message based on if the player eventually guessed correctly, and add this result to the statistics.
            a. If the player looses, it will also reveal what the random number was.
        7. Reset the "attempt" variable for the next game.
        8. Ask the player if it would like to keep playing or not. Repeat Steps 3-7 if they decide to keep going.
        9. Once the player decides to quit, display the statistics that were collected as they were playing.
*/

#include <iostream>
#include <iomanip>
#include <string>

using namespace std;

string name;
int guess;
int attempt = 1;

int games = 0;
double wins = 0;
double losses = 0;

int randomNumber() {
    int random;
    srand(time(NULL));
     random = ((rand() % 20) + 1 );
     cout << random << endl;

        return random;
}

int readNumber() {
    if(attempt <= 6) {
        cout << "You get 6 tries to guess the number. Take a guess. " << endl;
        while(true) {
            cin >> guess;
        if (guess >= 1 && guess <= 20) {
            break;
        } else {
            cout << "This number is not within the valid range. Please guess a number between 1 and 20." << endl;
            continue;
        } 
        }
    }

    return guess;   
}

int checkGuess(int guess, int random) {
    string comparison;
    int feedback = 0;
    
    while(attempt <= 6) {
        if (guess == random) {
            feedback = 1;
            break;
        } else if (guess < random) {
            attempt += 1;
            feedback = 2;
            comparison = "Your guess is too low.";
            cout << comparison << endl;
            guess = readNumber();    
            continue;
        } else {
            attempt += 1;
            feedback = 2;
            comparison = "Your guess is too high";
            cout << comparison << endl;
            guess = readNumber();
            continue;
        }
    }

    return feedback;
}

int Stats() {
    double percentWins = ((wins/games) * 100);
    double percentLosses = ((losses/games) * 100);

    cout << "--==+ Statistics +==--" << endl;
    cout << "Win Rate: " << percentWins << "%" << endl;
    cout << "Loss Rate: " << percentLosses << "%" << endl;
    cout << "Total Games Played: " << games << endl;

}

void game() {
    int random;
    int guess;
    char response;
    
        cout << "Welcome to -- Guess the Number -- game!" << endl;
        cout << "What is your name? ";
        cin >> name;
        cout << "Hello, " << name << ". I am thinking of a number between 1 and 20." << endl;
    
    while(true) {

        cout << "I am thinking of a number between 1 and 20." << endl;

        random = randomNumber();
        guess = readNumber();

        int feedback = checkGuess(guess, random);

        if (feedback == 1) {
            cout << "Congratulations, " << name << "! You Win!! You guessed my number in "<< attempt << " guesses." << endl;
            games += 1;
            wins += 1;
        } else {
            cout << "Game over! you used all of the guesses you had. Better luck next time!" << endl;
            cout << "The random number was... " << random << endl;
            games += 1;
            losses += 1;
        }

        attempt = 1;

        cout << "Would you like to play again? Enter [y/Y], anything else to quit." << endl;
        cin >> response;
        if (response == 'y' || response == 'Y') {
            continue;
        }
        else {
            break;
        }
    }
}

int main() {
    game();
    Stats();
    cout << "Goodbye!" << endl;
    return 0;
}