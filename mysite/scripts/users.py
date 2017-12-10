# from  django.contrib.auth.models import User
from  django.contrib.auth import get_user_model
User = get_user_model()
def run():
    # # Get all users
    # # users = User.objects.all()
    # # user = users[1]
    # # user.set_password('dily1234')
    global User
    user0 = User.objects.create_user(
        username = 'xiexin2011@gmail.com',
        email = 'xiexin2011@gmail.com',
        is_superuser = 0,
        first_name = 'XIE',
        last_name = 'XIN',
        is_active = 1,
        password = '1TJT599QE2' )

    user1 = User.objects.create_user(
        username = 'huangran1991@yahoo.com',
        email = 'huangran1991@yahoo.com',
        is_superuser = 0,
        first_name = 'HUANG',
        last_name = 'RAN',
        is_active = 1,
        password = 'CV3MVFY68O' )

    user2 = User.objects.create_user(
        username = 'gohengchye1992@msn.com',
        email = 'gohengchye1992@msn.com',
        is_superuser = 0,
        first_name = 'GOH',
        last_name = 'ENG CHYE',
        is_active = 1,
        password = 'USRVX0A2M7' )

    user3 = User.objects.create_user(
        username = 'gohhuiying1989@gmail.com',
        email = 'gohhuiying1989@gmail.com',
        is_superuser = 0,
        first_name = 'GOH',
        last_name = 'HUI YING',
        is_active = 1,
        password = 'FWTNTZ79NI' )

    user4 = User.objects.create_user(
        username = 'fanghan2011@hotmail.com',
        email = 'fanghan2011@hotmail.com',
        is_superuser = 0,
        first_name = 'FANG',
        last_name = 'HAN',
        is_active = 1,
        password = 'DFHQJYXGBF' )

    user5 = User.objects.create_user(
        username = 'dingkuanchong2010@msn.com',
        email = 'dingkuanchong2010@msn.com',
        is_superuser = 0,
        first_name = 'DING',
        last_name = 'KUAN CHONG',
        is_active = 1,
        password = 'J9GL6SHTK9' )

    user6 = User.objects.create_user(
        username = 'tayweiguo1989@msn.com',
        email = 'tayweiguo1989@msn.com',
        is_superuser = 0,
        first_name = 'TAY',
        last_name = 'WEI GUO',
        is_active = 1,
        password = '6B2LA7YXLE' )

    user7 = User.objects.create_user(
        username = 'ongkahhong1991@gmail.com',
        email = 'ongkahhong1991@gmail.com',
        is_superuser = 0,
        first_name = 'ONG',
        last_name = 'KAH HONG',
        is_active = 1,
        password = '0WGOM6AOBF' )

    user8 = User.objects.create_user(
        username = 'pengjiayuan2011@hotmail.com',
        email = 'pengjiayuan2011@hotmail.com',
        is_superuser = 0,
        first_name = 'PENG',
        last_name = 'JIAYUAN',
        is_active = 1,
        password = 'WSZE68YG1F' )

    user9 = User.objects.create_user(
        username = 'huangzhanpeng1992@msn.com',
        email = 'huangzhanpeng1992@msn.com',
        is_superuser = 0,
        first_name = 'HUANG',
        last_name = 'ZHANPENG',
        is_active = 1,
        password = 'LJ9II5LYLR' )

    user10 = User.objects.create_user(
        username = 'ngoogekping1990@hotmail.com',
        email = 'ngoogekping1990@hotmail.com',
        is_superuser = 0,
        first_name = 'NGOO',
        last_name = 'GEK PING',
        is_active = 1,
        password = 'A3M218KZU2' )

    user11 = User.objects.create_user(
        username = 'geyuwei1992@hotmail.com',
        email = 'geyuwei1992@hotmail.com',
        is_superuser = 0,
        first_name = 'GE',
        last_name = 'YUWEI',
        is_active = 1,
        password = 'OTSW1M6XC0' )

    user12 = User.objects.create_user(
        username = 'zhengzhemin1991@yahoo.com',
        email = 'zhengzhemin1991@yahoo.com',
        is_superuser = 0,
        first_name = 'ZHENG',
        last_name = 'ZHEMIN',
        is_active = 1,
        password = 'RRVRSIB9JD' )

    user13 = User.objects.create_user(
        username = 'liuzhanpeng2011@msn.com',
        email = 'liuzhanpeng2011@msn.com',
        is_superuser = 0,
        first_name = 'LIU',
        last_name = 'ZHANPENG',
        is_active = 1,
        password = 'TS4KRHNH0X' )

    user14 = User.objects.create_user(
        username = 'huangwenxin2010@msn.com',
        email = 'huangwenxin2010@msn.com',
        is_superuser = 0,
        first_name = 'HUANG',
        last_name = 'WENXIN',
        is_active = 1,
        password = '4GT46RXG9T' )

    user15 = User.objects.create_user(
        username = 'choyweixiang2011@gmail.com',
        email = 'choyweixiang2011@gmail.com',
        is_superuser = 0,
        first_name = 'CHOY',
        last_name = 'WEI XIANG',
        is_active = 1,
        password = '00MLK7ZHDU' )

    user16 = User.objects.create_user(
        username = 'wangna1990@yahoo.com',
        email = 'wangna1990@yahoo.com',
        is_superuser = 0,
        first_name = 'WANG',
        last_name = 'NA',
        is_active = 1,
        password = '61LBQNVOJM' )

    user17 = User.objects.create_user(
        username = 'zhouhuichan1990@msn.com',
        email = 'zhouhuichan1990@msn.com',
        is_superuser = 0,
        first_name = 'ZHOU',
        last_name = 'HUICHAN',
        is_active = 1,
        password = 'A2SNIMH15U' )

    user18 = User.objects.create_user(
        username = 'nganhquang1991@yahoo.com',
        email = 'nganhquang1991@yahoo.com',
        is_superuser = 0,
        first_name = 'NG',
        last_name = 'ANH QUANG',
        is_active = 1,
        password = '5Q4JYG2TXH' )

    user19 = User.objects.create_user(
        username = 'huangqi1990@msn.com',
        email = 'huangqi1990@msn.com',
        is_superuser = 0,
        first_name = 'HUANG',
        last_name = 'QI',
        is_active = 1,
        password = 'IM1CNEV20N' )

    user20 = User.objects.create_user(
        username = 'dinggekping1991@msn.com',
        email = 'dinggekping1991@msn.com',
        is_superuser = 0,
        first_name = 'DING',
        last_name = 'GEK PING',
        is_active = 1,
        password = 'ID5H4HD5AT' )

    user21 = User.objects.create_user(
        username = 'pohhuiling1992@hotmail.com',
        email = 'pohhuiling1992@hotmail.com',
        is_superuser = 0,
        first_name = 'POH',
        last_name = 'HUI LING',
        is_active = 1,
        password = 'DNDN02L107' )

    user22 = User.objects.create_user(
        username = 'ngqiyang1989@msn.com',
        email = 'ngqiyang1989@msn.com',
        is_superuser = 0,
        first_name = 'NG',
        last_name = 'QI YANG',
        is_active = 1,
        password = 'GC97YEFLHJ' )

    user23 = User.objects.create_user(
        username = 'neelamdeol2011@hotmail.com',
        email = 'neelamdeol2011@hotmail.com',
        is_superuser = 0,
        first_name = 'NEELAM',
        last_name = 'DEOL',
        is_active = 1,
        password = 'FTOGQNGWG5' )

    user24 = User.objects.create_user(
        username = 'liyuzhao1990@gmail.com',
        email = 'liyuzhao1990@gmail.com',
        is_superuser = 0,
        first_name = 'LI',
        last_name = 'YUZHAO',
        is_active = 1,
        password = '6AHZMPH0OJ' )

    user25 = User.objects.create_user(
        username = 'vargheseaneja1992@msn.com',
        email = 'vargheseaneja1992@msn.com',
        is_superuser = 0,
        first_name = 'VARGHESE',
        last_name = 'ANEJA',
        is_active = 1,
        password = '6VLXNPMFFG' )

    user26 = User.objects.create_user(
        username = 'liushaojun2010@msn.com',
        email = 'liushaojun2010@msn.com',
        is_superuser = 0,
        first_name = 'LIU',
        last_name = 'SHAOJUN',
        is_active = 1,
        password = 'GA2I114P81' )

    user27 = User.objects.create_user(
        username = 'qinyiyang2010@hotmail.com',
        email = 'qinyiyang2010@hotmail.com',
        is_superuser = 0,
        first_name = 'QIN',
        last_name = 'YIYANG',
        is_active = 1,
        password = 'XQCCUGEM8F' )

    user28 = User.objects.create_user(
        username = 'zhoucong1990@yahoo.com',
        email = 'zhoucong1990@yahoo.com',
        is_superuser = 0,
        first_name = 'ZHOU',
        last_name = 'CONG',
        is_active = 1,
        password = 'J9JKZ5YJVN' )

    user29 = User.objects.create_user(
        username = 'tayyongming1989@gmail.com',
        email = 'tayyongming1989@gmail.com',
        is_superuser = 0,
        first_name = 'TAY',
        last_name = 'YONG MING',
        is_active = 1,
        password = 'ETL4YV46S7' )

    user30 = User.objects.create_user(
        username = 'siowcaokhoa1991@msn.com',
        email = 'siowcaokhoa1991@msn.com',
        is_superuser = 0,
        first_name = 'SIOW',
        last_name = 'CAO KHOA',
        is_active = 1,
        password = 'Y9MY702SN5' )

    user31 = User.objects.create_user(
        username = 'nihanran1989@msn.com',
        email = 'nihanran1989@msn.com',
        is_superuser = 0,
        first_name = 'NI',
        last_name = 'HANRAN',
        is_active = 1,
        password = '32FGMX9Q1L' )

    user32 = User.objects.create_user(
        username = 'choyyiting1992@hotmail.com',
        email = 'choyyiting1992@hotmail.com',
        is_superuser = 0,
        first_name = 'CHOY',
        last_name = 'YI TING',
        is_active = 1,
        password = 'O0KAZMDFSI' )

    user33 = User.objects.create_user(
        username = 'dennisbeckham1989@msn.com',
        email = 'dennisbeckham1989@msn.com',
        is_superuser = 0,
        first_name = 'DENNIS',
        last_name = 'BECKHAM',
        is_active = 1,
        password = '8T3UTWKMVZ' )

    user34 = User.objects.create_user(
        username = 'zhangzhuo1989@hotmail.com',
        email = 'zhangzhuo1989@hotmail.com',
        is_superuser = 0,
        first_name = 'ZHANG',
        last_name = 'ZHUO',
        is_active = 1,
        password = '98HR8ZSJH0' )

    user35 = User.objects.create_user(
        username = 'anupamaanghan2010@yahoo.com',
        email = 'anupamaanghan2010@yahoo.com',
        is_superuser = 0,
        first_name = 'ANUPAMA',
        last_name = 'ANGHAN',
        is_active = 1,
        password = 'X3ZXEQ9WZ5' )

    user36 = User.objects.create_user(
        username = 'liuqian1991@yahoo.com',
        email = 'liuqian1991@yahoo.com',
        is_superuser = 0,
        first_name = 'LIU',
        last_name = 'QIAN',
        is_active = 1,
        password = 'OKLITSW12O' )

    user37 = User.objects.create_user(
        username = 'zhangyingbo1989@msn.com',
        email = 'zhangyingbo1989@msn.com',
        is_superuser = 0,
        first_name = 'ZHANG',
        last_name = 'YINGBO',
        is_active = 1,
        password = 'O3BYC796R7' )

    user38 = User.objects.create_user(
        username = 'chiayeuarng1991@hotmail.com',
        email = 'chiayeuarng1991@hotmail.com',
        is_superuser = 0,
        first_name = 'CHIA',
        last_name = 'YEU ARNG',
        is_active = 1,
        password = 'XSVT14JR19' )

    user39 = User.objects.create_user(
        username = 'zengyihui2010@yahoo.com',
        email = 'zengyihui2010@yahoo.com',
        is_superuser = 0,
        first_name = 'ZENG',
        last_name = 'YIHUI',
        is_active = 1,
        password = 'TBVTNETGOV' )

    user40 = User.objects.create_user(
        username = 'fengmeng1990@gmail.com',
        email = 'fengmeng1990@gmail.com',
        is_superuser = 0,
        first_name = 'FENG',
        last_name = 'MENG',
        is_active = 1,
        password = 'GRVLNF4GET' )

    user41 = User.objects.create_user(
        username = 'zhanghan1989@hotmail.com',
        email = 'zhanghan1989@hotmail.com',
        is_superuser = 0,
        first_name = 'ZHANG',
        last_name = 'HAN',
        is_active = 1,
        password = '9OPT3S6VXD' )

    user42 = User.objects.create_user(
        username = 'liudanni1991@yahoo.com',
        email = 'liudanni1991@yahoo.com',
        is_superuser = 0,
        first_name = 'LIU',
        last_name = 'DANNI',
        is_active = 1,
        password = 'S9LLJKHM8S' )

    user43 = User.objects.create_user(
        username = 'sohjiefeng1991@msn.com',
        email = 'sohjiefeng1991@msn.com',
        is_superuser = 0,
        first_name = 'SOH',
        last_name = 'JIE FENG',
        is_active = 1,
        password = 'HXZXHM3D5Y' )

    user44 = User.objects.create_user(
        username = 'tanchenghan1990@msn.com',
        email = 'tanchenghan1990@msn.com',
        is_superuser = 0,
        first_name = 'TAN',
        last_name = 'CHENG HAN',
        is_active = 1,
        password = '1G4FPR2O2Y' )

    user45 = User.objects.create_user(
        username = 'jennyhunt1991@gmail.com',
        email = 'jennyhunt1991@gmail.com',
        is_superuser = 0,
        first_name = 'JENNY',
        last_name = 'HUNT',
        is_active = 1,
        password = 'Q33V5UJVH7' )

    user46 = User.objects.create_user(
        username = 'dingyang1989@gmail.com',
        email = 'dingyang1989@gmail.com',
        is_superuser = 0,
        first_name = 'DING',
        last_name = 'YANG',
        is_active = 1,
        password = 'EYEF84U0O2' )

    user47 = User.objects.create_user(
        username = 'zhanghong2011@msn.com',
        email = 'zhanghong2011@msn.com',
        is_superuser = 0,
        first_name = 'ZHANG',
        last_name = 'HONG',
        is_active = 1,
        password = 'SFXHR9I6YN' )

    user48 = User.objects.create_user(
        username = 'xuhuajun1990@msn.com',
        email = 'xuhuajun1990@msn.com',
        is_superuser = 0,
        first_name = 'XU',
        last_name = 'HUAJUN',
        is_active = 1,
        password = '9337PL6DNV' )

    user49 = User.objects.create_user(
        username = 'someshaneja2011@yahoo.com',
        email = 'someshaneja2011@yahoo.com',
        is_superuser = 0,
        first_name = 'SOMESH',
        last_name = 'ANEJA',
        is_active = 1,
        password = 'EE23MQIFTP' )

    user50 = User.objects.create_user(
        username = 'seahteckkee1990@gmail.com',
        email = 'seahteckkee1990@gmail.com',
        is_superuser = 0,
        first_name = 'SEAH',
        last_name = 'TECK KEE',
        is_active = 1,
        password = '6NEB1KAQC4' )

    user51 = User.objects.create_user(
        username = 'liuyihui1990@hotmail.com',
        email = 'liuyihui1990@hotmail.com',
        is_superuser = 0,
        first_name = 'LIU',
        last_name = 'YIHUI',
        is_active = 1,
        password = 'G44QMSHG3Z' )

    user52 = User.objects.create_user(
        username = 'zhuchang2010@gmail.com',
        email = 'zhuchang2010@gmail.com',
        is_superuser = 0,
        first_name = 'ZHU',
        last_name = 'CHANG',
        is_active = 1,
        password = 'HGZAB0GDTL' )

    user53 = User.objects.create_user(
        username = 'zhengxi1990@yahoo.com',
        email = 'zhengxi1990@yahoo.com',
        is_superuser = 0,
        first_name = 'ZHENG',
        last_name = 'XI',
        is_active = 1,
        password = 'MKO8NM3M9N' )

    user54 = User.objects.create_user(
        username = 'yeojiahao1989@yahoo.com',
        email = 'yeojiahao1989@yahoo.com',
        is_superuser = 0,
        first_name = 'YEO',
        last_name = 'JIA HAO',
        is_active = 1,
        password = 'H7KPRGVD9K' )

    user55 = User.objects.create_user(
        username = 'anniechapman1991@yahoo.com',
        email = 'anniechapman1991@yahoo.com',
        is_superuser = 0,
        first_name = 'ANNIE',
        last_name = 'CHAPMAN',
        is_active = 1,
        password = '8C91FFJVMH' )

    user56 = User.objects.create_user(
        username = 'jerrybrown2010@gmail.com',
        email = 'jerrybrown2010@gmail.com',
        is_superuser = 0,
        first_name = 'JERRY',
        last_name = 'BROWN',
        is_active = 1,
        password = 'Z21MCKDRGZ' )

    user57 = User.objects.create_user(
        username = 'zhouxialin1990@yahoo.com',
        email = 'zhouxialin1990@yahoo.com',
        is_superuser = 0,
        first_name = 'ZHOU',
        last_name = 'XIALIN',
        is_active = 1,
        password = 'CUTENOSVSB' )

    user58 = User.objects.create_user(
        username = 'tanhuilin1989@hotmail.com',
        email = 'tanhuilin1989@hotmail.com',
        is_superuser = 0,
        first_name = 'TAN',
        last_name = 'HUI LIN',
        is_active = 1,
        password = 'AGTABAQA7O' )

    user59 = User.objects.create_user(
        username = 'jennybeckham1992@gmail.com',
        email = 'jennybeckham1992@gmail.com',
        is_superuser = 0,
        first_name = 'JENNY',
        last_name = 'BECKHAM',
        is_active = 1,
        password = 'UDKPQUU51M' )

    user60 = User.objects.create_user(
        username = 'henryhunt1992@yahoo.com',
        email = 'henryhunt1992@yahoo.com',
        is_superuser = 0,
        first_name = 'HENRY',
        last_name = 'HUNT',
        is_active = 1,
        password = 'AP44CWKV9H' )

    user61 = User.objects.create_user(
        username = 'liujun1992@msn.com',
        email = 'liujun1992@msn.com',
        is_superuser = 0,
        first_name = 'LIU',
        last_name = 'JUN',
        is_active = 1,
        password = 'EKOFVIGF7O' )

    user62 = User.objects.create_user(
        username = 'zhangzhanpeng1992@hotmail.com',
        email = 'zhangzhanpeng1992@hotmail.com',
        is_superuser = 0,
        first_name = 'ZHANG',
        last_name = 'ZHANPENG',
        is_active = 1,
        password = '4FVQ5SSW5A' )

    user63 = User.objects.create_user(
        username = 'davidchapman1989@msn.com',
        email = 'davidchapman1989@msn.com',
        is_superuser = 0,
        first_name = 'DAVID',
        last_name = 'CHAPMAN',
        is_active = 1,
        password = 'UFWSM2I2HD' )

    user64 = User.objects.create_user(
        username = 'qinyuwei2011@hotmail.com',
        email = 'qinyuwei2011@hotmail.com',
        is_superuser = 0,
        first_name = 'QIN',
        last_name = 'YUWEI',
        is_active = 1,
        password = 'KVWJNZFR0H' )

    user65 = User.objects.create_user(
        username = 'dennispalmer1992@yahoo.com',
        email = 'dennispalmer1992@yahoo.com',
        is_superuser = 0,
        first_name = 'DENNIS',
        last_name = 'PALMER',
        is_active = 1,
        password = 'RPPY55MX0M' )

    user66 = User.objects.create_user(
        username = 'krupeshandhak1991@yahoo.com',
        email = 'krupeshandhak1991@yahoo.com',
        is_superuser = 0,
        first_name = 'KRUPESH',
        last_name = 'ANDHAK',
        is_active = 1,
        password = 'R0UHB8XM0Z' )

    user67 = User.objects.create_user(
        username = 'leeyijia1989@gmail.com',
        email = 'leeyijia1989@gmail.com',
        is_superuser = 0,
        first_name = 'LEE',
        last_name = 'YI JIA',
        is_active = 1,
        password = 'UXKF81IWDB' )

    user68 = User.objects.create_user(
        username = 'davidhall1992@yahoo.com',
        email = 'davidhall1992@yahoo.com',
        is_superuser = 0,
        first_name = 'DAVID',
        last_name = 'HALL',
        is_active = 1,
        password = 'M7FKT0H5N1' )

    user69 = User.objects.create_user(
        username = 'seahwengfai1990@yahoo.com',
        email = 'seahwengfai1990@yahoo.com',
        is_superuser = 0,
        first_name = 'SEAH',
        last_name = 'WENG FAI',
        is_active = 1,
        password = 'JY5P9T5JZ0' )

    user70 = User.objects.create_user(
        username = 'shentianyi1991@msn.com',
        email = 'shentianyi1991@msn.com',
        is_superuser = 0,
        first_name = 'SHEN',
        last_name = 'TIANYI',
        is_active = 1,
        password = 'I8I5PHV2MH' )

    user71 = User.objects.create_user(
        username = 'wenna1990@msn.com',
        email = 'wenna1990@msn.com',
        is_superuser = 0,
        first_name = 'WEN',
        last_name = 'NA',
        is_active = 1,
        password = '3X5JDFMR4Q' )

    user72 = User.objects.create_user(
        username = 'liulinxi1991@yahoo.com',
        email = 'liulinxi1991@yahoo.com',
        is_superuser = 0,
        first_name = 'LIU',
        last_name = 'LINXI',
        is_active = 1,
        password = 'MFCJ0V1LM4' )

    user73 = User.objects.create_user(
        username = 'dingweixiang1990@yahoo.com',
        email = 'dingweixiang1990@yahoo.com',
        is_superuser = 0,
        first_name = 'DING',
        last_name = 'WEI XIANG',
        is_active = 1,
        password = 'PTVQUOTI0D' )

    user74 = User.objects.create_user(
        username = 'chewsoennam1989@msn.com',
        email = 'chewsoennam1989@msn.com',
        is_superuser = 0,
        first_name = 'CHEW',
        last_name = 'SOEN NAM',
        is_active = 1,
        password = 'GPOOHEZWKO' )

    user75 = User.objects.create_user(
        username = 'irisbrown1992@hotmail.com',
        email = 'irisbrown1992@hotmail.com',
        is_superuser = 0,
        first_name = 'IRIS',
        last_name = 'BROWN',
        is_active = 1,
        password = '0BQZXKZ0SN' )

    user76 = User.objects.create_user(
        username = 'kenowen2011@yahoo.com',
        email = 'kenowen2011@yahoo.com',
        is_superuser = 0,
        first_name = 'KEN',
        last_name = 'OWEN',
        is_active = 1,
        password = 'Q9IIC4U9FD' )

    user77 = User.objects.create_user(
        username = 'zhangyuzhao1990@gmail.com',
        email = 'zhangyuzhao1990@gmail.com',
        is_superuser = 0,
        first_name = 'ZHANG',
        last_name = 'YUZHAO',
        is_active = 1,
        password = 'GWLUV964G3' )

    user78 = User.objects.create_user(
        username = 'geduo2010@yahoo.com',
        email = 'geduo2010@yahoo.com',
        is_superuser = 0,
        first_name = 'GE',
        last_name = 'DUO',
        is_active = 1,
        password = 'HP1VJTS0AG' )

    user79 = User.objects.create_user(
        username = 'huangxuanti1992@msn.com',
        email = 'huangxuanti1992@msn.com',
        is_superuser = 0,
        first_name = 'HUANG',
        last_name = 'XUANTI',
        is_active = 1,
        password = 'F26V0B2CSL' )

    user80 = User.objects.create_user(
        username = 'lisasmith2011@msn.com',
        email = 'lisasmith2011@msn.com',
        is_superuser = 0,
        first_name = 'LISA',
        last_name = 'SMITH',
        is_active = 1,
        password = 'RK0RUDAI4P' )

    user81 = User.objects.create_user(
        username = 'choyjianmin1991@gmail.com',
        email = 'choyjianmin1991@gmail.com',
        is_superuser = 0,
        first_name = 'CHOY',
        last_name = 'JIAN MIN',
        is_active = 1,
        password = 'VALG7VDRVE' )

    user82 = User.objects.create_user(
        username = 'ngyongming2011@yahoo.com',
        email = 'ngyongming2011@yahoo.com',
        is_superuser = 0,
        first_name = 'NG',
        last_name = 'YONG MING',
        is_active = 1,
        password = 'JZJYQNVUUA' )

    user83 = User.objects.create_user(
        username = 'zhengnana1991@gmail.com',
        email = 'zhengnana1991@gmail.com',
        is_superuser = 0,
        first_name = 'ZHENG',
        last_name = 'NANA',
        is_active = 1,
        password = '5BGBM4LJAI' )

    user84 = User.objects.create_user(
        username = 'zhaoyang1989@yahoo.com',
        email = 'zhaoyang1989@yahoo.com',
        is_superuser = 0,
        first_name = 'ZHAO',
        last_name = 'YANG',
        is_active = 1,
        password = '9TC0YYUPH2' )

    user85 = User.objects.create_user(
        username = 'nehalkanwat1989@gmail.com',
        email = 'nehalkanwat1989@gmail.com',
        is_superuser = 0,
        first_name = 'NEHAL',
        last_name = 'KANWAT',
        is_active = 1,
        password = 'S8RPZASEYW' )

    user86 = User.objects.create_user(
        username = 'ngyanfen2010@msn.com',
        email = 'ngyanfen2010@msn.com',
        is_superuser = 0,
        first_name = 'NG',
        last_name = 'YAN FEN',
        is_active = 1,
        password = 'XH7YAVE2E4' )

    user87 = User.objects.create_user(
        username = 'angjiayi1990@hotmail.com',
        email = 'angjiayi1990@hotmail.com',
        is_superuser = 0,
        first_name = 'ANG',
        last_name = 'JIA YI',
        is_active = 1,
        password = 'Y7ZKDZDPM6' )

    user88 = User.objects.create_user(
        username = 'chnghuiling1992@gmail.com',
        email = 'chnghuiling1992@gmail.com',
        is_superuser = 0,
        first_name = 'CHNG',
        last_name = 'HUI LING',
        is_active = 1,
        password = 'EUTQHCYQ15' )

    user89 = User.objects.create_user(
        username = 'tanweisheng1989@gmail.com',
        email = 'tanweisheng1989@gmail.com',
        is_superuser = 0,
        first_name = 'TAN',
        last_name = 'WEI SHENG',
        is_active = 1,
        password = '06WKBECG32' )

    user90 = User.objects.create_user(
        username = 'liewlienler2010@yahoo.com',
        email = 'liewlienler2010@yahoo.com',
        is_superuser = 0,
        first_name = 'LIEW',
        last_name = 'LIEN LER',
        is_active = 1,
        password = '285IIF5S0D' )

    user91 = User.objects.create_user(
        username = 'ngookaiting1991@yahoo.com',
        email = 'ngookaiting1991@yahoo.com',
        is_superuser = 0,
        first_name = 'NGOO',
        last_name = 'KAI TING',
        is_active = 1,
        password = 'MPWAXKQ2SX' )

    user92 = User.objects.create_user(
        username = 'liujun1989@msn.com',
        email = 'liujun1989@msn.com',
        is_superuser = 0,
        first_name = 'LIU',
        last_name = 'JUN',
        is_active = 1,
        password = 'ZIPFQ4XMIM' )

    user93 = User.objects.create_user(
        username = 'shenwanting2011@yahoo.com',
        email = 'shenwanting2011@yahoo.com',
        is_superuser = 0,
        first_name = 'SHEN',
        last_name = 'WANTING',
        is_active = 1,
        password = 'GLJ1SLMHZR' )

    user94 = User.objects.create_user(
        username = 'zhangcong2010@hotmail.com',
        email = 'zhangcong2010@hotmail.com',
        is_superuser = 0,
        first_name = 'ZHANG',
        last_name = 'CONG',
        is_active = 1,
        password = '6EWQGSHQO2' )

    user95 = User.objects.create_user(
        username = 'subramaniamghantasala2011@msn.com',
        email = 'subramaniamghantasala2011@msn.com',
        is_superuser = 0,
        first_name = 'SUBRAMANIAM',
        last_name = 'GHANTASALA',
        is_active = 1,
        password = 'VITD02AVAO' )

    user96 = User.objects.create_user(
        username = 'tsohuilin1989@msn.com',
        email = 'tsohuilin1989@msn.com',
        is_superuser = 0,
        first_name = 'TSO',
        last_name = 'HUI LIN',
        is_active = 1,
        password = 'I5HRZ0CMWY' )

    user97 = User.objects.create_user(
        username = 'chiaweiguo1990@hotmail.com',
        email = 'chiaweiguo1990@hotmail.com',
        is_superuser = 0,
        first_name = 'CHIA',
        last_name = 'WEI GUO',
        is_active = 1,
        password = 'BU031QI15W' )

    user98 = User.objects.create_user(
        username = 'liuyiyang1992@msn.com',
        email = 'liuyiyang1992@msn.com',
        is_superuser = 0,
        first_name = 'LIU',
        last_name = 'YIYANG',
        is_active = 1,
        password = '025Q0QAYFU' )

    user99 = User.objects.create_user(
        username = 'liuzhencai1990@msn.com',
        email = 'liuzhencai1990@msn.com',
        is_superuser = 0,
        first_name = 'LIU',
        last_name = 'ZHENCAI',
        is_active = 1,
        password = '62SFR3MRI3' )

    user0.save()
    user1.save()
    user2.save()
    user3.save()
    user4.save()
    user5.save()
    user3.save()
    user4.save()
    user5.save()
    user6.save()
    user7.save()
    user8.save()
    user9.save()
    user10.save()
    user11.save()
    user12.save()
    user13.save()
    user14.save()
    user15.save()
    user16.save()
    user17.save()
    user18.save()
    user19.save()
    user20.save()
    user21.save()
    user22.save()
    user23.save()
    user24.save()
    user25.save()
    user26.save()
    user27.save()
    user28.save()
    user29.save()
    user30.save()
    user31.save()
    user32.save()
    user33.save()
    user34.save()
    user35.save()
    user36.save()
    user37.save()
    user38.save()
    user39.save()
    user40.save()
    user41.save()
    user42.save()
    user43.save()
    user44.save()
    user45.save()
    user46.save()
    user47.save()
    user48.save()
    user49.save()
    user50.save()
    user51.save()
    user52.save()
    user53.save()
    user54.save()
    user55.save()
    user56.save()
    user57.save()
    user58.save()
    user59.save()
    user60.save()
    user61.save()
    user62.save()
    user63.save()
    user64.save()
    user65.save()
    user66.save()
    user67.save()
    user68.save()
    user69.save()
    user70.save()
    user71.save()
    user72.save()
    user73.save()
    user74.save()
    user75.save()
    user76.save()
    user77.save()
    user78.save()
    user79.save()
    user80.save()
    user81.save()
    user82.save()
    user83.save()
    user84.save()
    user85.save()
    user86.save()
    user87.save()
    user88.save()
    user89.save()
    user90.save()
    user91.save()
    user92.save()
    user93.save()
    user94.save()
    user95.save()
    user96.save()
    user97.save()
    user98.save()
    user99.save()
    print("sdfjldh")



print("RUN")
# DON'T PUT RUN HERE OR IT WILL INSERT TWICE
# run()