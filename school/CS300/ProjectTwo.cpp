/*
 *Ryan Blackburn
 *Southern New Hampshire University
 *CS-300 Project Two
 * Oct 17th 2025
 */

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <cctype>
#include <limits>

static void trim(std::string& s) {          //Helpers for trimming leading and trailing whitespace
    size_t i = 0;
    while (i < s.size() && std::isspace(static_cast<unsigned char>(s[i]))) ++i;
    size_t j = s.size();
    while (j > i && std::isspace(static_cast<unsigned char>(s[j - 1]))) --j;
    s = s.substr(i, j - i);
}

static std::string normalizeCourseNum(std::string s) {      //Helper for changing lowercase to uppercase and removing spaces
    std::string out;
    out.reserve(s.size());
    for (char c : s) {
        if (!std::isspace(static_cast<unsigned char>(c))) {
            out.push_back(static_cast<char>(std::toupper(static_cast<unsigned char>(c))));
        }
    }
    return out;
}

struct Course {
    std::string number;              //normalized key
    std::string title;               // original title text
    std::vector<std::string> prereq;
};

struct Node {
    Course data;
    Node* left;
    Node* right;
    explicit Node(const Course& c) : data(c), left(nullptr), right(nullptr) {}
};

class CourseBST {                       //BST arranged by course.number
public:
    CourseBST() : root(nullptr), count(0) {}
    ~CourseBST() { clear(root); }

    void reset() { clear(root); root = nullptr; count = 0; }        //Clearing tool for clearing lingering data, prevents data corruption

    void insert(const Course& c) {                                  //Also error prevention for when duplicates in the key are found.
        root = insertRec(root, c);
    }

    const Course* find(const std::string& key) const {              //Finder for the course number which returns pointer to course.
        Node* cur = root;
        while (cur) {
            if (key == cur->data.number) return &cur->data;
            if (key < cur->data.number) cur = cur->left;
            else cur = cur->right;
        }
        return nullptr;
    }

    void printInOrder() const {                                     //Printer for the CODE and Title, in alphanumeric
        if (!root) {
            std::cout << "(No courses loaded)\n";
            return;
        }
        printInOrderRec(root);
    }

    size_t size() const { return count; }                       //Store the number of courses, confirmed after load

private:
    Node* root;
    size_t count;

    static void clear(Node* n) {                                //Error clearer
        if (!n) return;
        clear(n->left);
        clear(n->right);
        delete n;
    }

    Node* insertRec(Node* n, const Course& c) {                 //Record inserter
        if (!n) { ++count; return new Node(c); }
        if (c.number < n->data.number)      n->left  = insertRec(n->left, c);
        else if (c.number > n->data.number) n->right = insertRec(n->right, c);
        else {
            n->data = c;
        }
        return n;
    }

    static void printInOrderRec(Node* n) {                  //In order printer
        if (!n) return;
        printInOrderRec(n->left);
        std::cout << n->data.number << ", " << n->data.title << "\n";
        printInOrderRec(n->right);
    }
};

static std::vector<std::string> splitCSV(const std::string& line) {         //Device for parsing the CVS. Begins with pulling data separated by commas
    std::vector<std::string> out;
    std::stringstream ss(line);
    std::string cell;
    while (std::getline(ss, cell, ',')) {
        trim(cell);
        out.push_back(cell);
    }
    return out;
}

/*
 *This loads the CVS into data by going over it in two passes;
 * 1st, it creates a course for each line containing number and title, then insert
 * 2nd, it attaches the prereq numbers, which have been normalized, and reinserts to update
 *Prereqs appearing before and after definitions avoids problems wtih forward-reference
 */

static bool loadCourses(const std::string& filename, CourseBST& bst) {
    std::ifstream in(filename.c_str());
    if (!in) {
        std::cout << "Error: could not open file \"" << filename << "\"\n";
        return false;
    }

    std::vector<std::vector<std::string>> rows;             //Stores tokenized rows in memory so they can be reused on second pass
    rows.reserve(128);

    std::string line;                   //Get lines
    size_t valid = 0;
    while (std::getline(in, line)) {
        std::string tmp = line;
        trim(tmp);
        if (tmp.empty()) continue;      //Skip blank lines

        auto tokens = splitCSV(line);
        if (tokens.size() < 2) {
            continue;
        }

        tokens[0] = normalizeCourseNum(tokens[0]);              //Once course number is stored, normalize
        if (tokens[0].empty() || tokens[1].empty()) continue;

        rows.push_back(tokens);
        ++valid;
    }

    if (valid == 0) {                                           //Error handling
        std::cout << "Error: no valid rows found.\n";
        return false;
    }

    bst.reset();                                                //Fresh start Resetter

    for (const auto& r : rows) {                    //Pass 1: Insert course number and title
        Course c;
        c.number = r[0];
        c.title  = r[1];
        bst.insert(c);
    }

    for (const auto& r : rows) {                    //Pass 2: Add prereqs, and reinsert to override previous records.
        Course c;
        c.number = r[0];
        c.title  = r[1];

        for (size_t i = 2; i < r.size(); ++i) {
            std::string p = normalizeCourseNum(r[i]);
            if (!p.empty()) c.prereq.push_back(p);
        }
        bst.insert(c);
    }

    return bst.size() > 0;
}

static void printCourse(const CourseBST& bst, const std::string& raw) {             //Begin printing function
    std::string key = normalizeCourseNum(raw);                                      //Print Course
    const Course* c = bst.find(key);
    if (!c) {
        std::cout << key << " not found.\n";
        return;
    }

    std::cout << c->number << ", " << c->title << "\n";     //Formatting

    if (c->prereq.empty()) {                                //Print Prereqs
        std::cout << "Prerequisites: None\n";
    } else {
        std::cout << "Prerequisites: ";
        for (size_t i = 0; i < c->prereq.size(); ++i) {
            std::cout << c->prereq[i];
            if (i + 1 < c->prereq.size()) std::cout << ", ";
        }
        std::cout << "\n";
    }
}

static int readChoice() {                                                       //Begin menu function; error handling section
    int choice;
    if (std::cin >> choice) {
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');     //Ignores letters and symbols for error prevention
        return choice;
    }

    std::cin.clear();                                                           //Error handling for bad input, flushes memory
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    return -1;
}

int main() {                                                            //Main Menu Execution
    CourseBST bst;
    bool loaded = false;

    std::cout << "Welcome to the course planner.\n\n";                  //cout menu options
    while (true) {
        std::cout << "1. Load Data Structure.\n";
        std::cout << "2. Print Course List.\n";
        std::cout << "3. Print Course.\n";
        std::cout << "9. Exit\n\n";
        std::cout << "What would you like to do? ";

        int choice = readChoice();
        std::cout << "\n";

        if (choice == 1) {                          //Controller for user choices and output, including error
            std::cout << "Enter file name: ";
            std::string fname;
            std::getline(std::cin, fname);
            trim(fname);

            if (loadCourses(fname, bst)) {
                loaded = true;
            } else {
                loaded = false;
            }
            std::cout << "\n";

        } else if (choice == 2) {
            if (!loaded) {
                std::cout << "Please load the data first (option 1).\n\n";
                continue;
            }
            std::cout << "Schedule:\n\n";
            bst.printInOrder();
            std::cout << "\n";

        } else if (choice == 3) {
            if (!loaded) {
                std::cout << "Please load the data first (option 1).\n\n";
                continue;
            }
            std::cout << "What course do you want to know about? ";
            std::string q;
            std::getline(std::cin, q);
            std::cout << "\n";
            printCourse(bst, q);
            std::cout << "\n";

        } else if (choice == 9) {
            std::cout << "Thank you for using the course planner!\n";
            break;

        } else {
            if (choice != -1) {
                std::cout << choice << " is not a valid option.\n\n";
            } else {
                std::cout << "Invalid input. Please enter a number.\n\n";
            }
        }
    }
    return 0;       //End Program
}
