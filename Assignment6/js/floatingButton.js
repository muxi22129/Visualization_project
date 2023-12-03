// 实现拖拽
let isDragging = false;

function startDrag(event) {
    isDragging = true;
}

window.onmousemove = function (event) {
    event.preventDefault();
    if (isDragging) {
        const floatingBtn = document.querySelector('.floating-btn');
        floatingBtn.style.left = event.clientX - floatingBtn.offsetWidth / 2 + "px";
        floatingBtn.style.top = event.clientY - floatingBtn.offsetHeight / 2 + "px";
    }
}

function stopDrag() {
    isDragging = false;
}