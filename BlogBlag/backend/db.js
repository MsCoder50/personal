// db.js
import mysql from 'mysql2/promise';

// Create a connection pool
const pool = mysql.createPool({
  host: 'localhost', // Change this if your MariaDB server is hosted elsewhere
  user: 'root', // Replace with your MariaDB username
  password: '', // Replace with your MariaDB password
  database: 'BlogBlag' // Replace with your database name
});

export async function checkEmailExists(email) {
    const [rows] = await pool.query('SELECT COUNT(*) AS count FROM User WHERE email = ?', [email]);
    const [{ count }] = rows;
    return count > 0;
  }
  
  // Function to check if username exists
  export async function checkUsernameExists(username) {
    const [rows] = await pool.query('SELECT COUNT(*) AS count FROM User WHERE username = ?', [username]);
    const [{ count }] = rows;
    return count > 0;
  }
  
  export default pool;