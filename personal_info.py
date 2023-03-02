import ccxt
import time

#---코인 매수 매도 비율 변수
symbol0 ="(종목, ex) DOGE/USDT)" # symbol0=코인
standard = float(input('기준폭: '))  # 기준 구간
profit_position = float(input('매도폭: ')) # 매도폭
throw_position=float(input('1,2,3 구간 통과 폭: ')) #  1,2,3 번째 구간 비율
leverage1 =int(input('레버리지 입력: '))
input_rate= int(input('진입비율 입력: '))
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #기본 정보 셋팅
binance = ccxt.binance(config={
    'apiKey': '(본인 API)',
    'secret': '(개인키)',
    'enableRateLimit': True, 
    'options': {
        'defaultType': 'future'
    }
})
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#시장 정보 가져오기
markets = binance.load_markets()
symbol = symbol0
market = binance.market(symbol)
#레버리지 정보
binance.fapiPrivate_post_leverage({
    'symbol': market['id'],
    'leverage': leverage1
})
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

#지갑 잔고 불러오기
def My_wallet():
    time.sleep(1)
    balance_wallet = binance.fetch_balance()
    return float(balance_wallet['total']['USDT'])

#사용 잔고 불러오기
def My_wallet_used():
    time.sleep(1)
    balance_wallet = binance.fetch_balance()
    return float(balance_wallet['used']['USDT'])