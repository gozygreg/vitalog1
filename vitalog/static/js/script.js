document.addEventListener("DOMContentLoaded", function () {
    const toggles = document.querySelectorAll('.toggleText');
    toggles.forEach(toggle => {
        const moreBtn = toggle.querySelector('.more');
        moreBtn.addEventListener('click', function () {
            const additionalContent = toggle.querySelector('.additional-content');
            if (additionalContent.style.display === "none" || additionalContent.style.display === "") {
                additionalContent.style.display = 'block';
                moreBtn.textContent = "Read less";
            } else {
                additionalContent.style.display = 'none';
                moreBtn.textContent = "Read more";
            }
        });
    });
});