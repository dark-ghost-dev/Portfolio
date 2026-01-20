// Actualiza qué cards llevan la clase .extra según el ancho de la ventana
function updateCardExtras() {
    const cards = document.querySelectorAll('#card_container .card');
    const width = window.innerWidth;

    // >=1572px  -> primeras 4 no tienen .extra
    // 991-1571  -> primeras 3 no tienen .extra
    // 800-991   -> primeras 4 no tienen .extra
    // <=799     -> primeras 3 no tienen .extra
    const visibleCount = (width >= 1572 || (width >= 800 && width <= 991)) ? 4 : 3;

    cards.forEach((card, idx) => {
        if (idx < visibleCount) {
            card.classList.remove('extra');
            card.classList.remove('active');
        } else {
            card.classList.add('extra');
            card.classList.remove('active');
        }
    });
}

// Ejecutar al cargar
updateCardExtras();

// Ejecutar al redimensionar (debounced)
let resizeTimer;
window.addEventListener('resize', () => {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(updateCardExtras, 150);
});

// El botón debe consultar las cards que actualmente tengan .extra
document.querySelectorAll('.all_projects_btn').forEach(btn => {
    btn.addEventListener('click', () => {
        const extras = document.querySelectorAll('#card_container .extra');
        extras.forEach(el => el.classList.toggle('active'));

        const icon = btn.querySelector('.all_projects_btn_icon');
        const text = btn.querySelector('.all_projects_btn_text');
        if (!icon || !text) return;

        icon.classList.toggle('rotated');
        text.classList.add('changed');

        setTimeout(() => {
            const show = btn.dataset.show;
            const hidden = btn.dataset.hidden;
            text.textContent = icon.classList.contains('rotated') ? show : hidden;
            text.classList.remove('changed');
        }, 250);
    });
});