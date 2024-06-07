import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:io';

import 'package:kanji_ai_front/pages/home.dart';
import 'package:kanji_ai_front/pages/requestAPI.dart';
import 'package:kanji_ai_front/pages/showpredict.dart';
import 'package:kanji_ai_front/pages/unavailable.dart';

class ImgSend extends StatelessWidget {

   File ? kanji;
   String? path;
   ImgSend({super.key, required this.kanji, required this.path});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: appbar(),
      backgroundColor: const Color.fromARGB(255, 30, 30, 30),
      body: Center(
        child: Column(children: [
          const SizedBox(height: 100),
          structure(),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
            ElevatedButton(
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.green,
                elevation: 0,
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(15.0)),
              minimumSize: const Size(150, 80),
              ),
              onPressed: () async {
                final r = await requestPredictionAPI(kanji!, context);
                Navigator.of(context).push(MaterialPageRoute(builder: (context) => Pred(kanji: kanji, prediction: r))); 
              },
              child: const Text("Predict Kanji", style: TextStyle(color: Colors.white),),
            ),
            ElevatedButton(
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.red,
                elevation: 0,
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(15.0)),
              minimumSize: const Size(150, 80),
              ),
              onPressed: () {
                kanji = null;
                Navigator.of(context).push(MaterialPageRoute(builder: (context) => Homepage())); 
              },
              child: const Text("Retake image", style: TextStyle(color: Colors.white),),
            ),
          ],)
        ],)
      )

    );
  }

  Column structure() {
    return  Column(
      crossAxisAlignment: CrossAxisAlignment.center,
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        const SizedBox(height: 50),
        Container(
          height: 300,
          width: 300,
          decoration: BoxDecoration(
            border: Border.all(
            color: const Color.fromARGB(255, 169, 86, 184),
            width: 2
              ),
            image: DecorationImage(
              image: FileImage(kanji!),
              fit: BoxFit.fill),
            shape: BoxShape.rectangle,
            )
          ),
        const SizedBox(height: 100),
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

  Future<Prediction> requestPredictionAPI(File kanji, BuildContext context) async{
    final request = http.MultipartRequest('POST', Uri.parse('https://kanji.otterleek.com/'));
    request.files.add(await http.MultipartFile.fromPath('file', path!));
    final response = await request.send();
    if (response.statusCode==200){
      String b = (await http.Response.fromStream(response)).body;
      return Prediction.fromJson(jsonDecode(b));
    }
    else{
      Navigator.of(context).push(MaterialPageRoute(builder: (context) => Unavailable())); 
      throw Exception('Kanji AI Predict WebService is unavailable');
    }
  }
}
