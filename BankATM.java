class BankATM implements ATMOperations{
    private double balance;
    
    public BankATM(double balance) {
        this.balance = balance;
    }

    public void deposit(double amount) {
        if (amount > 0) 
    }
    public void withdraw(double amount) {
        if (amount <= balance && amount > 0) {
            balance -= amount;
            System.out.println("Withdrawal succesful");
        }
    }
}
