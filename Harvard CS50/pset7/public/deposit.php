<?php
    // configuration
    require_once("../includes/config.php"); 

    // if user reached page via GET (as by clicking a link or via redirect)
    if ($_SERVER["REQUEST_METHOD"] == "GET")
    {
        render("deposit_form.php", ["title" => "Deposit"]);
    }
    // else if user reached page via POST (as by submitting a form via POST)
    else if ($_SERVER["REQUEST_METHOD"] == "POST")
    {
        // validate submission
        if (empty($_POST["cash"]))
        {
            apologize("You must provide an amount of funds to deposit.");
        }
        else if (empty($_POST["confirmation"]))
        {
            apologize("Please confirm your deposit amount.");
        }
        else if ($_POST["cash"] != $_POST["confirmation"])
        {
            apologize("Your deposit amounts must match!");
        }
        else if ($_POST["cash"] < 0)
        {
            apologize("You can not deposit a negative amount!");
        }
        CS50::query("UPDATE users SET cash = cash + ? WHERE id = ?", $_POST["cash"], $_SESSION["id"]);
        CS50::query("INSERT INTO history (user_id, symbol, shares, order_type, transaction_amount) VALUES(?, 'CASH', 0, 'DEP', ?)", $_SESSION["id"], $_POST["cash"]);
        redirect("/");
    }
?>