import 'package:flutter/material.dart';
import 'bodyUI.dart';

void main() => runApp(new MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: new StatefulBody(), // home is required.
      );
  }
}
