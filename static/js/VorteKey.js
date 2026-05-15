// Range slider — affichage de la valeur
const range = document.getElementById('range');
const rangeValue = document.getElementById('range-value');

if (range && rangeValue) {
    range.addEventListener('input', () => {
        rangeValue.textContent = range.value;
    });
}

// Copier le mot de passe
function copyPassword() {
    const pw = document.getElementById('password');
    const msg = document.getElementById('copy-message');

    if (!pw) return;

    navigator.clipboard.writeText(pw.value).then(() => {
        msg.classList.add('show');
        setTimeout(() => msg.classList.remove('show'), 2000);
    });
}