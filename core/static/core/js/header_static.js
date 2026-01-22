const handleScrollResize = () => {
    if (!isMobile(media)) {
        toggleNavbar(true);
    } else {
        toggleNavbar(false);
        toggleOpenBtnContainer(true);
    }
}

window.addEventListener('resize', handleScrollResize);

document.addEventListener('DOMContentLoaded', () => {
    handleScrollResize();
});