FREE PALESTINE 🇮🇷🇵🇸 پاینده ایران

GO VEGAN 🌱

==================================

From the mighty people of Iran to the people of Switzerland to view examples:

https://platexample.ir/#/discover/switzerland:typescript

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

### Install (TypeScript)

Copy `typescript/src/countries/switzerland/` into `plate_core/typescript/src/countries/`.

Then run the tests from `plate_core/typescript/`: `npm test`.

### Use

```ts
import country from './countries/switzerland';

const spec = country.specs.get('ch.high');
console.log(country.package);
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

- Specs: `country.specs`, by id.
- Themes: `country.themes`.
- Validators: `country.validators` (`SwitzerlandValidator`, `SwitzerlandDiplomaticValidator`).

## License

See [LICENSE](https://github.com/ArAd1Beyranvand/switzerland_plate/blob/main/LICENSE).
