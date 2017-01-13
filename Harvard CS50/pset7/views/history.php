<h1>Previous Transactions</h1>
<div class = "Table">
    <table>
        <tr>
            <th>Order Type</th>
            <th>Symbol</th>
            <th>Shares</th>
            <th>Transaction Amount</th>
        </tr>
        <?php foreach ($transactions as $transaction): ?>
            <tr>
                <td><?= $transaction["order_type"] ?></td>
                <td><?= strtoupper($transaction["symbol"]) ?></td>
                <td><?= $transaction["shares"] ?></td>
                <td><?= "\$" . $transaction["transaction_amount"]?></td>
            </tr>
        <?php endforeach ?>
    </table>
</div>