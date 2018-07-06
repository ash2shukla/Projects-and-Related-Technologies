import 'package:flutter/material.dart';

class StatelessBody extends StatelessWidget {
	// StatelessBody 
	@override
	Widget build(BuildContext context) {
		return new Scaffold(
          floatingActionButton: new FloatingActionButton(child: new Icon(Icons.add)),
          appBar:new AppBar(title: new Text('Some App')),
          drawer: new Drawer(),
          body: new Text('abcdefg'),
        );
	}
}

class StatefulBody extends StatefulWidget {
	final someattr;
	final child;

	@override
	_StatefulWidget createState() => _StatefulWidget();
}

class _StatefulWidget extends State<StatefulBody> {
	int count = 0;
	List<BottomNavigationBarItem> items = new List();

	void incrementCount() {
		setState(() { count += 1; });
	}

	@override
	Widget build(BuildContext context) {
		return new Scaffold(
          floatingActionButton: new FloatingActionButton(
          								child: new Icon(Icons.add),
          								onPressed: incrementCount, 
          												),
          appBar: new AppBar(title: new Text('Some App')
          					),
          drawer: new Drawer(),
          body: new Center(child: new Text(count.toString(),style:new TextStyle(fontWeight: FontWeight.bold,
          															 color: Color(0xFF0000).withOpacity(count/200),
          															 fontSize: (count).toDouble()
          															))),
        );
	}
}