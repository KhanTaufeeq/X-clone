const menu = document.querySelectorAll('.menu-div'); 

let x = 0;

for (let i = 0; i < menu.length; i++){
    menu[i].addEventListener('click', () => {
        if (x === 0) {
            console.log(menu[i]);
            console.log(menu[i].nextElementSibling);
            menu[i].nextElementSibling.style.display = 'block';
            x = 1;
        } else {
            menu[i].nextElementSibling.style.display = 'none';
            x = 0;
        }
    })
}

console.log(menu);
