from bs4 import BeautifulSoup
import re

html = """<p class=MsoNormal style='margin-top:2.4pt;margin-right:0mm;margin-bottom:2.4pt; margin-left:0mm;text-align:justify;line-height:150%'><b><span style='font-size: 14.0pt;mso-bidi-font-size:12.0pt;line-height:150%;font-family:"Times New Roman",serif; mso-fareast-language:RU'>ЕДВА&#769;</span></b><b style='mso-bidi-font-weight: normal'><span style='font-size:14.0pt;mso-bidi-font-size:12.0pt;line-height: 150%;font-family:"Times New Roman",serif;mso-fareast-language:RU'>,</span></b><span style='font-size:14.0pt;mso-bidi-font-size:12.0pt;line-height:150%;font-family: "Times New Roman",serif;mso-fareast-language:RU'> <i>нареч</i><span style='mso-bidi-font-style:italic'>.<i> и союз</i>.</span> <b>I.</b> <i>нареч</i><span style='mso-bidi-font-style:italic'>.</span> <b>1.</b> <i>Обозначает начало какого</i><span style='mso-bidi-font-style:italic'>-<i>л</i>.<i> действия</i>,<i> в знач</i>.:<i> только что</i>,<i> чуть только</i>.</span> От сих единых погр&#1123;шностей многия &lt;женщины&gt; часто лишаются плода, едва его зачавши. Зыб. 1775 11. Разуму вашему, едва шествие свое начинающему, сие бы было непонятно. Рдщв Пут. 181. <o:p></o:p></span></p> <p class=MsoNormal style='margin-top:2.4pt;margin-right:0mm;margin-bottom:2.4pt; margin-left:0mm;text-align:justify;line-height:150%'><b><span style='font-size: 14.0pt;mso-bidi-font-size:12.0pt;line-height:150%;font-family:"Times New Roman",serif; mso-fareast-language:RU'>2.</span></b><span style='font-size:14.0pt;mso-bidi-font-size: 12.0pt;line-height:150%;font-family:"Times New Roman",serif;mso-fareast-language: RU'> <i>Обозначает неполноту</i><span style='mso-bidi-font-style:italic'>,<i> слабую</i>,<i> малую степень проявления чего</i>-<i>л</i>.,<i> в знач</i>.:<i> чуть</i>,<i> слегка</i>,<i> совсем немного</i>.</span> Голос их едва слышен становится. Нклв Розана 35. Ростущий по Алтайскому хребту &lt;золотарник&gt; едва вышиною достигает пядени. Паллас ОР 184. Он принял меня холодно, <span style='letter-spacing:2.0pt'>..</span> и едва удостоил меня отв&#1123;та, когда я спрашивал об его здоровь&#1123;. МЖ IV 148. &#9674; <span style='letter-spacing: 2.0pt'>Едва чт</span>о. Прохладный ветерок едва что ощущался. Мур. Ст. 167. &#9674; <span style='letter-spacing:2.0pt'>Едв</span>а,<span style='letter-spacing: 2.0pt'> едв</span>а. Н&#1123;жная травка едва, едва колеблется. Муза IV 147. &#9674; <span style='letter-spacing:2.0pt'>Едва н</span>е. <i>Чуть не</i><span style='mso-bidi-font-style:italic'>,<i> почти</i>.</span> Бернгард град Бризакский <span style='letter-spacing:2.0pt'>..</span> от нестерпимаго глада едва&#769; не измерший, штурмом взял. Феатр. ист. 433. На пути взб&#1123;сившиися кони в озеро его завозят, в котором он едва не потонул. Арг. I 289. Едва не позабыл я объявить моим читателям о самой удивительн&#1123;йшей вещи. Распе 109. || <i>Всего навсего</i><span style='mso-bidi-font-style:italic'>,<i> самое большее</i>.</span> Было французов пятдесят тысящь челов&#1123;к, а наших едва&#769; двадцать пять тысящь на том бою в шанцах. Вед. I 50. Доходы шаха персидскаго <span style='letter-spacing:2.0pt'>..</span> едва до осми милионов достигают. Геогр. 1710 65. Електрическая сила появилась в нарочито сильных искрах; но едва пять минут продолжалась. Лом. СС I 317. || <i>Насилу</i><span style='mso-bidi-font-style:italic'>,<i> с трудом</i>;<i> еле</i>.</span> Рукод&#1123;лный ч&#1155;лвк едва&#769; свой хл&#1123;б во изобилии получити может. Зрилище 27. Ионес, который едва сам на ногах стоять мог, подал ей свою руку. Т. Ионес I 222. Я едва мог разобрать сию надпись. ПД I 127. Надругой день, едва я мог встать от побоев с пост&#1123;ли. Рдщв Пут. 383. &#9674; <span style='letter-spacing:2.0pt'>Едв</span>а,<span style='letter-spacing:2.0pt'> едв</span>а. Леандр едва едва печаль такую сносит. Майк. Игрок 7. Под тяжкой древностью трясясь и задыхаясь, Едва, едва идут. Дмтр. III 55. <o:p></o:p></span></p> <p class=MsoNormal style='margin-top:2.4pt;margin-right:0mm;margin-bottom:2.4pt; margin-left:0mm;text-align:justify;line-height:150%'><b><span style='font-size: 14.0pt;mso-bidi-font-size:12.0pt;line-height:150%;font-family:"Times New Roman",serif; mso-fareast-language:RU'>3.</span></b><span style='font-size:14.0pt;mso-bidi-font-size: 12.0pt;line-height:150%;font-family:"Times New Roman",serif;mso-fareast-language: RU'> <i>Обозначает сомнение в возможности</i><span style='mso-bidi-font-style: italic'>,<i> допустимости чего</i>-<i>л</i>.,<i> в знач</i>.:<i> вряд ли</i>.</span> Париж <span style='letter-spacing:2.0pt'>..</span> при р&#1123;к&#1123; сеин&#1123;, началнои город всего королевства, и в е&#1141;роп&#1123; подобныи оному едва обр&#1123;тается. Геогр. 1719 33. Едва были такие философы, которые бы действительно были такими, какими себя св&#1123;ту представили. Эмн Фемист. 89. Опасность пл&#1123;на едва оправдать может убийство, войною называмое. Рдщв Пут. 76. &#9674; <span style='letter-spacing:2.0pt'>Едва ли </span>(<span style='letter-spacing:2.0pt'>л</span>ь). Герц едваль им&#1123;ет нам&#1123;рение сие д&#1123;ло окончать. ЖПВ II 562. Сия бол&#1123;знь едва ли изл&#1123;чимая. Трут. 1769 216. Дрезден едва ли уступает Берлину в огромности домов. Крм. ПРП I 267. &#9674; <span style='letter-spacing:2.0pt'>Едва ли н</span>е. <i>Очень вероятно</i><span style='mso-bidi-font-style:italic'>,<i> пожалуй что</i>.</span> [Баланцов:] И то правда: да едва ли не хуже еще было. Лжец (Г) 66. <o:p></o:p></span></p> <p class=MsoNormal style='margin-top:2.4pt;margin-right:0mm;margin-bottom:2.4pt; margin-left:0mm;text-align:justify;line-height:150%'><b><span style='font-size: 14.0pt;mso-bidi-font-size:12.0pt;line-height:150%;font-family:"Times New Roman",serif; mso-fareast-language:RU'>II.</span></b><span style='font-size:14.0pt; mso-bidi-font-size:12.0pt;line-height:150%;font-family:"Times New Roman",serif; mso-fareast-language:RU'> <i>союз</i><span style='mso-bidi-font-style:italic'>.</span> <i>Употр</i><span style='mso-bidi-font-style:italic'>.<i> во временном придат</i>.<i> предл</i>.<i> для указания на непосредственно предшествующее действие</i>,<i> в знач</i>.:<i> как только</i>,<i> чуть только</i>,<i> только что</i>.</span> Едва же царевич &lt;Алексей&gt; о смертной казни услышал, то з&#1123;ло побл&#1123;днел и пошатался. Устр. 622. Едва она &lt;коза&gt; ушла, как Волк там появился. Трд. СП I 198. Едва сей бурный вихрь несчастьем укротился И Я в спокойствии к наукам обратился. Лом. ПВ 22. Едва младенец родится, как показывает он расположение к сосанию. Дом. леч. I 93. &#9674; <span style='letter-spacing:2.0pt'>Едва лиш</span>ь<span style='letter-spacing:2.0pt'>, едва тольк</span>о. И едва лишь оное всеприятное м&#1123;сто мы оставили, как едина жена <span style='letter-spacing:2.0pt'>..</span> нам попалась на дорог&#1123;. ЕОЛ 47. Но Душенька, в сию тревогу, Едва открыла только ногу, Как вдруг умолкла адска тварь. Богд. 148. <o:p></o:p></span></p>"""

roman_re = re.compile(r'^[IVXLCDM]+\.$')
arabic_re = re.compile(r'^\d+\.$')

soup = BeautifulSoup(html, "html.parser")

result = []
current_meaning = None
current_sub = None
add_tag_to_definition = False

for p in soup.find_all("p"):
    for elem in p.descendants:

        text = elem.get_text(" ", strip=True)

        if elem.name == "b" and roman_re.match(text):
            current_meaning = {
                "label": text,
                "definition": "",
                "submeanings": []
            }
            result.append(current_meaning)
            current_sub = None
            add_tag_to_definition = True
            continue

        if elem.name == "b" and arabic_re.match(text):
            if current_meaning is None:
                current_meaning = {
                    "label": None,
                    "definition": "",
                    "submeanings": []
                }
                result.append(current_meaning)

            current_sub = {
                "label": text,
                "definition": ""
            }
            current_meaning["submeanings"].append(current_sub)
            add_tag_to_definition = True
            continue

        if elem.name == "i" and add_tag_to_definition:
            if current_sub is not None:
                current_sub["definition"] += " " + text
            else:
                current_meaning["definition"] += " " + text

    add_tag_to_definition = False

print(result)