const navbar = document.getElementById('navbar');
const openBtn = document.getElementById('open_navbar_button');
const closeBtn = document.getElementById('close_navbar_button');
const openBtnContainer = document.getElementById('open_navbar_button_container');
const triggerBtn = document.getElementById('button_trigger');
const overlay = document.getElementById('overlay');
const trigger = document.getElementById('trigger');
const media = window.matchMedia('(max-width: 563px)');
const navLinks = document.querySelectorAll('nav a');

// Alterna la clase `cls` en el elemento `el` según el estado booleano `state`.
const toggleClass = (el, cls, state) => el.classList.toggle(cls, state);
// Actualiza el atributo `aria-expanded` del botón de apertura con `expanded`.
const setAriaExpanded = (expanded) => openBtn.setAttribute('aria-expanded', expanded);

// Muestra u oculta la barra de navegación según `open` y actualiza ARIA en móvil.
const toggleNavbar = (open) => {
    toggleClass(navbar, 'visible', open);
    if (media.matches) setAriaExpanded(open);
};

// Muestra u oculta el contenedor del botón de apertura según `show`.
const toggleOpenBtnContainer = (show) => toggleClass(openBtnContainer, 'visible', show);
// Muestra u oculta el elemento `trigger` según `show`.
const toggleTrigger = (show) => toggleClass(trigger, 'visible', show);

// Devuelve true si la consulta de media indica vista móvil.
const isMobile = (media) => media.matches;

// Actualiza el atributo `inert` de la navbar según si es vista móvil.
const updateInert = () => {
    if (isMobile(media)) {
        navbar.setAttribute('inert', '');
    } else {
        navbar.removeAttribute('inert')
    }
};

// Restablece el estado de la navbar a su configuración inicial.
const resetNavbarState = () => {
    if (isMobile(media)) toggleNavbar(false);
    toggleOpenBtnContainer(true);
    toggleTrigger(false);
    updateInert();
};

media.addEventListener('change', updateInert);
// Al cargar el DOM: inicializa `inert` y el estado según scroll.
document.addEventListener('DOMContentLoaded', () => {
    updateInert();
});

// Al pulsar el botón de abrir: muestra la navbar y ajusta controles relacionados.
openBtn.addEventListener('click', () => {
    toggleNavbar(true);
    toggleOpenBtnContainer(false);
    toggleTrigger(false);
    navbar.removeAttribute('inert');
});

// Botones/overlay que restablecen el estado de la navbar.
closeBtn.addEventListener('click', resetNavbarState);
overlay.addEventListener('click', resetNavbarState);

// Toggle del trigger al pulsarlo.
triggerBtn.addEventListener('click', () => toggleTrigger(!trigger.classList.contains('visible')));

// Al hacer clic en un enlace de navegación: restablece la navbar.
navLinks.forEach(link => link.addEventListener('click', resetNavbarState));