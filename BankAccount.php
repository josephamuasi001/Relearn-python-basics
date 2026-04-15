<?php
class BankAccount {
    private $accountNumber;
    private $accountHolderName;
    private $balance;

    public function __construct($accountNumber, $accountHolderName, $initialBalance = 0) {
        $this->accountNumber = $accountNumber;
        $this->accountHolderName = $accountHolderName;
        $this->balance = $initialBalance;
    }

    public function deposit($amount) {
        if ($amount > 0) {
            $this->balance += $amount;
        }
    }
}