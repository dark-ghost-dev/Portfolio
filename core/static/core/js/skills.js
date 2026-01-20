document.querySelectorAll('.skill').forEach(btn => {
    btn.addEventListener('click', () => {
        btn.classList.toggle('clicked');
    });
});