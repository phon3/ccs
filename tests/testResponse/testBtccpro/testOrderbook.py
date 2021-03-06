import unittest
import ccs
import datetime
import time

####################################################################################################################
# BTCCPRO                                                                                                          #
####################################################################################################################

class Valid(unittest.TestCase):
    def setUp(self):
        self.stock = ccs.constants.BTCCPRO
        self.base = ccs.constants.XBT
        self.quote = ccs.constants.CNY
        symbol = ccs.btccpro.Symbol(self.base, self.quote)

        self.tz = datetime.timezone.utc

        self.json = '{"asks":[[6929,22],[6930,25]],"bids":[[6910.3,11],[6903,4]],"date":1486145574689}'
        self.orderbook = ccs.btccpro.public.response.OrderBook(self.json, symbol)

        self.m = ccs.btccpro.public.response
        #time.sleep(3)

    def testAsks(self):
        self.assertIsInstance(self.orderbook.asks(), self.m.Orders)

    def testBids(self):
        self.assertIsInstance(self.orderbook.bids(), self.m.Orders)

    def testStock(self):
        self.assertEqual(self.orderbook.stock(), self.stock)

    def testMethod(self):
        self.assertEqual(self.orderbook.method(), ccs.constants.ORDERBOOK)

    def testUsymbol(self):
        self.assertEqual(self.orderbook.usymbol(), self.base + ":" + self.quote)

    def testOsymbol(self):
        pass

    def testData(self):
        pass

    def testRaw(self):
        pass

    def testStr(self):
        pass


if __name__ == '__main__':
    unittest.main()
