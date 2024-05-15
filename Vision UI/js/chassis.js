function sendData(key,value) {
    var data = document.getElementById("dataInput").value;
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/chassis", true); // Define the method and endpoint to send data
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
        console.log("Data sent successfully");
        }
    };
    xhr.send(key+"=" + encodeURIComponent(value)); // Send the data as a URL-encoded parameter
}
const arr = document.querySelector("#up")
arr.addEventListener(click,()=>{
    sendData("key","up")
})