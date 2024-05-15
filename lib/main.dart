import 'package:flutter/material.dart';


void main() async{



  runApp(const MainPage());
}

class MainPage extends StatelessWidget {
  const MainPage({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Magic KeyBroad',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: const HomePage(title: 'Magic KeyBroad'),
    );
  }
}





class HomePage extends StatefulWidget {
  const HomePage({super.key, required this.title});
  final String title;
  @override
  State<HomePage> createState() => _HomePageState();
}


class _HomePageState extends State<HomePage> {

  double drawer_width = 0.20;

  double link_button_hight = 50;

  String title_text = 'Magical KeyBoard';

  PageController _pageController = PageController();

  List<List<String>> app_plus = [
    ['打字加速＋','顯示出你手指摸到的按鍵，減少低頭的平頻率，加速你的打字速度','魔法鍵盤'],
    ['快捷鍵小助手＋','在按下快捷鍵時，彈出快捷鍵功能的提示','魔法鍵盤'],
    ['魔法預覽','在觸摸功能鍵時提前預覽效果，放開即可取消','Yihuan'],

  ];
  
  List<Icon> app_plus_icon = [Icon(Icons.type_specimen),Icon(Icons.class_outlined),Icon(Icons.auto_mode_sharp )];

  List<bool> app_plus_on = [true,false,false];

  @override
  Widget build(BuildContext context) {

    int _currentPage = 0;

    void rebuild() {
      setState(() {
        // Update state variables here to trigger a rebuild
      });
    }

    final MaterialStateProperty<Icon?> thumbIcon =
    MaterialStateProperty.resolveWith<Icon?>(
          (Set<MaterialState> states) {
        if (states.contains(MaterialState.selected)) {
          return const Icon(Icons.check);
        }
        return const Icon(Icons.close);
      },
    );


    return Scaffold(
      body: Row(
        children: [
          AnimatedContainer(
            duration: Duration(milliseconds: 200), // 動畫持續時間
            width: MediaQuery.of(context).size.width * drawer_width,
            constraints: BoxConstraints(maxWidth: MediaQuery.of(context).size.width * drawer_width),
            curve: Curves.easeInOut,

            color: Color.fromARGB(100, 213, 230, 255),
            child: Column(
              children: [
                Container(
                  alignment: Alignment.topLeft,
                  height: MediaQuery.of(context).size.width*0.5,
                  child: Column(
                    children: [
                      Container(
                        margin: EdgeInsets.all(20),
                        alignment: Alignment.topLeft,
                        child: IconButton(
                          icon: Icon(Icons.dehaze),
                          color: Colors.black38,
                          onPressed: (){
                            if(drawer_width == 0.20){
                              drawer_width = 0.056;
                            }else{
                              drawer_width = 0.20;
                            }
                            setState(() {

                            });
                          },
                        ),
                      ),

                      Column(
                        children: [
                          SizedBox(
                            height: 250,
                          ),




                          Container(
                            margin: EdgeInsets.only(left: 20,right: 20),
                            alignment: Alignment.topLeft,
                            child: IconButton(
                              icon: Icon(Icons.keyboard),
                              color: Colors.black38,
                              tooltip: '裝置',
                              onPressed: (){
                                _pageController.animateToPage(0, duration: Duration(milliseconds: 500),curve: Curves.easeOut);
                              },
                            ),
                          ),


                          SizedBox(
                            height: 25,
                          ),

                          Container(
                            margin: EdgeInsets.only(left: 20,right: 20),
                            alignment: Alignment.topLeft,
                            child: IconButton(
                              icon: Icon(Icons.auto_awesome),
                              color: Colors.black38,
                              tooltip: '功能',
                              onPressed: (){
                                _pageController.animateToPage(1, duration: Duration(milliseconds: 500),curve: Curves.easeOut);
                              },
                            ),
                          ),

                          SizedBox(
                            height: 25,
                          ),

                          Container(
                            margin: EdgeInsets.only(left: 20,right: 20),
                            alignment: Alignment.topLeft,
                            child: IconButton(
                              icon: Icon(Icons.build_sharp),
                              color: Colors.black38,
                              tooltip: '校正',
                              onPressed: (){
                                _pageController.animateToPage(2, duration: Duration(milliseconds: 500),curve: Curves.easeOut);

                              },
                            ),
                          ),

                          SizedBox(
                            height: 25,
                          ),

                          Container(
                            margin: EdgeInsets.only(left: 20,right: 20),
                            alignment: Alignment.topLeft,
                            child: IconButton(
                              icon: Icon(Icons.settings),
                              color: Colors.black38,
                              tooltip: '設定',
                              onPressed: (){
                                _pageController.animateToPage(3, duration: Duration(milliseconds: 500),curve: Curves.easeOut);

                              },
                            ),
                          ),
                        ],
                      ),

                    ],
                  )
                )
              ],
            ),
          ),
          AnimatedContainer(
            duration: Duration(milliseconds: 200), // 動畫持續時間
            width: MediaQuery.of(context).size.width * (1-drawer_width),
            constraints: BoxConstraints(maxWidth: MediaQuery.of(context).size.width * (1-drawer_width)),
            curve: Curves.easeInOut,
            color: Colors.white,
            child:Column(
              children: [
                Container(
                  margin: EdgeInsets.all(30),
                  alignment: Alignment.topLeft,
                  height: 50,
                  child: Text(
                    (title_text).toString(),
                    style: TextStyle(
                      fontFamily: 'Arial',
                      fontSize: 25,
                      fontWeight: FontWeight.bold,
                      color: Colors.black38,
                    ),
                  ),
                ),

                SizedBox(
                  height: 800,
                  child: PageView(
                    controller: _pageController,
                    scrollDirection: Axis.vertical,
                    onPageChanged: (int page){
                      setState(() {
                        _currentPage = page;
                        title_text = ['Magical KeyBoard','功能開關','鍵盤校正','設定'][page];
                        rebuild();
                      });
                    },

                    children: [
                      Column(
                        children: [
                          SizedBox(
                            height: 50,
                          ),
                          Container(
                            padding: EdgeInsets.all(50),
                            width: 1300,
                            height: 700,
                            child: keyboard(),
                          )
                        ],
                      ),
                      Column(
                        crossAxisAlignment: CrossAxisAlignment.center,
                        children: [

                          SizedBox(
                            height: 700,
                            width: 1200,
                            child: GridView.count(
                              padding: EdgeInsets.all(50),
                              childAspectRatio: 2,
                              crossAxisCount: 2,
                              children: List.generate(app_plus.length, (index){
                                return SizedBox(
                                  height: 50,
                                  width: 200,
                                  child: Card(
                                    color: Colors.white,
                                    margin: EdgeInsets.all(15),
                                    child: Container(
                                      padding: EdgeInsets.only(top: 30,left: 40,right: 20),
                                      child: Column(
                                        children: [
                                          Row(
                                            crossAxisAlignment: CrossAxisAlignment.start,
                                            children: [
                                              Column(
                                                children: [
                                                  SizedBox(
                                                    height: 10,
                                                  ),
                                                  app_plus_icon[index]
                                                ],
                                              ),
                                              Container(
                                                margin: EdgeInsets.only(left: 30),
                                                child: Column(
                                                  crossAxisAlignment: CrossAxisAlignment.start,
                                                  children: [
                                                    Text(
                                                      app_plus[index][0],
                                                      style: TextStyle(
                                                        color: Colors.black,
                                                        fontSize: 15,
                                                      ),
                                                    ),
                                                    SizedBox(
                                                      height: 10,
                                                    ),
                                                    SizedBox(
                                                      width: 380,
                                                      height: 130,
                                                      child:  Text(
                                                        app_plus[index][1],
                                                        style: TextStyle(
                                                          color: Colors.black38,
                                                          fontSize: 15,
                                                        ),
                                                        softWrap: true,
                                                        maxLines: 2,
                                                      ),
                                                    ),

                                                  ],
                                                ),
                                              ),
                                            ],
                                          ),

                                          Row(
                                            children: [
                                              SizedBox(
                                                width: 370,
                                                child:  Text(
                                                  ('資訊：由'+app_plus[index][2]+'提供').toString(),

                                                  style: TextStyle(
                                                    color: Colors.black38,
                                                    fontSize: 12,
                                                  ),
                                                  softWrap: true,
                                                  maxLines: 2,
                                                ),
                                              ),
                                              SizedBox(
                                                height: 25,
                                                width: 70,
                                                child: FittedBox(
                                                  fit: BoxFit.contain,
                                                  child: Switch(
                                                    thumbIcon: thumbIcon,
                                                    value: app_plus_on[index],
                                                    onChanged: (bool value) {
                                                      setState(() {
                                                        app_plus_on[index] = value;
                                                      });
                                                    },
                                                    activeColor: Colors.black12,
                                                  ),
                                                ),
                                              )
                                            ],
                                          ),
                                        ],
                                      )
                                    )
                                  ),
                                );
                              }),
                            ),
                          ),
                        ],
                      ),


                      //校正頁面

                      Column(
                        children: [
                          Text(
                            '請雙手離開鍵盤',
                            style: TextStyle(
                              color: Colors.black54,
                              fontSize: 20,
                            ),
                          ),
                        ],
                      ),


                      //設定頁面 page4 03

                      Column(
                        children: [
                          Text(
                            '基礎設定',
                            style: TextStyle(
                              color: Colors.black54,
                              fontSize: 20,
                            ),
                          ),
                        ],
                      )


                    ],
                  ),
                ),

              ],
            ),
          ),
        ],
      ),
    );
  }
}




class keyboard extends StatefulWidget{
  @override
  State<keyboard> createState() => _keyboard();
}

class _keyboard extends State<keyboard> {





  List<List<String>> keyboard_key = [
    ['esc','f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','f12','back'],
    ['Tab','Q','W','E','R','T','Y','U','I','O','P','[{',']}','\\|','Del'],
    ['Capslock','A','S','D','F','G','H','J','K','L',';:','\n','Enter','Paup'],
    ['Shift','Z','X','C','V','B','N','M',',<','.>','\/？','Shift','上'],
    ['Ctrl','Win','Alt','Space','Alt','Fn','Ctrl','左','下','右']
  ];

  List<List<String>> keyboard_cap_width = [
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','2.1'],
    ['1.5','1','1','1','1','1','1','1','1','1','1','1','1','1.6','1'],
    ['1.7','1','1','1','1','1','1','1','1','1','1','1','2.4','1'],
    ['2.1','1','1','1','1','1','1','1','1','1','1','1.3','1'],
    ['1.3','1.3','1.3','5.8','1','1','1','1','1','1']
  ];

  int keycap_base = 60;


  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Row(children: _buildKeyboardKeys1(),),
        Row(children: _buildKeyboardKeys2(),),
        Row(children: _buildKeyboardKeys3(),),
        Row(children: _buildKeyboardKeys4(),),
        Row(children: _buildKeyboardKeys5(),),
      ],
    );
  }

  List<Widget> _buildKeyboardKeys1() {
    return keyboard_key[0].map((key) => _buildKeyboardKey(key)).toList();
  }
  List<Widget> _buildKeyboardKeys2() {
    return keyboard_key[1].map((key) => _buildKeyboardKey(key)).toList();
  }
  List<Widget> _buildKeyboardKeys3() {
    return keyboard_key[2].map((key) => _buildKeyboardKey(key)).toList();
  }
  List<Widget> _buildKeyboardKeys4() {
    return keyboard_key[3].map((key) => _buildKeyboardKey(key)).toList();
  }
  List<Widget> _buildKeyboardKeys5() {
    return keyboard_key[4].map((key) => _buildKeyboardKey(key)).toList();
  }

  Widget _buildKeyboardKey(String key) {

    double keycap_w = 0;
    double test1 = 0;

    for(int i=0;i<5;i++){
      if(keyboard_key[i].indexOf(key)!=-1){
        keycap_w = keycap_base * double.parse(keyboard_cap_width[i][keyboard_key[i].indexOf(key)]);
        test1 = double.parse(keyboard_cap_width[i][keyboard_key[i].indexOf(key)]);

      }
    }


    return SizedBox(
      width: keycap_w, // 按鍵寬度
      height: 60,
      child: Card(
        child: Center(
          child: Text(
            key,
            style: TextStyle(
              fontSize: 14,
              color: Colors.black54
            ),
          ),
        )
      ),
    );
  }


}