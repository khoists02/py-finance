from yahoo_lib import FinancialModule
import yfinance as yf
import json

"""
GET CASHFLOW DATA OF STOCK BY QUATERLY
"""


class QuaterlyCashflow(FinancialModule):
    def __init__(self, ticker: str):
        super().__init__(ticker)
        self.name = 'Quaterly Cashflow'
        self.description = 'Quaterly Cashflow'

    def get_quarterly_cashflow(self):
        data = yf.Ticker(self.ticker).quarterly_cashflow
        return json.loads(data.to_json())

    # TODO: Data keys
    """
    list of date
    """

    def get_quarterly_cashflow_keys(self) -> list[str]:
        return list(self.get_quarterly_cashflow().keys())

    # TODO: labels cashflow
    """
        Free Cash Flow
        Repurchase Of Capital Stock
        Issuance Of Capital Stock
        Capital Expenditure
        Interest Paid Supplemental Data
        End Cash Position
        Beginning Cash Position
        Changes In Cash
        Financing Cash Flow
        Cash Flow From Continuing Financing Activities
        Net Other Financing Charges
        Proceeds From Stock Option Exercised
        Net Common Stock Issuance
        Common Stock Payments
        Common Stock Issuance
        Investing Cash Flow
        Cash Flow From Continuing Investing Activities
        Net Other Investing Changes
        Net Investment Purchase And Sale
        Sale Of Investment
        Purchase Of Investment
        Net Business Purchase And Sale
        Sale Of Business
        Purchase Of Business
        Net PPE Purchase And Sale
        Purchase Of PPE
        Operating Cash Flow
        Cash Flow From Continuing Operating Activities
        Change In Working Capital
        Change In Other Current Liabilities
        Change In Other Current Assets
        Change In Payables And Accrued Expense
        Change In Accrued Expense
        Change In Payable
        Change In Account Payable
        Change In Prepaid Assets
        Change In Inventory
        Change In Receivables
        Changes In Account Receivables
        Other Non Cash Items
        Stock Based Compensation
        Provision and Write Off of Assets
        Asset Impairment Charge
        Amortization Of Securities
        Deferred Tax
        Deferred Income Tax
        Depreciation Amortization Depletion
        Depreciation And Amortization
        Depreciation
        Operating Gains Losses
        Gain Loss On Investment Securities
        Gain Loss On Sale Of Business
        Net Income From Continuing Operations
    """

    def get_labels_of_cashflow_obj(self) -> list[str]:
        values = list(self.get_quarterly_cashflow().values())
        first = values[0]
        return list(first.keys())

    # TODO: values of label key
    def get_quarterly_cashflow__values_by_index_and_label(self, index, label):
        return list(self.get_quarterly_cashflow().values())[index][label]

    def __repr__(self):
        return "Ticker {}".format(self.ticker)