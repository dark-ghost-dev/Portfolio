// Estado global: si las cards extra están expandidas o no
let expanded = false;

// Actualiza qué cards llevan la clase .extra según el ancho
function updateCardExtras() {
    const cards = document.querySelectorAll('#card_container .card');
    const width = window.innerWidth;

    // >=1400px  -> primeras 4 no tienen .extra
    // 992-1399  -> primeras 3 no tienen .extra
    // 768-991   -> primeras 4 no tienen .extra
    // <=767     -> primeras 3 no tienen .extra
    const visibleCount = (width >= 1400 || (width >= 768 && width <= 991)) ? 4 : 3;

    cards.forEach((card, idx) => {
        if (idx < visibleCount) {
            card.classList.remove('extra');
        } else {
            card.classList.add('extra');

            // Reaplicar estado si está expandido
            if (expanded) {
                card.classList.add('active');
            } else {
                card.classList.remove('active');
            }
        }
    });
}

// Ejecutar al cargar
updateCardExtras();

// Resize con debounce (pero sin romper estado)
let resizeTimer;
window.addEventListener('resize', () => {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(() => {
        updateCardExtras();
    }, 150);
});

// Botón mostrar/ocultar
document.querySelectorAll('.all_projects_btn').forEach(btn => {
    btn.addEventListener('click', () => {
        expanded = !expanded;

        const extras = document.querySelectorAll('#card_container .extra');
        extras.forEach(el => {
            el.classList.toggle('active', expanded);
        });

        const icon = btn.querySelector('.all_projects_btn_icon');
        const text = btn.querySelector('.all_projects_btn_text');

        if (icon) icon.classList.toggle('rotated', expanded);
        if (text) text.classList.add('changed');

        setTimeout(() => {
            if (text) {
                text.textContent = expanded ? btn.dataset.show : btn.dataset.hidden;
                text.classList.remove('changed');
            }
        }, 250);
    });
});