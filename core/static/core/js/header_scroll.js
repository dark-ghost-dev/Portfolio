const handleScrollResize = () => {
    const scrollY = window.scrollY;
    const threshold = window.innerHeight * 0.7;

    if (!isMobile(media)) {
        toggleNavbar(scrollY > threshold);
    } else {
        toggleNavbar(false);
        toggleOpenBtnContainer(scrollY > threshold);
    }
};

window.addEventListener('scroll', () => {
    handleScrollResize();
    if (media.matches) toggleTrigger(false);
});

window.addEventListener('resize', handleScrollResize);

document.addEventListener('DOMContentLoaded', () => {
    handleScrollResize();
});