<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Collect and sanitize form inputs
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
    $subject = filter_input(INPUT_POST, 'subject', FILTER_SANITIZE_STRING);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);
    
    // Define the recipient and subject of the email
    $to = "mscoder50@gmail.com";
    $email_subject = "Contact Form Submission: " . $subject;
    
    // Create the email body
    $email_body = "You have received a new message from the contact form on your website.\n\n".
                  "Here are the details:\n\n".
                  "Name: $name\n".
                  "Email: $email\n\n".
                  "Message:\n$message";
    
    // Create the email headers
    $headers = "From: $email\n";
    $headers .= "Reply-To: $email";
    
    // Send the email
    if (mail($to, $email_subject, $email_body, $headers)) {
        echo "Message sent successfully.";
    } else {
        echo "Failed to send message.";
    }
}
?>
