
import threading

lock = threading.Lock()
print(lock)
def deposit_task(account, amount):
    account_lock = lock
    account_lock.acquire()
    account += amount
    account_lock.release()
#    print('Deposited',amount, 'new ballance = ',account)
    return account

def withdraw_task(account, amount):
    account_lock = lock
    account_lock.acquire()
    account -= amount
    account_lock.release()
#    print('Withdrew', amount, 'new ballance = ',account)
    return account

# ---------------------------------------------------------------

account = 1000
amount_in = 115
amount_out = 140
print('Start ballance = ',account)

for i in range (5):
    print('Step No: ',i)

    deposit_thread = threading.Thread(target=deposit_task, args=(account, amount_in))
    account = deposit_task(account,amount_in)
    print('Deposited', amount_in,';', 'new ballance = ', account)

    withdraw_thread = threading.Thread(target=withdraw_task, args=(account, amount_out))
    account = withdraw_task(account,amount_out)
    print('Withdrew ', amount_out,';', 'new ballance = ', account)

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()