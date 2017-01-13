<?php

    // configuration
    require("../includes/config.php"); 

    // query portfolio
    $rows = CS50::query("SELECT * FROM portfolio WHERE user_id = ?", $_SESSION["id"]);
    
    // build the positions array
    $positions = [];
    foreach ($rows as $row)
    {
        $stock = lookup($row["symbol"]);
        if ($stock != false)
        {
            $positions[] = [
                "name" => $stock["name"],
                "price" => $stock["price"],
                "shares" => $row["shares"],
                "symbol" => $row["symbol"]
            ];
        }
    }
    // get information about the current user
    $info = [];
    $info = CS50::query("SELECT * FROM users WHERE id = ?", $_SESSION["id"]);
    
    $user = [];
    
    // build the necessary information into the user variable
    $user = [
        "username" => $info[0]["username"],
        "cash" => $info[0]["cash"]
    ];
    
    // set default timezone to CST for greeting
    date_default_timezone_set('America/Chicago');
    
    //create greeting variable
    if (date('H') < 12)
        $greet = ['time' => 'morning'];
    elseif (date('H') < 17)
        $greet = ['time' =>'afternoon'];
    else
        $greet = ['time' => 'evening'];
    
    // render portfolio
    render("portfolio.php", ["positions" => $positions, "title" => "Portfolio", "user" => $user, "greet" => $greet]);

?>
