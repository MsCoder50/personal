const isOn = document.getElementById('start')
const text = document.getElementById('text')
const notification = document.getElementById('notification')
isOn.addEventListener('click',()=>{
    if (isOn.checked) {
        text.innerText = 'Drop Disc/Ball'
        notification.style.display = 'flex'
        notification.innerText = "Grabbed Disc/Ball"
        setTimeout(() => {
            notification.style.display = 'none'
        }, 1000);
    } else {
        text.innerText = 'Grab Disc/Ball'
        notification.style.display = 'flex'
        notification.innerText = "Dropped Disc/Ball"
        setTimeout(() => {
            notification.style.display = 'none'
        }, 1000);
    }
})

