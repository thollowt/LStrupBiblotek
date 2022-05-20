<?php


    if(isset($_POST['send'])){
        $name = $_POST['name'];
        $email = $_POST['email'];
        $subject = $_POST['subject'];
        $message = $_POST['message'];
        $to = "";
        $headers = "From: $email";
        mail($to, $subject, $message, $headers);
        echo "Mail sent successfully";
    }
?>