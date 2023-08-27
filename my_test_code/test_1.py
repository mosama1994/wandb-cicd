print("I was also run")

def calculate(num):
    print("Running calculate function ...")
    final_price = num * 12.0
    return final_price

def test_num_bought():
    print("Running test_num_bought function ...")
    price = calculate(5)
    assert price == 100