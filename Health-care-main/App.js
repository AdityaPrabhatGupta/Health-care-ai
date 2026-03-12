// App.js - Global utilities
// Note: Each page has its own inline JS. This file handles shared utilities.

document.addEventListener('DOMContentLoaded', function () {
  // Mark active nav link based on current page
  const currentPage = window.location.pathname.split('/').pop();
  document.querySelectorAll('nav ul li a').forEach(link => {
    if (link.getAttribute('href') === currentPage) {
      link.classList.add('active');
    }
  });
});