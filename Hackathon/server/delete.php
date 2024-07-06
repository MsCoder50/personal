<?php
include "../db/config.php";
session_start();
if(isset($_SESSION['v_id'])){
$vehicle_id = $_SESSION['v_id'];
// echo $vehicle_id;
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
$res = mysqli_query($con,"DELETE FROM bus WHERE Vehicle_ID = '" . $vehicle_id . "'");
if($res){
    echo "<script>alert('Done');</script>";
    header("Location: ./index.php");
    session_destroy();
}
}
}
else{
    header("Location: ./index.php");
}
?> 