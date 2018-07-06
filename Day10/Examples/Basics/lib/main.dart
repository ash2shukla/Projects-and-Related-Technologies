import 'package:flutter/material.dart';
import 'bodyUI.dart';

void main() => runApp(new MyApp());

class MyApp extends StatelessWidget {
  @override // Stateless Widgets must implement a build method
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Some App', // title is not necessary
      home: new StatefulBody(), // home is required.
      );
  }
}