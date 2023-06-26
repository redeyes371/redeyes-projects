@echo off
rem set the url of the file to download
set url=https://example.com/file.exe
rem set the name of the file to save
set file=file.exe
rem use bitsadmin to download the file
bitsadmin /transfer job /priority high %url% %cd%\%file%
rem run the file
%file%
