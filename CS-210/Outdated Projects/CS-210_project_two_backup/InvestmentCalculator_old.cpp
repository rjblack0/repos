#include <iostream>
#include <iomanip>
#include <limits>  // For std::numeric_limits
#include "InvestmentCalculator.h"

// Constructor
InvestmentCalculator::InvestmentCalculator() {
    m_initialInvestment = 0;
    m_monthlyDeposit = 0;
    m_interestRate = 0;
    m_numberOfYears = 0;
}

// Setters with input validation
void InvestmentCalculator::setInitialInvestment(double initialInvestment) {
    while (initialInvestment <= 0) {
        std::cout << "Invalid input; please enter a positive number.\n";
        std::cout << "Initial Investment Amount: $";
        std::cin >> initialInvestment;
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    }
    m_initialInvestment = initialInvestment;
}

void InvestmentCalculator::setMonthlyDeposit(double monthlyDeposit) {
    while (monthlyDeposit < 0) {
        std::cout << "Invalid input; please enter a positive number.\n";
        std::cout << "Monthly Deposit: $";
        std::cin >> monthlyDeposit;
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    }
    m_monthlyDeposit = monthlyDeposit;
}

void InvestmentCalculator::setInterestRate(double interestRate) {
    while (interestRate <= 0) {
        std::cout << "Invalid input; please enter a positive number.\n";
        std::cout << "Annual Interest (as a percentage): %";
        std::cin >> interestRate;
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    }
    m_interestRate = interestRate;
}

void InvestmentCalculator::setNumYears(int numYears) {
    while (numYears <= 0) {
        std::cout << "Invalid input; please enter a positive number.\n";
        std::cout << "Number of Years: ";
        std::cin >> numYears;
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    }
    m_numberOfYears = numYears;
}

// Method to gather user input
void InvestmentCalculator::getUserInput() {
    double initialInvestment, monthlyDeposit, interestRate;
    int numYears;

    // Prompt user with formatted input screen
    std::cout << "\n********** Data Input **********\n";
    std::cout << "Initial Investment Amount: $";
    std::cin >> initialInvestment;
    setInitialInvestment(initialInvestment);

    std::cout << "Monthly Deposit: $";
    std::cin >> monthlyDeposit;
    setMonthlyDeposit(monthlyDeposit);

    std::cout << "Annual Interest (as a percentage): %";
    std::cin >> interestRate;
    setInterestRate(interestRate);

    std::cout << "Number of Years: ";
    std::cin >> numYears;
    setNumYears(numYears);

    // Now directly prompt for "Press any key to continue..." without repeating the menu
    std::cout << "\nPress any key to continue...\n";
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');  // Clear input buffer
    std::cin.get();  // Wait for any key press
}

// Method to calculate balance without monthly deposit
double InvestmentCalculator::calculateBalanceWithoutMonthlyDeposit() {
    double balance = m_initialInvestment;
    double monthlyInterestRate = (m_interestRate / 100) / 12;

    for (int year = 1; year <= m_numberOfYears; ++year) {
        double interestEarnedThisYear = 0.0;

        for (int month = 1; month <= 12; ++month) {
            double monthlyInterest = balance * monthlyInterestRate;
            interestEarnedThisYear += monthlyInterest;
            balance += monthlyInterest;
        }

        printDetails(year, balance, interestEarnedThisYear);
    }

    return balance;
}

// Method to calculate balance with monthly deposit
double InvestmentCalculator::balanceWithMonthlyDeposit() {
    double balance = m_initialInvestment;
    double monthlyInterestRate = (m_interestRate / 100) / 12;

    for (int year = 1; year <= m_numberOfYears; ++year) {
        double interestEarnedThisYear = 0.0;

        for (int month = 1; month <= 12; ++month) {
            double monthlyInterest = balance * monthlyInterestRate;
            interestEarnedThisYear += monthlyInterest;
            balance += monthlyInterest;
            balance += m_monthlyDeposit;  // Add monthly deposit after interest
        }

        printDetails(year, balance, interestEarnedThisYear);
    }

    return balance;
}

// Method to print year-end details with proper alignment
void InvestmentCalculator::printDetails(int year, double yearEndBalance, double interestEarned) const {
    std::cout << std::fixed << std::setprecision(2);
    std::cout << std::setw(5) << year << "\t\t"
        << std::setw(10) << yearEndBalance << "\t\t"
        << std::setw(10) << interestEarned << std::endl;
}
