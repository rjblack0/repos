// Prompt the user for their information
let userName = prompt("What is your name?");
let birthYear = parseInt(prompt("What year were you born?"), 10);
let birthMonth = parseInt(prompt("What month were you born? (1-12)"), 10);
let birthDay = parseInt(prompt("What day were you born?"), 10);

// Prompt the user for their hobbies
let hobbies = [];
let addMoreHobbies = true;

while (addMoreHobbies) {
    let hobby = prompt("Enter a hobby:");
    hobbies.push(hobby);
    
    let anotherHobby = prompt("Do you want to add another hobby? (yes/no)").toLowerCase();
    if (anotherHobby !== "yes") {
        addMoreHobbies = false;
    }
}

// Current date info
var today = new Date();
var currentDay = today.getDate();
var currentMonth = today.getMonth() + 1; // This is done because January is considered 0!
var currentYear = today.getFullYear();

// Calculate the user's age
let userAge = currentYear - birthYear;

if (currentMonth < birthMonth || (currentMonth === birthMonth && currentDay < birthDay)) {
    userAge -= 1;
}

// Determine if the user is a millennial
function isMillennial(year) {
    return year >= 1981 && year <= 1996;
}

let millennialStatus = isMillennial(birthYear);

// Object representing a person
let person = {
    name: userName,
    age: userAge,
    birthYear: birthYear,
    hobbies: hobbies
};

// Concise output
let message = `Hello, ${person.name}! You are ${person.age} years old, born in ${person.birthYear}, and ${millennialStatus ? 'you are' : 'you are not'} a millennial. Your hobbies include ${person.hobbies.join(', ')}.`;

console.log(message);

// Array of numbers
let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// Use map to create a new array with each number squared
let squaredNumbers = numbers.map(function(num) {
    return num * num;
});
console.log("Squared Numbers:", squaredNumbers);

// Use filter to create a new array with only even numbers
let evenNumbers = numbers.filter(function(num) {
    return num % 2 === 0;
});
console.log("Even Numbers:", evenNumbers);

// Use reduce to sum all numbers in the array
let sumOfNumbers = numbers.reduce(function(accumulator, currentValue) {
    return accumulator + currentValue;
}, 0);
console.log("Sum of Numbers:", sumOfNumbers);

// Use forEach to print each number
numbers.forEach(function(num) {
    console.log("Number:", num);
});

// Define a class for a Book
class Book {
    constructor(title, author, year) {
        this.title = title;
        this.author = author;
        this.year = year;
    }

    // Method to get the book's details
    getDetails() {
        return `${this.title} by ${this.author}, published in ${this.year}`;
    }
}

// Create an instance of the Book class
let myBook = new Book("The Great Gatsby", "F. Scott Fitzgerald", 1925);

console.log(myBook.getDetails());

// Function that returns a promise
function fetchData() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            let data = { name: "John", age: 30 };
            resolve(data);
        }, 2000);
    });
}

// Use .then() to handle the resolved value
fetchData().then(data => {
    console.log("Data fetched:", data);
}).catch(error => {
    console.log("Error:", error);
});

// Function that returns a promise
async function getData() {
    try {
        let data = await fetchData();
        console.log("Data fetched using async/await:", data);
    } catch (error) {
        console.log("Error:", error);
    }
}

// Call the async function
getData();

// Create a new paragraph element
let paragraph = document.createElement("p");
paragraph.textContent = "This is a dynamically created paragraph.";

// Append the paragraph to the body
document.body.appendChild(paragraph);

// Change the background color of the paragraph
paragraph.style.backgroundColor = "lightblue";

// Add an event listener to the paragraph
paragraph.addEventListener("click", function() {
    alert("You clicked the paragraph!");
});