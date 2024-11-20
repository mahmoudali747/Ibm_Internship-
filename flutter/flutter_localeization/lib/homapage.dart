import 'package:flutter/material.dart';
import 'package:flutter_localeization/app_localizations.dart';

class Homapage extends StatelessWidget {
  const Homapage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Color.fromARGB(255, 74, 171, 228),
      ),
      drawer: Drawer(),
      body: Center(
          child: Padding(
        padding: EdgeInsets.all(8.0),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Text(
              AppLocalizations.of(context)?.translate("hello_msg") ??
                  "Translation not found",
              style: TextStyle(fontSize: 25),
              textAlign: TextAlign.center,
            ),
            Text(
              'This text will not be translated',
              style: TextStyle(fontSize: 25),
              textAlign: TextAlign.center,
            )
          ],
        ),
      )),
      floatingActionButton: FloatingActionButton(
        onPressed: () {},
        child: Icon(Icons.add),
      ),
    );
  }
}
