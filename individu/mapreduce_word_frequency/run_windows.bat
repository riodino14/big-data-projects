@echo off
if not exist output mkdir output

echo ==========================================
echo MapReduce Word Frequency - Windows
echo ==========================================
echo.

echo [1/3] Running Mapper...
python mapper.py < input\data.txt > output\map_output.txt
if errorlevel 1 goto error

echo [2/3] Running Shuffle/Sort...
sort output\map_output.txt > output\sorted_output.txt
if errorlevel 1 goto error

echo [3/3] Running Reducer...
python reducer.py < output\sorted_output.txt > output\result.txt
if errorlevel 1 goto error

echo.
echo DONE!
echo Result saved to:
echo output\result.txt
echo.
type output\result.txt
goto end

:error
echo.
echo Something went wrong.
echo Make sure Python is installed and available as "python".

:end
pause
