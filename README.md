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

```
   Copyright 2018 Miquel Beltran

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
   ```
