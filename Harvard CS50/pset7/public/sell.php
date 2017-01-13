<?php
    // configuration
    require_once("../includes/config.php"); 

    $positions = [];
    $user = [];
    // if user reached page via GET (as by clicking a link or via redirect)
    if ($_SERVER["REQUEST_METHOD"] == "GET")
    {
        // query portfolio
        $rows = CS50::query("SELECT * FROM portfolio WHERE user_id = ?", $_SESSION["id"]);
        
        // build the positions array
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
        
        // build the necessary information into the user variable
        $user = [
            "username" => $info[0]["username"],
            "cash" => $info[0]["cash"]
        ];
        // render sell_form
        render("sell_form.php", ["positions" => $positions, "title" => "Sell", "user" => $user]);
    }
    
    // else if user reached page via POST (as by submitting a form via POST)
    else if ($_SERVER["REQUEST_METHOD"] == "POST")
    {
        // validate submission
        if (empty($_POST["symbol"]))
        {
            apologize("You must provide a symbol of a stock to sell");
        }
        else if (empty($_POST["shares"]))
        {
            apologize("You must provide an amount of shares to sell");
        } 
        $sell_order = CS50::query("SELECT shares FROM portfolio WHERE symbol = ? AND user_id = ?", strtoupper($_POST['symbol']), $_SESSION["id"]);
        if ($sell_order == false)
        {
            apologize("You must provide the symbol of a stock you currently own.");
        } 
        else if ($sell_order[0]["shares"] < $_POST["shares"])
        {
            apologize("You can not sell shares you don't own!");
        }
        
        $stock = lookup(strtoupper($_POST["symbol"]));
        $new_cash = $_POST["shares"] * $stock["price"];
        
        if ($sell_order[0]["shares"] > $_POST["shares"])
        {
            CS50::query("UPDATE portfolio SET shares = shares - ? WHERE user_id = ? AND symbol = ?", $_POST["shares"], $_SESSION["id"], $_POST["symbol"]);
        } else {
            CS50::query("DELETE FROM portfolio WHERE user_id = ? AND symbol = ?", $_SESSION["id"], $_POST["symbol"]);
        }
        CS50::query("UPDATE users SET cash = cash + ? WHERE id = ?", $new_cash, $_SESSION["id"]);
        CS50::query("INSERT INTO history (user_id, symbol, shares, order_type, transaction_amount) VALUES(?, ?, ?, 'SELL', ?)", $_SESSION["id"], strtoupper($_POST["symbol"]), $_POST["shares"], $new_cash); 
        redirect("/");
    }
?>