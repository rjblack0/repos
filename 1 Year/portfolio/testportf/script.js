// Smooth scrolling animation for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      document.querySelector(this.getAttribute('href')).scrollIntoView({
        behavior: 'smooth'
      });
    });
  });
  
  // Show/hide navigation menu on mobile devices
  const menuToggle = document.querySelector('.menu-toggle');
  const menu = document.querySelector('.menu');
  
  menuToggle.addEventListener('click', () => {
    menu.classList.toggle('show');
  });
  
  // Filter projects based on category
  const projectList = document.querySelectorAll('.project');
  const filterButtons = document.querySelectorAll('.filter-button');
  
  filterButtons.forEach(button => {
    button.addEventListener('click', () => {
      const category = button.dataset.category;
  
      // Remove active class from all buttons
      filterButtons.forEach(btn => {
        btn.classList.remove('active');
      });
  
      // Add active class to clicked button
      button.classList.add('active');
  
      // Show/hide projects based on category
      projectList.forEach(project => {
        if (category === 'all') {
          project.style.display = 'block';
        } else if (project.dataset.category === category) {
          project.style.display = 'block';
        } else {
          project.style.display = 'none';
        }
      });
    });
  });
  
  // Example of additional JavaScript functionality
  // Replace it with your own custom functionality
  
  // Display current year in the footer
  const currentYear = new Date().getFullYear();
  document.querySelector('footer p').textContent += ` ${currentYear}`;