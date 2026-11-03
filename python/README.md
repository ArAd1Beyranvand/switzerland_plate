FREE PALESTINE 🇮🇷🇵🇸 پاینده ایران

GO VEGAN 🌱

==================================

From the mighty people of Iran to the people of Switzerland to view examples:

https://platexample.ir/#/discover/switzerland:python

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

### Install (Python)

Copy `python/plates/countries/switzerland/` into `plate_core/python/plates/countries/`.

Then run the tests from `plate_core/python/`: `pytest`.

### Use

```python
from plates.countries.switzerland.data import SPECS, THEMES

spec = SPECS["ch.high"]
theme = THEMES["SwitzerlandThemes.standard"]
print(spec.id)
```

## Specs

The specs are the same in every language (they come from shared data).

- `ch.high`
- `ch.dealer`
- `ch.temporary`
- `ch.long`
- `ch.military`
- `ch.front`
- `ch.customs`
- `ch.motorcycle`
- `ch.scooter`
- `ch.diplomatic`
- `ch.consular`

## Themes

- `SwitzerlandThemes.standard`
- `SwitzerlandThemes.utility`
- `SwitzerlandThemes.exceptional`
- `SwitzerlandThemes.agricultural`
- `SwitzerlandThemes.scooter`
- `SwitzerlandThemes.red`
- `SwitzerlandThemes.military`

## Change it

- Pick a spec: use another key of `SPECS`.
- Pick a theme: use another key of `THEMES`.
- Validators: `VALIDATORS` maps the names `SwitzerlandValidator`, `SwitzerlandDiplomaticValidator` to classes.

## License

See [LICENSE](https://github.com/ArAd1Beyranvand/switzerland_plate/blob/main/LICENSE).
