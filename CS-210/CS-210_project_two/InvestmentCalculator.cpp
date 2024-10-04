#include <iostream>
#include <iomanip>
#include "InvestmentCalculator.h"

// Constructor to initialize values
InvestmentCalculator::InvestmentCalculator(double initialInvestment, double monthlyDeposit, double interestRate, int numberOfYears)
    : m_initialInvestment(initialInvestment), m_monthlyDeposit(monthlyDeposit), m_interestRate(interestRate), m_numberOfYears(numberOfYears) {}

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
            balance += m_monthlyDeposit;
        }

        printDetails(year, balance, interestEarnedThisYear);
    }

    return balance;
}

// Method to print details
void InvestmentCalculator::printDetails(int year, double yearEndBalance, double interestEarned) const {
    std::cout << std::fixed << std::setprecision(2);
    std::cout << year << "\t\t" << yearEndBalance << "\t\t" << interestEarned << std::endl;
}