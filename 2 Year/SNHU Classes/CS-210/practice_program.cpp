#include <iostream>
#include <string>

int main() {
    std::string answer;
    char choice;

    do {
        // Ask the question
        std::cout << "Who is the cutest? ";
        std::getline(std::cin, answer);

        // Convert the answer to lowercase for easier comparison
        for (auto &c : answer) c = tolower(c);

        // Check the answer and respond accordingly
        if (answer == "jiayi" || answer == "i am" || answer == "me") {
            std::cout << "That's Right!" << std::endl;
        } else if (answer == "logan") {
            std::cout << "He's the second cutest." << std::endl;
        } else if (answer == "nico") {
            std::cout << "He's pretty cute but not the cutest." << std::endl;
        } else if (answer == "zuko") {
            std::cout << "His butt is cute." << std::endl;
        } else if (answer == "meimei") {
            std::cout << "She's a bad girl and not cute." << std::endl;
        } else if (answer == "ryan") {
            std::cout << "Definitely not the cutest." << std::endl;
        } else {
            std::cout << "That's not a valid answer." << std::endl;
        }

        // Ask if the user wants to guess again
        std::cout << "Do you want to guess again? (y/n): ";
        std::cin >> choice;
        std::cin.ignore(); // Ignore the newline character left in the buffer

    } while (choice == 'y' || choice == 'Y');

    return 0;
}