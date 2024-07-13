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
        contract=contract,
        endDateTime='',
        durationStr='10 D',
        barSizeSetting='1 min',
        whatToShow='TRADES',
        useRTH=True
    )

    # convert to pandas dataframe
    df = util.df(bars)
    print(df)

    # 'file.json', orient='split', compression='infer', index=True
    df.to_json('SLQT_60D.json',orient='split',compression='infer',index=True)