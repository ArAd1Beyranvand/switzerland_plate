FREE PALESTINE 🇮🇷🇵🇸 پاینده ایران

GO VEGAN 🌱

==================================

From the mighty people of Iran to the people of Switzerland to view examples:

https://platexample.ir/#/discover/switzerland:flutter

# switzerland_plate

Switzerland's licence plates for the plate_core library: high, long, front, small and diplomatic formats in the federal colours, with an advisory validator.

## Languages

| Language | Folder | Example |
| --- | --- | --- |
| Flutter / Dart | [`flutter/`](https://github.com/ArAd1Beyranvand/switzerland_plate/tree/main/flutter) | [platexample](https://platexample.ir/#/discover/switzerland:flutter) |
| Kotlin | [`kotlin/`](https://github.com/ArAd1Beyranvand/switzerland_plate/tree/main/kotlin) | [platexample](https://platexample.ir/#/discover/switzerland:kotlin) |
| Python | [`python/`](https://github.com/ArAd1Beyranvand/switzerland_plate/tree/main/python) | [platexample](https://platexample.ir/#/discover/switzerland:python) |
| TypeScript | [`typescript/`](https://github.com/ArAd1Beyranvand/switzerland_plate/tree/main/typescript) | [platexample](https://platexample.ir/#/discover/switzerland:typescript) |

## Quick start

### Install

```yaml
dependencies:
  plate_core: ^0.12.0
  switzerland_plate: ^0.1.0
```

### Use

```dart
import 'package:plate_core/plate_core.dart';
import 'package:switzerland_plate/switzerland_plate.dart';

PlateCanvas(
  spec: SwitzerlandPlates.high,
  theme: SwitzerlandThemes.standard,
  validator: const SwitzerlandValidator(),
  autoValidate: true,
  onChooseCharacter: noCharacterChooser,
);
```

## Specs

Each spec is one plate layout.

- `SwitzerlandPlates.high`
- `SwitzerlandPlates.dealer`
- `SwitzerlandPlates.temporary`
- `SwitzerlandPlates.long`
- `SwitzerlandPlates.military`
- `SwitzerlandPlates.front`
- `SwitzerlandPlates.customs`
- `SwitzerlandPlates.motorcycle`
- `SwitzerlandPlates.scooter`
- `SwitzerlandPlates.diplomatic`
- `SwitzerlandPlates.consular`

## Themes

- `SwitzerlandThemes.standard`
- `SwitzerlandThemes.utility`
- `SwitzerlandThemes.exceptional`
- `SwitzerlandThemes.agricultural`
- `SwitzerlandThemes.scooter`
- `SwitzerlandThemes.red`
- `SwitzerlandThemes.military`
- `SwitzerlandThemes.diplomatic`

## Change it

`PlateCanvas` takes `spec:` (an entry of `SwitzerlandPlates`) and `theme:` (an entry of `SwitzerlandThemes`). Set `validator:` to `SwitzerlandValidator()` and `autoValidate: true` to show validation hints.

## Also included

- `SwitzerlandCountry` — the country panel.
- `SwitzerlandValidator` — the plate validator.
- `SwitzerlandMissions` — code table.
- `SwitzerlandRegions` — code table.

## Plates

Switzerland's current plates.

* `high` — the 300 × 160 rear plate, canton over number; `dealer` and
  `temporary` are the same canvas with a `U` mark or a sticker.
* `long` — the 500 × 110 rear plate on one line; `military` opens with a
  lone `M`.
* `front` — 300 × 80.
* `customs` — duty-unpaid plate: canton, control number, sticker, `Z`.
* `motorcycle`, `scooter` — canton over a five-digit number.
* `diplomatic`, `consular` — `CD` / `CC` band, canton, serial, country
  code. Code 7 is refused; see `SwitzerlandMissions`.

The colour is the theme: utility blue, exceptional gold and the red
bicycle-carrier plate are `high` or `long` with the matching
`SwitzerlandThemes` livery.

Not implemented: moped and Segway plates (their photographs could not be
rectified and have no artwork), the discontinued Administration (`A`) and
PTT/SBB (`P`) plates, the `AT` diplomatic prefix (no picture), and the
3 + 3 digit gap of the red plate.

## Part of plate

Painted by [`plate_core`](https://pub.dev/packages/plate_core); alphabets shared through [`plate_alphabet`](https://pub.dev/packages/plate_alphabet); optional character picker in [`plate_keypad`](https://pub.dev/packages/plate_keypad).

## License

See [LICENSE](https://github.com/ArAd1Beyranvand/switzerland_plate/blob/main/LICENSE).
