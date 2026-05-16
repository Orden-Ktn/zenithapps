/* ══════════════════════════════════════════
   Depenso.js
   ══════════════════════════════════════════ */

// ── THÈME ──────────────────────────────────
const html = document.documentElement;

(function initTheme() {
    const saved = localStorage.getItem('depenso-theme');
    if (saved) {
        html.setAttribute('data-theme', saved);
        updateToggleUI(saved);
    }
})();

function toggleTheme() {
    const next = html.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    html.setAttribute('data-theme', next);
    localStorage.setItem('depenso-theme', next);
    updateToggleUI(next);
}

function updateToggleUI(theme) {
    const icon  = document.getElementById('themeIcon');
    const label = document.getElementById('themeLabel');
    if (!icon) return;
    icon.textContent  = theme === 'dark' ? '🌙' : '☀️';
    if (label) label.textContent = theme === 'dark' ? 'Sombre' : 'Clair';
}

// ── MODAL ──────────────────────────────────
const backdrop = document.getElementById('modalBackdrop');
const modal    = document.getElementById('modal');

function openModal() {
    backdrop.classList.add('is-open');
    modal.classList.add('is-open');
    document.body.style.overflow = 'hidden';
    // Focus premier champ
    const first = modal.querySelector('input, textarea, select');
    if (first) setTimeout(() => first.focus(), 50);
}

function closeModal() {
    backdrop.classList.remove('is-open');
    modal.classList.remove('is-open');
    document.body.style.overflow = '';
}

// Fermer avec Échap
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') closeModal();
});

// Rouvrir si erreurs de formulaire Django (rechargement de page)
document.addEventListener('DOMContentLoaded', function () {
    const hasErrors = modal && modal.querySelector('.field-error');
    if (hasErrors) openModal();
});

// Auto-hide notifications
document.querySelectorAll('.alert').forEach(el => {
    setTimeout(() => {
        el.classList.add('hiding');
        setTimeout(() => el.remove(), 500);
    }, 4000);
});

// ── Modal modification ──
function openEditModal(btn) {
    const pk     = btn.dataset.pk;
    const amount = btn.dataset.amount;
    const reason = btn.dataset.reason;
    const date   = btn.dataset.date;

    document.getElementById('editForm').action = `/Depenso/depense/${pk}/update/`;
    document.getElementById('edit_amount').value = amount;
    document.getElementById('edit_reason').value = reason;
    document.getElementById('edit_date').value   = date;

    document.getElementById('editModal').classList.add('is-open');
    document.getElementById('editModalBackdrop').classList.add('is-open');
    document.body.style.overflow = 'hidden';
}

function closeEditModal() {
    document.getElementById('editModal').classList.remove('is-open');
    document.getElementById('editModalBackdrop').classList.remove('is-open');
    document.body.style.overflow = '';
}

// ── Modal suppression ──
function openDeleteModal(btn) {
    const pk     = btn.dataset.pk;
    const reason = btn.dataset.reason;
    const amount = btn.dataset.amount;

    document.getElementById('deleteForm').action = `/Depenso/depense/${pk}/delete/`;
    document.getElementById('deleteModalDetail').textContent = `${reason} — ${amount} FCFA`;

    document.getElementById('deleteModal').classList.add('is-open');
    document.getElementById('deleteModalBackdrop').classList.add('is-open');
    document.body.style.overflow = 'hidden';
}

function closeDeleteModal() {
    document.getElementById('deleteModal').classList.remove('is-open');
    document.getElementById('deleteModalBackdrop').classList.remove('is-open');
    document.body.style.overflow = '';
}

document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        closeModal();
        closeEditModal();
        closeDeleteModal();
    }
});