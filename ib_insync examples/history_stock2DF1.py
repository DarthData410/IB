from ib_insync import *
# util.startLoop()  # uncomment this line when in a notebook


if __name__ == '__main__':
    # define a connection
    ib = IB()
    ib.connect('127.0.0.1', 7497, clientId=1)

    # define contract
    contract = Stock('SLQT','NYSE','USD')
    
    # define historical data request
    bars = ib.reqHistoricalData(
        contract,
        '',
        '60 D',
        '1 hour',
        'MIDPOINT',
        True
    )

    # convert to pandas dataframe
    df2 = util.df(bars)
    print(df2)