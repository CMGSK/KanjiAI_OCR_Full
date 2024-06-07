import 'dart:io';
import 'package:flutter/material.dart';

class Holder extends StatefulWidget {
  final Widget body;
  final String title;
  final Color backgroundColor;
  final GlobalKey<ScaffoldState> scaffoldKey;

  const Holder(
      { Key? key,
        required this.body,
        required this.title,
        required this.scaffoldKey,
        this.backgroundColor = Colors.white,
       })
      : super(key: key);

  @override
  ScreenHolderState createState() => ScreenHolderState();
}

class ScreenHolderState extends State<Holder> {

  late String imageString;
  File? kanji;

@override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
        title: Text(widget.title),
        ) ,
        drawer: Drawer(
          child: Padding(
            padding: const EdgeInsets.all(40),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.center,
              children: <Widget>[
                Container(
                  width: 150.0,
                  height: 150.0,
                  decoration: BoxDecoration(
                    border: Border.all(color: Colors.white),
                    shape: BoxShape.circle,
                    image:  DecorationImage(
                    fit: BoxFit.fill,
                    // ignore: unnecessary_null_comparison
                    image: kanji != null ? 
                        Image.file(kanji!).image
                        : const ExactAssetImage('assets/placeholder.png',
                        scale: 1.0)))),
                  ]),
            )),
    body: widget.body
    );
  }
}