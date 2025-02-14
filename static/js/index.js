document.addEventListener("DOMContentLoaded", function () {
    const learnMoreBtn = document.getElementById("learnMoreBtn");
    const extraText = document.getElementById("extraText");

    learnMoreBtn.addEventListener("click", function () {
        extraText.style.display = extraText.style.display === "none" ? "block" : "none";
    });
});
