<form action="sell.php" method="post">
    <fieldset>
        <div class="form-group">
            <input autocomplete="off" autofocus class="form-control" name="symbol" placeholder="Symbol" type="text"/>
        </div>
        <div class="form-group">
            <input class="form-control" name="shares" placeholder="# of shares to sell" type="text"/>
        </div>
        <div class="form-group">
            <button class="btn btn-default" type="submit">
                <span aria-hidden="true" class="glyphicon glyphicon-log-in"></span>
                Sell
            </button>
        </div>
    </fieldset>
</form>
<h1>Current Portfolio</h1>
<div class = "Table">
    <table>
        <tr>
            <th>Symbol</th>
            <th>Shares</th>
            <th>Price</th>
            <th>Total Value</th>
        </tr>
        <?php $total = 0 ?>
        <?php foreach ($positions as $position): ?>
            <tr>
                <td><?= $position["symbol"] ?></td>
                <td><?= $position["shares"] ?></td>
                <td><?= "\$" . $position["price"] ?></td>
                <td><?= "\$" . $position["price"] * $position["shares"] ?></td>
            </tr>
            <?php $total += $position["price"] * $position["shares"] ?>
        <?php endforeach ?>
        <tr>
            <td>Total Invested Value</td>
            <td></td>
            <td></td>
            <td><?= "\$" . $total ?></td>
        </tr>
    </table>
</div>