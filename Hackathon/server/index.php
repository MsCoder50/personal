
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="index.css">
</head>
<body>
    <form id="form" action="./index.php" method="post">
        <input type="text" name="bus_num" placeholder="Enter Bus Number">
        <input type="text" name="vehicle_id" placeholder="Enter Vehicle ID">
        <input type="submit" value="Submit">
    </form>
</body>
</html>
<?php
include "../db/config.php";
session_start();
if(!isset($_SESSION['v_id'])){
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $bus_num = $_POST['bus_num'];
    $vehicle_id = $_POST['vehicle_id'];

    $_SESSION['v_id'] = $vehicle_id;

    // Check if a row with the same Vehicle_ID already exists in the database
    $query = "SELECT * FROM bus WHERE Vehicle_ID = '$vehicle_id'";
    $result = mysqli_query($con, $query);

    if (mysqli_num_rows($result) > 0) {
        // A row with the same Vehicle_ID already exists
        echo "<script>alert('A bus with this Vehicle ID already exists.');</script>";
    } else {
        // Insert the new data into the database
        $query = "INSERT INTO bus (Vehicle_ID, Bus_num, Occ_seats, Remaining_seats) VALUES ('$vehicle_id', '$bus_num', 0, 15)";

        // Check for errors in the INSERT query
        if (mysqli_query($con, $query)) {
            echo "<script>alert('Done'); window.location.href = 'bus.php';</script>";
        } else {
            echo "<script>alert('Error: " . mysqli_error($con) . "');</script>";
        }
    }
}
}
else{
  echo "<script>window.location.href = 'bus.php'</script>";
}
?>
