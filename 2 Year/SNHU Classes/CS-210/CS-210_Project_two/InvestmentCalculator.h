#ifndef INVESTMENT_CALCULATOR_H
#define INVESTMENT_CALCULATOR_H

class InvestmentCalculator {                                    //Create the class
public:                                                     //Define all public values and initialize them
    InvestmentCalculator();                                     //Constructor

    void setInitialInvestment(double initialInvestment);        //Create all of my setters, with initialized values
    void setMonthlyDeposit(double monthlyDeposit);
    void setInterestRate(double interestRate);
    void setNumYears(int numYears);

    double getInitialInvestment() const;                        //Create all of my getters, with initialized values
    double getMonthlyDeposit() const;
    double getInterestRate() const;
    int getNumYears() const;

    double calculateBalanceWithoutMonthlyDeposit();             //Create the functions that are used inside of the class
    double balanceWithMonthlyDeposit();
    void getUserInput();

private:                                                    //Define all Private values
    int m_numberOfYears;
    double m_initialInvestment;
    double m_monthlyDeposit;
    double m_interestRate;

    void printDetails(                                      //Define the printing function for main
        int year, 
        double yearEndBalance, 
        double interestEarned
    ) const;
}; //Close program

#endif // INVESTMENT_CALCULATOR_H