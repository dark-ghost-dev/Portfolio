const dialog = document.getElementById('dialog_carousel');
const dialogImg = document.getElementById('dialog_image');

const observer = new MutationObserver(() => {
    if (dialog.open) {
        document.documentElement.classList.add('no-scroll');
        document.body.classList.add('no-scroll');
    } else {
        document.documentElement.classList.remove('no-scroll');
        document.body.classList.remove('no-scroll');
    }
});

observer.observe(dialog, {
    attributes: true,
    attributeFilter: ['open']
});

document.querySelectorAll('.carousel-img-wrapper').forEach(button => {
    button.addEventListener('click', () => {
        const img = button.querySelector('img');
        dialogImg.src = img.src;
        dialogImg.alt = img.alt || '';
    });
});