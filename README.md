# Gui captcha generator
Simple text captcha generator with gui that can help to quickly test different captcha designs and build your own generator using code parts from this project

# Goal
The goal of this project is to create easy to use and kinda robust system for testing different setting for creating text captchas (different backgrounds, patterns, distortions and much more).
Also developers can use backend api in their projects to generate text captchas.

# Stack
## Backend
Python is used for backend api. Main reason is that there are already bits of code ready for this project in python, so it would be unwise to rewrite everything in c#.
## Frontend
For frontend I'm using c# and AvaloniaUI, because python has bearly any libraries to build decent UI. For example qt5 could be sometimes quite confusing when creating complicated and modern UI. Although I wouldn't be able to build something modern and cool just yet, but Avalonia is a good starting point in my opinion.

# TODO
- [ ] 0. UnitTesting
- [ ] 1. Random background colors and gradients
- [ ] 2. Random characters colors and gradients
- [ ] 3. Check for characters visibility
- [ ] 4. Add different distortions for background
- [ ] 5. Add distortion for foreground (characters)
- [ ] 6. Add noise patterns
- [ ] 7. Random lines in background and random overlapping with characters
- [ ] 8. Add postprocessing 
- [ ] 9. Add ability to view changes to different captcha's layers without regenerating whole captcha