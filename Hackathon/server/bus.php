<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bus-API</title>
    <script src="https://code.jquery.com/jquery-3.6.4.min.js"></script>
    <style>
        body {
    display: grid;
    height: 100vh;
    place-items: center;
    background-color: #FFF6E9;
}

.rectangle {
    background-color: #fff;
    /* border: 1px solid #2c2c2c; */
    width: 60%;
    height: 50%;
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    grid-template-rows: repeat(3, 1fr);
    gap: 1px;
}

.rectangle .box {
    background-color: #0D9276;
}

.box.clicked {
    background-color: rgb(110, 7, 21); /* Change the color for the clicked state */
}

.hidden {
    display: none;
}

form {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}

input[type=text] {
    margin-left: 5px;
    width: 20%;
    padding: 30px;
    font-size: 20px;
    border: 0.25px solid black;
    transition: all ease 1s;
}

input[type=submit] {
    width: 20%;
    padding: 30px;
    margin-left: 10px;
    font-size: 20px;
    font-family: 'Times New Roman', Times, serif;
}

input[type=text]:focus {
    border: 1px solid black;
}

#dlt {
    padding: 20px;
}
    </style>
</head>
<body>

<?php
session_start();
if (!isset($_SESSION['v_id'])) {
    echo "<script>window.location.href = 'index.php';</script>";
}
?>

<div id="rectangle" class="rectangle">
    <div class="box" onclick="handleBoxClick(this)"></div>
    <div class="box" onclick="handleBoxClick(this)"></div>
    <div class="box" onclick="handleBoxClick(this)"></div>
    <div class="box" onclick="handleBoxClick(this)"></div>
    <div class="box" onclick="handleBoxClick(this)"></div>
    <div class="box" onclick="handleBoxClick(this)"></div>
    <div class="box" onclick="handleBoxClick(this)"></div>
    <div class="box" onclick="handleBoxClick(this)"></div>
    <div class="box" onclick="handleBoxClick(this)"></div>
    <div class="box" onclick="handleBoxClick(this)"></div>
    <div class="box" onclick="handleBoxClick(this)"></div>
    <div class="box" onclick="handleBoxClick(this)"></div>
    <div class="box" onclick="handleBoxClick(this)"></div>
    <div class="box" onclick="handleBoxClick(this)"></div>
    <div class="box" onclick="handleBoxClick(this)"></div>
</div>

<form id="submit" action="delete.php" method="post">
    <input type="submit" value="Destination Arrived">
</form>


    <input class="hidden" type="text" name="clicked" id="clicked_count">
    <button class="hidden" id="submit-form" onclick="updateData()">Click me</button>


<script>
let clickedCount = 0;

function handleBoxClick(box) {
    
    
    box.classList.toggle('clicked')
    if (box.classList.contains('clicked')) {
        clickedCount++;
        const clickedElements = document.querySelectorAll('.box.clicked')
        const clickedCountElement = document.getElementById('clicked_count')
        clickedCountElement.value = Math.abs(clickedCount)
        document.getElementById("submit-form").click()
    } else {
        clickedCount--;
        const clickedElements = document.querySelectorAll('.box.clicked')
        const clickedCountElement = document.getElementById('clicked_count')
        clickedCountElement.value = Math.abs(clickedCount)
        document.getElementById("submit-form").click()
    }
}

function updateData() {
            // Get data from the input field
            var data = $('#clicked_count').val();

            // Make an AJAX request to the PHP backend
            $.ajax({
                type: 'POST',
                url: 'update.php',
                data: { data: data },
                dataType: 'json',
            });
        }
</script>

</body>
</html>
