
import 'package:flutter/material.dart';

class Unavailable extends StatelessWidget {

  const Unavailable({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: appbar(),
      backgroundColor: const Color.fromARGB(255, 30, 30, 30),
      body: const Center(
        child: Column(children: [
          SizedBox(height: 150),
          Text("The KanjiAi WebService is unavailable at this moment. Please try again later.",
          style: TextStyle(color: Colors.white, fontSize: 20),),
        ],)
      )
    );
  }

  AppBar appbar(){
        return AppBar(
          title:const Text('Kanji AI Recognizer',
            style: TextStyle(
              color: Color.fromARGB(255, 169, 86, 184),
              fontWeight: FontWeight.bold),
            ),
          centerTitle: true,
          backgroundColor: Colors.black,
          elevation: 0,
        );
  }
}