import telepot
import time
import urllib3
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton


# You can leave this bit out if you're using a paid PythonAnywhere account
proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))
# end of the stuff that's only needed for free accounts

bot = telepot.Bot('')

def handle(raw_msg):
    content_type, chat_type, chat_id = telepot.glance(raw_msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        message = raw_msg["text"]

        if message == '/start':
            bot.sendMessage(chat_id, start_message)
            on_chat_message(chat_id)

def on_chat_message(chat_id):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Area', callback_data='Area')],
                   [InlineKeyboardButton(text='Perimeter', callback_data='Perimeter')],
                   [InlineKeyboardButton(text='Volume', callback_data='Volume')],
                   [InlineKeyboardButton(text='Surface Area', callback_data='Surface Area')],
                   [InlineKeyboardButton(text='Consumer Math', callback_data='Consumer Math')],
                   [InlineKeyboardButton(text='Percent', callback_data='Percent')]

               ])

    bot.sendMessage(chat_id, 'Please pick one of the following.', reply_markup=keyboard)

def on_callback_query(raw_msg):
    query_id, from_id, query_data = telepot.glance(raw_msg, flavor='callback_query')
    #print('Callback Query:', query_id, from_id, query_data)

    bot.answerCallbackQuery(query_id, text='Processing...')
    if query_data == 'Area':
       bot.sendMessage(from_id, "YOU HAVE CHOSEN AREA" + "\n" + area_formulae)
    elif query_data == 'Perimeter':
       bot.sendMessage(from_id, "YOU HAVE CHOSEN PERIMETER" + "\n" + perimeter_formulae)
    elif query_data == 'Volume':
       bot.sendMessage(from_id, "YOU HAVE CHOSEN VOLUME" + "\n" +volume_formulae)
    elif query_data == 'Surface Area':
       bot.sendMessage(from_id, "YOU HAVE CHOSEN SURFACE AREA" + "\n" + surfacearea_formulae)
    elif query_data == 'Consumer Math':
       bot.sendMessage(from_id, "YOU HAVE CHOSEN CONSUMER MATH" + "\n" + consumermath_formulae)
    elif query_data == 'Percent':
       bot.sendMessage(from_id, "YOU HAVE CHOSEN PERCENT" + "\n" + percent_formulae)


start_message = "Hello, this is FormulaBot! How may I help you?"

area_formulae = "Area of a square: s × s \ns: length of one side \n\nArea of a rectangle: l × w \nl: length \nw: width \n\nArea of a triangle: (b × h)/2 \nb: length of base\nh: length of height \n\nArea of a trapezoid: (b1 + b2) × h/2 \nb1 and b2: parallel sides or the bases \nh: length of height"

volume_formulae= "Volume of a cube: s × s × s \ns: length of one side \n\nVolume of a box: l × w × h \nl: length \nw: width \nh: height \n\nVolume of a sphere: (4/3) × pi × r3 \npi: 3.14 \nr: radius of sphere \n\nVolume of a triangular prism: area of triangle × Height = (1/2 base × height) × Height \nbase: length of the base of the triangle \nheight: height of the triangle \nHeight: height of the triangular prism \n\nVolume of a cylinder:pi × r2 × Height \npi: 3.14 \nr: radius of the circle of the base \nHeight: height of the cylinder"

perimeter_formulae= "Perimeter of a square: s + s + s + s \ns:length of one side \n\nPerimeter of a rectangle: l + w + l + w\nl: length \nw: width \n\nPerimeter of a triangle: a + b + c \na, b, and c: lengths of the 3 sides"

surfacearea_formulae="Surface Area of a cube: \n6 × a2 \na is the length of one side \n\nSurface Area of a Right circular cylinder:\n2 × pi × r2   +  2 × pi × r × h \npi = 3.14 \nh is the height \nr is the radius \n\nSurface Area of a Rectangular Prism: \n2 × l × w  +  2 × l × h  +  2 × w × h \nl is the length \nw is the width \nh is the height \n\nSurface Area of a Sphere: \n4 × pi × r2 \npi = 3.14 \nr is the radius \n\nSurface Area of a Right circular cone: \npi × r2  +  pi × r ×( √(h2 + r2)) \npi = 3.14 \nr is the radius \nh is the height \nl is the slant height \n\nSurface Area of a Right square pyramid: \ns2 + 2 × s × l \ns is the length of the base \nh is the height \nl is the slant height"






consumermath_formulae= " Discount = list price × discount rate \n\nSale price = list price − discount \n\nDiscount rate = discount ÷ list price \n\nSales tax = price of item × tax rate \n\nInterest = principal × rate of interest × time \n\nTips = cost of meals × tip rate \n\nCommission = cost of service × commission rate"

percent_formulae= "Percent to fraction: x% = x/100 \n\nPercentage formula: Rate/100 = Percentage/base \nRate: The percent. \nBase: The amount you are taking the percent of.\nPercentage: The answer obtained by multiplying the base by the rate"

bot.message_loop({'chat': handle, 'callback_query': on_callback_query})
#bot.message_loop(handle)

print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
	
