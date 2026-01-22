const copyButton = document.getElementById('copy_button');
const emailButton = document.getElementById('email_button');
const facebookButton = document.getElementById('facebook_button');
const whatsappButton = document.getElementById('whatsapp_button');

const toastContainer = document.getElementById('toast_container');
const toast = document.getElementById('copy_toast');
const toastBody = document.getElementById('toast_message');
const toastInstance = bootstrap.Toast.getOrCreateInstance(toast);

const message = 'Mira este gran proyecto de Uziel';
const pageUrl = window.location.href;
const pageTitle = document.title;
const pageDescription = document.querySelector('meta[name="description"]')?.getAttribute('content') || '';

document.addEventListener('DOMContentLoaded', () => {
    copyButton.addEventListener('click', async () => {
        toast.classList.remove('success_copy_toast', 'error_copy_toast');
        try {
            await navigator.clipboard.writeText(pageUrl);
            toastBody.textContent = 'Enlace copiado al portapapeles';
            toast.classList.add('success_copy_toast');
            toastInstance.show();
        } catch (err) {
            toastBody.textContent = 'Error al intentar copiar el enlace';
            toast.classList.add('error_copy_toast');
            toastInstance.show();
        }
    });
    emailButton.href = `mailto:?subject=${encodeURIComponent(message)}&body=${encodeURIComponent(pageTitle + '\n' + pageDescription + '\n' + pageUrl)}`;
    facebookButton.href = `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(pageUrl)}`;
    whatsappButton.href = `https://api.whatsapp.com/send?text=${encodeURIComponent(message + '\n' + pageUrl)}`;
});