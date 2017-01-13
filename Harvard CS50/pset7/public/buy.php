<?php
    // configuration
    require_once("../includes/config.php"); 

    $positions = [];
    $user = [];
    // if user reached page via GET (as by clicking a link or via redirect)
    if ($_SERVER["REQUEST_METHOD"] == "GET")
    {
        // get information about the current user
        $info = [];
        $info = CS50::query("SELECT * FROM users WHERE id = ?", $_SESSION["id"]);
        
        // build the necessary information into the user variable
        $user = [
            "username" => $info[0]["username"],
            "cash" => $info[0]["cash"]
        ];
        // render sell_form
        render("buy_form.php", ["title" => "Buy", "user" => $user]);
    }
     // else if user reached page via POST (as by submitting a form via POST)
    else if ($_SERVER["REQUEST_METHOD"] == "POST")
    {
        // validate submission
        if (empty($_POST["symbol"]))
        {
            apologize("You must provide a symbol of a stock to buy");
        }
        else if (empty($_POST["shares"]))
        {
            apologize("You must provide an amount of shares to buy");
        } else if (!preg_match("/^\d+$/", $_POST["shares"]))
        {
            apologize("You can only puchase whole shares of stock.");
        }
        // get information about the current user
        $info = [];
        $info = CS50::query("SELECT * FROM users WHERE id = ?", $_SESSION["id"]);
        
        // build the necessary information into the user variable
        $user = [
            "username" => $info[0]["username"],
            "cash" => $info[0]["cash"]
        ];
        $buy_order = lookup(strtoupper($_POST["symbol"]));
        if ($buy_order == false)
        {
            apologize("{$POST['symbol']} is not a valid symbol");
        }
        elseif ($buy_order["price"] * $_POST["shares"] > $user["cash"])
        {
            apologize("You do not have enough cash to complete this transaction, please deposit additional funds or sell stock");
        }
        $cost = $buy_order["price"] * $_POST["shares"];
        CS50::query("INSERT INTO portfolio (user_id, symbol, shares) VALUES(?, ?, ?) ON DUPLICATE KEY UPDATE shares = shares + VALUES(shares)", $_SESSION["id"], strtoupper($_POST["symbol"]), $_POST["shares"]);
        CS50::query("UPDATE users SET cash = cash - ? WHERE id = ?", $cost, $_SESSION["id"]);
        CS50::query("INSERT INTO history (user_id, symbol, shares, order_type, transaction_amount) VALUES(?, ?, ?, 'BUY', ?)", $_SESSION["id"], $_POST["symbol"], $_POST["shares"], $cost);
        redirect("/");
    }
    
?>