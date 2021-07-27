#!/usr/bin/env python
# -*- coding:utf-8 -*-

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import logging
import random

token = '機器人的token'

updater = Updater(token=token, use_context=True)

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start(update, context):
    message = '大家好!我是戴夫!最近因為投資失利，連肝、腎都輸掉了，因此只好去公園住紙箱。請各位大佬行行好，幫助我早日買回腎臟TAT \n\n' \
              '另外因為我輸得太慘，連我的拔拔都放生我，所以萬一發現我的行為不正常時請去求救蝦聊管理員，他們應該能幫我送醫院!'
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=fun('戴夫')[1])


dispatcher.add_handler(handler=CommandHandler('start', start))


def donate(update, context):
    name = str(update.effective_user['first_name']) + ' ' + str(update.effective_user['last_name'])
    context.bot.send_message(chat_id=update.effective_chat.id, text='謝謝' + name + '的救助!! \n'
                                                                                  '戴夫的捐款地址: \n'
                                                                                  'BCH: qp57zd7mfxpr0zc4q569avx5l390ssj2ygkl4futk8 \n\n'
                                                                                  'ETH(包含所有ERC20): 0x9aAe4a9171572c61d6541aF990267B99539E9F5b \n\n'
                                                                                  'XMR: 88GzwpA46cr8gmwbuobCsBbrfGaoHVU4wGKMNQ6g1b69haTLMYsWFuwFNFfmjEoqCHjY3JoQgjNPRLByDtXLLnxbHS9HzKm \n\n'
                                                                                  'IOTA: iota1qrwc0yr3cxkq8wd54kf2pdqffhtqjgxzt7x9lsggc9y4h70tazaxvmklvlc \n\n'
                                                                                  '問我為什麼沒有BTC地址?BTC我不想要，你留著吧!'
                                                                                  '我不想再增加破產的可能性了!'
                                                                                  '如果你真的很想捐，我可以勉為其難的用BCH地址收一下')


dispatcher.add_handler(handler=CommandHandler('donate', donate))


def endpull(update, context):
    message = '不好意思，因為我最近....被醫#^$%....醫生診斷出....阿米)(%@^&.....阿米巴原蟲正在啃蝕我.....)@#!_$%我的大腦，' \
              '導致%&$....導#^&%$#...導致我的智商....&$$@%%.....大幅降低。接下來應^($*^@*%...應該%#^&@%%.....%#*$^*(該會....' \
              '應該會有一段住院時間，謝....(#*^%)@(^....^(*#$%謝謝大家這段時間以來的照%#(^%(^!@$^^@&$#%)__+^@#$......'
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


dispatcher.add_handler(handler=CommandHandler('end', endpull))


def emergencyshutdown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='關閉')
    updater.stop()
    import sys
    sys.exit()


dispatcher.add_handler(handler=CommandHandler('emergencyshutdown', emergencyshutdown))


def newmember(update, context):
    context.bot.send_video(chat_id=update.effective_chat.id,
                           video='BAACAgUAAxkBAAIDy2D_iASFMaD1QB_nuVuE2kkNiUssAAIcCAACKiH4V-VpAvcNTlUyIAQ')


new_handler = MessageHandler(Filters.status_update.new_chat_members, newmember)
dispatcher.add_handler(new_handler)


def botreply(update, context):
    message = update.message.text
    if '/' == message[0]:
        retmessage = fun(message[1:len(message)])
        if retmessage[0] == 'p':
            photo = retmessage[1]
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo)
        elif retmessage[0] == 's':
            sticker = retmessage[1]
            context.bot.send_sticker(chat_id=update.effective_chat.id, sticker=sticker)
        elif retmessage[0] == 'm':
            context.bot.send_message(chat_id=update.effective_chat.id, text=retmessage[1])
    else:
        bakmg = findkeyword(message)
        if bakmg[0] == 'p':
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=bakmg[1])
        elif bakmg[0] == 's':
            context.bot.send_sticker(chat_id=update.effective_chat.id, sticker=bakmg[1])
        elif bakmg[0] == 'm':
            context.bot.send_message(chat_id=update.effective_chat.id, text=bakmg[1])
        elif bakmg[0] == 'v':
            context.bot.send_video(chat_id=update.effective_chat.id, video=bakmg[1])


reply_handler = MessageHandler(Filters.text & (~Filters.command), botreply)
dispatcher.add_handler(reply_handler)


def fun(message):
    rtmes = ['m', '']
    if message == '戴夫':
        rtmes[1] = '這是我的智商程度，請不要欺負我QAQ \n' \
                   '/戴夫        :顯示說明 \n' \
                   '/donate       :幫助戴夫離開公園 \n' \
                   '/肝、腎        :你的剩餘價值 \n' \
                   '/藍寶          :大佬的藍寶 \n' \
                   '/分           :分 \n' \
                   '晚安          :祝你一夜好眠 \n' \
                   '喵/描/苗/妙    :喵喵 \n' \
                   '好吃          :美味的便當 \n' \
                   '我全都要       :我全都要 \n' \
                   '女孩          :可愛的女孩子 \n' \
                   '開車           :快開 \n' \
                   '血流成河       :我要看到血流成河 \n' \
                   '管理員         :管理員上陣 \n' \
                   '好耶           :好耶 \n' \
                   '沒了           :啪 \n' \
                   '還錢           :抗議 \n\n' \
                   '另外還有一些彩蛋會在我高興時出現，我的智商可能會增加?'
    elif message == '肝':
        rtmes[1] = '肝:   157000 USD'
    elif message == '腎':
        rtmes[1] = '腎:   200000 USD'
    elif message == '心':
        rtmes[1] = '心:   500000 USD，但買入葉克膜，扣除8000000 USD'
    elif message == '肺':
        rtmes[1] = '肺:   250000 USD，但買入葉克膜，扣除8000000 USD'
    elif message == '胰臟' or message == '胰':
        rtmes[1] = '胰:   150000 USD'
    elif message == '大腸':
        rtmes[1] = '大腸:  50000 USD'
    elif message == '小腸':
        rtmes[1] = '小腸:  100000 USD'
    elif message == '睪丸':
        rtmes[1] = '你的睪丸沒有任何價值，請支付變性手續費10000 USD'
    elif message == '藍寶':
        rtmes = ['p', tgphoto(10)]
    elif '分' in message:
        num = int(random.random() * 10) % 2 + 13
        rtmes = ['s', tgsticker(4, num)]
    else:
        rtmes = ['no', '123']

    return rtmes


def findkeyword(message):
    if '喵' in message or '描' in message or '苗' in message or '妙' in message:
        num1 = int(random.random() * 100)
        num2 = int(random.random() * 22080)
        num1 = num1 % 20
        if num1 < 1:
            num2 = num2 % 48
            bak = tgsticker(3, num2)
        elif num1 > 0 and num1 < 6:
            num2 = num2 % 23
            bak = tgsticker(2, num2)
        else:
            num2 = num2 % 20
            bak = tgsticker(1, num2)
        return ['s', bak]
    elif '趴' in message or '啪' in message or '沒了' in message:
        return ['s', tgsticker(4, int(random.random() * 100) % 4)]
    elif '晚安' in message:
        num = int(random.random() * 110) % 11
        if num < 6:
            return ['p', tgphoto(num)]
        else:
            return ['v', tgvideo(num - 6)]
    elif '好吃' in message or '吃土' in message:
        return ['p', tgphoto(9)]
    elif '我全都要' in message or '選' in message:
        return ['p', tgphoto(7)]
    elif '女孩' in message:
        return ['p', tgphoto(6)]
    elif '開車' in message:
        if int(random.random() * 10) % 2 == 0:
            return ['v', tgvideo(6)]
        else:
            return ['s', tgsticker(4, 15)]
    elif '血流成河' in message:
        return ['v', tgvideo(5)]
    elif '管理員' in message or 'admin' in message:
        return ['v', tgvideo(7)]
    elif '好耶' in message or '好也' in message or '好野' in message or '好欸' in message:
        return ['s', tgsticker(4, 4)]
    elif '還錢' in message:
        return ['s', tgsticker(4, 5)]
    elif '怎麼辦' in message:
        num = int(random.random() * 30) % 3 + 6
        return ['s', tgsticker(4, num)]
    elif '死' in message or '上吊' in message:
        num = int(random.random() * 100) % 4 + 9
        return ['s', tgsticker(4, num)]
    elif '戴夫' in message:
        return ['m', '找我嗎?']
    elif '歡迎' in message:
        return ['m', '歡迎你']
    elif '幣' in message or 'BTC' in message or 'ETH' in message or 'SOL' in message or 'BCH' in message \
            or 'btc' in message or 'eth' in message or 'sol' in message or 'bch' in message:
        if '台幣' in message or '人民幣' in message or '新加坡幣' in message or '日幣' in message or '澳幣' in message or '紐幣' in message or '外幣' in message:
            return ['no', '123']
        else:
            return ['m', '逼－逼－!! \n 這裡不聊幣，你踩到版規惹!!請左轉蝦聊~~ \n t.me/shrimpchat']
    else:
        return ['no', '123']


def tgphoto(number):
    number = int(number)
    photos = [
        'AgACAgUAAxkBAAIB2mD-7G1cnBARUT6ObnrVJrYgoRsHAALKrTEbKiH4Vz8pg9-ziLMWAQADAgADcwADIAQ',  # 吃0
        'AgACAgUAAxkBAAIB22D-7G5z5jIf1M23NYpSlfz6b9_aAALLrTEbKiH4V8oYHbof3CRmAQADAgADcwADIAQ',
        'AgACAgUAAxkBAAIB3GD-7G5EBIfUK-YRNBOG9q-TcqHXAALMrTEbKiH4V7Ixccm-EFdGAQADAgADcwADIAQ',
        'AgACAgUAAxkBAAIB3WD-7G4I52_QqmV8aHSxnDhEZDG_AALNrTEbKiH4V-gSgDnjDcLdAQADAgADcwADIAQ',
        'AgACAgUAAxkBAAIB3mD-7G7_8ScuAAHtA_PDp-ghWPtI5QACzq0xGyoh-FegkhuURDUSzQEAAwIAA3MAAyAE',
        'AgACAgUAAxkBAAIB32D-7G5V2h_aTPJ2F5ejWW3dJzMfAALPrTEbKiH4V8JbzHgg8KMOAQADAgADcwADIAQ',
        'AgACAgUAAxkBAAIB5mD-7N3-NsSBdR79M1GsBjl1AuS-AALRrTEbKiH4Vz-t0_ZlSYVqAQADAgADcwADIAQ',  # 女孩6
        'AgACAgUAAxkBAAIB6GD-7TYHCTUpmpqlOsPjXM40zssAA9KtMRsqIfhXW4T9oNneluwBAAMCAANzAAMgBA',  # 我全都要7
        'AgACAgUAAxkBAAIB6mD-8u3-dv2m2SeXd7eoaYcZOez8AALWrTEbKiH4Vx6XtTWO-wTkAQADAgADcwADIAQ',  # 我好興奮8
        'AgACAgUAAxkBAAIB8WD_UxuYKEhgVpAVMtF_l0LbwFE7AALprTEbKiH4V0aDpHUrEVOUAQADAgADcwADIAQ',  # 石頭便當9
        'AgACAgUAAxkBAAIBnmD-4Ybk6TmB6Z_hb7Y5XK62Mo94AALArTEbKiH4V7NAZORH4vxMAQADAgADcwADIAQ'  # 藍寶10
    ]

    return photos[number]


def tgvideo(number):
    videos = [
        'BAACAgUAAxkBAAIDu2D_h0Fbd2uld-8cLXuh3MBPTygZAAIVCAACKiH4VyluFbFX3L8bIAQ',  # 吃0
        'BAACAgUAAxkBAAIDvGD_h0EkUWAanLk9sm7rVo0yVN9NAAIWCAACKiH4VwVVn5Pb1G1bIAQ',
        'BAACAgUAAxkBAAIDvWD_h0GTL1sYwXNe5kvFAb8GtNVoAAIXCAACKiH4V3XNVI3S4eM4IAQ',
        'BAACAgUAAxkBAAIDvmD_h0EtV45Up80UTkgCg1hCDPsLAAIYCAACKiH4VzCUtOJevDrIIAQ',
        'BAACAgUAAxkBAAIDv2D_h0HJTpkwFbp3gIsrAAH70I6vzwACFAgAAioh-FeRohWReqxpaCAE',
        'BAACAgUAAxkBAAIDxWD_h7IszyvdzalhBxeNbLDEf3jsAAIZCAACKiH4Vwn1yIs_0zzFIAQ',  # 血流成河5
        'BAACAgUAAxkBAAIDx2D_h8sFx9xc8Ij0mEpxXPOJWNtoAAIaCAACKiH4VxwUBmQC2LT2IAQ',  # 開車6
        'BAACAgUAAxkBAAIDyWD_h-b9SrnQX5g4F9fPXBiv2chsAAIbCAACKiH4Vx6MkIOHnpGMIAQ',  # 管理員7
        'BAACAgUAAxkBAAIDy2D_iASFMaD1QB_nuVuE2kkNiUssAAIcCAACKiH4V-VpAvcNTlUyIAQ'  # 新人8
    ]

    return videos[number]


def tgsticker(group, number):
    if group == 1:  # 白貓20
        group1 = [
            'CAACAgIAAxkBAAPFYP7QBLU7lm5P-KpULYPggWuhbrUAAnwSAALo1uISY-wfmJCkoKsgBA',
            'CAACAgIAAxkBAAPHYP7QEoqUJ83ciuHSEmklhwPdZI0AAn0SAALo1uISzlWUfxUvzgUgBA',
            'CAACAgIAAxkBAAPJYP7QE1ufvBIblGOMX8tmFTPcj3QAAn4SAALo1uISM8xBcSGmVi4gBA',
            'CAACAgIAAxkBAAPLYP7QFUpAZZN5GvZoITAo2re4LCMAAn8SAALo1uISTVrF7D21tekgBA',
            'CAACAgIAAxkBAAPNYP7QFmWK_HMsx_OjnCIM1RpPUn0AAoASAALo1uISaQVsddb-iJMgBA',
            'CAACAgIAAxkBAAPPYP7QGD5iMJ6Ohnl4G8fR7cqWmnQAAoESAALo1uISvKrKP2NtNqggBA',
            'CAACAgIAAxkBAAPRYP7QGudAu5QAAe6Vt2uxs5_8Yz9kAAKCEgAC6NbiEp9cPiQIPPzSIAQ',
            'CAACAgIAAxkBAAPTYP7QG_YrnNupt1LIIFiAklWVkX4AAoQSAALo1uISESUT24ZxDLIgBA',
            'CAACAgIAAxkBAAPVYP7QHIs3xd65FNMVWjVd1xjsiVAAAoUSAALo1uISjzxiqMn5TAQgBA',
            'CAACAgIAAxkBAAPXYP7QHifFs_-locwubDeAIJe4KWIAAoYSAALo1uISinef17QGVNAgBA',
            'CAACAgIAAxkBAAPZYP7QIvctHyPpscd3aEqWt-CxVCQAAocSAALo1uISYJhxoq600PggBA',
            'CAACAgIAAxkBAAPbYP7QIx2xswABVoKXThhKTLhv62bfAAKIEgAC6NbiEn2RxD_oel6BIAQ',
            'CAACAgIAAxkBAAPdYP7QJfC5eVI3v-PX5WYhlLK3RFYAAokSAALo1uIS_tG5MBOfel0gBA',
            'CAACAgIAAxkBAAPfYP7QJn24K_Af816RIiJXcBcxotgAAooSAALo1uISB9cKmgWWDVAgBA',
            'CAACAgIAAxkBAAPhYP7QKMSxZ7PcgnqxZSmyd1ebwX4AAosSAALo1uISidUZf1xG1eAgBA',
            'CAACAgIAAxkBAAPjYP7QKc5-0OhSt7PWZkBd4sbh87UAAowSAALo1uISLKOGot1RFzYgBA',
            'CAACAgIAAxkBAAPlYP7QK7Fsnnr2zVrlj3yv2208PHYAAo0SAALo1uISI4sa5suWWtEgBA',
            'CAACAgIAAxkBAAPnYP7QLFt3dx3vjfObQRxUo6W_QOgAAo4SAALo1uISCs3GH1R3sR8gBA',
            'CAACAgIAAxkBAAPpYP7QLeelOPDKoi9U4vNSsxiMoaEAAo8SAALo1uISd--yCFMOy_QgBA',
            'CAACAgIAAxkBAAPrYP7QL0nYQex08_WiBq-lU-e--ooAApASAALo1uISNtSI1Ffd-14gBA',
        ]
        return group1[number]
    elif group == 2:  # 真貓 23
        group2 = [
            'CAACAgEAAxkBAAIC12D_fNJmd78kn4BpvcURcHmYgNzIAAJtAQACyuanJNJ-4vCZt28KIAQ',
            'CAACAgEAAxkBAAIC2WD_fNS1NDpYKYyJHj5w8ffD22UaAAJsAQACyuanJLR2fcijF1hXIAQ',
            'CAACAgEAAxkBAAIC22D_fNlaH4v7vDwWk7j7A2pFCJc7AAJOAQACyuanJDxXBjbUhMsJIAQ',
            'CAACAgEAAxkBAAIC3WD_fNsi7H2ifEl0rE6Pk4INvPLDAAJNAQACyuanJGkSEg44VAe0IAQ',
            'CAACAgEAAxkBAAIC32D_fNzLkHGkFo-wZtIRqi-mlQ85AAJMAQACyuanJOrNeg0hoMzMIAQ',
            'CAACAgEAAxkBAAIC4WD_fN02QTnQkfCe9RFT_Rwipt2XAAJLAQACyuanJCozx3hbXTDcIAQ',
            'CAACAgEAAxkBAAIC42D_fN83ge061fHEDcp08wddjSgXAAJKAQACyuanJOFERj7mu5rBIAQ',
            'CAACAgEAAxkBAAIC5WD_fOC53TgYRtD9gQN47ofHfp9CAAJFAQACyuanJJDdlwX9tdVAIAQ',
            'CAACAgEAAxkBAAIC52D_fOKtl5n66SIUunhgyl_Wy0lMAAJEAQACyuanJKhmvnDcFAK3IAQ',
            'CAACAgEAAxkBAAIC6WD_fOMm8rcccRNa0s6clEDTPmjvAAJCAQACyuanJGW3yu82i1CEIAQ',
            'CAACAgEAAxkBAAIC62D_fOR0ksVKb3povR1VkCIhHuGqAAJAAQACyuanJJL_nMnZtqKXIAQ',
            'CAACAgEAAxkBAAIC7WD_fObkVxF9ydVZFsmQ72SaX9_AAAI8AQACyuanJNJPh9sE-8AJIAQ',
            'CAACAgEAAxkBAAIC72D_fOjKo-Lree2Vnq62L7FmIhBNAAI7AQACyuanJOHZlpMCBu0jIAQ',
            'CAACAgEAAxkBAAIC8WD_fOmsLE70RD76Fp7zxoIywR-XAAI6AQACyuanJFQyf6fKNGugIAQ',
            'CAACAgEAAxkBAAIC82D_fOr6ruYmcearFEpER9z17NW6AAI5AQACyuanJI4ro-uj_WucIAQ',
            'CAACAgEAAxkBAAIC9WD_fOxm9wRxPkbywuO8h0DEo49tAAI4AQACyuanJMXN2M0YOJTyIAQ',
            'CAACAgEAAxkBAAIC92D_fO9hcTjBoh4l9gVKj7xo0518AAI2AQACyuanJBRACGgCmxaRIAQ',
            'CAACAgEAAxkBAAIC-WD_fPBgH7i1VL673dQJZ1ySFAVLAAI1AQACyuanJJICTP95nE9gIAQ',
            'CAACAgEAAxkBAAIC-2D_fPIpZDVpN3YsY7J5MnhGBEuKAAI3AQACyuanJLjm82dw0uV1IAQ',
            'CAACAgEAAxkBAAIC_WD_fPMEFpVb86GsC-LxOK53k3O6AAI0AQACyuanJAPR3li4jNcGIAQ',
            'CAACAgEAAxkBAAIC_2D_fPWAYuJYZ9jirHiMKPwkQGV8AAJmAQACyuanJNw0mgRdh6zuIAQ',
            'CAACAgEAAxkBAAIDAWD_fPbHY_bIrpBkEpGsv-NaA_63AAIwAQACyuanJFjPVVD3EFPMIAQ',
            'CAACAgEAAxkBAAIDA2D_fPhy2YqcEMqMIlWKhRDRv_pkAAKMAQACyuanJEjs2GheG2yGIAQ'
        ]
        return group2[number]
    elif group == 3:  # 甘城 48
        group3 = [
            'CAACAgEAAxkBAAIDEGD_fyUuiMdYenOvLxjBSQJm62UIAAIhAANp9dwpVwoRYaOxrUYgBA',
            'CAACAgEAAxkBAAIDEmD_fyczBrLG8WJl6bO3Q9jYLBENAAIiAANp9dwpxwABpPABUze4IAQ',
            'CAACAgEAAxkBAAIDFGD_fykOwcdMjE0LEhssW8vAXQzNAAIkAANp9dwpQcuOM8epa1kgBA',
            'CAACAgEAAxkBAAIDFmD_fzBiRdsTAulWyhyjTneCWYzQAAImAANp9dwp9rQzN_BADGYgBA',
            'CAACAgEAAxkBAAIDGGD_fzKx8qliG3S4eOCd1EloiqHgAAInAANp9dwp96zzCCB6TkYgBA',
            'CAACAgEAAxkBAAIDGmD_fzSpBedcYOB55lWJcDoS5KHdAAIpAANp9dwpQXX_Ki_0nBEgBA',
            'CAACAgEAAxkBAAIDHGD_fzU0kW7ybEBXfpUnM4T52pgXAAIqAANp9dwpPITZjoLq2nQgBA',
            'CAACAgEAAxkBAAIDHmD_fzeVaZ_bf4_TjeCOGHf4HZ66AAIrAANp9dwpzPuidCYtXkkgBA',
            'CAACAgEAAxkBAAIDIGD_fzmndGKhitMYqPF-h1wThaHiAAIsAANp9dwpPNI7JQXunb4gBA',
            'CAACAgUAAxkBAAIDImD_f0Whnfh4OwJnNe8MBjR5ut3UAAIlAQACHkGlCLavdyiKKtIMIAQ',
            'CAACAgUAAxkBAAIDJGD_f0ciKW4mYRVevrSFr-bfP3-HAAImAQACHkGlCJByhCf8EGy6IAQ',
            'CAACAgUAAxkBAAIDJmD_f0gLKZXl1v9MQJp3A7NuyLfnAAInAQACHkGlCBYP0qWKzJTCIAQ',
            'CAACAgUAAxkBAAIDKGD_f0lIjasz5tZRLpNE7oTbN96XAAIoAQACHkGlCOXErU7za5crIAQ',
            'CAACAgUAAxkBAAIDKmD_f0uxGAodraZPgEoCf3huMkz1AAIpAQACHkGlCHjI-K6Dpm6nIAQ',
            'CAACAgUAAxkBAAIDLGD_f0xPE-d796e-CJ9rmJ3M1jF5AAIqAQACHkGlCIJcbU5zRCpHIAQ',
            'CAACAgUAAxkBAAIDLmD_f035vw8gAAHmpqeEP7a4pcFzMwACKwEAAh5BpQgLpzcQLa5vAiAE',
            'CAACAgUAAxkBAAIDMGD_f05iC25zrH6K2N40Q2ghQwfuAAIsAQACHkGlCIhX5IWzMMbTIAQ',
            'CAACAgUAAxkBAAIDMmD_f1AnpGUEf3lfpMnBu8Cl7nzOAAItAQACHkGlCJ5XZgt02oXNIAQ',
            'CAACAgUAAxkBAAIDNGD_f1F80R89C-AHqkJS0FyiOT2qAAIuAQACHkGlCDoH1mWHDjjxIAQ',
            'CAACAgUAAxkBAAIDNmD_f1NYnbFn46TD7YA4YWnjp7CzAAIvAQACHkGlCE75Ako9v_g-IAQ',
            'CAACAgUAAxkBAAIDOGD_f1WWzfsPKuoLMTso9ZMeSgqyAAIwAQACHkGlCHqU0mcfcSSxIAQ',
            'CAACAgUAAxkBAAIDOmD_f201wcDPnsv567R7oG1Q_Rs7AAIWBQAC-MbFCjna2Q2DzBhrIAQ',
            'CAACAgUAAxkBAAIDPGD_f43GZXBSxefrTgZgbUzGesxeAAJDBwAC-MbFCua3B9T-hvIjIAQ',
            'CAACAgUAAxkBAAIDPmD_f5VbIrobXaMKPFqCu5GymeC1AAKYBgAC-MbFCjTHY0iDwxrjIAQ',
            'CAACAgUAAxkBAAIDQGD_f5gtRdvOqhOGnaX75hHS9l62AAJFBwAC-MbFCgflvSf_R7SMIAQ',
            'CAACAgUAAxkBAAIDQmD_f6Pl3h9_pc2EVtfuhFQNGj6RAAJiAQACHkGlCIzFVFu_XOfbIAQ',
            'CAACAgUAAxkBAAIDRGD_f6qSUOC9jpeH2tb1OdkYgQzFAAJjAQACHkGlCBZL7UDzkhNZIAQ',
            'CAACAgUAAxkBAAIDRmD_f60yvsCaW12ZJf_jLAACL2FsAAJnAQACHkGlCCql-h5stmIsIAQ',
            'CAACAgUAAxkBAAIDSGD_f7IeWSLTcGdJBrjIKhI33QABAgACbAEAAh5BpQj54C9vas5o-CAE',
            'CAACAgUAAxkBAAIDSmD_f7WXsoClau5n-T6qVpwAAVfQFQACcQEAAh5BpQhRSP3ROBlxoiAE',
            'CAACAgUAAxkBAAIDTGD_f7hJNoGBBN8AAQh3nbPbFrxsJAACcwEAAh5BpQhSkNHJKYzUPyAE',
            'CAACAgUAAxkBAAIDTmD_f7orb9oImMP07mvHgXsGMlXmAAJ1AQACHkGlCPf_uIbu9xfKIAQ',
            'CAACAgUAAxkBAAIDUGD_f7vcEuakbZGAYzNuhTxUN1QGAAJ2AQACHkGlCNTnMSHakF8nIAQ',
            'CAACAgUAAxkBAAIDUmD_f8gFThXfVBp1Z1QgGvnvrgkGAAL-AAMeQaUIsfkOq8mbBbsgBA',
            'CAACAgUAAxkBAAIDVGD_f8qoDR4KECo9dNZf9GEGx83OAAL_AAMeQaUIIYjMRKIkleggBA',
            'CAACAgUAAxkBAAIDVmD_f-AeDvnTQmtv6N1MQ8OaM6U0AALsBQAC-MbFCqghX89_6Hr7IAQ',
            'CAACAgUAAxkBAAIDWGD_f-K2rWlheOW6M2KWdZ2ukv7cAALtBQAC-MbFCoZ6Voz2yTOjIAQ',
            'CAACAgUAAxkBAAIDWmD_f-ZUwiOvz3tuBUFoXUYRZVM3AALwBQAC-MbFCthnm-5Vr5IDIAQ',
            'CAACAgUAAxkBAAIDXGD_f-k4WAYpd1uoF49mnTrCR_dbAALyBQAC-MbFCl9HzpOwtzyDIAQ',
            'CAACAgUAAxkBAAIDXmD_f-yxMSEfncL2rhSxuwhzBbfZAAL0BQAC-MbFCkFJAgEiX4dWIAQ',
            'CAACAgUAAxkBAAIDYGD_f-0zLVjPzSoVTOmMD8Up9WLpAAL1BQAC-MbFCuCElDGjJDgNIAQ',
            'CAACAgUAAxkBAAIDYmD_f_WCa_Bz4ftCg5DSWCz-GJPJAAL9BQAC-MbFCrF9KgsDRzS1IAQ',
            'CAACAgUAAxkBAAIDZGD_f_vvajUNlrjLF1QdI3X97JtwAAICBgAC-MbFCv4BjWK9NVkXIAQ',
            'CAACAgUAAxkBAAIDZmD_f_7x6WMj-bacbho8k4ms88VPAAIFBgAC-MbFCmyBz09WorDFIAQ',
            'CAACAgUAAxkBAAIDaGD_gAABZFTa_MZ2MVL-lRvqhYA6OQACCAYAAvjGxQomL5naSebI6yAE',
            'CAACAgUAAxkBAAIDamD_gAdksYGozOhx3WVcC7u5_NYaAAIFBgAC-MbFCmyBz09WorDFIAQ',
            'CAACAgUAAxkBAAIDbGD_gAhMVFECjAEuyHqAhmbPsw15AAIJBgAC-MbFCpi1cXwE1kJkIAQ',
            'CAACAgUAAxkBAAIDbmD_gAoVsSQVIJoT8rzTHoN2kGtwAAIDBgAC-MbFCgRMr-oAARNJKCAE'
        ]
        return group3[number]
    elif group == 4:  # 其他
        group4 = [
            'CAACAgUAAxkBAAIBhGD-23JvdK1X7fpYsf7YMfsrsp5eAAJfAgACHHmgVuRDXuqxTWz8IAQ',  # 啪0
            'CAACAgUAAxkBAAIBhmD-24NWT7PhkZayAy1_pZwOp_FKAAIyAwACONiZVofNveIWfB9-IAQ',
            'CAACAgUAAxkBAAIDdGD_hMzgkaUEFITunua6y0NfpH0OAAKQAgAC5yJxV64XmF_LdELkIAQ',
            'CAACAgUAAxkBAAIDdmD_hM5C7REF34Ku5Hw9nEHnrvCVAAKXAgACuNBxV7B7kFTQI2pIIAQ',
            'CAACAgUAAxkBAAIBiGD-3GcjNkDd_LZ9B5aeYXM5RSU4AAL0AQACbp3xVTZplz90SJyDIAQ',  # 好耶4
            'CAACAgUAAxkBAAIBimD-3G9ZLDppa9hc10gAAdxpf2JSIwACsgIAAkWdUFdztZYh9Px35iAE',  # 還錢5
            'CAACAgUAAxkBAAIBjGD-3OM2nhNe3vJw8ZGO7cUoO9cQAAJuAgAC9p8IV02bAYu74llSIAQ',  # 你自己決定6
            'CAACAgUAAxkBAAIBjmD-3PkGgiY3kYBW-4XaEFM0cR-oAAI6AgACjjw5VdRqxUAO1Rf6IAQ',
            'CAACAgUAAxkBAAIDeGD_hSWw--PfwgR71L78g2srvrqiAALpAQAC7yLQVf0LK0B-IoeRIAQ',
            'CAACAgUAAxkBAAIBkGD-3cQ8IyccxcQbI8fkTcnRmBXCAAKYAgACK6_AVY5fjFy8D097IAQ',  # 上吊9
            'CAACAgUAAxkBAAIBkmD-3cUXR_ZmxuHw8thReYMBN4vLAAKeAwACqDxJVobKlWuSVfHaIAQ',
            'CAACAgIAAxkBAAIBlGD-3zIbaKdQOAM9Y2opx_MIIQisAAL4AwACierlByp3dvbJG_twIAQ',
            'CAACAgQAAxkBAAIBlmD-3zy39buf2inxgu2pb_qO_LJ8AAKiAgACcxpEBQSHKIR_qqYKIAQ',
            'CAACAgUAAxkBAAICWmD_dZE7SFnMxogAAWHLQxn7MXIRqQACfAIAAqnoEVeROzLrlG1pySAE',  # 分13
            'CAACAgUAAxkBAAICXGD_dZqQU3k3ONaoVrqjGZgYIVzOAAI5AgACQr05VWop71iFmFTTIAQ',
            'CAACAgUAAxkBAAIDemD_hcgAAYmTClVQFpxLg-Jwgiq7bAACZgIAAi8_KVfzx0c7Nl1DISAE'  # 開車15

        ]
        return group4[number]
    else:
        print('貼圖錯誤')
        exit()


updater.start_polling()
