#include <iostream>
#include <vector>
using namespace std;

// First step is to define the function outside of main
void SortVector(vector<int>& myVec) {   // As assigned; next, I will assign my variables
    int temp;                            // I need to be able to swap, so this variable exists as a buffer
    int n = myVec.size();                // This will store the size of the vector
    
    // Next generate the Bubble sort algorithm
    for (int i = 0; i < n - 1; ++i) {    // This is the outer loop that allows for passes
        for (int j = 0; j < n - i - 1; ++j) { // Inner loop that compares the values during each pass
                                        // Start inner if; if the current element is less than the next, they will swap
            if (myVec[j] < myVec[j + 1]) {   // Set the condition comparing the current and next in the vector
                temp = myVec[j];             // The element that I'm currently holding is saved to temp
                myVec[j] = myVec[j + 1];     // The next element in the vector moves to the old slot
                myVec[j + 1] = temp;         // Move the value stored to temp into the next position in the vector.
            }
        }
    }    
}

int main() {                               // Initialize and define variables
    vector<int> myVec;                     // Vector for input numbers
    int numElements;                       // Define the number of variables to sort
    int input;                             // Variable to store each input number

    cin >> numElements;                    // Accept user input for number of variables

    for (int i = 0; i < numElements; ++i) { // Takes all numbers and adds them to the vector
        cin >> input;
        myVec.push_back(input);
    }

    SortVector(myVec);                     // Call the function and perform the sorting.

    // Take all variables and output them
    for (int i = 0; i < myVec.size(); ++i) { // Moves one by one through the vector
        cout << myVec[i];                    // Outputs
        cout << ",";                         // Always add a comma after each element
    }
    cout << endl;                            // Print a newline at the end

    return 0;                                // End the program
}