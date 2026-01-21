document.addEventListener('DOMContentLoaded', () => {
    const reloadButton = document.getElementById('reload-btn');
    const emailButton = document.getElementById('email-btn');

    if (!reloadButton || !emailButton) return;

    const pathname =
        window.location.pathname === '/'
            ? 'la pantalla de inicio'
            : window.location.pathname;

    const message = `
        Hola, intentaba acceder a ${pathname} en tu web uziel.dev y me arrojó un error 500.
        ¿Podrías ayudarme?`;

    const title = `Error 500 en ${window.location.href}`;

    fetch('/static/error/contact.json')
        .then(res => res.json())
        .then(data => {
            emailButton.href =
                `mailto:${data.email}?subject=${encodeURIComponent(title)}&body=${encodeURIComponent(message)}`;
        })
        .catch(() => {
            // fallback absoluto
            emailButton.href = "mailto:uzielo8017518@gmail.com";
        });

    reloadButton.addEventListener('click', () => {
        window.location.reload();
    });
});