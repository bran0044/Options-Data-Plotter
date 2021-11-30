import pprint
import yfinance as yf
import matplotlib.pyplot as plt
import wallstreet as ws


# CALLS
callsimpv = []
callsbid = []
callsask = []
callschange = []

# PUTS
putsimpv = []
putsbid = []
putsask = []
putschange = []

# STRIKE PRICE
StrikeC = []
StrikeP = []

ticker = input('Choose a ticker: ').upper()
print(yf.Ticker(ticker).options)
expiry1 = input('Choose an expiry: ')
try:
    stock = yf.Ticker(ticker.upper())
    expiry = stock.option_chain(expiry1)
    Strike_priceC = expiry.calls['strike']
    Strike_priceP = expiry.puts['strike']

    # Calls
    calls_impliedv = expiry.calls['impliedVolatility']
    calls_bid = expiry.calls['bid']
    calls_ask = expiry.calls['ask']
    calls_change = expiry.calls['change']

    # Puts
    puts_impliedv = expiry.puts['impliedVolatility']
    puts_bid = expiry.puts['bid']
    puts_ask = expiry.puts['ask']
    puts_change = expiry.puts['change']

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    fig.suptitle('Options Data ' + ticker + ' $' + str(ws.Stock(ticker).price))

    # CALLS
    for x in range(len(calls_impliedv)):
        callsimpv.append(calls_impliedv[x])
        StrikeC.append(Strike_priceC[x])
        callsbid.append(calls_bid[x])
        callsask.append(calls_ask[x])
        callschange.append(calls_change[x])

    # PUTS
    for i in range(len(puts_impliedv)):
        putsimpv.append(puts_impliedv[i])
        StrikeP.append(Strike_priceP[i])
        putsbid.append(puts_bid[i])
        putsask.append(puts_ask[i])
        putschange.append(puts_change[i])

    # CALLS
    # Bid/Ask
    ax1.set_title('CALLS Bid/Ask')
    ax1.plot(StrikeC, callsbid)
    ax1.plot(StrikeC,callsask)
    ax1.legend(["Bid", "Ask"])

    ax3.set_title('CALLS Change%')
    ax3.plot(StrikeC, callschange)
    ax3.legend(["Change%"])

    # PUTS
    # Bid/Ask
    ax2.set_title('PUTS Bid/Ask')
    ax2.plot(StrikeP, putsbid)
    ax2.plot(StrikeP, putsask)
    ax2.legend(["Bid", "Ask"])

    ax4.set_title('PUTS Change%')
    ax4.plot(StrikeP, putschange)
    ax4.legend(["Change%"])

    # function to show the plot
    plt.show()
except Exception:
    print('Choose an valid ticker')