/* 
   ==========================================================================
   Global Scripts & Interactivity
   ========================================================================== 
*/

document.addEventListener('DOMContentLoaded', () => {
    initTheme();
    initAnimations();
    initNavbar();
});

/* Theme Management */
function initTheme() {
    const toggleBtn = document.getElementById('toggle-theme');
    const html = document.documentElement;
    
    // Check local storage, system preference, or default to light
    const savedTheme = localStorage.getItem('theme');
    const systemDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    
    // Set initial theme
    let currentTheme = 'light';
    if (savedTheme) {
        currentTheme = savedTheme;
    } else if (systemDark) {
        currentTheme = 'dark';
    }
    
    html.setAttribute('data-theme', currentTheme);
    updateThemeIcon(toggleBtn, currentTheme);

    // Listen for system theme changes
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
        if (!localStorage.getItem('theme')) {
            const newTheme = e.matches ? 'dark' : 'light';
            html.setAttribute('data-theme', newTheme);
            updateThemeIcon(toggleBtn, newTheme);
        }
    });

    if (toggleBtn) {
        toggleBtn.addEventListener('click', () => {
            const currentTheme = html.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            
            html.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            updateThemeIcon(toggleBtn, newTheme);
            
            // Animate icon
            toggleBtn.style.transform = 'rotate(360deg)';
            setTimeout(() => toggleBtn.style.transform = 'rotate(0deg)', 300);
        });
    }
}

function updateThemeIcon(btn, theme) {
    if (!btn) return;
    const icon = btn.querySelector('i');
    if (icon) {
        icon.className = theme === 'dark' ? 'fa-solid fa-sun' : 'fa-solid fa-moon';
    }
}

/* Scroll Animations */
function initAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-fade-in');
                entry.target.style.opacity = '1';
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.glass-card, .section-card, .animate-on-scroll').forEach(el => {
        el.style.opacity = '0';
        observer.observe(el);
    });
}

/* Navbar Glass Effect on Scroll */
function initNavbar() {
    const navbar = document.querySelector('.navbar');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });
}
