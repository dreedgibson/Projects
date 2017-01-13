<?php
    // configuration
    require_once("../includes/config.php"); 

    // if user reached page via GET (as by clicking a link or via redirect)
    if ($_SERVER["REQUEST_METHOD"] == "GET")
    {
        // else render form
        render("quote_form.php", ["title" => "Quote"]);
    }
    $stock = lookup($_POST["symbol"]);
    
    if ($stock == false)
    {
        apologize("That stock ticker was not found");
    } else {
        render("quote.php", $stock);
    }
?>