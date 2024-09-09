// marquee-script.js

// Function to select a random phrase from the list
function getRandomPhrase() {
    const phrases = [
        "The cake is a lie",
        "Welcome to Pasalacqua",
        "Building 6 is empty",
        "You forget a thousand things every day, make sure this is one of them",
        "The workers are going home.",
        "I shouldn't complain, I should have no feeling"
    ];

    // Select a random phrase from the list
    const randomIndex = Math.floor(Math.random() * phrases.length);
    return phrases[randomIndex];
}

// Function to update the marquee with a random phrase
function updateMarquee() {
    const marquee = document.getElementById("randomMarquee");
    marquee.textContent = getRandomPhrase();
}

// Run the update function when the page loads
window.onload = function() {
    updateMarquee();
};
