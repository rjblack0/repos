#ifndef INVESTMENT_CALCULATOR_H
#define INVESTMENT_CALCULATOR_H

#include <string>

class InvestmentCalculator 
{
public:
    // Constructor
    InvestmentCalculator();

    // Setters
    void setInitialInvestment(double initialInvestment);
    void setMonthlyDeposit(double monthlyDeposit);
    void setInterestRate(double interestRate);
    void setNumYears(int numYears);

    // Getters
    double getInitialInvestment() const;
    double getMonthlyDeposit() const;
    double getInterestRate() const;
    int getNumYears() const;

    // Core functionalities
    double calculateBalanceWithoutMonthlyDeposit();
    double balanceWithMonthlyDeposit();
    void getUserInput();

    void getUserInput();  // Method for handling user input and validation
    double calculateBalanceWithoutMonthlyDeposit();  // Method to calculate balance without monthly deposits
    double balanceWithMonthlyDeposit();  // Method to calculate balance with monthly deposits
    void printDetails(int year, double yearEndBalance, double interestEarned) const;  // Method to print the results for each year

private:
    int m_numberOfYears;
    double m_initialInvestment;
    double m_monthlyDeposit;
    double m_interestRate;

    void printDetails(int year, double yearEndBalance, double interestEarned) const;
};

#endif // INVESTMENT_CALCULATOR_H
