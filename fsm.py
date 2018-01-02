from transitions.extensions import GraphMachine

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )
    def on_enter_homeport(self, update):
        update.message.reply_text("Jawohl! Herr Kaleun.\n今天是個晴朗的一天，請：\n[查看] 船隻資訊\n或指示巡航區域：\n往 [大西洋] ？\n往美東參加 [擊鼓行動] ？\n [宅在基地] ？\n還有養在船上的貓好像躲起來了我一時找不到牠......")
        
    def is_going_to_convoy(self, update):
        text = update.message.text
        return text == "大西洋"
    
    def is_going_to_info(self, update):
        text = update.message.text
        return text == "查看"
    
    def on_enter_info(self, update):
        photo = open('photo/info.jpg', 'rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("這是一艘VIIC型潛艇。\n1940年下水，第七潛艇區艦隊所屬。\n潛航極限深度230公尺\n5門魚雷發射管\n兩座柴油引擎和兩座電力引擎\n船上共有40人，還有一隻貓叫奧托")
        self.go_back(update)
        
    def is_going_to_temp(self, update):
        text = update.message.text
        return text == "開始"

    def is_going_to_cargo(self, update):
        text = update.message.text
        return text == "擊鼓行動"

    def is_going_to_otaku(self, update):
        text = update.message.text
        return text == "宅在基地"
    
    def on_enter_temp(self, update):
        self.go_back(update)

    def on_enter_convoy(self, update):
        photo = open('photo/convoy.jpg', 'rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("報告！發現了一支規模不小的運輸船團，但是周遭有護航艦隻。\n請指示：\n[下潛] 到潛望鏡深度攻擊？\n[直接攻擊] ？")
        
    def on_enter_cargo(self, update):
        photo = open('photo/cargo.jpg', 'rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("報告！發現了幾艘落單的商船！\n請指示：\n[發射魚雷] ？\n開 [甲板砲] ？")

    def on_enter_otaku(self, update):
        update.message.reply_text("您這個宅宅艇長這樣不行，老鄧會生氣")
        photo = open('photo/thug.jpg', 'rb')
        update.message.reply_photo(photo)
        photo.close()
        self.go_back(update)

    def is_going_to_victory(self, update):
        text = update.message.text
        return text == "下潛"

    def is_going_to_destroyer(self, update):
        text = update.message.text
        return text == "直接攻擊"

    def on_enter_victory(self, update):
        photo = open('photo/topp.jpg', 'rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("Torpedo...Los!")
        photo = open('photo/victory.jpg', 'rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("擊沉了四艘商船！ [繼續] 待在水面下等到護航艦遠離比較安全。")

    def on_enter_destroyer(self, update):
        hoto = open('photo/topp.jpg', 'rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("Torpedo...Los!")
        photo = open('photo/victory.jpg', 'rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("擊沉了兩艘商船！")
        photo = open('photo/england.jpg', 'rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("噢...糟糕！一艘英國皇家海軍驅逐艦似乎發現我們了！\n（但是開船的流氓傢伙看起來很可疑）\n現在該怎麼行動？\n請指示：\n[緊急下潛] 並保持靜默？\n[全速逃離] ？")

    def is_going_to_underwater(self, update):
        text = update.message.text
        return text == "緊急下潛"

    def on_enter_underwater(self, update):
        update.message.reply_text("水下一片詭異的寧靜...我有種不好的預感\n現在是 [白天] 還是 [夜晚] 呢？")
    
    def is_going_to_sunk(self, update):
        text = update.message.text
        return text == "白天" or text == "往南"
    
    def on_enter_sunk(self, update):
        update.message.reply_text("遭到深水炸彈攻擊！船隻嚴重受損！......")
        update.message.reply_text("（您的U艇遭到擊沉，回港重生）")
        self.go_back(update)

    def is_going_to_kameraden(self, update):
        text = update.message.text
        return text == "全速逃離" or text == "上浮" or  text == "往北"

    def on_enter_kameraden(self, update):
        photo = open('photo/hello.jpg', 'rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("遇見了另一艘U艇！快向他們打招呼吧！\n例如 [嗨] [你好] 之類的，要說什麼都可以。\n離開的時候記得說 [再見] 就可以了。")

    def is_going_to_greet(self, update):
        text = update.message.text
        return text != "再見"
    
    def on_enter_greet(self, update):
        text = update.message.text
        update.message.reply_text(text)
        self.go_back(update)
        
    def is_going_to_outofo2(self, update):
        text = update.message.text
        return text == "夜晚" or text == "繼續"

    def on_enter_outofo2(self, update):
        update.message.reply_text("待在水下太久，氧氣和電池再繼續消耗可能會不夠用。\n請下指示 [上浮] 吧。")

    def is_going_to_outofdiesel(self, update):
        text = update.message.text
        update.message.reply_text(text)
        return text == "再見"

    def on_enter_outofdiesel(self, update):
        photo = open('photo/diesel_engine.jpg', 'rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("魚雷和柴油都用掉不少了。\n我們 [放置水雷] 後回港補給吧。")

    def is_going_to_lorient(self, update):
        text = update.message.text
        return text == "放置水雷"

    def on_enter_lorient(self, update):
        update.message.reply_text("成功完成這次巡航！\n恭喜您獲得了一枚勳章和法國妹子的鮮花！")
        photo = open('photo/lorient.jpg', 'rb')
        update.message.reply_photo(photo)
        photo.close()
        self.go_back(update)

    def is_going_to_banana(self, update):
        text = update.message.text
        return text == "發射魚雷" or text == "甲板砲"

    def on_enter_banana(self, update):
        photo = open('photo/victory.jpg', 'rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("您擊沉的商船滿載香蕉！\n快到海面上 [撈香蕉] 補充糧食！")

    def is_going_to_allbanana(self, update):
        text = update.message.text
        return text == "撈香蕉"
    
    def on_enter_allbanana(self, update):
        photo = open('photo/cat.jpg', 'rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("現在船上到處都掛著香蕉串，空間變得有點擁擠...\n到甲板上 [吃香蕉] 好了。\n...啊，原來貓貓奧托在這裡，果然看到食物就跑出來了，這傢伙")

    def is_going_to_aircraft(self, update):
        text = update.message.text
        return text == "吃香蕉"
    
    def on_enter_aircraft(self, update):
        photo = open('photo/swordfish.jpg', 'rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("報告！發現空中有偵察機的影子！\n要往哪裡躲呢，[往南] 還是 [往北] ？")
