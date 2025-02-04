// marquee-script.js
function randomStringGenerator() {
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    const charactersLength = characters.length;
    let result = '';
    for (let i = 0; i < 20; i++) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;
}

function updateMarquee() {
    const marquee = document.getElementById("randomMarquee");
    marquee.textContent = randomStringGenerator();
}

window.onload = function() {
    updateMarquee();
};
