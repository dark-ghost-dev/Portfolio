function updateErrorInfo() {
    const now = new Date();

    const formattedTime = now.getFullYear() + "-" +
        String(now.getMonth() + 1).padStart(2, "0") + "-" +
        String(now.getDate()).padStart(2, "0") + " " +
        String(now.getHours()).padStart(2, "0") + ":" +
        String(now.getMinutes()).padStart(2, "0") + ":" +
        String(now.getSeconds()).padStart(2, "0");

    document.querySelectorAll(".path").forEach(path => {
        path.textContent = window.location.pathname;
    })

    document.getElementById("current-time").textContent =
        formattedTime;
}

function generateRandomId(long = 8) {
    const caracters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let result = '';

    for (let i = 0; i < long; i++) {
        const index = Math.floor(Math.random() * caracters.length);
        result += caracters.charAt(index);
    }

    return result;
}

// Ejecutar al cargar
updateErrorInfo();

// Actualizar cada segundo
setInterval(updateErrorInfo, 1000);

const id = document.getElementById('id');

document.addEventListener('DOMContentLoaded', () => {
    id.textContent = generateRandomId(8);
});