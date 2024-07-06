const isOn = document.getElementById('start')
const load = document.getElementById('load')
const text = document.getElementById('text')
isOn.addEventListener('click',()=>{
    if (isOn.checked) {
        load.style.display = 'block'
        text.innerText = 'Stop Shooter'
        notification.style.display = 'flex'
        notification.innerText = "Shooter Started"
        setTimeout(() => {
            notification.style.display = 'none'
        }, 1000);
    } else {
        load.style.display = 'none'
        text.innerText = 'Start Shooter'
        notification.style.display = 'flex'
        notification.innerText = "Shooter Stopped"
        setTimeout(() => {
            notification.style.display = 'none'
        }, 1000);
    }
})

