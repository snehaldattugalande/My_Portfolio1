/**
 * Futuristic Data Engineer Portfolio - Interactions & Animations
 */

document.addEventListener("DOMContentLoaded", () => {
    initTerminalTyping();
    initMobileMenu();
});

/**
 * Mobile Hamburger Menu
 */
function initMobileMenu() {
    const hamburger = document.getElementById('hamburger');
    const navRight = document.getElementById('nav-right');
    const overlay = document.getElementById('nav-overlay');
    const navLinks = document.querySelectorAll('.nav-links a');

    function toggleMenu() {
        hamburger.classList.toggle('active');
        navRight.classList.toggle('open');
        overlay.classList.toggle('active');
        document.body.style.overflow = navRight.classList.contains('open') ? 'hidden' : '';
    }

    function closeMenu() {
        hamburger.classList.remove('active');
        navRight.classList.remove('open');
        overlay.classList.remove('active');
        document.body.style.overflow = '';
    }

    hamburger.addEventListener('click', toggleMenu);
    overlay.addEventListener('click', closeMenu);

    // Close menu when a nav link is clicked
    navLinks.forEach(link => {
        link.addEventListener('click', closeMenu);
    });
}

/**
 * Node-based Data Flow Background Animation
 */
function initCanvasAnimation() {
    const canvas = document.getElementById('bg-canvas');
    const ctx = canvas.getContext('2d');
    
    let width, height;
    let particles = [];
    
    function resize() {
        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;
    }
    
    window.addEventListener('resize', resize);
    resize();
    
    class Particle {
        constructor() {
            this.x = Math.random() * width;
            this.y = Math.random() * height;
            this.vx = (Math.random() - 0.5) * 0.5;
            this.vy = (Math.random() - 0.5) * 0.5;
            this.radius = Math.random() * 2 + 1;
            this.color = Math.random() > 0.5 ? '#2563eb' : '#7c3aed';
            this.opacity = Math.random() * 0.5 + 0.1;
        }
        
        update() {
            this.x += this.vx;
            this.y += this.vy;
            
            // Wrap around
            if (this.x < 0) this.x = width;
            if (this.x > width) this.x = 0;
            if (this.y < 0) this.y = height;
            if (this.y > height) this.y = 0;
        }
        
        draw() {
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
            ctx.fillStyle = this.color;
            ctx.globalAlpha = this.opacity;
            ctx.fill();
            
            // Add glow
            ctx.shadowBlur = 10;
            ctx.shadowColor = this.color;
        }
    }
    
    // Create particles
    const particleCount = Math.min(Math.floor(window.innerWidth / 10), 100); // Responsive count
    for (let i = 0; i < particleCount; i++) {
        particles.push(new Particle());
    }
    
    function drawConnections() {
        for (let i = 0; i < particles.length; i++) {
            for (let j = i + 1; j < particles.length; j++) {
                const dx = particles[i].x - particles[j].x;
                const dy = particles[i].y - particles[j].y;
                const distance = Math.sqrt(dx * dx + dy * dy);
                
                if (distance < 150) {
                    ctx.beginPath();
                    ctx.moveTo(particles[i].x, particles[i].y);
                    ctx.lineTo(particles[j].x, particles[j].y);
                    
                    // Opacity based on distance
                    const opacity = 1 - (distance / 150);
                    ctx.strokeStyle = `rgba(139, 155, 180, ${opacity * 0.2})`; // subtle connection
                    ctx.lineWidth = 1;
                    ctx.stroke();
                }
            }
        }
    }
    
    function animate() {
        ctx.clearRect(0, 0, width, height);
        
        // Disable shadow for connections to save performance
        ctx.shadowBlur = 0;
        drawConnections();
        
        for (const p of particles) {
            p.update();
            p.draw();
        }
        
        requestAnimationFrame(animate);
    }
    
    animate();
}

/**
 * Terminal Typing Effect Reset
 * Re-triggers the animation so it looks dynamic.
 */
function initTerminalTyping() {
    const terminalBody = document.getElementById('terminal-body');
    // Optional: Add more interactive terminal commands later
    
    // Simple intersection observer to trigger terminal animation when visible
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Remove and re-add elements to trigger CSS animations
                const delayEls = terminalBody.querySelectorAll('[class*="delay-"]');
                delayEls.forEach(el => {
                    el.style.animation = 'none';
                    el.offsetHeight; /* trigger reflow */
                    el.style.animation = null; 
                });
            }
        });
    }, { threshold: 0.5 });
    
    observer.observe(document.querySelector('.terminal'));
}
