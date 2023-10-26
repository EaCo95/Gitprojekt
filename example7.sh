#example3.sh

pathCSW=/home/tuc1/TesCCode/
pathPyton=python3
pathPytonCode=/home/tuc1/TesCCode/PythonCode.py
pathJava=java
pathJavaCode=/home/tuc1/TesCCode/JavaCode.java

testpass=0
testfail=0
testRun=0

timestamp="$(date +"%T")"
logNamed="log$timestamp.txt"

filename=$1
n=1
while read line || [ -n "$line" ]; do
echo "Testsvar $n : $line"

timestamp="$(date +"%T")"
echo $timestamp>>$logNamed

timestampstartC="$(date +"%s")"
echo $timestampstartC>>$logNamed
echo $timestampstartC

echo "_________________________________">>$logNamed

comp="Testsvar: $line"
timestamp="$(date +"%T")"
echo $timestamp>>$logNamed
echo "C Code">>$logNamed
testSvarC=$($pathCSW/helloWorld $line)
echo $testSvarC>>$logNamed

if [ "$testSvarC" = "$comp" ];then
   echo "pass">>$logNamed
   testpass=$((testpass + 1))
else
   echo "FAIL">>$logNamed
   testfail=$((testfail + 1))
fi


n=$((n+1))
done < $filename

timestampstopC="$(date +%s)"
echo $timestampstopC>>$logNamed
echo $timestampstopC

while read line || [ -n "$line" ]; do
comp="Testsvar: $line"
echo "Testsvar $n : $line"
echo $timestampstart
echo "_______________">>$logNamed
timestamp="$(date +"%T")"
echo $timestamp>>$logNamed
echo "Pyton">>$logNamed
testSvarP=$($pathPyton $pathPytonCode $line)
echo $testSvarP>>$logNamed

if [ "$testSvarP" = "$comp" ];then
   echo "pass">>$logNamed
   testpass=$((testpass + 1))
else
   echo "FAIL">>$logNamed
   testfail=$((testfail + 1))
fi
n=$((n+1))
done < $filename

timestampstopP="$(date +%s)"
echo $timestampstopP>>$logNamed
echo $timestampstopP

while read line || [ -n "$line" ]; do
comp="Testsvar: $line"
echo "Testsvar $n : $line"
echo $timestampstartJ
echo "_______________">>$logNamed
timestamp="$(date +"%T")"
echo $timestamp>>$logNamed
echo "Java">>$logNamed
testSvarJ=$($pathJava $pathJavaCode $line)
echo $testSvarJ>>$logNamed

if [ "$testSvarJ" = "$comp" ];then
   echo "pass">>$logNamed
   testpass=$((testpass + 1))
else
   echo "FAIL">>$logNamed
   testfail=$((testfail + 1))
fi
n=$((n+1))
done < $filename

timestampstopJ="$(date +%s)"
echo $timestampstopJ>>$logNamed
echo $timestampstopJ

totime=$((timestampstop - timestampstart))

echo "_______________">>$logNamed

n=$((n+1))
echo $testRun
testRun=$((testpass+testfail)) 
echo "Test Run: "$testRun 
echo "Test Passed: "$testpass
echo "Test Failed: "$testfail

echo "Test Run: "$testRun >>$logNamed
echo "Test Passed: "$testpass >>$logNamed
echo "Test Failed: "$testfail >>$logNamed
echo "_______________">>$logNamed

htmlReport="TestReport$timestampStart.html"

echo "<h1>Test Report $timestamp </h1>">>$htmlReport
echo "<body>Time to run in Seconds : $totime<br></body>">>$htmlReport
echo "<body>Test Run : $testRun<br></body>">>$htmlReport
echo "<body>Test Pass : $testPass<body></body>">>$htmlReport
echo "<body>Test Fail : $testFail<body></body>">>$htmlReport
pathLOG=$(pwd)
echo "<a href=$pathLOG/$logNamed> Log file : $logNamed<br><br></a>">>$htmlReport


byWHO=$(whoami)
echo "<body>Run By : $byWHO<br></body>">>$htmlReport


#<body>Test 1</body>>>$htmlReport

#cat $logNamed

echo "EOF" >>$logNamed