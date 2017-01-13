<h1>Deposit Additional Funds</h1>
<form action="deposit.php" method="post">
    <fieldset>
        <div class="form-group">
            <input autocomplete="off" autofocus class="form-control" name="cash" placeholder="cash to deposit" type="text"/>
        </div>
        <div class="form-group">
            <input class="form-control" name="confirmation" placeholder="Please confirm amount" type="text"/>
        </div>
        <div class="form-group">
            <button class="btn btn-default" type="submit">
                <span aria-hidden="true" class="glyphicon glyphicon-log-in"></span>
                Deposit
            </button>
        </div>
    </fieldset>
</form>