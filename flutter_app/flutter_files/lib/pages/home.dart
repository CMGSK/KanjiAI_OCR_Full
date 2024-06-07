import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'dart:io';

import 'package:kanji_ai_front/pages/holder.dart';
import 'package:kanji_ai_front/pages/imagesender.dart';

class Homepage extends StatelessWidget {

   Homepage({super.key});
   File ? kanji;
   String? path;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: appbar(),
      backgroundColor: const Color.fromARGB(255, 30, 30, 30),
      body: Center(
        child: Column(children: [
          const SizedBox(height: 150),
          structure(),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
            ElevatedButton(
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.red,
                elevation: 0,
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(15.0)),
              minimumSize: const Size(150, 80),
              ),
              onPressed: () {
                imgFromCamera(context);
              },
              child: const Text("Camera",style: TextStyle(color: Colors.white)),
            ),
            ElevatedButton(
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.blue,
                elevation: 0,
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(15.0)),
              minimumSize: const Size(150, 80),
              ),
              onPressed: () {
                imgFromGallery(context);
              },
              child: const Text("Gallery",style: TextStyle(color: Colors.white)),
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
      instructionText(),
      const SizedBox(height: 100),
    ],
  );
}


Holder imageContainer(){
  return Holder(
    scaffoldKey: (GlobalKey<ScaffoldState>()),
    title: "Kanji",
    body: Column(
        mainAxisAlignment: MainAxisAlignment.start,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: <Widget>[
          Container(
              padding: const EdgeInsets.only(top: 20, bottom: 20),
              child: Center(
                child: Column(
                  children: <Widget>[
                    GestureDetector(
                        child: Container(
                            width: 190.0,
                            height: 190.0,
                            decoration: BoxDecoration(
                              shape: BoxShape.circle,
                              image:  DecorationImage(
                                  fit: BoxFit.fill,
                                  image: kanji != null ?
                                      Image.file(kanji!).image
                                      : const ExactAssetImage(
                                      'assets/placeholder.png',
                                      scale: 1.0)),
                            )),
                        onTap: () {kanji = null;}),
                    const SizedBox(
                      height: 10,
                    ),
                    const Text('Tap image to delete')
                  ],
                ),
              )),
]));
}

Text instructionText() {
  return const Text(
      'Please adjust the kanji to the edges for the algorithm to work properly',
      textAlign: TextAlign.center,
      style: TextStyle(
        color: Color.fromARGB(255, 169, 86, 184),
        fontSize: 16,
      ),
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

void imgFromGallery(BuildContext context) async{
  final pic = await ImagePicker().pickImage(source: ImageSource.gallery);
  kanji = pic == null ? null : File(pic.path);
  if (kanji != null){
    path = pic!.path;
    Navigator.of(context).push(MaterialPageRoute(builder: (context) => ImgSend(kanji: kanji, path: path))); 
  }
}
void imgFromCamera(BuildContext context) async{
  final pic = await ImagePicker().pickImage(source: ImageSource.camera);
  kanji = pic == null ? null : File(pic.path);
  if (kanji != null){
    path = pic!.path;
    Navigator.of(context).push(MaterialPageRoute(builder: (context) => ImgSend(kanji: kanji, path: path))); 
  }
}

}
