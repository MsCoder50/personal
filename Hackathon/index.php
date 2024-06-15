<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
    <link rel="stylesheet" href="css/client.css">
    <script src="https://code.jquery.com/jquery-3.6.4.min.js"></script>
</head>
<body>
<div id="search-container">
  <form action="index.php" method="POST">
    <input type="text" name="searchquery" id="search-box" placeholder="Search for a bus..." required />
    <button type="submit" id="search-button">Search</button>
  </form>
  </div>
<?php
// Assuming you have a valid database connection established before this point
// Replace these placeholders with your actual database connection details
include "./db/config.php";

// Check if the form has been submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Assuming you have sanitized your input to prevent SQL injection
    $searchquery = mysqli_real_escape_string($con, $_POST['searchquery']);

    // Perform your database query
    $query = "SELECT Vehicle_ID, Bus_num, Occ_seats, Remaining_seats FROM bus WHERE Bus_num LIKE '%$searchquery%'";
    $result = mysqli_query($con, $query);

    // Check if there are any rows in the result set
    if ($result && mysqli_num_rows($result) > 0) {
?>
        <table>
            <thead>
                <tr>
                    <th>Vehicle ID</th>
                    <th>Bus Number</th>
                    <th>Occupied Seats</th>
                    <th>Remaining Seats</th>
                </tr>
            </thead>
            <tbody>
                <?php while ($row = mysqli_fetch_assoc($result)) : ?>
                    <tr>
                        <td><?php echo $row['Vehicle_ID']; ?></td>
                        <td><?php echo $row['Bus_num']; ?></td>
                        <td><?php echo $row['Occ_seats']; ?></td>
                        <td><?php echo $row['Remaining_seats']; ?></td>
                    </tr>
                <?php endwhile; ?>
            </tbody>
        </table>
<?php
    } else {
        echo "<p style='color:white;'>No results found.</p>";
    }
}

mysqli_close($con);
?>
</body>
</html>