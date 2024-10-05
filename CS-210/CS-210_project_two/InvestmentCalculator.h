#ifndef INVESTMENT_CALCULATOR_H
#define INVESTMENT_CALCULATOR_H

#include <string>

class InvestmentCalculator 
{
public:
    InvestmentCalculator();

    void getUserInput();  // Method for handling user input and validation
    double calculateBalanceWithoutMonthlyDeposit();  // Method to calculate balance without monthly deposits
    double balanceWithMonthlyDeposit();  // Method to calculate balance with monthly deposits
    void printDetails(int year, double yearEndBalance, double interestEarned) const;  // Method to print the results for each year

private:
    int m_numberOfYears;  // User input: Number of years to calculate
        m_initialInvestment;  // User input: Initial investment amount
        m_monthlyDeposit;  // User input: Monthly deposit amount
        m_interestRate;  // User input: Annual interest rate
    
};

#endif // INVESTMENT_CALCULATOR_H