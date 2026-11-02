/// Switzerland's licence plates for the `plate_core` library.
///
/// High, long, front, small and diplomatic formats in the federal colours,
/// with an advisory validator.
library;

// TODO(py): [D5] one module `plates.countries.switzerland`; assets via importlib.resources.
// TODO(ts): [D5] one subpath export `./countries/switzerland`; tree-shakable.
// TODO(kt): [D5] package `countries.switzerland` in the countries module.
export 'package:plate_alphabet/plate_alphabet.dart' show SwitzerlandAlphabets;

export 'src/switzerland_colors.dart';
export 'src/switzerland_country.dart';
export 'src/switzerland_missions.dart';
export 'src/switzerland_plates.dart';
export 'src/switzerland_regions.dart';
export 'src/switzerland_serial_generator.dart';
export 'src/switzerland_themes.dart';
export 'src/switzerland_validators.dart';
