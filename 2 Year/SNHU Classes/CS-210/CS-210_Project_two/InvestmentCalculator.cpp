#include <iostream>
#include <iomanip>
#include <limits>                               //Import necessary libraries
#include "InvestmentCalculator.h"               //Include my calculator class

InvestmentCalculator::InvestmentCalculator() {  //Constructor initializes the object variables with default values
    m_initialInvestment = 0;
    m_monthlyDeposit = 0;
    m_interestRate = 0;
    m_numberOfYears = 0;
}

void InvestmentCalculator::setInitialInvestment(double initialInvestment) {     //Initialize the setter for Initial Investment
    while (initialInvestment <= 0) {
        std::cout << "Invalid input; please enter a positive number.\n";        //Input validation; if the value is less than 0, stops progress and asks for input again, repeating instructions
        std::cout << "Initial Investment Amount: $";
            std::cin >> initialInvestment;                                      //Populate input to variable
            std::cin.clear();                                                   //Clear error flags for invalid input
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); //Clear leftover characters from input buffer
    }
    m_initialInvestment = initialInvestment;                                    //Populate the main value with the getter value
} //Close InitialInvestment 

void InvestmentCalculator::setMonthlyDeposit(double monthlyDeposit) {           //Initialize the setter for Monthly Deposit
    while (monthlyDeposit < 0) {
        std::cout << "Invalid input; please enter a positive number.\n";        //Input Validation
        std::cout << "Monthly Deposit: $";
            std::cin >> monthlyDeposit;
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    }
    m_monthlyDeposit = monthlyDeposit;
} //Close MonthlyDeposit

void InvestmentCalculator::setInterestRate(double interestRate) {               //Initialize the setter for Interest Rate
    while (interestRate <= 0) {
        std::cout << "Invalid input; please enter a positive number.\n";        //Input Validation
        std::cout << "Annual Interest (as a percentage): %";
            std::cin >> interestRate;
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    }
    m_interestRate = interestRate;
} //Close InterestRate

void InvestmentCalculator::setNumYears(int numYears) {                          //Initialize the setter for Number of Years
    while (numYears <= 0) {
        std::cout << "Invalid input; please enter a positive number.\n";        //Input Validation
        std::cout << "Number of Years: ";
            std::cin >> numYears;
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    }
    m_numberOfYears = numYears;
} //Close NumYears

void InvestmentCalculator::getUserInput() {                                     //Method to gather now populated calculator items
    double initialInvestment, monthlyDeposit, interestRate;
    int numYears;

    std::cout << "\n********** Data Input **********\n";                        //Now display all values as they were entered to the user
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

    std::cout << "\nPress any key to continue...\n";                            //Set up the Press Any Key menu, and wait for input before continuing
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');             //Clear input buffer
    std::cin.get();                                                                 // Wait for any key press
}

double InvestmentCalculator::calculateBalanceWithoutMonthlyDeposit() {          //Method for calculating balance (no deposits)
    double balance = m_initialInvestment;                                           //Follows math conventions
    double monthlyInterestRate = (m_interestRate / 100) / 12;

    for (int year = 1; year <= m_numberOfYears; ++year) {                       //For Loop calculates based on number of years entered
        double interestEarnedThisYear = 0.0;

        for (int month = 1; month <= 12; ++month) {                             //Calculate new interest monthly
            double monthlyInterest = balance * monthlyInterestRate;
            interestEarnedThisYear += monthlyInterest;
            balance += monthlyInterest;                                         //Add interest to current balance
        } //Close monthly interest accural loop

        printDetails(year, balance, interestEarnedThisYear);                    //Print the balances based on yearly
    } //Close yearly balance accural

    return balance;
} //Close Balance Calculation (no deposits)

                                                                                //For loop calculates with interest and monthly deposits
double InvestmentCalculator::balanceWithMonthlyDeposit() {                      
    double balance = m_initialInvestment;                           //Takes initial investment
    double monthlyInterestRate = (m_interestRate / 100) / 12;       //Divides into monthly increments

    for (int year = 1; year <= m_numberOfYears; ++year) {           //Calculate interest
        double interestEarnedThisYear = 0.0;

        for (int month = 1; month <= 12; ++month) {                 //Tabulate new interest monthly
            double monthlyInterest = balance * monthlyInterestRate;
            interestEarnedThisYear += monthlyInterest;
            balance += monthlyInterest;
            balance += m_monthlyDeposit;                            //Add monthly deposit after interest
        } //Close monthly calculation

        printDetails(year, balance, interestEarnedThisYear);            //Display results
    } //Close yearly calculation

    return balance;     
} //Close Balance calculation (with deposits)

// Method to print final end of year balance for either method, with with proper alignment
void InvestmentCalculator::printDetails(int year, double yearEndBalance, double interestEarned) const {
    std::cout << std::fixed << std::setprecision(2);
    std::cout << std::setw(5) << year << "\t\t"
        << std::setw(10) << yearEndBalance << "\t\t"
        << std::setw(10) << interestEarned << std::endl;
}
