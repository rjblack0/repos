#include <iostream>
#include "InvestmentCalculator.h"

int main() {
    // Gather user input
    double initialInvestment, monthlyDeposit, annualInterest;
    int numberOfYears;

    std::cout << "Initial Investment Amount: ";
    std::cin >> initialInvestment;
    std::cout << "Monthly Deposit: ";
    std::cin >> monthlyDeposit;
    std::cout << "Annual Interest: ";
    std::cin >> annualInterest;
    std::cout << "Number of Years: ";
    std::cin >> numberOfYears;

    // Create the InvestmentCalculator object
    InvestmentCalculator calculator(initialInvestment, monthlyDeposit, annualInterest, numberOfYears);

    // Display results without monthly deposit
    std::cout << "\nBalance and Interest Without Additional Monthly Deposits\n";
    calculator.calculateBalanceWithoutMonthlyDeposit();

    // Display results with monthly deposit
    std::cout << "\nBalance and Interest With Additional Monthly Deposits\n";
    calculator.balanceWithMonthlyDeposit();

    return 0;
}