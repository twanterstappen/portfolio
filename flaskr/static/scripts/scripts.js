// Modern JavaScript for enhanced portfolio functionality
document.addEventListener('DOMContentLoaded', function() {
    
    // Set current year in footer
    const currentYearElement = document.getElementById('current-year');
    if (currentYearElement) {
        currentYearElement.textContent = new Date().getFullYear();
    }
    
    // Navbar scroll effect and mobile menu handling
    const navbar = document.querySelector('.navbar');
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');
    let lastScrollTop = 0;
    let isNavbarOpen = false;
    
    // Simple function to close mobile menu
    function closeMobileMenu() {
        if (navbarCollapse && navbarCollapse.classList.contains('show')) {
            navbarCollapse.classList.remove('show');
            navbarToggler.setAttribute('aria-expanded', 'false');
            isNavbarOpen = false;
        }
    }
    
    // Track navbar state
    if (navbarToggler && navbarCollapse) {
        navbarToggler.addEventListener('click', function() {
            setTimeout(() => {
                isNavbarOpen = navbarCollapse.classList.contains('show');
            }, 50);
        });
    }
    
    // Close navbar when clicking on nav links (mobile)
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', function(e) {
            if (window.innerWidth < 992) {
                closeMobileMenu();
            }
        });
    });
    
    // Close navbar when clicking outside (mobile)
    document.addEventListener('click', function(e) {
        if (window.innerWidth < 992 && 
            isNavbarOpen && 
            !navbar.contains(e.target)) {
            closeMobileMenu();
        }
    });
    
    // Close navbar on escape key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && isNavbarOpen) {
            closeMobileMenu();
        }
    });
    
    window.addEventListener('scroll', function() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        if (scrollTop > 100) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
        
        // Only hide navbar on scroll if it's not open on mobile
        if (!isNavbarOpen && window.innerWidth >= 992) {
            if (scrollTop > lastScrollTop && scrollTop > 200) {
                navbar.style.transform = 'translateY(-100%)';
            } else {
                navbar.style.transform = 'translateY(0)';
            }
        } else if (!isNavbarOpen) {
            // For mobile, always keep navbar visible when closed
            navbar.style.transform = 'translateY(0)';
        }
        
        lastScrollTop = scrollTop;
    });
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Intersection Observer for fade-in animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    // Observe all fade-in elements
    document.querySelectorAll('.fade-in-up').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
    
    // Hero title entrance animation (if on home page)
    const heroTitle = document.querySelector('.hero-title');
    if (heroTitle && window.location.pathname === '/') {
        // Set initial state
        heroTitle.style.opacity = '0';
        heroTitle.style.transform = 'translateY(30px) scale(0.95)';
        heroTitle.style.transition = 'all 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94)';
        
        // Trigger animation after a short delay
        setTimeout(() => {
            heroTitle.style.opacity = '1';
            heroTitle.style.transform = 'translateY(0) scale(1)';
        }, 300);
        
        // Add a subtle glow effect after animation
        setTimeout(() => {
            heroTitle.style.textShadow = '0 0 20px rgba(0, 102, 255, 0.3)';
            
            // Remove glow after a moment
            setTimeout(() => {
                heroTitle.style.textShadow = 'none';
            }, 1500);
        }, 1100);
    }
    
    // Parallax effect for background blobs
    window.addEventListener('scroll', function() {
        const scrolled = window.pageYOffset;
        const parallaxElements = document.querySelectorAll('.blob');
        
        parallaxElements.forEach((element, index) => {
            const speed = (index + 1) * 0.5;
            element.style.transform = `translateY(${scrolled * speed}px)`;
        });
    });
    
    // Enhanced card hover effects
    document.querySelectorAll('.card, .achievement-card').forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-8px) scale(1.02)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });
    
    // Social link hover effects
    document.querySelectorAll('.social-link').forEach(link => {
        link.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-3px) rotate(5deg)';
        });
        
        link.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) rotate(0deg)';
        });
    });
    
    // Button ripple effect
    document.querySelectorAll('.btn-primary, .btn-secondary').forEach(button => {
        button.addEventListener('click', function(e) {
            const ripple = document.createElement('span');
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;
            
            ripple.style.width = ripple.style.height = size + 'px';
            ripple.style.left = x + 'px';
            ripple.style.top = y + 'px';
            ripple.classList.add('ripple');
            
            this.appendChild(ripple);
            
            setTimeout(() => {
                ripple.remove();
            }, 600);
        });
    });
    
    // Performance optimization: Throttle scroll events
    function throttle(func, limit) {
        let inThrottle;
        return function() {
            const args = arguments;
            const context = this;
            if (!inThrottle) {
                func.apply(context, args);
                inThrottle = true;
                setTimeout(() => inThrottle = false, limit);
            }
        }
    }
    
    // Apply throttling to scroll events
    window.addEventListener('scroll', throttle(function() {
        // Additional scroll-based animations can be added here
    }, 16)); // ~60fps
    
    // Loading screen (if needed)
    window.addEventListener('load', function() {
        document.body.classList.add('loaded');
        
        // Trigger initial animations
        setTimeout(() => {
            document.querySelectorAll('.fade-in-up').forEach((el, index) => {
                setTimeout(() => {
                    el.style.opacity = '1';
                    el.style.transform = 'translateY(0)';
                }, index * 100);
            });
        }, 100);
    });
    
    // Keyboard navigation improvements
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Tab') {
            document.body.classList.add('keyboard-navigation');
        }
    });
    
    document.addEventListener('mousedown', function() {
        document.body.classList.remove('keyboard-navigation');
    });
    
    // Dark mode system preference detection (future enhancement)
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        // Already using dark theme
        console.log('Dark mode detected and applied');
    }
    
    // Console Easter egg for fellow developers
    console.log('%c👋 Hello fellow developer!', 'color: #0066ff; font-size: 16px; font-weight: bold;');
    console.log('%cThis portfolio was built with modern web technologies.', 'color: #00d4ff; font-size: 14px;');
    console.log('%cInterested in the code? Check out the GitHub repository!', 'color: #00ff88; font-size: 14px;');
});

// Add CSS for ripple effect
const style = document.createElement('style');
style.textContent = `
    .ripple {
        position: absolute;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.3);
        transform: scale(0);
        animation: ripple-animation 0.6s linear;
        pointer-events: none;
    }
    
    @keyframes ripple-animation {
        to {
            transform: scale(4);
            opacity: 0;
        }
    }
    
    .keyboard-navigation *:focus {
        outline: 2px solid var(--primary-blue) !important;
        outline-offset: 2px;
    }
    
    body:not(.keyboard-navigation) *:focus {
        outline: none;
    }
    
    .loaded .fade-in-up {
        animation: fadeInUp 0.6s ease-out forwards;
    }
`;
document.head.appendChild(style);