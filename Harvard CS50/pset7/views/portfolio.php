<div id = "welcome">
    <?= "Good " . $greet['time'] . " " . $user["username"] . ", your available cash balance is: \$" . $user["cash"] ?>
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