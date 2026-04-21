let hrsPerDay = 4;
let days = 5;
    let calcStuTime = hrsPerDay * days;

console.log(calcStuTime);


document.addEventListener('DOMContentLoaded', function() {
    // Basic Form Validation
    const loginForm = document.querySelector('form');
    if (loginForm) {
        loginForm.addEventListener('submit', function(event) {
            // Simple validation for demonstration
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            if (!email || !password) {
                alert('Please enter both an email and a password.');
                event.preventDefault(); // Prevent form from submitting
            }
        });
    }

    // Example of handling a dynamic content update (mock functionality)
    const roomLinks = document.querySelectorAll('nav a');
    roomLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault(); // Prevent the default link behavior
            // Simulate loading content dynamically
            const contentArea = document.querySelector('main');
            contentArea.innerHTML = `<h2>${this.textContent} Content Loading...</h2>`;
            // Load content after a delay to simulate fetching data
            setTimeout(() => {
                contentArea.innerHTML = `<h2>${this.textContent}</h2><p>This is dynamically loaded content for the ${this.textContent} section.</p>`;
            }, 1000);
        });
    });

    // Logout Mock-up (no actual logout functionality without server-side)
    const logoutLink = document.querySelector('a[href="logout.html"]');
    if (logoutLink) {
        logoutLink.addEventListener('click', function(event) {
            event.preventDefault();
            alert('Logout Successful!');
            // Redirect to login page or home page
            window.location.href = 'login.html';
        });
    }
});