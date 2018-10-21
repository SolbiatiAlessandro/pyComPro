"""script to profile different solutions"""
import l370
import l370b
import l370c
import l370d
import l370e
import sys
import random
import string
import time

def generate_input(input_size):
    """generate a random input of input_size 
    proportional to 'input_size' (int) for l370"""
    words = ['balla', 'assdd']
    append_random(words, input_size)
    words.append('areae')
    append_random(words, input_size)
    words.append('lekbc')
    append_random(words, input_size)
    words.append('labyd')
    append_random(words, input_size)
    words.append('aecdz')
    return words

def append_random(words, input_size):
    """append random strings to words"""
    letters = string.letters[:26]
    for _ in xrange(input_size):
        new_string = ""
        for _ in xrange(5):
            new_string += (random.choice(letters))
        words.append(new_string)


custom_input = ["baffs","sloop","octad","brens","gammy","sones","perdy","myope","burbs","doeth","yirds","bolls","veils","pause","niton","kibbi","salal","redid","gaped","anise","derby","oinks","dormy","wagon","soupy","ephah","goody","foals","rusks","memos","pareo","levee","prosy","earls","gator","urged","welly","boils","wells","gecko","cline","gamps","shaft","jiver","eyers","packs","eased","adman","ackee","recce","defog","cadis","jives","germy","umbos","gypsy","miler","swive","clubs","plots","fille","dodos","sylph","indol","lodes","chore","flute","tauts","chams","poilu","folds","jimpy","yodhs","swang","thymi","spite","equal","wrack","roses","degas","etyma","yecch","phyle","ducks","scape","tepas","flams","nidal","sells","geest","talus","bilgy","weets","dorps","wolfs","bilks","spurn","rinse","serfs","iodid","hying","boast","leben","fussy","stour","eches","bored","cones","tiled","forms","purda","pants","whops","udder","coles","apeak","nippy","skimp","jolty","ilium","ordos","shews","title","grate","kibes","pryer","bleep","utile","orles","lamia","selva","meant","frump","gaurs","defat","ormer","cramp","cured","sloyd","bates","bowed","samek","knave","jupon","exons","plica","uncus","murrs","sowed","fishy","halid","nisus","fives","spays","quoth","rants","justs","sewed","orzos","click","kings","repay","grope","bring","teach","expos","supra","dight","lines","shred","chide","biked","fugue","manna","bruin","mouch","syces","sophs","retax","alary","litai","unrig","dwell","jells","thuja","ovals","snare","snide","abate","femme","numbs","fount","undid","pyxes","warms","fines","ansae","fards","nabis","garni","false","naric","hales","tores","kilty","rewon","grail","synth","vowel","sagas","progs","snags","genii","swath","pross","exine","jaups","desex","acmes","pilei","treed","genic","weeks","hosed","chela","suave","duple","anger","cohos","dahls","essay","grans","tarty","vines","shoal","north","hertz","pecks","fairs","hylas","ochry","parge","witan","shawm","nylon","plier","kolas","umiaq","zoeal","apple","abaca","miked","meths","karma","yummy","thorn","tuyer","nappe","duels","shame","rowdy","plush","toyos","batts","emirs","braxy","quilt","voles","ileus","husks","kinos","vying","segue","toker","wynds","scaly","tardy","preed","wonts","prune","ikons","asset","evoke","rosin","omasa","fados","jehad","vises","roues","laris","snack","bhuts","edify","cloys","newts","sonic","teams","kempt","peeve","biffs","cisco","begot","knout","pesos","soldi","appal","unwon","axles","shins","decay","betta","hence","gowan","froes","usury","early","sugar","sotol","boggy","roads","exult","cheap","shivs","stiff","whigs","ousel","livre","flush","jaunt","clued","venue","green","promo","gybes","vimen","amici","dumky","kalpa","oboli","chafe","parch","shrub","raped","magus","cozey","braze","ikats","skats","jupes","irate","gibed","pecky","evict","synod","plums","puffs","drupe","rumor","scrip","sappy","yells","shiel","beaux","apses","damps","lamed","gally","wines","skids","laked","blimp","spoil","beech","plage","mothy","bally","gager","flora","latke","secco","salve","peony","overt","tofus","yogic","finer","kinin","rakis","tunas","lolly","trash","boart","fordo","longs","lacer","momus","moory","picul","ament","cocci","taper","luged","scuff","azure","gaffe","tubby","opsin","twits","veldt","forgo","lotah","banes","murid","venin","sooty","bhang","allow","scour","lours","chubs","ureal","basts","argot","rehem","ichor","kerne","shear","copse","bathe","perky","onion","stade","bises","dopes","dexie","peens","letch","gamer","passe","sudds","prahu","yerks","hippy","oxeye","rills","gulpy","dulse","hokey","tammy","paler","cutin","kafir","tarps","zowie","eruct","upbow","armed","viced","rosed","strap","shuls","harps","whizz","epics","manos","elver","kefir","noter","bowls","kicks","pewee","fugus","hiker","vexil","tides","manes","crepy","relay","acres","snobs","kecks","vogie","dowel","theft","doozy","daffy","joked","pecan","zineb","chias","grain","point","spate","shalt","rayed","kolos","jurat","mooed","grows","scuba","skees","exams","tutti","aliya","wiles","pilot","netty","nabes","berme","poind","zones","coyed","abaci","panty","moved","peise","sughs","llano","volte","peppy","shies","mixed","whale","whity","bandy","layup","nodus","vigas","fifes","oared","daddy","waspy","dales","crony","pikes","reifs","kaiak","coted","hyper","monks","bravi","diner","slung","rishi","bawdy","steps","cusks","wiver","trips","slink","ambit","genie","dikes","faker","quags","savin","amids","desks","spook","gonof","whisk","hotel","brags","carny","queer","poler","pawns","toner","nowts","truce","pekes","reeds","baals","ouzel","dairy","hoers","sepal","butle","petit","mucky","liege","rajah","cades","bogie","esses","juicy","kelly","bogus","silly","dotes","direr","tucks","aglee","miffy","freak","dildo","maids","words","cakes","ocker","lurid","tophs","event","drams","leash","clags","plank","butts","ruffe","sends","actor","dials","mesas","caput","yearn","suite","yucca","naevi","swots","namer","sojas","along","crams","eyrie","brins","comer","blocs","spade","hexad","steel","moony","nyala","lathe","grego","titty","gleys","melic","aunty","sural","shool","avers","rides","getup","barbe","bluey","saute","globs","foods","amiga","triol","qaids","deign","leone","gawks","heigh","dexes","shits","lodge","dives","obits","ileum","whets","power","duked","helix","yogas","skeps","sluff","bleak","chess","spend","force","haver","snubs","punts","reuse","debye","cubit","buret","pepla","ziram","route","pined","still","spica","alifs","gazoo","balsa","papal","twier","didos","carns","gulls","bakes","brows","gulch","cadgy","jakes","ethic","tuffs","alley","ossia","faery","glial","tawny","carpi","smaze","champ","gated","quest","dines","middy","guilt","vitta","sicko","kaury","yills","soled","flics","tache","avgas","sages","belay","arils","erect","omits","mopes","weedy","spode","glove","stack","omens","years","roven","tythe","zloty","chirr","keeps","ridgy","mover","range","sutta","eight","misdo","issue","bebop","juked","turbo","tough","emits","prude","hogan","infer","quash","reefy","toros","annul","muser","turds","flans","clomp","fails","equip","oasis","covey","iodic","tense","chimp","whaup","lores","spake","sasin","those","lough","lacey","skegs","heist","loved","times","sulks","beige","potto","zerks","dryer","towed","dined","cerci","flung","fluke","elemi","schmo","phons","dropt","bales","argle","carom","whort","gloze","hymns","twirl","amiss","atmas","cates","pukes","craps","sirup","balks","domes","retag","dorky","septa","spiks","shads","gemma","beets","inlet","ropes","aroma","chits","thuds","peels","fogie","stela","mythy","drier","thrip","burst","salad","rainy","bilge","woful","prick","props","stock","ofays","hosel","areic","clang","sexes","pyxie","haled","nawab","boche","fanos","aurum","tours","funky","dynes","raias","hexyl","welch","shyly","hemic","shade","netts","fiefs","topis","muton","nicol","updos","jubes","blite","xebec","swear","moult","pagod","cecum","rewet","nopal","holds","ruana","meany","juice","cobbs","mated","helms","dared","muley","bails","tench","blimy","tepoy","duroc","helps","quasi","stake","galas","mizen","spics","scudi","stook","pleas","hooly","gowks","hocks","hooey","octan","modal","minny","gaudy","neats","calfs","troop","amaze","zebra","jemmy","berms","shent","spasm","batty","menad","porks","jests","miaou","busty","buran","endow","juror","arias","stall","carry","tarre","colog","grout","ixias","alecs","resee","jowly","lochs","nines","yangs","byssi","sixty","gyros","tools","every","penes","dinks","storm","arles","chiro","waler","masts","gluts","siver","antre","treat","flair","lurks","overs","ratal","audit","tipis","vroom","spank","moors","paves","vinos","ghost","opine","toras","cauld","mokes","antsy","liman","outer","mufti","gores","baled","urine","minds","sorbs","hefty","cozen","musky","booed","wrier","jibes","reify","block","rebus","atoms","risus","zetas","dauby","rayas","razee","sagos","roset","yarer","fetes","award","filth","credo","gutsy","inter","yards","obeah","waist","oyers"]

if __name__ == "__main__":
    input_size = int(sys.argv[1])
    generated_input = generate_input(input_size)
    print len(generated_input)
    
    solution1 = l370.Solution()
    solution2 = l370b.Solution()
    solution3 = l370c.Solution()
    solution4 = l370d.Solution()
    solution5 = l370e.Solution()

    print "solution1"
    start = time.time()
    res1 = solution1.wordSquares(generated_input)
    end = time.time()
    print end-start
    
    print "solution2"
    start = time.time()
    res2 = solution2.wordSquares(generated_input)
    end = time.time()
    print end-start

    print "solution3"
    start = time.time()
    res3 = solution3.wordSquares(generated_input)
    end = time.time()
    print end-start

    print "solution4"
    start = time.time()
    res4 = solution4.wordSquares(generated_input)
    end = time.time()
    print end-start

    print "solution5"
    start = time.time()
    res5 = solution5.wordSquares(generated_input)
    end = time.time()
    print end-start

    print ""
    print ""
    print res1
    print res2
    print res3
    print res4
    print ""
    print ""

    print "solution5"
    start = time.time()
    res5 = solution5.wordSquares(custom_input)
    end = time.time()
    print end-start

    print "solution4"
    start = time.time()
    res4 = solution4.wordSquares(custom_input)
    end = time.time()
    print end-start

    print "solution3"
    start = time.time()
    res3 = solution3.wordSquares(custom_input)
    end = time.time()
    print end-start

    print "solution2"
    start = time.time()
    res2 = solution2.wordSquares(custom_input)
    end = time.time()
    print end-start

    print "solution1"
    start = time.time()
    res1 = solution1.wordSquares(custom_input)
    end = time.time()
    print end-start
