// Thème
const html = document.documentElement;
const saved = localStorage.getItem('depenso-theme');
if (saved) { html.setAttribute('data-theme', saved); updateToggleUI(saved); }

function toggleTheme() {
    const next = html.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    html.setAttribute('data-theme', next);
    localStorage.setItem('depenso-theme', next);
    updateToggleUI(next);
}
function updateToggleUI(theme) {
    document.getElementById('themeIcon').textContent = theme === 'dark' ? '🌙' : '☀️';
    document.getElementById('themeLabel').textContent = theme === 'dark' ? 'Sombre' : 'Clair';
}

// Afficher/masquer mot de passe
function togglePass(inputId, btn) {
    const input = document.getElementById(inputId);
    const isHidden = input.type === 'password';
    input.type = isHidden ? 'text' : 'password';
    btn.textContent = isHidden ? '🙈' : '👁';
}

// Force du mot de passe
function checkStrength(val) {
    const fill = document.getElementById('strengthFill');
    const label = document.getElementById('strengthLabel');
    if (!val) { fill.style.width = '0%'; label.textContent = ''; return; }

    let score = 0;
    if (val.length >= 8) score++;
    if (val.length >= 12) score++;
    if (/[A-Z]/.test(val)) score++;
    if (/[0-9]/.test(val)) score++;
    if (/[^A-Za-z0-9]/.test(val)) score++;

    const levels = [
        { pct: '20%', color: '#f87171', text: 'Très faible' },
        { pct: '40%', color: '#fbbf24', text: 'Faible' },
        { pct: '60%', color: '#facc15', text: 'Moyen' },
        { pct: '80%', color: '#4ade80', text: 'Fort' },
        { pct: '100%', color: '#22c55e', text: 'Très fort 💪' },
    ];
    const lvl = levels[Math.min(score - 1, 4)] || levels[0];
    fill.style.width = lvl.pct;
    fill.style.background = lvl.color;
    label.textContent = lvl.text;
    label.style.color = lvl.color;
}

document.querySelectorAll('[data-auto-hide]').forEach(alert => {
    setTimeout(() => {
        alert.classList.add('hiding');
        alert.addEventListener('transitionend', () => alert.remove(), { once: true });
    }, 4000); // disparaît après 4 secondes
});
