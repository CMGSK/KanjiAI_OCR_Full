
import 'dart:io';
import 'package:flutter/material.dart';
import 'package:kanji_ai_front/pages/home.dart';
import 'package:kanji_ai_front/pages/requestAPI.dart';

class Pred extends StatelessWidget {

   File ? kanji;
   Prediction prediction;
   
   Pred({super.key, required this.kanji, required this.prediction});


  @override
  Widget build(BuildContext context) {
    
    return Scaffold(
      appBar: appbar(),
      backgroundColor: const Color.fromARGB(255, 30, 30, 30),
      body: Center(
        child: Column(children: [
          const SizedBox(height: 100),
          (prediction.content.elementAt(0).certainty > 95.0 ? singleKanjiStructure(prediction) : multiKanjiStructure(prediction)),
          const SizedBox(height: 100),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
            ElevatedButton(
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.red.shade900,
                elevation: 0,
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(15.0)),
              minimumSize: const Size(150, 80),
              ),
              onPressed: () {
                kanji = null;
                Navigator.of(context).push(MaterialPageRoute(builder: (context) => Homepage())); 
              },
              child: const Text("Back"),
            ),
          ],)
        ],)
      )

    );
  }

  Column singleKanjiStructure(Prediction prediction) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.center,
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        const SizedBox(height: 50),
        SizedBox(
          height: 300,
          width: 300,
          child: Material(
            color: const Color.fromARGB(0, 0, 0, 0),
            borderRadius: BorderRadius.zero,
            child: Center(child: SelectableText(
              prediction.content.elementAt(0).character,
              style: const TextStyle(fontSize: 130, color:Color.fromARGB(255, 169, 86, 184)),),),
              )
            ),
        const SizedBox(height: 40),
      ],
    );
  }

  Column multiKanjiStructure(Prediction prediction) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.center,
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        const SizedBox(height: 50),
        SizedBox(
          height: 200,
          width: 200,
          child: Material(
            color: const Color.fromARGB(0,0, 0, 0),
            borderRadius: BorderRadius.zero,
            child: Center(child: SelectableText(
              prediction.content.elementAt(0).character,
              style: const TextStyle(fontSize: 120, color:Color.fromARGB(255, 169, 86, 184)),),),
              )
            ),
        const SizedBox(height: 20),
        Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
          SizedBox(
            height: 60,
            width: 60,
            child: Material(
            color: const Color.fromARGB(0,0, 0, 0),
              borderRadius: BorderRadius.zero,
              child: Center(child: SelectableText(
              prediction.content.elementAt(1).character,
                style: const  TextStyle(fontSize: 40, color:Color.fromARGB(255, 255, 255, 255)),),),
                )
              ),
          SizedBox(
            height: 60,
            width: 60,
            child: Material(
            color: const Color.fromARGB(0,0, 0, 0),
              borderRadius: BorderRadius.zero,
              child: Center(child: SelectableText(
              prediction.content.elementAt(2).character,
                style: const TextStyle(fontSize: 40, color:Color.fromARGB(255, 255, 255, 255)),),),
                )
              ),
          SizedBox(
            height: 60,
            width: 60,
            child: Material(
            color: const Color.fromARGB(0,0, 0, 0),
              borderRadius: BorderRadius.zero,
              child: Center(child: SelectableText(
              prediction.content.elementAt(3).character,
                style: const TextStyle(fontSize: 40, color:Color.fromARGB(255, 255, 255, 255)),),),
                )
              ),
          SizedBox(
            height: 60,
            width: 60,
            child: Material(
            color: const Color.fromARGB(0,0, 0, 0),
              borderRadius: BorderRadius.zero,
              child: Center(child: SelectableText(
              prediction.content.elementAt(4).character,
                style: const TextStyle(fontSize: 40, color:Color.fromARGB(255, 255, 255, 255)),),),
                )
              ),
          ],
        ),
        const SizedBox(height: 20),
        const  Text("""Due to complexity of the kanji or busy backgrounds, in some cases the prediction might be a tad off. Since our certainty about the result is not as high as we'd like, these kanji might be better matches for your request.""",
          textAlign: TextAlign.center,
          style: TextStyle(
            color: Color.fromARGB(255, 169, 86, 184),
            fontSize: 16,
          ),)
      ],
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