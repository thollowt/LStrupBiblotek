<?php
    session_start();
   # phpinfo();
    error_reporting(E_ALL);
    ini_set('display_errors', 1);
    #Set to utf 8
    mb_internal_encoding('UTF-8');
    $servername = "localhost";
    $connectionOptions = [
        "Database"=>"BiblotekDB",
        "Uid"=>"",
        "PWD"=>""
    ];
    $db = sqlsrv_connect($servername, $connectionOptions);
    if($db == false)
    {
        echo "Connection could not be established.<br>";
        die(print_r(sqlsrv_errors(), true));
    }
    else
    {
        echo "Connection established.<br>";
    }

 //Login
    if(isset($_POST['username'])){
        $username = $_POST['username'];
        $password = $_POST['password'];
        $options =  array( "Scrollable" => SQLSRV_CURSOR_KEYSET );
        $params = array();
        $query = "SELECT * FROM users WHERE username =  '$username' AND Upassword = '$password'";
        $result = sqlsrv_query($db, $query,  $params, $options);
       
    }
       
        if(sqlsrv_num_rows($result) == 1){
            $_SESSION['username'] = $username;
            header("Location: index.html");
        }else{
            echo "Incorrect username or password";
        }
       
    
?>