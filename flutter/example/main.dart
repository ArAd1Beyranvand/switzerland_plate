import 'package:flutter/widgets.dart';
import 'package:plate_core/plate_core.dart';
import 'package:switzerland_plate/switzerland_plate.dart';

void main() => runApp(
  PlateExampleApp(
    spec: SwitzerlandPlates.high,
    theme: SwitzerlandThemes.standard,
  ),
);
