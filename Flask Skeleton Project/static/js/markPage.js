const activePge = window.location.href;
console.log(activePge);
const navList = document.querySelectorAll('nav a').
 forEach(link => {
    if(link.href == activePge){
        console.log(activePge);
        link.classList.add('active');
    }
});