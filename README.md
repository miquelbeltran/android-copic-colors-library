# android-copic-colors-library

[![JitPack](https://jitpack.io/v/miquelbeltran/android-copic-colors-library.svg)](https://jitpack.io/#miquelbeltran/android-copic-colors-library/)

Use Copic colors in your Android projects.

## Usage:

Reference to the colors with `@color/copic_<code>`, for example:

```
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="colorPrimary">@color/copic_B69</color>
    <color name="colorPrimaryDark">@color/copic_B79</color>
    <color name="colorAccent">@color/copic_R59</color>
</resources>
```

## Setup

Step 1: Add it in your root build.gradle at the end of repositories:

```
	allprojects {
		repositories {
			...
			maven { url 'https://jitpack.io' }
		}
	}
```

Step 2: Add the dependency

```
	dependencies {
		compile 'com.github.miquelbeltran:android-copic-colors-library:1.0'
	}
```

## License

COPIC is a trademark of KABUSHIKI KAISHA TOO (TOO CORPORATION).

