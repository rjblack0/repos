#include <iostream>
#include "InvestmentCalculator.h"               //Import the calculator class

int main() {                                    //Start program
    InvestmentCalculator calculator;            //Import Investment Calculator

    calculator.getUserInput();                  //Call Method for user input

    std::cout << "\nBalance and Interest Without Additional Monthly Deposits\n";                //Output headers are formatted
    std::cout << "Year\t\tYear End Balance\tYear End Interest Earned\n";
    std::cout << "================================================================\n";
    calculator.calculateBalanceWithoutMonthlyDeposit();                                         //Display the results for calculations without Monthly Deposit

    // Display results with monthly deposit
    std::cout << "\nBalance and Interest With Additional Monthly Deposits\n";
    std::cout << "Year\t\tYear End Balance\tYear End Interest Earned\n";
    std::cout << "================================================================\n";
    calculator.balanceWithMonthlyDeposit();                                                     //Display the results for calcualtions with monthly deposit

    return 0;                                   //End program
} //Close main