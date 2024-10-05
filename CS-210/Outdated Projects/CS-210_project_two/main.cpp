#include <iostream>
#include "InvestmentCalculator.h"

int main() {
    // Create the InvestmentCalculator object
    InvestmentCalculator calculator;

    // Call method to gather user input
    calculator.getUserInput();

    // Display results without monthly deposit
    std::cout << "\nBalance and Interest Without Additional Monthly Deposits\n";
    std::cout << "Year\t\tYear End Balance\tYear End Interest Earned\n";
    std::cout << "================================================================\n";
    calculator.calculateBalanceWithoutMonthlyDeposit();

    // Display results with monthly deposit
    std::cout << "\nBalance and Interest With Additional Monthly Deposits\n";
    std::cout << "Year\t\tYear End Balance\tYear End Interest Earned\n";
    std::cout << "================================================================\n";
    calculator.balanceWithMonthlyDeposit();

    return 0;
}
