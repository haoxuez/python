print("1，水瓶，1月21-2月18""\n"
"2，双鱼，2月19-3月20""\n"
"3，白羊，3月21-4月19""\n"
"4，金牛，4月20-5月20""\n"
"5，双子，5月21-6月21""\n"
"6，巨蟹，6月21-7月22""\n"
"7，狮子，7月23-8月22""\n"
"8，处女，8月23-9月23""\n"
"9，天枰，9月24-10月23""\n"
"10，天蝎，10月24-11月22""\n"
"11，射手，11月23-12月21""\n"
"12，摩羯，12月22-1月20)""\n")
s=('.水瓶座的人喜欢简单，不喜欢麻烦和累的感觉',
'.双鱼座的人喜欢吃，顶级吃货；懒，超级怕麻烦。',
'.白羊座的人倔强，遇到讨厌的人，宁可受罪也不向对方求助',
'金牛座的人吃软不吃硬，经常口是心非。',
'双子座的人善忘，不论重不重要的事都容易忘记，不记仇。',
'狮子座的人霸道且控制欲强，其实是没安全感，喜欢占主导地位，被赞美。',
'处女座的人细心大方，外表柔和，内在充满激情。',
'天枰座的人敏感多疑，喜欢胡思乱想，爱钻牛角尖。',
'天蝎座的人有魅力，个性张扬或内敛都对旁人很有吸引力。',
'射手座的人强迫症，神经质，每晚睡觉前都觉得窗没关，门没锁。',
'摩羯座的人吃软不吃硬，经常口是心非。',)
name=input("你的名字是：")
number=int(input("你的星座编码是："))
print("%s你好，你的星座性格是：%s"%(name,s[number]))