@echo off
echo Installing Game4Blind, please wait...
set install_path=%userprofile%\Game4Blind
set get_files=%install_path%\getFiles.vbs
if not exist "%install_path%" (
	mkdir %install_path%
)
echo dim xHttp: Set xHttp = createobject("Microsoft.XMLHTTP")> %get_files%
echo dim bStrm: Set bStrm = createobject("Adodb.Stream")>> %get_files%
echo xHttp.Open "GET", "https://raw.githubusercontent.com/XEXABYT3X/Game4Blind/master/piano.mp3", False>> %get_files%
echo xHttp.Send>> %get_files%
echo with bStrm>> %get_files%
echo     .type = 1 '//binary>> %get_files%
echo     .open>> %get_files%
echo     .write xHttp.responseBody>> %get_files%
echo     .savetofile "piano.mp3", 2 '//overwrite>> %get_files%
echo end with>> %get_files%
echo bStrm.Close>> %get_files%
echo xHttp.Open "GET", "https://www.python.org/ftp/python/3.6.2/python-3.6.2-amd64.exe", False>> %get_files%
echo xHttp.Send>> %get_files%
echo with bStrm>> %get_files%
echo     .type = 1 '//binary>> %get_files%
echo     .open>> %get_files%
echo     .write xHttp.responseBody>> %get_files%
echo     .savetofile "install_python-3.6.2-64bit.exe", 2 '//overwrite>> %get_files%
echo end with>> %get_files%
echo bStrm.Close>> %get_files%
echo xHttp.Open "GET", "https://raw.githubusercontent.com/XEXABYT3X/Game4Blind/master/game4blind.pyw", False>> %get_files%
echo xHttp.Send>> %get_files%
echo with bStrm>> %get_files%
echo     .type = 1 '//binary>> %get_files%
echo     .open>> %get_files%
echo     .write xHttp.responseBody>> %get_files%
echo     .savetofile "game4blind.pyw", 2 '//overwrite>> %get_files%
echo end with>> %get_files%
cd %install_path%
start "" /wait "getFiles.vbs"
cls
echo Please go through with this install or you won't be able to open my file. Press enter to continue.
pause>nul
start "" /wait "install_python-3.6.2-64bit.exe"
del %get_files%
cd %userprofile%\Desktop
echo @echo off> Game4Blind.bat
echo :start>> Game4Blind.bat
echo cls>> Game4Blind.bat
echo echo Would you like to:>> Game4Blind.bat
echo echo (1) Play Game>> Game4Blind.bat
echo echo (2) Uninstall Game>> Game4Blind.bat
echo set /p play_or_uninstall="">> Game4Blind.bat
echo if "%%play_or_uninstall%%" == "1" (>> Game4Blind.bat
echo 	cd %%userprofile%%\Game4Blind\>> Game4Blind.bat
echo 	start game4blind.pyw >> Game4Blind.bat
echo 	exit>> Game4Blind.bat
echo )>> Game4Blind.bat
echo if "%%play_or_uninstall%%" == "2" (>> Game4Blind.bat
echo 	cls>> Game4Blind.bat
echo ) else (>> Game4Blind.bat
echo 	cls>> Game4Blind.bat
echo 	echo You did not enter 1 or 2. Press enter to continue>> Game4Blind.bat
echo 	pause^>nul>> Game4Blind.bat
echo 	goto start>> Game4Blind.bat
echo )>> Game4Blind.bat
echo echo Are you sure?>> Game4Blind.bat
echo echo (1) Yes>> Game4Blind.bat
echo set /p sure="">> Game4Blind.bat
echo if "%%sure%%" == "1" (>> Game4Blind.bat
echo 	cls>> Game4Blind.bat
echo 	start "" /wait "%%userprofile%%\Game4Blind\install_python-3.6.2-64bit.exe">> Game4Blind.bat
echo 	timeout /t 2 /nobreak>> Game4Blind.bat
echo 	rmdir /s /q %install_path%>> Game4Blind.bat
echo 	del /s /q Game4Blind.bat>> Game4Blind.bat
echo 	echo Successfully uninstalled. Press enter to continue>> Game4Blind.bat
echo 	pause^>nul>> Game4Blind.bat
echo )>> Game4Blind.bat
echo Successfully installed. Press enter to close.
pause>nul
