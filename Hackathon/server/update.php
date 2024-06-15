<?php 
include "../db/config.php";
session_start();  // Fix the typo here
$v_id = $_SESSION['v_id'];
$occupied = $_POST['data'];
$remaining = 15 - $occupied;

if ($_SERVER['REQUEST_METHOD'] === "POST") {
    $sql = "UPDATE bus SET Occ_seats = '" . $occupied . "', Remaining_seats = '" . $remaining . "' WHERE Vehicle_ID = '" . $v_id . "'";
    if (mysqli_query($con, $sql)) {
        echo json_encode(['status' => 'success']);  // Return JSON response
    } else {
        echo json_encode(['status' => 'error', 'message' => mysqli_error($con)]);  // Return JSON response
    }
}
?>
