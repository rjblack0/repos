#ifndef INVESTMENT_CALCULATOR_H
#define INVESTMENT_CALCULATOR_H

class InvestmentCalculator {
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

private:
    int m_numberOfYears;
    double m_initialInvestment;
    double m_monthlyDeposit;
    double m_interestRate;

    void printDetails(int year, double yearEndBalance, double interestEarned) const;
};

#endif // INVESTMENT_CALCULATOR_H
