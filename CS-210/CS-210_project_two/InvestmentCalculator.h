#ifndef INVESTMENT_CALCULATOR_H
#define INVESTMENT_CALCULATOR_H

class InvestmentCalculator {
public:
    InvestmentCalculator(double initialInvestment, double monthlyDeposit, double interestRate, int numberOfYears);
    
    double calculateBalanceWithoutMonthlyDeposit();
    double balanceWithMonthlyDeposit();
    void printDetails(int year, double yearEndBalance, double interestEarned) const;

private:
    double m_initialInvestment;
    double m_monthlyDeposit;
    double m_interestRate;
    int m_numberOfYears;
};

#endif // INVESTMENT_CALCULATOR_H