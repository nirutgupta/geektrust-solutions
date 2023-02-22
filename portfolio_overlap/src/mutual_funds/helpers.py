from src.models.mutual_fund import MutualFund

OVERLAP_NUMERATOR = 2
HUNDRED = 100


def stocks_overlap_between(mutual_fund_1: MutualFund, mutual_fund_2: MutualFund):
    return ((OVERLAP_NUMERATOR * common_stocks_between(mutual_fund_1, mutual_fund_2)) / (mutual_fund_1.no_of_stocks + mutual_fund_2.no_of_stocks)) * HUNDRED


def common_stocks_between(mutual_fund_1: MutualFund, mutual_fund_2: MutualFund):
    return len(set(mutual_fund_1.stocks).intersection(mutual_fund_2.stocks))
