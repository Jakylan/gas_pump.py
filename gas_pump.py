from datetime import datetime


def main():
    print('\nHello Welcome to Sprint Mart!!!\n')


while True:
    main()
    payment = input('Prepay or Pay After?\n').strip().upper()
    if payment == 'PREPAY':
        Gas_Type = input(
            '\nType of Gas: Plus, Premium, or Regular\n').strip().upper
        amount = float(input('\nHow much gas are you buying?\n'))
        if Gas_Type == 'PLUS':
            price = 2.8
        elif Gas_Type == 'PREMIUM':
            price = 3.3
        # if Gas_Type == 'REGULAR':
        else:
            price = 2.5
        cost = amount / price  #Gallons per dollar
        print(cost)
        print('\n${}: {:.2f} Total Gallons of Gas!'.format(amount, cost))
        print('\nThanks For Shopping With Sprint Mart Have A Nice Day!!!')
        break
    elif payment == 'PAY AFTER':
        Gas_Type = input('\nType of Gas?: Plus, Premium, or Regular\n')
        amount = float(input('\nHow many gallons are you pumping?\n'))
        if Gas_Type == 'PLUS':
            price = 2.8
        elif Gas_Type == 'PREMIUM':
            price = 3.3
        # if Gas_Type == 'Regular':
        else:
            price = 2.5
        cost = amount * price  #Gallons per dollar
        print(cost)
        print('\n{} Gallons ${:.2f}'.format(amount, cost))
        print('\nThanks For Shopping With Sprint Mart Have A Nice Day!!!')
        break

        time = datetime.now()
        text = '\n{}, {}, {}'.format(time, Gas_Type, amount)

        with open('store_money.txt', 'a') as file:
            file.write(text)

if __name__ == '__main__':
    main()
