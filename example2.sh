#example1.sh

pathCSW=/home/tuc1/TesCCode/
pathPyton=python3
pathPytonCode=/home/tuc1/TesCCode/PythonCode.py
pathJava=java
pathJavaCode=/home/tuc1/TesCCode/JavaCode.java

filename='/home/tuc1/TesCCode/testData.txt'
n=1
while read line || [ -n "$line" ]; do
echo "Testsvar $n : $line"

n=$((n+1))
done < $filename

$pathCSW/helloWorld kalle

$pathPyton $pathPytonCode pelle

$pathJava $pathJavaCode lisa

