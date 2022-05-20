<?php
    session_start();
    header('Content-type: text/plain; charset=utf-8');
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
 
    //be able to add and delete books from BibloekDB
    if(isset($_POST['Titel'])){
        $title = $_POST['Titel'];
        $author = $_POST['Forfatter'];
        $isbn = $_POST['ISBN'];
        $publisher = $_POST['Forlag'];
        $year = $_POST['Udgivelsesår'];
        $catID = $_POST['Bogkategori'];
        echo $query = "INSERT INTO [dbo].[Books] (Titel, Forfatter, ISBN, Forlag, [Udgivelse], BogkategoriID) VALUES ('$title', '$author', '$isbn', '$publisher', '$year', '$catID')";
        $result = sqlsrv_query($db, $query);
        if(!$result){
            echo "Error: Unable to execute query." . PHP_EOL;
            echo "Debugging error: " . PHP_EOL;
            foreach(sqlsrv_errors() as $error) {
                echo "SQLSTATE: ". $error['SQLSTATE'] . "<br />";
                echo "code: ". $error['code'] . "<br />";
                echo "message: ". $error['message'] . "<br />";
            }
            exit;
        }
    }

    



?>