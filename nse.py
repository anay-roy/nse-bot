
from nsetools import Nse

def sharename(x):
    
    q = Nse().get_quote(x) 
    mylist = list()
    mylist.append({'companyName': q['companyName']})
    mylist.append({'symbol': q['symbol']})
    mylist.append({'basePrice': q['basePrice']})
    mylist.append({'closePrice': q['closePrice']})
    mylist.append({'averagePrice': q['averagePrice']})
    mylist.append({'open': q['open']})
    mylist.append({'previousClose': q['previousClose']})
    mylist.append({'dayHigh': q['dayHigh']})
    mylist.append({'dayLow': q['dayLow']})
    mylist.append({'high52': q['high52']})
    mylist.append({'low52': q['low52']})
    mylist.append({'pricebandupper': q['pricebandupper']})
    mylist.append({'pricebandlower': q['pricebandlower']})
    mylist.append({'totalBuyQuantity': q['totalBuyQuantity']})
    mylist.append({'totalSellQuantity': q['totalSellQuantity']})
    mylist.append({'totalTradedVolume': q['totalTradedVolume']})
    mylist.append({'quantityTraded': q['quantityTraded']})
    mylist.append({'deliveryQuantity': q['deliveryQuantity']})
    mylist.append({'deliveryToTradedQuantity': q['deliveryToTradedQuantity']})

    return(mylist)


def final(x):
    myDict = {"companyName":"Company Name", "symbol":"Symbol", "basePrice":"previous close", "closePrice":"todays close", "averagePrice":"Average price", "open":"opening price", "previousClose":"previous closing", "dayHigh":"todays high", "dayLow":"todays low", "high52":"52 weeks high", "low52":"52 weeks low", "pricebandupper":"upper circuit", "pricebandlower":"lower circuit", "totalBuyQuantity":"total buy orders", "totalSellQuantity":"total sell orders", "totalTradedVolume":"traded volume", "quantityTraded":"traded quantity", "deliveryQuantity":"deliverable quantity", "deliveryToTradedQuantity":"delivery percentage"}
    columns = ["companyName", "symbol", "basePrice", \
        "closePrice", "averagePrice", "open", \
        "previousClose", "dayHigh", "dayLow", \
        "high52", "low52", "pricebandupper", \
        "pricebandlower", "totalBuyQuantity", "totalSellQuantity", \
        "totalTradedVolume", "quantityTraded", "deliveryQuantity", \
        "deliveryToTradedQuantity"]
    data = sharename(x)
    final = ""
    for first, second in zip(columns, data):
        final += f"{myDict[first]}: {second[first]}\n"
    return final




# from urllib.request import urlopen, Request
# from bs4 import BeautifulSoup
 
# Telegram bot configs




import logging, os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


 
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
 
logger = logging.getLogger(__name__)
 
def start(update, context):
    update.message.reply_text('Hi! \nThis bot can give you information about the share you want \nType /help for more details')
 
def help(update, context):
    update.message.reply_text('Commands\n\n/help - shows this menu\n/share share_name - for getting share details')
 
def share(update, context):
    user_says = " ".join(context.args)
    update.message.reply_text(final(user_says.lower()))
 
 
def command_not_found(update, context):
    update.message.reply_text('Command not found!\nCommands\n\n/help - shows this menu\n/share share_name - for getting details about particular share.')
 
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)
 
 
def main():
    updater = Updater("1368949563:AAHp5eGyzMKPkbBF0rnboJbHWCr-_QGrE3U", use_context=True)
    dp = updater.dispatcher
 
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("share", share))
 
    # If user types anything else
    dp.add_handler(MessageHandler(Filters.text, command_not_found))
 
    dp.add_error_handler(error)
 
    # Start the Bot
    updater.start_polling()
 
    updater.idle()
 
 
if __name__ == '__main__':
    main()