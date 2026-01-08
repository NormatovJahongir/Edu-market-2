// ==================== //
// GLOBAL FUNCTIONS    //
// ==================== //

// Auto-hide flash messages after 5 seconds
document.addEventListener('DOMContentLoaded', function() {
    const flashMessages = document.querySelectorAll('.alert');
    flashMessages.forEach(alert => {
        setTimeout(() => {
            alert.style.animation = 'slideOut 0.3s ease';
            setTimeout(() => alert.remove(), 300);
        }, 5000);
    });
});

// Smooth scroll for anchor links
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

// Mobile menu toggle
function toggleMobileMenu() {
    const navLinks = document.querySelector('.nav-links');
    navLinks.classList.toggle('active');
}

// Search functionality
function searchCenters() {
    const searchInput = document.getElementById('searchInput');
    if (!searchInput) return;
    
    const searchTerm = searchInput.value.toLowerCase();
    const cards = document.querySelectorAll('.center-card');
    
    cards.forEach(card => {
        const text = card.textContent.toLowerCase();
        if (text.includes(searchTerm)) {
            card.style.display = 'block';
            card.style.animation = 'fadeIn 0.3s ease';
        } else {
            card.style.display = 'none';
        }
    });
}

// Filter functionality
function applyFilters() {
    const ratingFilter = document.getElementById('ratingFilter');
    const subjectFilter = document.getElementById('subjectFilter');
    
    if (!ratingFilter) return;
    
    const cards = Array.from(document.querySelectorAll('.center-card'));
    const grid = document.getElementById('centersGrid');
    
    // Filter by subject
    if (subjectFilter && subjectFilter.value) {
        const subject = subjectFilter.value.toLowerCase();
        cards.forEach(card => {
            const text = card.textContent.toLowerCase();
            card.style.display = text.includes(subject) ? 'block' : 'none';
        });
    }
    
    // Sort by rating
    if (ratingFilter.value === 'high') {
        cards.sort((a, b) => {
            const ratingA = parseFloat(a.querySelector('.rating-badge').textContent);
            const ratingB = parseFloat(b.querySelector('.rating-badge').textContent);
            return ratingB - ratingA;
        });
    } else if (ratingFilter.value === 'low') {
        cards.sort((a, b) => {
            const ratingA = parseFloat(a.querySelector('.rating-badge').textContent);
            const ratingB = parseFloat(b.querySelector('.rating-badge').textContent);
            return ratingA - ratingB;
        });
    }
    
    // Re-append sorted cards
    cards.forEach(card => {
        if (card.style.display !== 'none') {
            grid.appendChild(card);
        }
    });
}

// Enrollment function
function enrollCourse(centerId, subjectId) {
    if (confirm('Bu fanga ro\'yxatdan o\'tmoqchimisiz?')) {
        // Here you would make an AJAX call to the backend
        fetch('/api/enroll', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                center_id: centerId,
                subject_id: subjectId
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Ro\'yxatdan o\'tish muvaffaqiyatli!');
                location.reload();
            } else {
                alert('Xatolik yuz berdi: ' + data.error);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Xatolik yuz berdi. Qayta urinib ko\'ring.');
        });
    }
}

// Form validation
function validateForm(formId) {
    const form = document.getElementById(formId);
    if (!form) return false;
    
    const inputs = form.querySelectorAll('input[required], select[required]');
    let isValid = true;
    
    inputs.forEach(input => {
        if (!input.value.trim()) {
            input.style.borderColor = 'var(--danger)';
            isValid = false;
        } else {
            input.style.borderColor = 'var(--border)';
        }
    });
    
    if (!isValid) {
        alert('Iltimos, barcha majburiy maydonlarni to\'ldiring!');
    }
    
    return isValid;
}

// Number formatting
function formatNumber(num) {
    return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ");
}

// Date formatting
function formatDate(dateString) {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return new Date(dateString).toLocaleDateString('uz-UZ', options);
}

// Loading spinner
function showLoading() {
    const loader = document.createElement('div');
    loader.id = 'loading-spinner';
    loader.className = 'loading-spinner';
    loader.innerHTML = '<div class="spinner"></div>';
    document.body.appendChild(loader);
}

function hideLoading() {
    const loader = document.getElementById('loading-spinner');
    if (loader) {
        loader.remove();
    }
}

// Notification system
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `alert alert-${type}`;
    notification.innerHTML = `
        ${message}
        <button class="close-btn" onclick="this.parentElement.remove()">×</button>
    `;
    
    const container = document.querySelector('.flash-messages') || document.body;
    container.appendChild(notification);
    
    setTimeout(() => {
        notification.remove();
    }, 5000);
}

// Real-time search with debounce
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Initialize real-time search
const searchInput = document.getElementById('searchInput');
if (searchInput) {
    searchInput.addEventListener('input', debounce(searchCenters, 300));
}

// Tab switching
function switchTab(tabName) {
    const tabs = document.querySelectorAll('.tab-content');
    const buttons = document.querySelectorAll('.tab-button');
    
    tabs.forEach(tab => {
        tab.style.display = tab.id === tabName ? 'block' : 'none';
    });
    
    buttons.forEach(button => {
        if (button.dataset.tab === tabName) {
            button.classList.add('active');
        } else {
            button.classList.remove('active');
        }
    });
}

// Print functionality
function printPage() {
    window.print();
}

// Export to CSV (for admin reports)
function exportToCSV(data, filename) {
    const csv = data.map(row => row.join(',')).join('\n');
    const blob = new Blob([csv], { type: 'text/csv' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    a.click();
}

// Confirm action
function confirmAction(message, callback) {
    if (confirm(message)) {
        callback();
    }
}

// Copy to clipboard
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        showNotification('Nusxalandi!', 'success');
    }).catch(err => {
        console.error('Copy failed:', err);
        showNotification('Nusxalash xato ketdi!', 'danger');
    });
}

// Theme toggle (dark mode)
function toggleTheme() {
    document.body.classList.toggle('dark-theme');
    const isDark = document.body.classList.contains('dark-theme');
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
}

// Load saved theme
document.addEventListener('DOMContentLoaded', () => {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        document.body.classList.add('dark-theme');
    }
});

// Animation observer (for scroll animations)
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animate-in');
        }
    });
}, observerOptions);

// Observe all cards for animation
document.querySelectorAll('.center-card, .stat-card, .teacher-card').forEach(card => {
    observer.observe(card);
});

// Add animations CSS
const style = document.createElement('style');
style.textContent = `
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes slideOut {
        from { transform: translateX(0); opacity: 1; }
        to { transform: translateX(400px); opacity: 0; }
    }
    
    .animate-in {
        animation: fadeIn 0.6s ease forwards;
    }
    
    .loading-spinner {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0,0,0,0.5);
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 9999;
    }
    
    .spinner {
        width: 50px;
        height: 50px;
        border: 5px solid #f3f3f3;
        border-top: 5px solid var(--primary);
        border-radius: 50%;
        animation: spin 1s linear infinite;
    }
    
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
`;
document.head.appendChild(style);

console.log('EduMarket System loaded successfully! 🎓');
