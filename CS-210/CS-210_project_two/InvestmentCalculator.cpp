#include <iostream>
#include <iomanip>
#include "InvestmentCalculator.h"

// Constructor
InvestmentCalculator::InvestmentCalculator() : m_initialInvestment(0), m_monthlyDeposit(0), m_interestRate(0), m_numberOfYears(0) {}

// Method to handle user input with formatted display
void InvestmentCalculator::getUserInput() {
    // Input for Initial Investment Amount
    do {
        std::cout << "\n********** Data Input **********\n";
        std::cout << "Initial Investment Amount: ";
        if (m_initialInvestment > 0) {
            std::cout << "$" << std::fixed << std::setprecision(2) << m_initialInvestment << "\n";
        }
        else {
            std::cout << "\n";
        }

        std::cout << "Monthly Deposit: ";
        if (m_monthlyDeposit > 0) {
            std::cout << "$" << std::fixed << std::setprecision(2) << m_monthlyDeposit << "\n";
        }
        else {
            std::cout << "\n";
        }

        std::cout << "Annual Interest: ";
        if (m_interestRate > 0) {
            std::cout << "%" << std::fixed << std::setprecision(2) << m_interestRate << "\n";
        }
        else {
            std::cout << "\n";
        }

        std::cout << "Number of Years: ";
        if (m_numberOfYears > 0) {
            std::cout << m_numberOfYears << "\n";
        }
        else {
            std::cout << "\n";
        }

        std::cout << "\nPlease enter the Initial Investment Amount: $";
        std::cin >> m_initialInvestment;

        if (m_initialInvestment <= 0) {
            std::cout << "Error: Initial investment must be a positive number.\n";
            std::cin.clear();
            std::cin.ignore(1000, '\n');
        }
    } while (m_initialInvestment <= 0);

    // Input for Monthly Deposit
    do {
        std::cout << "\n********** Data Input **********\n";
        std::cout << "Initial Investment Amount: $" << std::fixed << std::setprecision(2) << m_initialInvestment << "\n";
        std::cout << "Monthly Deposit: ";
        if (m_monthlyDeposit > 0) {
            std::cout << "$" << std::fixed << std::setprecision(2) << m_monthlyDeposit << "\n";
        }
        else {
            std::cout << "\n";
        }

        std::cout << "Annual Interest: ";
        if (m_interestRate > 0) {
            std::cout << "%" << std::fixed << std::setprecision(2) << m_interestRate << "\n";
        }
        else {
            std::cout << "\n";
        }

        std::cout << "Number of Years: ";
        if (m_numberOfYears > 0) {
            std::cout << m_numberOfYears << "\n";
        }
        else {
            std::cout << "\n";
        }

        std::cout << "\nPlease enter the Monthly Deposit: $";
        std::cin >> m_monthlyDeposit;

        if (m_monthlyDeposit < 0) {
            std::cout << "Error: Monthly deposit must be zero or a positive number.\n";
            std::cin.clear();
            std::cin.ignore(1000, '\n');
        }
    } while (m_monthlyDeposit < 0);

    // Input for Annual Interest
    do {
        std::cout << "\n********** Data Input **********\n";
        std::cout << "Initial Investment Amount: $" << std::fixed << std::setprecision(2) << m_initialInvestment << "\n";
        std::cout << "Monthly Deposit: $" << std::fixed << std::setprecision(2) << m_monthlyDeposit << "\n";
        std::cout << "Annual Interest: ";
        if (m_interestRate > 0) {
            std::cout << "%" << std::fixed << std::setprecision(2) << m_interestRate << "\n";
        }
        else {
            std::cout << "\n";
        }

        std::cout << "Number of Years: ";
        if (m_numberOfYears > 0) {
            std::cout << m_numberOfYears << "\n";
        }
        else {
            std::cout << "\n";
        }

        std::cout << "\nPlease enter the Annual Interest: %";
        std::cin >> m_interestRate;

        if (m_interestRate <= 0) {
            std::cout << "Error: Annual interest must be a positive number.\n";
            std::cin.clear();
            std::cin.ignore(1000, '\n');
        }
    } while (m_interestRate <= 0);

    // Input for Number of Years
    do {
        std::cout << "\n********** Data Input **********\n";
        std::cout << "Initial Investment Amount: $" << std::fixed << std::setprecision(2) << m_initialInvestment << "\n";
        std::cout << "Monthly Deposit: $" << std::fixed << std::setprecision(2) << m_monthlyDeposit << "\n";
        std::cout << "Annual Interest: %" << std::fixed << std::setprecision(2) << m_interestRate << "\n";
        std::cout << "Number of Years: ";
        if (m_numberOfYears > 0) {
            std::cout << m_numberOfYears << "\n";
        }
        else {
            std::cout << "\n";
        }

        std::cout << "\nPlease enter the Number of Years: ";
        std::cin >> m_numberOfYears;

        if (m_numberOfYears <= 0) {
            std::cout << "Error: Number of years must be a positive number.\n";
            std::cin.clear();
            std::cin.ignore(1000, '\n');
        }
        else {
            // Show the updated form with the "Number of Years" value filled in
            std::cout << "\n********** Data Input **********\n";
            std::cout << "Initial Investment Amount: $" << std::fixed << std::setprecision(2) << m_initialInvestment << "\n";
            std::cout << "Monthly Deposit: $" << std::fixed << std::setprecision(2) << m_monthlyDeposit << "\n";
            std::cout << "Annual Interest: %" << std::fixed << std::setprecision(2) << m_interestRate << "\n";
            std::cout << "Number of Years: " << m_numberOfYears << "\n";

            // Wait for the user to press a key to continue
            std::cout << "\nPress any key to continue...\n";
            std::cin.ignore();  // Clear input
            std::cin.get();     // Wait for user input to continue
        }
    } while (m_numberOfYears <= 0);
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
            balance += m_monthlyDeposit;  // Add the monthly deposit after interest
        }

        printDetails(year, balance, interestEarnedThisYear);
    }

    return balance;
}

// Method to print year-end details with proper alignment
void InvestmentCalculator::printDetails(int year, double yearEndBalance, double interestEarned) const {
    std::cout << std::fixed << std::setprecision(2);

    // Print year, balance, and interest earned with proper alignment using std::setw()
    std::cout << std::setw(5) << year << "\t\t"
        << std::setw(10) << yearEndBalance << "\t\t"
        << std::setw(10) << interestEarned << std::endl;
}