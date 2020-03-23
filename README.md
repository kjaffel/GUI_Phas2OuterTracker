# GUI_Phas2OuterTracker

customDeeGraphicsItem.py 
- Place PS and 2S modules on the Dee: TEDD1, surface1

- Main windows for the Assembly:
```
pyuic5 -x Assembly/assembly.ui -o assemby.py
pyuic5 -x Assembly/start_assembly.ui -o start_assemby.py
pyuic5 -x Assembly/guide_assembly.ui -o guide_assemby.py
```
- Window to Navigate through Modules:
```
pyuic5 -x ModuleNavigator/browsemodules.ui -o browsemodules.py
```
- Help Windows:
- FIXME : pass to https://cp3-git.irmp.ucl.ac.be/cp3-support/helpdesk/issues instead !
```
pyuic5 -x Help/IssuesWin.ui -o IssuesWin.py
pyuic5 -x Help/NewIssueOpenWin.ui -o NewIssueOpenWin.py
```
actions.py will allow you to attach files and this script should be moved to GUIRun.py # FIXME

- FC7 Window:
```
pyuic5 -x FC7/setupfc7.ui -o setupfc7.py
```
- Login Window:
```
pyuic5 -x Login/ssh.ui -o ssh.py
```

- N.B:
  GUIRun.py 
- should be able to run all window mentionned above
- Work in progress ...

