<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
   $fullName = htmlspecialchars($_POST['fullName']);
   $email = htmlspecialchars($_POST['email']);
   $phoneNumber = htmlspecialchars($_POST['phoneNumber']);
   $message = htmlspecialchars($_POST['message']);

   $to = "forchangeprojects@gmail.com";
   $subject = "New Contact Form Submission";
   $body = "You have received a new message from the contact form on your website.\n\n".
           "Full Name: $fullName\n".
           "Email: $email\n".
           "Phone Number: $phoneNumber\n".
           "Message: \n$message";
   $headers = "From: no-reply@yourdomain.com\r\n";
   $headers .= "Reply-To: $email\r\n";

   if (mail($to, $subject, $body, $headers)) {
      http_response_code(200);
      echo "Message sent successfully.";
   } else {
      http_response_code(500);
      echo "Message sending failed.";
   }
} else {
   http_response_code(405);
   echo "Method Not Allowed";
}
?>
