<h1 align="center">jdDiff</h1>

<h3 align="center">A graphical cross platform diff viewer</h3>

<p align="center">
    <img alt="jdDiff" src="screenshots/MainWindow.png"/>
</p>

jdDiff shows the difference between two Files or two Directories

## Install

### Flatpak
You can get jdDiff from [Flathub](https://flathub.org/apps/page.codeberg.JakobDev.jdDiff)

### AUR
Arch Users can get jdDiff from the [AUR](https://aur.archlinux.org/packages/jdDiff)

### pip
You can install jdDiff from [PyPI](https://pypi.org/project/jdDiff) using `pip`:
```shell
pip install jdDiff
```
Using this Method, it will not include a Desktop Entry or any other Data file, so you need to run jdDiff from the Command Line.
Use this only, when nothing else works.

### From source
This is only for experienced Users and someone, who wants to package jdDiff for a Distro.
jdDiffshould be installed as a Python package.
You can use `pip` or any other tool that can handle Python packages.
YOu need to have `lrelease` installed to build the Package.
After that, you should run `install-unix-datafiles.py` which wil install things like the Desktop Entry or the Icon in the correct place.
It defaults to `/usr`, but you can change it with the `--prefix` argument.
It also applies the translation to this files.
You need gettext installed to run `install-unix-datafiles.py`.

Here's a example of installing jdDiff into `/usr/local`:
```shell
sudo pip install --prefix /usr/local .
sudo ./install-unix-datafiles.py --prefix /usr/local
```

## Translate
You can help translating jdDiff on [Codeberg Translate](https://translate.codeberg.org/projects/jdDiff)

## Develop
jdDiffis written in Python and uses PyQt6 as GUI toolkit. You should have some experience in both.
You can run `jdDiff.py`to start jdDiff from source and test your local changes.
It ships with a few scripts in the tools directory that you need to develop.

#### CompileUI.py
This is the most important script. It will take all `.ui` files in `jdDiff/ui` and compiles it to a Python class
and stores it in `jdDiff/ui_compiled`. Without running this script first, you can't start jdDiff.
You need to rerun it every time you changed or added a `.ui` file.

#### BuildTranslations.py
This script takes all `.ts` files and compiles it to `.qm` files.
The `.ts` files are containing the translation source and are being used during the translation process.
The `.qm` contains the compiled translation and are being used by the Program.
You need to compile a `.ts` file to a `.qm` file to see the translations in the Program.

#### UpdateTranslations.py
This regenerates the `.ts` files. You need to run it, when you changed something in the source code.
The `.ts` files are contains the line in the source, where the string to translate appears,
so make sure you run it even when you don't changed a translatable string, so the location is correct.

####  UpdateUnixDataTranslations.py
This regenerates the translation files in `deploy/translations`. these files contains the translations for the Desktop Entry and the AppStream File.
It uses gettext, as it is hard to translate this using Qt.
These files just exists to integrate the translation with Weblate, because Weblate can't translate the Desktop Entry and the AppStream file.
Make sure you run this when you edited one of these files.
You need to have gettext installed to use it.