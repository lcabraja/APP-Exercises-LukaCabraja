import functools
import logging
import random

logging.basicConfig(level=logging.INFO)

class TopupRequest:
    def __init__(self, accountId, amount):
        self.accountId = accountId
        self.amount = amount

class Account:
    def __init__(self, accountId, balance):
        self.accountId = accountId
        self.balance = balance

class DataService:
    def update_account(self, account):
        # Simulate data service update with a random chance of failure
        if random.random() < 0.3:
            raise Exception("Data service update failed")
        account.balance += account.topup_amount

data_service = DataService()

def validate_request(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if args[1] is None:
            raise ValueError("TopupRequest must not be null")
        return func(*args, **kwargs)
    return wrapper

def log_start_end(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Start of {func.__name__}")
        result = func(*args, **kwargs)
        logging.info(f"End of {func.__name__}")
        return result
    return wrapper

def retry_on_failure(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        max_retries = 2
        retries = 0
        while retries <= max_retries:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if retries == max_retries:
                    raise e
                retries += 1
                logging.warning(f"Retry {retries} on {func.__name__} due to {str(e)}")
    return wrapper

class TopupService:
    @retry_on_failure
    @log_start_end
    @validate_request
    def top_up(self, topup_request):
        accountId = topup_request.accountId
        amount = topup_request.amount
        topup_amount = 10 if amount <= 50 else 20

        account = Account(accountId, amount)
        account.topup_amount = topup_amount

        try:
            data_service.update_account(account)
        except Exception as e:
            raise e

if __name__ == "__main__":
    topup_service = TopupService()
    topup_request = TopupRequest(1, 40)
    topup_service.top_up(topup_request)
