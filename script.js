const menuBtn = document.querySelector('#menu_btn');
const closeBtn = document.querySelector('#close_btn');
const sidebar = document.querySelector('.sidebar');

menuBtn.addEventListener('click', () => {
    sidebar.style.display = 'block';
});

closeBtn.addEventListener('click', () => {
    sidebar.style.display = 'none';
});
