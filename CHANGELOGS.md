# Changelogs:

## [v0.1_alpha 2024.10.15](https://github.com/synexcoder01/synex_cubing_tools/releases/tag/v0.1_alpha)
- Initial release.
- Added the main menu.
- Added the ability to start a new session, or continue an existing one.
- Added the ability to manage your sessions (delete, rename).

## [v0.2_alpha 2024.10.16](https://github.com/synexcoder01/synex_cubing_tools/releases/tag/v0.2_alpha)
- Added the ability to see the available sessions, when you continuing a session.
- Added an "are you sure" question, when you are deleting a session.
- Added a check, that if you enter a time, it checks, if it is a workable data.
- Added breaklines, to make the instructions more clear and nice.

## [v0.3_alpha 2024.10.17](https://github.com/synexcoder01/synex_cubing_tools/releases/tag/v0.3_alpha)
- The idea to import csv files, is replaced, with importing cstimer.net .json files. (Still WIP)
- Made it clear, that when you can type anything to do something, you can just press 'enter'. It is faster.
- If you are making a new session, it does not starts it immediately. You need to choose the 'continue session' option.
- If you create a session, it does not create a comment and P.1 segment in the save file, because it was pointless.
- Made the code more clear, but that does not affects the user experience, only developers (in a good way).

## [v0.3.1_alpha 2024.10.17](https://github.com/synexcoder01/synex_cubing_tools/releases/tag/v0.3.1_alpha)
- Fixed a bug, where you couldn't continue a session you just created, because it couldn't understand the header of the saved file.

## [v0.4_alpha 2024.10.24](https://github.com/synexcoder01/synex_cubing_tools/releases/tag/v0.4_alpha)
### Please note that the old save files are not compatible with the new version.
- Updated the save file format with adding a new line, that says the type of the session.
- Added the ability to choose the type of the session you want to create.
- You can now choose from 222, 333 and 444.
- Added new scrambles for 222, 333 and 444.
- Added a function, that replaces " " with "_" in the name of the session.