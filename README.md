FREE PALESTINE 🇮🇷🇵🇸 پاینده ایران

GO VEGAN 🌱

==================================

From the mighty people of Iran to the people of Switzerland to view examples:

https://platexample.ir/#/discover/switzerland

# switzerland_plate

Switzerland's licence plates for the `plate_core` library. High, long, front, small and diplomatic formats in the federal colours, with an advisory validator.

## Install

```yaml
dependencies:
  plate_core: ^0.12.0
  switzerland_plate: ^0.1.0
```

## Use

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

## Contains

- `SwitzerlandCountry` — country panel: `switzerland`.
- `SwitzerlandPlates` — 11 plate specs: `high`, `dealer`, `temporary`, `long`, `military`, `front`, `customs`, `motorcycle`, `scooter`, `diplomatic`, `consular`.
- `SwitzerlandThemes` — 8 themes: `standard`, `utility`, `exceptional`, `agricultural`, `scooter`, `red`, `military`, `diplomatic`.
- `SwitzerlandValidator` — advisory validator; flags the frame, never blocks a keystroke.
- `SwitzerlandDiplomaticValidator` — advisory validator; flags the frame, never blocks a keystroke.
- `SwitzerlandSerialGenerator` — random plate generator.
- `SwitzerlandMissions` — code table.
- `SwitzerlandRegions` — code table.
- 1 bundled asset (`swiss_shield.png`).

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

