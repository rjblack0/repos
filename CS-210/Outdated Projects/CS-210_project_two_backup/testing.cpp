double calculateBalanceWithoutMonthlyDeposit(double initialInvestment, double interestRate, int numberOfYears) {
    double balance = initialInvestment;

    double monthlyInterestRate = (interestRate / 100) / 12;

    for (int year = 1; year <= numberOfYears; ++year) {
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

double balanceWithMonthlyDeposit(double initialInvestment, double monthlyDeposit, double interestRate, int numberOfYears) {
    double balance = initialInvestment;
    double monthlyInterestRate = (interestRate / 100) / 12;
    double interestEarnedThisYear;
    double monthlyInterest;

    for (int year = 1; year <= numberOfYears; ++year) {
        interestEarnedThisYear = 0.0;
        
        for (int month = 1; month <= 12; ++month) {
            monthlyInterest = balance * monthlyInterestRate;

            interestEarnedThisYear += monthlyInterest;
            
            balance += monthlyInterest;
            balance += monthlyDeposit;
        }
        printDetails(year, balance, interestEarnedThisYear);
    }
    return balance;
}on

#include <iostream>
#include <iomanip>

void printDetails(int year, double yearEndBalance, double interestEarned) {
    std::cout << std::fixed << std::setprecision(2);
    std::cout << year << "\t\t" << yearEndBalance << "\t\t" << interestEarned << std::endl;
}