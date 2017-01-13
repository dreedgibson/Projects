<?php
    // configuration
    require_once("../includes/config.php"); 
    
     if ($_SERVER["REQUEST_METHOD"] == "GET")
    {
        // query portfolio
        $rows = CS50::query("SELECT * FROM history WHERE user_id = ?", $_SESSION["id"]);
        
        // build the positions array
        foreach ($rows as $row)
        {
            $transactions[] = [
                "order_type" => $row["order_type"],
                "transaction_amount" => $row["transaction_amount"],
                "shares" => $row["shares"],
                "symbol" => $row["symbol"]
            ];
        }
        // render history
        render("history.php", ["transactions" => $transactions, "title" => "History"]);
    }
?>