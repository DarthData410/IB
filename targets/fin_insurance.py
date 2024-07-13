from ib_insync import *
# util.startLoop()  # uncomment this line when in a notebook

class target:
    _symbol:str = ''

    def __init__(self,symbol:str):
        self._symbol = symbol

    def run(self):
        # define a connection
        ib = IB()
        ib.connect('127.0.0.1', 7497, clientId=1)

        # define contract
        contract = Stock(self._symbol,'NYSE','USD')
        
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
        df.to_csv(self._symbol+'10day.csv',header=True,index=False)

        ib.disconnect()

if __name__ == '__main__':
    SLQTt = target('SLQT')
    SLQTt.run()

    ABLt = target('ABL')
    ABLt.run()

    WDHt = target('WDH')
    WDHt.run()

    HIPOt = target('HIPO')
    HIPOt.run()