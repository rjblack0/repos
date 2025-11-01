#include <iostream>      // lets us use cout to print things
#include <vector>        // gives us access to dynamic lists (vectors)
#include <algorithm>     // lets us use built-in tools like "sort"
#include <unordered_set> // gives us a hash set (to track what we've seen)

using namespace std;     // so we can just write "cout" instead of "std::cout"



#include <iostream>
#include <string>
using namespace std;

int main() {
    string name;
    int age;
    double height;

    cout << "Hello\n\n\n\n Who are you?";
    cin >> name;

    cout << "Enter your age: ";
    cin >> age;

    cout << "Enter your height in meters: ";
    cin >> height;

    cout << "Name: " << name << endl;
    cout << "Age: " << age << endl;
    cout << "Height: " << height << endl;

    return 0;
}

