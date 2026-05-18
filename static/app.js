/* =========================
   LOADING SCREEN
========================= */

const form = document.querySelector("form");

const loadingOverlay =
    document.getElementById("loadingOverlay");

const loadingText =
    document.getElementById("loadingText");

const loadingMessages = [

    "Analyzing soil conditions...",

    "Checking climate patterns...",

    "Calculating rainfall compatibility...",

    "Generating AI farming strategy...",

    "Optimizing crop recommendations...",

    "Preparing smart agriculture insights..."

];

let loadingIndex = 0;

setInterval(() => {

    loadingIndex++;

    if(loadingIndex >= loadingMessages.length){

        loadingIndex = 0;

    }

    loadingText.innerText =
        loadingMessages[loadingIndex];

}, 2200);


form.addEventListener("submit", function(){

    loadingOverlay.classList.add("active");

});