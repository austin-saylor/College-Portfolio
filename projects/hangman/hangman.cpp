/*
CSCI 111 - Final Project: The Hangman Game
Updated by: Austin Saylor
Date: 12/15/22

This program simulates a game of hangman. The steps to it are below:

    1. Upon launching the program, the player is welcomed, and is asked to choose a theme for the game.
       The theme that is chosen dictates the types of words that will be generated for the player to guess.

    2. After choosing the theme, the program reads from the corresponding file, and uses it to generate a random
       word from that file.

    3. After picking a word, the program gives the player the first letter of the word, and prints underscores
       in place of every other letter, as blanks.
    
    4. The player then has to guess a letter that may be in the word.
        - If they are correct, the program will reveal where the guessed letter is in the word
        - If they are incorrect, the program will advance the hangman to the next "stage"
    
    5. The game will end either when the hangman is in Stage 6, or when the player has guessed all of the letters.
        - If the player has guessed all of the letters, they win that game.
        - If the hangman is in Stage 6, that means that the player guessed incorrectly too many times. As a result,
          the player looses that game.

    6. After the game has ended, the program prompts the player to enter a letter, which will determine if the program
       starts a new game, or ends.
       - If the player enters Y or y, the program will start a new hangman game.
       - If the player enters any other letter, the program will end.
*/

// Including libraries
#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <cassert>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cctype>
#include <cstdio>

// Including header files. These files contain the various stages of the hangman.
#include "Stages/stage0.h"
#include "Stages/stage1.h"
#include "Stages/stage2.h"
#include "Stages/stage3.h"
#include "Stages/stage4.h"
#include "Stages/stage5.h"
#include "Stages/stage6.h"

using namespace std;


const float EPSILON = 1e-4; //accuracy upto 4 decimal points

string inFile;
string word;

vector<string> word_list;

vector<char> guesses;

int stage = 0;
int underscores = 10;

int games = 0;
int wins = 0;
int losses = 0;

// Function Prototypes
void test();
void printMenu();
bool Themes();
void readFile(const string inputFileName);
string wordGenerator();
void game();
void printCurrentStage();
char guessEntry();
void checkGuess();
void printCurrentLetters();
void WonOrLost();
char ContinueOrQuit();
int Statistics();
void clearScreen();

int main(int argc, char* argv[]) {
    if (argc == 2 && string(argv[1]) == "test") {
        test();
        return 0;
    }

    cout << "-=+ Welcome to the Hangman Game! +=-" << endl;

    // Prompt the player to select a theme
    Themes();

    // Read data from the selected word file, and put the words into a vector
    readFile(inFile);

    char response = 'y';
    
    // As long as response is equal to y or Y, a new word will be picked, and a new game will be started.
    while(response == 'y' || response == 'Y')
    {
        // Pick a random word from the selected word list.
        word = wordGenerator();

        underscores = 10;
        // Start a game.
        game();

        // Determine if the player won or lost, and provide corresponding feedback.
        clearScreen();
        WonOrLost();

        // Gives the player a chance to change the variable "response" into a different letter, ending the program.
        response = ContinueOrQuit();
        // Clears the vector of guessed letters.
        guesses.clear();
    }
    
    clearScreen();
    Statistics();
    cout << "Goodbye...";
    cin.get();
    return 0;
}

void test() {

}

void printMenu() {
    cout << "Please choose a theme for your hangman game:\n";
    cout << "[1] Food\n";
    cout << "[2] Landscapes\n";
    cout << "[3] Weather\n";
    cout << "[4] Random\n";
    cout << "Enter one of the menu options [1-4]: ";
}

bool Themes() {
    int option = 1; // variable to store user entered option

    // display menu options
    printMenu();
    // Input validation
    do {
        if (cin >> option && option >= 1 && option <= 5) {
            //input is valid, break loop
            break;
        }
        else {
            cin.clear();
            cin.ignore(1000, '\n');
            cout << "Invalid option! please enter a value between 1 and 5" << endl;
        }
    } while (true);
            
    // Call the function(s) or perform some operations based on user input
    switch(option) {
        case 1:
        {
            inFile = "Lists/food.txt";
            break;
        }
        case 2:
        {
            inFile = "Lists/landscapes.txt";
            break;
        }
        case 3:
        {
            inFile = "Lists/weather.txt";
            break;
        }
        case 4:
        {
            inFile = "Lists/random.txt";
            break;
        }
    }
    return true;
}

void readFile(const string inputFileName)
{
    // Gathers data from the selected word file, and puts it into a vector.
    ifstream file;
    file.open (inFile);
    if (!file.is_open()) return;

    while (file >> word)
    {
        word_list.push_back(word);
    }
}

string wordGenerator()
{
    // Generates a random word from the selected word list.
    srand((unsigned) time(NULL));
    int random = rand() % word_list.size();
    string element = word_list[random];

    return element;
}

void printCurrentStage()
{
    // Draws data from the header files to print the stages of the hangman.
    if(stage == 0) {
        printStage0();
    } else if(stage == 1) {
        printStage1();
    } else if(stage == 2) {
        printStage2();
    } else if(stage == 3) {
        printStage3();
    } else if(stage == 4) {
        printStage4();
    } else if(stage == 5) {
        printStage5();
    } else {
        printStage6();
    }
}

char guessEntry()
{
    // Takes the player's letter guess, and pushes it into the "guesses" vector
    char letter_guess;
    cin >> letter_guess;
    char guess = tolower(letter_guess);
    guesses.push_back(guess);
    return letter_guess;
}

string checkGuess(char letter_guess)
{
    // Checks if the player has guessed correctly.
    string guess_results = "Incorrect";
    char lower_guess = tolower(letter_guess);

    for (int i = 0; i < word.size(); i++)
    {
        if (lower_guess == word[i]) {
                return "Correct";
        }
        
    }

    /*
    In the case that the player is incorrect, the hangman will proceed one stage,
    and the function will return "Incorrect".
    */
    stage += 1;
    return "Incorrect";
}

void printCurrentLetters()
{
    // Prints the letters that have been given to, or guessed by the player
    int i;
    int j;
    int printed;
    int size = word.length();
    int guess_count = guesses.size();
    underscores = 0;

    for (i = 1; i < size; i++)
    {
        printed = 0;
        for (j = 0; j < guess_count; j++)
        {
            if (guesses[j] == word[i]) {
                cout << guesses[j] << " ";
                printed = 1;
                break;
        }
        }
        if (printed != 1)
        {
            underscores += 1;
            cout << "_ ";
        }
    }
}

void WonOrLost()
{
    // Checks if the player has won or lost the game, and provides corresponding feedback.
    if (stage == 6){
        printCurrentStage();

        cout << "Game Over! You failed to guess the word... Better luck next time!" << endl;
        cout << "The word was: " << word << endl;
        losses += 1;
    } else {
        printCurrentStage();

        cout << word[0] << " ";
        printCurrentLetters();
        cout << "" << endl;

        cout << "Congratulations! You have successfully guessed the word!" << endl;
        wins += 1;
    }
}

char ContinueOrQuit()
{
    // Determines if the player would like to play more games, or quit.
    char response;
    cout << "Would you like to play again? (y/n): ";
    cin >> response;

    return response;
}

int Statistics()
{
    cout << "-=+ Game Stats: +=-" << endl;
    cout << "Total Wins: " << wins << endl;
    cout << "Total Losses: " << losses << endl;
    cout << "Total Games Played: " << games << endl;
}

// function clears the screen system call
void clearScreen() {
    #ifdef _WIN32
        system("clS");
    #else
        system("clear");
    #endif
}

void game() 
{
    /* 
    The main game function. This function is responsible for keeping the game going, if the stage is less than 6, and if
    there are letters that still need to be guessed.
    */
    int size = word.length();
    char letter_guess = word[0];
    int i = 1;
    int j;
    int round = 1;
    string guess_results = "Correct";
    guesses.push_back(word[0]);

    games += 1;

    stage = 0;
    while (stage < 6)
    {
        if (underscores != 0)
        {
            clearScreen();
            printCurrentStage();

            cout << word[0] << " ";
            printCurrentLetters();
            cout  << "" << endl;
        
            if (guess_results == "Correct")
            {
                cout << "Please guess a letter: ";
            } else {
                cout << "You have guessed incorrectly! Try guessing again: ";
            }

            if (underscores != 0)
            {
                letter_guess = guessEntry();
                
                guess_results = checkGuess(letter_guess);
            }
        } else {
            break;
        }
    }
}