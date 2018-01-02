# TOC Project 2017
### 從海底出擊 @Das_U_Bot
![Das_U_Bot LOGO](https://i.imgur.com/X8bE7O3.jpg)

A telegram bot based on a finite state machine.  
進擊的U艇日常  
~~這不是個電影Das Boot(1981)的捏他作品，這只是個U艇控的私心推廣小遊戲。~~

## Windows
```
ngrok.exe http 5000
```
獲得URL後修改：
```python=11
API_TOKEN = 'YOUR_Telegram_API_TOKEN'
WEBHOOK_URL = 'https://YOUR_WEBHOOK_URL.ngrok.io/hook'
```

## Finite State Machine Graph
![](https://i.imgur.com/TnEpgF9.png)

## Usage
**What can this bot do?**
> (Lorient, 1941)  
Jawohl! Herr Kaleun.  
這是一艘VIC型U艇。  
接下來請按照 [ ] 內的文字下指令指揮這艘U艇。  
請在按下 [ **/start** ] 後 [ **開始** ] 今天的巡航吧!  

* homeport  
一開始的initial state，必須先輸入 **開始** bot才會啟動對話。  
之後只要按照指示輸入 [ ] 中的文字就可以在state之間轉換，無論成功或失敗，最後都會回歸到*homeport*。  
進入有情境的state都會接到bot傳過來的歷史照片（~~有些經過惡搞，如有雷同純屬巧合~~）  

> Jawohl! Herr Kaleun.  
今天是個晴朗的一天，請：  
[ **查看** ] 船隻資訊  
或指示巡航區域：  
往 [ **大西洋** ] ？  
往美東參加 [ **擊鼓行動** ] ？  
 [ **宅在基地** ] ？  
還有養在船上的貓好像躲起來了我一時找不到牠.....  

**查看**、**大西洋**、**擊鼓行動**和**宅在基地**是*homeport*分支出去的四個選項。  
* info  
在*homeport*選擇**查看**會出現船隻資訊  
> 這是一艘VIIC型潛艇。  
1940年下水，第七潛艇區艦隊所屬。  
潛航極限深度230公尺  
5門魚雷發射管  
兩座柴油引擎和兩座電力引擎  
船上共有40人，還有一隻貓叫奧托  

，再回到*homeport*  
* otaku  
在*homeport*選擇**宅在基地**會原地loop（~~但是會接到吐槽~~）  
* temp  
用來偵測**開始**  
---
* convoy  
在*homeport*選擇**大西洋**  
* cargo  
在*homeport*選擇**擊鼓行動**  

為遊戲的兩大主線，遇到商船，各有兩個攻擊方式的選項可以選擇。  
* victory  
在*convoy*（大西洋海域）成功擊沉船隻會到達這個state  
* destroyer  
在*convoy*選項中可能遭到驅逐艦追殺  
* underwater  
下潛時會到達這個state，可能會*sunk*或繼續進行遊戲  
* sunk  
遭到擊沉，回到*homeport*  
* kameraden  
在海上遇到另一艘U艇，說出**再見**才會離開*greet*這個loop  
* greet  
echo玩家輸入的文字  
* banana  
在*cargo*（美東海域）擊沉船隻會發現船上滿載香蕉（歷史梗）  
* aircraft  
空中有偵察機出現，一樣有兩個選項，可能會*sunk*或繼續進行遊戲  
* allbanana  
吃香蕉，並且發現遊戲一開始不見的貓  
* outofo2  
*underwater*的狀態下若安全沒有*sunk*會到這個state，會被要求上浮  
* outofdiesel  
最後兩條線都會會合到這個state，資源匱乏，回*lorient*港補給  
* lorient  
完成一輪遊戲，接到成功訊息並回到*homeport*  

## Author
<!--ASCIIART:U-BOOT/byYoshiyasu Ishi@greywolfKarl-->
```
                                                     _
                                                     ]|
                                                  | |||
                                          __\___\_|_+||===
                   ____________-----|_/]_|\__\++++|/=||   \----------------------------......_______ 
 _______.....-----/_________________()___|___|+---[]-||)____....____________..________/---..|-----__/
/=_|__|________====--=======================|=========================  |=|+========|=|___[+]=====||
     \|-|__|__-------------------------------------------------------------------- _|_|__|==|___[]=/
      |_|\==[]====[|]___\=|====================================================---/  ----|++|===_/
        \_[]/            \========================================================|======|----/
   __  __      ____              __                             __           __ __      __       __
  / / / /     / __ )____  ____  / /____    __      _____  _____/ /__      __/_//_/_____/ /______/ /
 / / / /_____/ __  / __ \/ __ \/ __/ _ \   | | /| / / _ \/ ___/ __/ | /| / / __ `/ ___/ __/ ___/ / 
/ /_/ /_____/ /_/ / /_/ / /_/ / /_/  __/   | |/ |/ /  __(__  ) /_ | |/ |/ / /_/ / /  / /_(__  )_/  
\____/     /_____/\____/\____/\__/\___/    |__/|__/\___/____/\__/ |__/|__/\__,_/_/   \__/____(_) 
```
* **Yoshiyasu Ishi**  Github-> [@greywolfKarl](https://github.com/greywolfKarl)  
* fb粉專連動企劃 **卡爾·鄧尼茨**  Facebook fanpage->[@DonitzAndHisUWolves](https://www.facebook.com/DonitzAndHisUWolves)  
